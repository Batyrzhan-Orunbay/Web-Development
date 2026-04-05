"""
Level 5: Generic Views (minimal code)
ListCreateAPIView and RetrieveUpdateDestroyAPIView handle everything automatically.
Also includes Category endpoints and custom CategoryProductsAPIView.
"""
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer


# ── Product views ────────────────────────────────────────────────────────────

class ProductListAPIView(generics.ListCreateAPIView):
    """
    GET  /api/products/ — list all products
    POST /api/products/ — create a product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/products/<product_id>/ — retrieve
    PUT    /api/products/<product_id>/ — full update
    PATCH  /api/products/<product_id>/ — partial update
    DELETE /api/products/<product_id>/ — delete
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'


# ── Category views ───────────────────────────────────────────────────────────

class CategoryListAPIView(generics.ListCreateAPIView):
    """
    GET  /api/categories/ — list all categories
    POST /api/categories/ — create a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/categories/<category_id>/ — retrieve
    PUT    /api/categories/<category_id>/ — full update
    PATCH  /api/categories/<category_id>/ — partial update
    DELETE /api/categories/<category_id>/ — delete
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'


class CategoryProductsAPIView(APIView):
    """
    Custom view: GET /api/categories/<category_id>/products/
    Returns all products belonging to a given category.
    """

    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response({
            'category': CategorySerializer(category).data,
            'products': serializer.data,
        })
