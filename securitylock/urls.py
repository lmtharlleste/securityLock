from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


BASE_URL = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_URL, include('core.urls')),
]
