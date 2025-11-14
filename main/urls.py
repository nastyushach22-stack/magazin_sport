from django.urls import path
from . import views
from .views import create_payment

urlpatterns = [
    path('', views.index, name='home'),
    #мужское
    path('m_boots/', views.m_boots, name='m_boots'),
    path('m_clothes/', views.m_clothes, name='m_clothes'),
    path('m_accessories/', views.m_accessories, name='m_accessories'),
    path('m_inventory/', views.m_inventory, name='m_inventory'),
    #женское
    path('zh_boots/', views.zh_boots, name='zh_boots'),
    path('zh_clothes/', views.zh_clothes, name='zh_clothes'),
    path('zh_accessories/', views.zh_accessories, name='zh_accessories'),
    path('zh_inventory/', views.zh_inventory, name='zh_inventory'),
    #детское
    path('d_boots/', views.d_boots, name='d_boots'),
    path('d_clothes/', views.d_clothes, name='d_clothes'),
    path('d_accessories/', views.d_accessories, name='d_accessories'),
    path('d_inventory/', views.d_inventory, name='d_inventory'),
    #избарнное
    path('favorites/', views.favorites, name='favorites'),
    path('product/<slug:category_slug>/<int:product_id>/', views.product_detail, name='product_detail'),
    #корзина
    path('cart/', views.cart, name='cart'),
    # Страница товаров
    path('<str:category_slug>/<int:product_id>/', views.product_detail, name='product_detail'),
    #оплата
    path('pay/', create_payment, name='create_payment'),
]