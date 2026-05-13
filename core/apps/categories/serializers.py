from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["id", "name", "slug", "created_at", "updated_at"]


class RenovationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RenovationType
        fields = ["id", "title", "slug", "created_at", "updated_at"]


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PropertyType
        fields = ["id", "title", "slug", "created_at", "updated_at"]
