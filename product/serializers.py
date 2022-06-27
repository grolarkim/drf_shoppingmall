from rest_framework import serializers

from product.models import Category, Product, ProductImage, ProductOption


class CategorySerialier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "category"]
        extra_kwargs = {}
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["thumbnail", "full_image"]
        extra_kwargs = {}
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["user", "category", "images", "is_active", "title", "description"]
        extra_kwargs = {}
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product", "name", "description", "price"]
        extra_kwargs = {}
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)