from rest_framework import serializers

from . import models


class AdvertisementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertisementImage
        fields = ["id", "image", "created_at", "updated_at"]


class AdvertisementCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertisementCharacterstic
        fields = ["id", "key", "value", "created_at", "updated_at"]


class AdvertisementListSerializer(serializers.ModelSerializer):
    images = AdvertisementImageSerializer(many=True)
    characteristics = AdvertisementCharacteristicSerializer(many=True)

    class Meta:
        model = models.Advertisement
        fields = [
            "id",
            "title",
            "slug",
            "price_usd",
            "price_uzs",
            "preview",
            "complex_name",
            "images",
            "characteristics",
            "created_at",
        ]
