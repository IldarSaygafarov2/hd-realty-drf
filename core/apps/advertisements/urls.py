from django.urls import path

from . import views

urlpatterns = [
    path(
        "v1/advertisements/",
        views.AdvertisementListView.as_view(),
        name="advertisements-list",
    )
]
