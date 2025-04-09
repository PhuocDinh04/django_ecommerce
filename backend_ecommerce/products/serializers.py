from rest_framework import serializers
from .models import Category, Product, ProductImage, ProductComment

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    comments = ProductCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'unit', 'price', 'discount', 'amount', 'is_public', 'thumbnail', 'images', 'comments', 'category_id', 'created_at', 'updated_at', 'deleted_at')

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'icon_url', 'products', 'created_at', 'updated_at')