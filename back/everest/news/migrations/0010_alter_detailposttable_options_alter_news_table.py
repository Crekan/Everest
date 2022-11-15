# Generated by Django 4.1.3 on 2022-11-10 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_detailposttable_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailposttable',
            options={'verbose_name': 'Таблица для поста', 'verbose_name_plural': 'Таблицы для постов'},
        ),
        migrations.AlterField(
            model_name='news',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_table', to='news.detailposttable', verbose_name='Таблица'),
        ),
    ]
