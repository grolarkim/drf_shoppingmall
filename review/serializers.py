from rest_framework import serializers

from review.models import Review, Like


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["product", "user", "rating", "content"]
        extra_kwargs = {}

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["product", "user"]
        extra_kwargs = {}

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
