# from django.shortcuts import render
# from django import http
# from website.models import Product,cart as cartitems
# # Create your views here.
# def home(request):
#     product_list = Product.objects.all()
#     data={'products': product_list}
#     return render(request, 'website/index.html',data)

# def cart(request):
#     cart_list = cartitems.objects.all()
#     # cart_items=cart_list.product.all()/
#     # print(cart_list)
#     data={'cartitems': cart_list}
#     return render(request, 'website/cart.html',data)


# def product_api(request):
#     pro=Product.objects.all().values('id','name','price','description')
#     return http.JsonResponse(list(pro),safe=False)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, cart as Cart
from .serializers import ProductSerializer, CartSerializer

# ================= PRODUCTS API =================
@api_view(['GET', 'POST'])
def product_api(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def product_detail_api(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response({'message': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)


# ================= CART API =================
@api_view(['GET'])
def cart_api(request):
    cart_items = Cart.objects.all()
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data)
