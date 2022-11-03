from rest_framework import serializers

from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('slider_images', 'slider_title', 'slider_description')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'news_images', 'news_date', 'total_views', 'news_title', 'slug')


class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCategory
        fields = ('id', 'parent_category_name')


class CategorySerializer(serializers.ModelSerializer):
    parent = ParentCategorySerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Category
        fields = ('id', 'category_images', 'category_title', 'parent')
