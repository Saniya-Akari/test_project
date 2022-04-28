from rest_framework import serializers

from shop.models import Product, Shop, Category


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    shop = ShopSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'shop', 'image', 'update_counter']


