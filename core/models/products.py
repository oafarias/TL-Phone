from django.db import models

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    slug = models.SlugField('Identificador URL', unique=True, help_text='Ex: iphones-novos')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Categoria')
    name = models.CharField('Nome do Produto', max_length=200)
    slug = models.SlugField('Identificador URL', unique=True, help_text='Ex: iphone-14-pro-max-256gb')
    
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    old_price = models.DecimalField('Preço Antigo', max_digits=10, decimal_places=2, blank=True, null=True, help_text='Para promoções (De R$ X por Y)')
    
    # Imagem principal (requer biblioteca Pillow)
    image = models.ImageField('Imagem Principal', upload_to='products/', blank=True, null=True)
    
    stock = models.IntegerField('Estoque', default=0)
    is_active = models.BooleanField('Ativo?', default=True)
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-created_at'] # Mostra os mais novos primeiro

    def __str__(self):
        return self.name