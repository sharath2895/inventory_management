from rest_framework import serializers
from django.db import models
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'first_name', 'last_name', 'role', 'mobile',
        #           'email', 'created_at', 'updated_at', 'intro', 'profile','username',]
        fields = "__all__"
        depth = 1
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user_instance = super().create(validated_data)
        if password:
            user_instance.set_password(password)
            user_instance.save()
        return user_instance


