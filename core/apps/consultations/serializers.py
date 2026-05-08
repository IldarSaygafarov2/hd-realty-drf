from rest_framework import serializers
from . import models


class ConsultationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConsultationRequest
        fields = ["id", "name", "phone", "goal", "comment", "created_at", "updated_at"]


class ConsultationRequestCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConsultationRequest
        fields = ["name", "phone", "goal", "comment"]
