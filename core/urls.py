from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

# O Router cria as URLs automaticamente (/categories/, /products/)
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Inclui todas as rotas geradas pelo router
    path('', include(router.urls)),
]