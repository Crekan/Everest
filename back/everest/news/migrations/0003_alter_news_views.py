# Generated by Django 4.1.3 on 2022-11-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='news.ip'),
        ),
    ]
