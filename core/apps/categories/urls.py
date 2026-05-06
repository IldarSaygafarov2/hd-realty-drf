from django.urls import path
from . import views

urlpatterns = [
    path("v1/categories/", views.CategoryListView.as_view(), name="categories-list")
]
