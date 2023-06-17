import logging
import environ
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, IntegerField, \
    Serializer, CharField, SerializerMethodField, DecimalField
from yandex_geocoder import Client

from Object.models import Company, Advertisement

logger = logging.getLogger(__name__)

env = environ.Env()
environ.Env.read_env()

YandexApiKey = env.str("YANDEX_GEOCODER", "")

yandex_client = Client(YandexApiKey)


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "title", "description", "email", "phone",
                  "location", "latitude", "longitude", "category", "administrator")
        extra_kwargs = {
            'latitude': {'read_only': True},
            'longitude': {'read_only': True},
            'administrator': {'read_only': True},
        }

    def create(self, validated_data):
        coords = yandex_client.coordinates(validated_data['location'])
        validated_data['latitude'] = coords[0]
        validated_data['longitude'] = coords[1]
        return super().create(validated_data)


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ("id", "title", "body", "email", "phone", "administrator", "is_active")
        extra_kwargs = {
            'administrator': {'read_only': True},
            '"is_active"': {'read_only': True},
        }
