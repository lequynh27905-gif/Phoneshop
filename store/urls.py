from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # Home & Product
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('category/<slug:slug>/', views.category_list, name='category_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Cart
    path('cart/', views.cart, name='cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    
    # Checkout & Orders
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/<str:order_number>/', views.order_confirmation, name='order_confirmation'),
    path('orders/', views.order_history, name='order_history'),
    path('order/<str:order_number>/', views.order_detail, name='order_detail'),
    
    # Reviews
    path('product/<slug:slug>/review/', views.add_review, name='add_review'),
    
    # Wishlist
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:phone_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:phone_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Other
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
