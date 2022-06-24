from user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "fullname", "phone_number", "email"]
        extra_kwargs = {"password":{"write_only": True}}
        


