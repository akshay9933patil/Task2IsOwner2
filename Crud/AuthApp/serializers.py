from rest_framework import serializers
from django.contrib.auth.models import User as UserModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('username', 'password', 'first_name', 'last_name')


    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)