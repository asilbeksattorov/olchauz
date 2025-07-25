from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Category, SubCategory, Product, Attribute, Comment
from .serializers import CategorySerializer, ProductSerializer, CommentSerializer, SubCategorySerializer, AttributeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related(
        'subcategory', 'subcategory__category'
    ).prefetch_related(
        'attributes', 'comments'
    )

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['subcategory__category', 'price']
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'quantity']

    @method_decorator(cache_page(60 * 5)) # 5 daqiqa cache qushtim
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('product').all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


