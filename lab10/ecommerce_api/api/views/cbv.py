"""
Level 3: Class-Based Views (CBV)
Uses APIView with explicit get(), post(), put(), delete() methods.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Product
from api.serializers import ProductSerializer


class ProductListAPIView(APIView):
    """
    GET  /api/products/ — list all products
    POST /api/products/ — create a new product
    """

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    """
    GET    /api/products/<product_id>/ — retrieve a product
    PUT    /api/products/<product_id>/ — update a product
    DELETE /api/products/<product_id>/ — delete a product
    """

    def get_object(self, product_id):
        """Helper to get product or return None if not found."""
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id):
        product = self.get_object(product_id)
        if product is None:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        if product is None:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        if product is None:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
