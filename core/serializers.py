from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    # Isso faz com que, ao pedir um produto, venha os dados da categoria dele junto (não só o ID)
    category = CategorySerializer(read_only=True) 
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'stock', 'is_active', 'category']