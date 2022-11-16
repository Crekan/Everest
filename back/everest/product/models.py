from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


class Product(models.Model):
    images = models.ImageField(upload_to='product_images/', verbose_name='Изображение', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    new_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Новая цена')
    old_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Старая цена', blank=True, null=True)
    about_the_product = HTMLField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                verbose_name='Продукт', related_name='product_image')
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Изображения для продукта'
        verbose_name_plural = 'Изображения для продукта'


class Characteristics(models.Model):
    product_characteristics = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', null=True,
                                                related_name='product_characteristics')
    color = models.CharField(max_length=250, verbose_name='Цвет', blank=True, null=True)
    brand_name = models.CharField(max_length=250, verbose_name='Торговая марка')
    base_material = models.CharField(max_length=250, verbose_name='Материал основания', blank=True, null=True)
    solvent = models.CharField(max_length=250, verbose_name='Растворитель', blank=True, null=True)
    application_type = models.CharField(max_length=250, verbose_name='Тип применения', blank=True, null=True)
    degree_of_gloss = models.CharField(max_length=250, verbose_name='Степень блеска', blank=True, null=True)
    base = models.CharField(max_length=250, verbose_name='Основа ', blank=True, null=True)
    frequency = models.CharField(max_length=250, verbose_name='Частота', blank=True, null=True)
    application_temperature = models.CharField(max_length=250, verbose_name='Температура применения, гр.', blank=True,
                                               null=True)
    tare_size = models.CharField(max_length=250, verbose_name='Размер тары', blank=True, null=True)
    Packing = models.CharField(max_length=250, verbose_name='Фасовка', blank=True, null=True)
    tinting_base = models.CharField(max_length=250, verbose_name='База колеровки', blank=True, null=True)
    gross_weight = models.CharField(max_length=250, verbose_name='Вес брутто', blank=True, null=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment_post')
    user = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Впечатления о товаре')
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user} | left a comment on a post - {self.post}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


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
