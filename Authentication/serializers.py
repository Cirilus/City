import logging
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, IntegerField, \
    Serializer, CharField, SerializerMethodField, DecimalField

from Authentication.models import CustomUser

logger = logging.getLogger(__name__)


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("phone", "username", "email", "rating")
        extra_kwargs = {
            'rating': {'read_only': True},
        }
