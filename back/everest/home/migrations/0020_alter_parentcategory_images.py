# Generated by Django 4.1.3 on 2022-11-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_parentcategory_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentcategory',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='parent_category_images/', verbose_name='Изображение'),
        ),
    ]