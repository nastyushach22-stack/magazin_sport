#views.py
from django.shortcuts import render
from .data import products_data
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import uuid
import traceback

def index(request):
    products = [
        {
            'id': '38',
            'img': 'img/children/d_clothes1.jpg',
            'name': 'Термофутболка с рукавами',
            'price': '20999 ₽'
        },
        {
            'id': '39',
            'img': 'img/children/d_clothes2.jpg',
            'name': 'Термолеггинсы',
            'price': '15499 ₽'
        },
        {
            'id': '40',
            'img': 'img/children/d_clothes3.jpg',
            'name': 'Парка зимняя',
            'price': '50299 ₽'
        }
    ]
    return render(request, 'index.html', {'products': products, 'category_slug': 'children'})

# мужские товары

def m_boots(request):
    products = [
        {
            'id': '1',
            'img': 'img/mens/m_boots1.jpg',
            'name': 'Бутсы Nike',
            'price': '30999 ₽'
        },
        {
            'id': '2',
            'img': 'img/mens/m_boots2.jpg',
            'name': 'Кроссовки Adidas Gazelle',
            'price': '50499 ₽'
        },
        {
            'id': '3',
            'img': 'img/mens/m_boots3.jpg',
            'name': 'Кроссовки Adidas',
            'price': '40299 ₽'
        }
    ]
    return render(request, 'm_boots.html', {'products': products, 'category_slug': 'm_boots'})

def m_clothes(request):
    products = [
        {
            'id': '4',
            'img': 'img/mens/m_clothes1.jpg',
            'name': 'Футболка мужская',
            'price': '20999 ₽'
        },
        {
            'id': '5',
            'img': 'img/mens/m_clothes2.jpg',
            'name': 'Футболка мужская Balenciaga',
            'price': '40499 ₽'
        },
        {
            'id': '6',
            'img': 'img/mens/m_clothes3.jpg',
            'name': 'Свитшот Stone Island',
            'price': '50299 ₽'
        }
    ]
    return render(request, 'm_clothes.html', {'products': products, 'category_slug': 'm_clothes'})

def m_accessories(request):
    products = [
        {
            'id': '7',
            'img': 'img/mens/m_accessories1.jpg',
            'name': 'Кожаный ремень Gancini',
            'price': '40030 ₽'
        },
        {
            'id': '8',
            'img': 'img/mens/m_accessories2.jpg',
            'name': 'Панама Marni',
            'price': '32665 ₽'
        },
        {
            'id': '9',
            'img': 'img/mens/m_accessories3.jpg',
            'name': 'Солнцезащитные очки Prada',
            'price': '32184 ₽'
        }
    ]
    return render(request, 'm_accessories.html', {'products': products, 'category_slug': 'm_accessories'})

def m_inventory(request):
    products = [
        {
            'id': '10',
            'img': 'img/mens/m_inventory1.jpg',
            'name': 'Велосипедный шлем',
            'price': '35675 ₽'
        },
        {
            'id': '11',
            'img': 'img/mens/m_inventory2.jpg',
            'name': 'Наколенники Adidas',
            'price': '3200 ₽'
        },
        {
            'id': '12',
            'img': 'img/mens/m_inventory3.jpg',
            'name': 'Теннисная сумка',
            'price': '14000 ₽'
        }
    ]
    return render(request, 'm_inventory.html', {'products': products, 'category_slug': 'm_inventory'})

# женские товары

def zh_boots(request):
    products = [
        {
            'id': '13',
            'img': 'img/woman/zh_boots1.webp',
            'name': 'Кроссовки Hogan',
            'price': '28800 ₽'
        },
        {
            'id': '14',
            'img': 'img/woman/zh_boots2.jpg',
            'name': 'Кроссовки на платформе',
            'price': '34499 ₽'
        },
        {
            'id': '15',
            'img': 'img/woman/zh_boots3.jpg',
            'name': 'Кеды',
            'price': '26299 ₽'
        }
    ]
    return render(request, 'zh_boots.html', {'products': products, 'category_slug': 'zh_boots'})

def zh_clothes(request):
    products = [
        {
            'id': '16',
            'img': 'img/woman/zh_clothes1.jpg',
            'name': 'Боди',
            'price': '42800 ₽'
        },
        {
            'id': '17',
            'img': 'img/woman/zh_clothes2.jpg',
            'name': 'Куртка Valles',
            'price': '746499 ₽'
        },
        {
            'id': '18',
            'img': 'img/woman/zh_clothes3.jpg',
            'name': 'Черный свитшот',
            'price': '34299 ₽'
        }
    ]
    return render(request, 'zh_clothes.html', {'products': products, 'category_slug': 'zh_clothes'})

def zh_accessories(request):
    products = [
        {
            'id': '19',
            'img': 'img/woman/zh_accessories1.webp',
            'name': 'Носки для пилатеса',
            'price': '3400 ₽'
        },
        {
            'id': '20',
            'img': 'img/woman/zh_accessories2.jpg',
            'name': 'Солнцезащитные очки',
            'price': '32665 ₽'
        },
        {
            'id': '21',
            'img': 'img/woman/zh_accessories3.jpg',
            'name': 'Бутылка для воды',
            'price': '5458 ₽'
        }
    ]
    
    return render(request, 'zh_accessories.html', {'products': products, 'category_slug': 'zh_accessories'})


def zh_inventory(request):
    products = [
        {
            'id': '22',
            'img': 'img/woman/zh_inventory1.jpg',
            'name': 'Деревянный скейтборд',
            'price': '8368 ₽'
        },
        {
            'id': '23',
            'img': 'img/woman/zh_inventory2.jpg',
            'name': 'Шлем Salomon',
            'price': '17144 ₽'
        },
        {
            'id': '24',
            'img': 'img/woman/zh_inventory3.webp',
            'name': 'Чехол для ручных гантелей',
            'price': '14000 ₽'
        }
    ]
    return render(request, 'zh_inventory.html', {'products': products, 'category_slug': 'zh_inventory'})

# детские товары

def d_boots(request):
    products = [
        {
            'id': '25',
            'img': 'img/children/d_boots1.webp',
            'name': 'Кеды Adidas',
            'price': '40999 ₽'
        },
        {
            'id': '26',
            'img': 'img/children/d_boots2.webp',
            'name': 'Кеды Adidas розовые',
            'price': '50499 ₽'
        },
        {
            'id': '27',
            'img': 'img/children/d_boots3.webp',
            'name': 'Бутцы Adidas',
            'price': '40299 ₽'
        }
    ]
    return render(request, 'd_boots.html', {'products': products, 'category_slug': 'd_boots'})

def d_clothes(request):
    products = [
        {
            'id': '28',
            'img': 'img/children/d_clothes1.jpg',
            'name': 'Термофутболка с рукавами',
            'price': '20999 ₽'
        },
        {
            'id': '29',
            'img': 'img/children/d_clothes2.jpg',
            'name': 'Термолеггинсы',
            'price': '15499 ₽'
        },
        {
            'id': '30',
            'img': 'img/children/d_clothes3.jpg',
            'name': 'Парка зимняя',
            'price': '50299 ₽'
        }
    ]
    return render(request, 'd_clothes.html', {'products': products, 'category_slug': 'd_clothes'})

def d_accessories(request):
    products = [
        {
            'id': '31',
            'img': 'img/children/d_accessories1.webp',
            'name': 'Варежки',
            'price': '8030 ₽'
        },
        {
            'id': '32',
            'img': 'img/children/d_accessories2.webp',
            'name': 'Шапка и снуд Бини',
            'price': '18665 ₽'
        },
        {
            'id': '33',
            'img': 'img/children/d_accessories3.webp',
            'name': 'Балаклава',
            'price': '5184 ₽'
        },
        {
            'id': '34',
            'img': 'img/children/d_accessories4.webp',
            'name': 'Перчатки горнолыжные',
            'price': '14184 ₽'
        }
    ]
    return render(request, 'd_accessories.html', {'products': products, 'category_slug': 'd_accessories'})

def d_inventory(request):
    products = [
        {
            'id': '35',
            'img': 'img/children/d_inventory1.webp',
            'name': 'Перчатки боксерские',
            'price': '18675 ₽'
        },
        {
            'id': '36',
            'img': 'img/children/d_inventory2.webp',
            'name': 'Сумка спортивная',
            'price': '3200 ₽'
        },
        {
            'id': '37',
            'img': 'img/children/d_inventory3.webp',
            'name': 'Очки для плавания',
            'price': '6000 ₽'
        }
    ]
    return render(request, 'd_inventory.html', {'products': products, 'category_slug': 'd_inventory'})

# избаранные 
def favorites(request):
    return render(request, 'favorites.html')

# Корзина
def cart(request):
    return render(request, 'cart.html')

def product_detail(request, category_slug, product_id):
    category_products = products_data.get(category_slug)
    if not category_products:
        from django.http import Http404
        raise Http404("Категория не найдена")
    product = next((item for item in category_products if item['id'] == int(product_id)), None)
    if not product:
        from django.http import Http404
        raise Http404("Товар не найден")
    return render(request, 'product_detail.html', {'product': product})

