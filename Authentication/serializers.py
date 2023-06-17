import logging
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, IntegerField, \
    Serializer, CharField, SerializerMethodField, DecimalField

from Authentication.models import CustomUser

logger = logging.getLogger(__name__)


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "phone", "username", "email", "rating", "password")
        extra_kwargs = {
            'rating': {'read_only': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
