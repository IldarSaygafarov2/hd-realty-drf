from rest_framework import serializers

from . import models
from core.apps.categories.serializers import (
    CategorySerializer,
    RenovationTypeSerializer,
)
from core.apps.districts.serializers import DistrictSerializer


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


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    images = AdvertisementImageSerializer(many=True)
    characteristics = AdvertisementCharacteristicSerializer(many=True)
    category = CategorySerializer(many=False)
    renovation_type = RenovationTypeSerializer(many=False)
    district = DistrictSerializer(many=False)

    class Meta:
        model = models.Advertisement
        fields = [
            "id",
            "title",
            "slug",
            "price_usd",
            "price_uzs",
            "total_area",
            "living_space",
            "ceiling_height",
            "address",
            "city",
            "complex_name",
            "special_conditions",
            "description",
            "operation_type",
            "number_of_floors",
            "year_of_construction",
            "rooms_quantity",
            "is_moderated",
            "district",
            # foreigns
            "renovation_type",
            "category",
            "images",
            "characteristics",
        ]

    # with default values
