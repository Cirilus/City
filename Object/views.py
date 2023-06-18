from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiParameter
from rest_framework import status
from rest_framework.exceptions import NotFound, APIException
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, \
    ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin

from django.shortcuts import get_object_or_404, get_list_or_404

from Object.models import Company, Advertisement, News
from Object.serializers import CompanySerializer, AdvertisementSerializer, NewsSerializer


@extend_schema_view(
    retrieve=extend_schema(
        tags=['company'],
        summary="return company by id",
    ),
    list=extend_schema(
        tags=['company'],
        summary="return all company"
    ),
    destroy=extend_schema(
        tags=['company'],
        summary="delete the company",
    ),
    partial_update=extend_schema(
        tags=['company'],
        summary="update the company"
    ),
    create=extend_schema(
        tags=['company'],
        summary="create the company"
    ),
)
class CompanyView(GenericViewSet,
                  ListModelMixin,
                  RetrieveModelMixin,
                  CreateModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin):
    serializer_class = CompanySerializer

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Company, id=pk)

    def get_queryset(self):
        return Company.objects.all()

    http_method_names = ["patch", "get", "delete", "post"]


class AddCompanyView(GenericViewSet):

    @extend_schema(tags=["company"],
                   summary="add the user to company",
                   parameters=[OpenApiParameter("user_id", str, "query", True)],
                   responses={
                       201: None
                   }, )
    def post(self, request, id):
        company_id = id
        user_id = request.query_params.get("user_id")
        try:
            Company.objects.get(pk=company_id).administrator.add(user_id)
        except Exception as e:
            raise NotFound(e)
        return Response(status=201)


@extend_schema_view(
    retrieve=extend_schema(
        tags=['advertisement'],
        summary="return company by advertisement",
    ),
    list=extend_schema(
        tags=['advertisement'],
        summary="return all advertisement"
    ),
    destroy=extend_schema(
        tags=['advertisement'],
        summary="delete the advertisement",
    ),
    partial_update=extend_schema(
        tags=['advertisement'],
        summary="update the advertisement"
    ),
    create=extend_schema(
        tags=['advertisement'],
        summary="create the advertisement"
    ),
)
class AdvertisementView(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin,
                        CreateModelMixin,
                        UpdateModelMixin,
                        DestroyModelMixin):
    serializer_class = AdvertisementSerializer
    http_method_names = ["patch", "get", "delete", "post"]

    def get_object(self):
        pk = self.kwargs['pk']
        advertisement = get_object_or_404(Advertisement, id=pk)
        if advertisement.is_active:
            return advertisement
        else:
            raise APIException("The object haven't been moderated yet")

    def get_queryset(self):
        return Advertisement.objects.all().filter(is_active=True)


class AddAdvertisementView(GenericViewSet):
    @extend_schema(tags=["advertisement"],
                   summary="add the user to advertisement",
                   parameters=[OpenApiParameter("user_id", str, "query", True)],
                   responses={
                       201: None
                   }, )
    def post(self, request, id):
        advertisement_id = id
        user_id = request.query_params.get("user_id")
        try:
            Advertisement.objects.get(pk=advertisement_id).administrator.add(user_id)
        except Exception as e:
            raise NotFound(e)
        return Response(status=201)


@extend_schema_view(
    retrieve=extend_schema(
        tags=['news'],
        summary="return company by news",
    ),
    list=extend_schema(
        tags=['news'],
        summary="return all news"
    ),
    destroy=extend_schema(
        tags=['news'],
        summary="delete the news",
    ),
    partial_update=extend_schema(
        tags=['news'],
        summary="update the news"
    ),
    create=extend_schema(
        tags=['news'],
        summary="create the news"
    ),
)
class NewsView(GenericViewSet,
               ListModelMixin,
               RetrieveModelMixin,
               CreateModelMixin,
               UpdateModelMixin,
               DestroyModelMixin):
    serializer_class = NewsSerializer
    http_method_names = ["patch", "get", "delete", "post"]

    def get_object(self):
        pk = self.kwargs['pk']
        news = get_object_or_404(News, id=pk)
        if news.is_active:
            return news
        else:
            raise APIException("The object haven't been moderated yet")

    def get_queryset(self):
        return News.objects.all().filter(is_active=True)


class AddNewsView(GenericViewSet):
    @extend_schema(tags=["news"],
                   summary="add the user to news",
                   parameters=[OpenApiParameter("user_id", str, "query", True)],
                   responses={
                       201: None
                   }, )
    def post(self, request, id):
        news_id = id
        user_id = request.query_params.get("user_id")
        try:
            News.objects.get(pk=news_id).administrator.add(user_id)
        except Exception as e:
            raise NotFound(e)
        return Response(status=201)
