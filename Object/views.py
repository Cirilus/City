from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiParameter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, \
    ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404, get_list_or_404

from Object.models import Company
from Object.serializers import CompanySerializer


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
    queryset = Company

    @extend_schema(tags=["company"],
                   summary="add the user to company",
                   request=[OpenApiParameter("company_id", str, "path", True),
                            OpenApiParameter("user_id", str, "query", True)],
                   responses={
                       201: None
                   }, )
    def post(self, request, id):
        company_id = id
        user_id = request.query_params.get("user_id")
        Company.objects.get(pk=company_id).administrator.add(user_id)
        return Response(status=201)
