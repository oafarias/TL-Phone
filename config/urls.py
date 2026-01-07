"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Imports do Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import index, product_detail # Import das views para renderizar templates

# Configuração da Documentação
schema_view = get_schema_view(
   openapi.Info(
      title="TL Phone API",
      default_version='v1',
      description="Documentação da API de Produtos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="seu-email@exemplo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', index, name='index'),  # Rota para a view index

    path('product/<int:id>/', product_detail, name='product_detail'),  # Rota para a view de detalhes do produto

    # Rotas da Documentação (Swagger e Redoc)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Configuração para servir imagens no modo DEBUG (Local)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)