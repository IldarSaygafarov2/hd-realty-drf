from django.urls import path
from . import views

urlpatterns = [
    path("v1/districts/", views.DistrictListView.as_view(), name="districts-list"),
]
