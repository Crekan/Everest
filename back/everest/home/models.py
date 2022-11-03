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

    def total_views(self):
        return self.news_views.count()

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Category(models.Model):
    category_images = models.ImageField(upload_to='category_images/', verbose_name='Изображение')
    category_title = models.CharField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ParentCategory(models.Model):
    parent_category = models.ForeignKey(Category, related_name='parent', on_delete=models.CASCADE, null=True,
                                        verbose_name='К какой категории отностится')
    parent_category_name = models.CharField(max_length=250, verbose_name='Под категория')

    def __str__(self):
        return self.parent_category_name

    class Meta:
        verbose_name = 'Под категория'
        verbose_name_plural = 'Под категории'
