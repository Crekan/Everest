# Generated by Django 4.1.3 on 2022-11-10 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_detailposttable_options_alter_news_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='table',
        ),
        migrations.AddField(
            model_name='detailposttable',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_table', to='news.news', verbose_name='Таблицы'),
        ),
    ]