from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Product instances.

    Supports:
      - Search:   GET /api/products/?search=<keyword>   (searches name & description)
      - Ordering: GET /api/products/?ordering=price     (ascending)
                  GET /api/products/?ordering=-price    (descending)
                  GET /api/products/?ordering=name
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Task 6a: Configure ViewSet Backends
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Task 6b: Define Filter Fields
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']
    ordering = ['id']  # default ordering
