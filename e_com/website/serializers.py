from rest_framework import serializers
from .models import Product,cart as Cart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # include product details
    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']