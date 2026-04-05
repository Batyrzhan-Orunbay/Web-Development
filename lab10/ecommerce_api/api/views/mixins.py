"""
Level 4: Mixins
Uses DRF mixins combined with GenericAPIView.
Mixins provide list(), create(), retrieve(), update(), destroy() methods.
"""
from rest_framework import mixins, generics

from api.models import Product
from api.serializers import ProductSerializer


class ProductListAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    GET  /api/products/ — list all products  (via ListModelMixin.list)
    POST /api/products/ — create a product   (via CreateModelMixin.create)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """
    GET    /api/products/<product_id>/ — retrieve  (via RetrieveModelMixin)
    PUT    /api/products/<product_id>/ — update     (via UpdateModelMixin)
    DELETE /api/products/<product_id>/ — destroy    (via DestroyModelMixin)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'   # maps URL kwarg to pk lookup

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
