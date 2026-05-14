from rest_framework import generics
from . import models, serializers

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Advertisements"])
class AdvertisementListView(generics.ListAPIView):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementListSerializer


@extend_schema(tags=["Advertisements"])
class AdvertisementDetailView(generics.RetrieveAPIView):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementDetailSerializer
    lookup_field = "slug"
