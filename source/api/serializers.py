from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get("category", instance.category)
        instance.save()

        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
