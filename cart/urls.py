from django.urls import path
from . import views

urlpatterns = [
     path('cartdetails', views.cart_details, name='cart_details'),
     path('add/<int:product_id>/',views.add_cart,name='add_cart'),
     path('item_dec/<int:product_id>/', views.minus_cart, name='item_dec'),
     path('item_del/<int:product_id>/', views.cart_delete, name='item_del'),

]