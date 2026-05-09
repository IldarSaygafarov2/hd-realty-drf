from rest_framework import serializers
from . import models


class ConsultationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConsultationRequest
        fields = ["id", "name", "phone", "goal", "comment", "created_at", "updated_at"]


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactRequest
        fields = ["id", "name", "phone", "comment", "created_at", "updated_at"]


class NextStepRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NextStepRequest
        fields = ["id", "name", "phone", "task_description", "created_at", "updated_at"]
