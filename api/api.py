from rest_framework import viewsets
from rest_framework import pagination

from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer


class MyPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 50


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = MyPagination

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
