# from django.contrib import admin
# from django.urls import path,include
# from website import views

# urlpatterns = [
#    path('',views.home,name='home'),
#    path('cart/',views.cart,name='cart'),

#    path('api/products/', views.product_api,name='product_api'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_api, name='product_api'),
    path('products/<int:pk>/', views.product_detail_api, name='product_detail_api'),  # DELETE
      path('cart/', views.cart_api, name='cart_api'),
]
