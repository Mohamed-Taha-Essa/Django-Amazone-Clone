from . import serializers
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from .pagination import MyPagination

from .models import Product ,Brand,Review ,ProductImages


class ProductListAPI(generics.ListAPIView):
    queryset =Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtitle']
    ordering_fields = ['price']
    permission_classes = [IsAuthenticated]


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class BrandListAPI(generics.ListAPIView):
    queryset =Brand.objects.all()
    serializer_class = serializers.BrandListSerializer
    pagination_class =MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandDetailSerializer




