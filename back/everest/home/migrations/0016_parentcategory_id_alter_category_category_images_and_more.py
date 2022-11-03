# Generated by Django 4.1.3 on 2022-11-03 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_parentcategory_id_remove_parentcategory_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_images',
            field=models.ImageField(null=True, upload_to='category_images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='home.category', verbose_name='К какой категории отностится'),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='parent_category_name',
            field=models.CharField(max_length=250, null=True, verbose_name='Под категория'),
        ),
    ]