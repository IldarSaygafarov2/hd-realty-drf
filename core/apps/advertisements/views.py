from rest_framework import generics
from . import models, serializers

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Advertisement"])
class AdvertisementListView(generics.ListAPIView):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementListSerializer
