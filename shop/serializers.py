from rest_framework import serializers

from shop.models import Product, Basket, ProductName, BrandName


class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductName
        fields = '__all__'


class BrandNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandName
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'
