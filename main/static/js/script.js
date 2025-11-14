
document.querySelectorAll('.dropdown').forEach(item => {
  item.addEventListener('click', () => {
    const submenu = item.querySelector('.submenu');
    if (submenu.style.display === 'flex') {
      submenu.style.display = 'none';
    } else {
      submenu.style.display = 'flex';
    }
  });
});

// добавление в избранное и изменения цвета
document.addEventListener('DOMContentLoaded', () => {
  // Обработчик для категории "Мужская обувь"
  const categoryShoesMen = document.querySelector('.category-shoes-men');
  if (categoryShoesMen) {
    categoryShoesMen.addEventListener('click', () => {
      // Перенаправление на страницу категории
      window.location.href = '/category/shoes/men/';
    });
  }

  // Добавление в избранное и установка цвета сердечка
  document.querySelectorAll('.favorite').forEach(btn => {
    // Назначение обработчика клика
    btn.addEventListener('click', (e) => {
      e.stopPropagation(); // чтобы не было конфликтов, если есть другие обработчики
      console.log('Клик по сердечку', e.target);

      const parent = btn.closest('.product-card');
      const name = parent.getAttribute('data-name');
      const price = parent.getAttribute('data-price');
      const img = parent.getAttribute('data-img');
      const favoriteIcon = btn.querySelector('.heart-icon');

      const product = { name, price, img };
      let favorites = JSON.parse(localStorage.getItem('favorites')) || [];

      const index = favorites.findIndex(p => p.name === name);

      if (index === -1) {
        // Добавляем товар
        favorites.push(product);
        if (favoriteIcon) favoriteIcon.setAttribute('fill', 'red');
      } else {
        // Удаляем товар
        favorites.splice(index, 1);
        if (favoriteIcon) favoriteIcon.setAttribute('fill', 'none');
      }

      localStorage.setItem('favorites', JSON.stringify(favorites));

      // Обновляем список избранных, если есть контейнер
      const favoritesContainer = document.getElementById('favorites-container');
      if (favoritesContainer) {
        renderFavorites();
      }
    });

    // Изначально устанавливаем цвет сердечка, если товар в избранных
    const parent = btn.closest('.product-card');
    if (parent) {
      const name = parent.getAttribute('data-name');
      const favorites = JSON.parse(localStorage.getItem('favorites')) || [];
      const index = favorites.findIndex(p => p.name === name);
      const svg = btn.querySelector('.heart-icon');
      if (svg) {
        if (index !== -1) {
          svg.setAttribute('fill', 'red');
        } else {
          svg.setAttribute('fill', 'grey');
        }
      }
    }
  });

  // Функция отображения избранных
  function renderFavorites() {
    const container = document.getElementById('favorites-container');
    if (!container) return;

    container.innerHTML = '';

    const favorites = JSON.parse(localStorage.getItem('favorites')) || [];
    if (favorites.length === 0) {
      container.innerHTML = '<p>Нет избранных товаров.</p>';
      return;
    }

    favorites.forEach(p => {
      const div = document.createElement('div');
      div.innerHTML = `
        <img src="${p.img}" alt="${p.name}" style="width:150px; height:auto;"/>
        <h3>${p.name}</h3>
        <p>${p.price}</p>
      `;
      container.appendChild(div);
    });
  }

  // Если страница содержит блок для отображения избранных, вызываем функцию
  if (document.getElementById('favorites-container')) {
    renderFavorites();
  }
});