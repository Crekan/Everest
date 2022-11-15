from django.db import models
from tinymce.models import HTMLField


class Ip(models.Model):
    ip = models.CharField(max_length=255, verbose_name='Ip', default=0)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Ip'
        verbose_name_plural = 'Ip'


class News(models.Model):
    news_images = models.ImageField(upload_to='news_images/', verbose_name='Изображение')
    news_date = models.DateField(auto_now=True, verbose_name='Дата добавления')
    news_views = models.ManyToManyField(Ip, related_name="post_views", blank=True)
    news_title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    description = HTMLField(verbose_name='Описание', null=True)

    def total_views(self):
        return self.news_views.count()

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class DetailPostTable(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    table = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Таблицы', null=True,
                              related_name='post_table')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таблица для поста'
        verbose_name_plural = 'Таблицы для постов'
