from django.shortcuts import render

from rest_framework import generics
from drf_spectacular.utils import extend_schema
from . import models, serializers


@extend_schema(tags=["Main"])
class FAQListView(generics.ListAPIView):
    queryset = models.FAQ
    serializer_class = serializers.FAQSerializer


@extend_schema(tags=["Main"])
class ServiceListView(generics.ListAPIView):
    queryset = models.Service
    serializer_class = serializers.ServiceSerializer


@extend_schema(tags=["Main"])
class PortfolioListView(generics.ListAPIView):
    queryset = models.Portfolio
    serializer_class = serializers.PortfolioSerializer
