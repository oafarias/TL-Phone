from rest_framework import viewsets
from core.models import Category, Product
from core.serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    # Só vamos mostrar na API os produtos que estiverem marcados como ativos
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer