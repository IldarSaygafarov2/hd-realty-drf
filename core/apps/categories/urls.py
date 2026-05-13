from django.urls import path
from . import views

urlpatterns = [
    path("v1/categories/", views.CategoryListView.as_view(), name="categories-list"),
    path(
        "v1/renovation-types/",
        views.RenovationTypesListView.as_view(),
        name="renovation-types-list",
    ),
    path(
        "v1/property-types/",
        views.PropertyTypesListView.as_view(),
        name="property-types-list",
    ),
]
