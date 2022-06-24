from user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "fullname", "phone_number", "email"]
        extra_kwargs = {"password":{"write_only": True}}
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

