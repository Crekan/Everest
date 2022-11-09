from django.db import models


class Product(models.Model):  # Albom
    images = models.ImageField(upload_to='product_images/', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    new_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Новая цена')
    old_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Старая цена', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название каткгории')
    category_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Категория',
                                         related_name='cat_product', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Trademark(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    trademark_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Категория',
                                          related_name='brand_name', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Торговая марка'
        verbose_name_plural = 'Торговые марки'
