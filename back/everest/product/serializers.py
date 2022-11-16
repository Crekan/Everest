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


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'is_active')


class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'email', 'text', 'date_added')


class ProductSerializer(serializers.ModelSerializer):
    cat_product = CategorySerializer(
        many=True,
        read_only=True
    )
    brand_name = TrademarkSerializer(
        many=True,
        read_only=True
    )
    product_image = ProductImageSerializer(
        many=True,
        read_only=True
    )
    product_characteristics = CharacteristicsSerializer(
        many=True,
        read_only=True
    )
    comment_post = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = ('id', 'images', 'title', 'new_price', 'old_price', 'cat_product', 'brand_name', 'product_image',
                  'about_the_product', 'product_characteristics', 'comment_post')
