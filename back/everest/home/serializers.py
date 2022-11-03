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


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='parent_category_name'
    )

    class Meta:
        model = Category
        fields = ('id', 'category_images', 'category_title', 'parent')
