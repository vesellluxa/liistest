from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import ArticleUser


class ArticleUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8,
                                     max_length=256,
                                     required=True)

    class Meta:
        model = ArticleUser
        fields = ('email', 'password')

    def validate_email(self, value):
        if self.Meta.model.objects.filter(email=value).exists():
            raise ValidationError('Email must be unique!')
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(**validated_data)
        return user
