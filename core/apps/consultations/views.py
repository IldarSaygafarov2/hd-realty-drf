from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from . import models, serializers
from rest_framework import generics


@extend_schema(tags=["Consulations"])
class ConsulationRequestCreateView(generics.CreateAPIView):
    queryset = models.ConsultationRequest
    # serializer_class = serializers.ConsultationRequestCreationSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.ConsultationRequestCreationSerializer
        return serializers.ConsultationRequestSerializer
