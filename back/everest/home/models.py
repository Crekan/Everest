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



