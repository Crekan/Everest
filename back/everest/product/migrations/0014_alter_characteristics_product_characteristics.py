# Generated by Django 4.1.3 on 2022-11-15 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_characteristics_product_characteristics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='product_characteristics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_characteristics', to='product.product', verbose_name='Продукт'),
        ),
    ]
