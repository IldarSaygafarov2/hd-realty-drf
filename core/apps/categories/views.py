from django.shortcuts import render

from rest_framework import generics

from . import models, serializers
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Categories"])
class CategoryListView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


@extend_schema(tags=["Categories"])
class RenovationTypesListView(generics.ListAPIView):
    queryset = models.RenovationType.objects.all()
    serializer_class = serializers.RenovationTypeSerializer


@extend_schema(tags=["Categories"])
class PropertyTypesListView(generics.ListAPIView):
    queryset = models.PropertyType.objects.all()
    serializer_class = serializers.PropertyTypeSerializer
