from django.shortcuts import render

from .serializers import DistrictSerializer
from .models import District

from rest_framework.generics import ListAPIView


class DistrictListView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
