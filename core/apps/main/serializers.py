from rest_framework import serializers

from . import models


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ["id", "question", "answer", "created_at", "updated_at"]


class ServiceIncludeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceInclude
        fields = ["id", "title"]


class ServiceSerializer(serializers.ModelSerializer):
    service_includes = ServiceIncludeSerializer(many=True)

    class Meta:
        model = models.Service
        fields = [
            "id",
            "title",
            "description",
            "deadlines",
            "format",
            "created_at",
            "updated_at",
            "service_includes",
        ]


class PortfolioJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PortfolioJob
        fields = ["id", "job", "created_at", "updated_at"]


class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PortfolioImage
        fields = ["id", "image", "created_at", "updated_at"]


class PortfolioSerializer(serializers.ModelSerializer):
    jobs = PortfolioJobSerializer(many=True)
    images = PortfolioImageSerializer(many=True)

    class Meta:
        model = models.Portfolio
        fields = ["id", "video", "created_at", "updated_at", "jobs", "images"]
