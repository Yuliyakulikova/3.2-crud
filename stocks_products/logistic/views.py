from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'description']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title', 'description']
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['address', 'products']
    search_fields = ['address', 'products__title', 'products__description']
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации
