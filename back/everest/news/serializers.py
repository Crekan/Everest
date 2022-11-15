from rest_framework import serializers

from .models import *


class DetailPostTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPostTable
        fields = ('id', 'name', 'description', 'price')


class NewsSerializer(serializers.ModelSerializer):
    post_table = DetailPostTableSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'news_images', 'news_date', 'news_views', 'news_title', 'slug', 'description', 'post_table')
