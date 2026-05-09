from django.shortcuts import render

from .serializers import DistrictSerializer
from .models import District
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView


@extend_schema(tags=["Districts"])
class DistrictListView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
