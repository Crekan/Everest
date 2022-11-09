from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TrademarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trademark
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    cat_product = CategorySerializer(
        many=True,
        read_only=True
    )
    brand_name = TrademarkSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = ('id', 'images', 'title', 'new_price', 'old_price', 'cat_product', 'brand_name')
