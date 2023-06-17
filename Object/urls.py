from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CompanyView, AddCompanyView, AdvertisementView, AddAdvertisementView

router = routers.DefaultRouter()
router.register('company', CompanyView, basename="company")
router.register('advertisement', AdvertisementView, basename="advertisement")

urlpatterns = [
    path("", include(router.urls)),
    path("company/user/<int:id>", AddCompanyView.as_view({"post": "post"}), name="add user to company"),
    path("advertisement/user/<int:id>", AddAdvertisementView.as_view({"post": "post"}), name="add user to advertisement"),
]