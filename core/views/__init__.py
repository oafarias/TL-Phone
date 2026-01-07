from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404 # Import para renderizar templates
from core.models import Category, Product
from core.serializers import CategorySerializer, ProductSerializer

# --- PARTE DA API (Já existente) ---
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    # Só mostra na API os ativos
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

# --- PARTE DAS VIEWS PARA RENDERIZAR TEMPLATES ---
def index(request):
    # Renderiza a página inicial com a lista de produtos ativos
    products = Product.objects.filter(is_active=True)
    return render(request, 'index.html', {'products': products})
def product_detail(request, id):
    # Renderiza a página de detalhes do produto
    product = get_object_or_404(Product, id=id, is_active=True)
    return render(request, 'product_detail.html', {'product': product})