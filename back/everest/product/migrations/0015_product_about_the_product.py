# Generated by Django 4.1.3 on 2022-11-15 18:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_characteristics_product_characteristics'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about_the_product',
            field=tinymce.models.HTMLField(null=True, verbose_name='Описание'),
        ),
    ]
