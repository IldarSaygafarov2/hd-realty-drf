from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Categories"])
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
