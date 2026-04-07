from rest_framework import serializers
from .models import Category, Product

# Category моделийг JSON руу хөрвүүлэгч
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Product моделийг JSON руу хөрвүүлэгч
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'