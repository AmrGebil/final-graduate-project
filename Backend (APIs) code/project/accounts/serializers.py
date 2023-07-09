# from django.contrib.auth.models import User
# from rest_framework import serializers
# # from rest_framework.authtoken.models import Token
# # from rest_framework.response import Response
#
# fields = ['username', 'email', 'password1', 'password2']
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password1', 'password2')
#         extra_kwargs = {'password1': {'write_only': True, 'required': True},
#                         'password2': {'write_only': True, 'required': True}}
#*******************************************************************************

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile,MedicalHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        UserProfile.objects.create(user=user)
        MedicalHistory.objects.create(user=user)

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        return super().update(instance, validated_data)







class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        exclude = ('user',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        return super().update(instance, validated_data)




