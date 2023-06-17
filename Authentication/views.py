from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiParameter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, \
    ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserSerializer
from .models import CustomUser


@extend_schema_view(
    retrieve=extend_schema(
        tags=['auth'],
        summary="return user by id",
    ),
    list=extend_schema(
        tags=['auth'],
        summary="return all user"
    ),
    destroy=extend_schema(
        tags=['auth'],
        summary="delete the user",
    ),
    partial_update=extend_schema(
        tags=['auth'],
        summary="update the user"
    ),
    create=extend_schema(
        tags=['auth'],
        summary="create the user"
    ),
)
class UserView(GenericViewSet,
               ListModelMixin,
               RetrieveModelMixin,
               CreateModelMixin,
               UpdateModelMixin,
               DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = CustomUser

    http_method_names = ["patch", "get", "delete", "post"]
