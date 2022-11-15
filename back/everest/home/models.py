from django.db import models


class Slider(models.Model):
    slider_images = models.ImageField(upload_to='slider_images/', verbose_name='Изображение')
    slider_title = models.CharField(max_length=250, verbose_name='Заголовок')
    slider_description = models.CharField(max_length=250, verbose_name='Описнаие')

    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'


class Category(models.Model):
    images = models.ImageField(upload_to='category_images/', verbose_name='Изображение')
    title = models.CharField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ParentCategory(models.Model):
    category = models.ForeignKey(Category, related_name='parent', on_delete=models.CASCADE, null=True,
                                 verbose_name='К какой категории отностится')
    name = models.CharField(max_length=250, verbose_name='Под категория', null=True)
    images = models.ImageField(upload_to='parent_category_images/', verbose_name='Изображение', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Под категория'
        verbose_name_plural = 'Под категории'
