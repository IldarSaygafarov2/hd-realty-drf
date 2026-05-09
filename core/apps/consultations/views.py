from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from . import models, serializers
from rest_framework import generics


@extend_schema(tags=["Consultations"])
class ConsulationRequestCreateView(generics.CreateAPIView):
    queryset = models.ConsultationRequest
    serializer_class = serializers.ConsultationRequestSerializer


@extend_schema(tags=["Consultations"])
class ContactRequestCreateView(generics.CreateAPIView):
    queryset = models.ContactRequest
    serializer_class = serializers.ContactRequestSerializer


@extend_schema(tags=["Consultations"])
class NextStepRequestCreateView(generics.CreateAPIView):
    queryset = models.NextStepRequest
