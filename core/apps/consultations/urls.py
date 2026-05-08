from django.urls import path
from . import views

urlpatterns = [
    path(
        "v1/consultations/consultation-request/",
        views.ConsulationRequestCreateView.as_view(),
        name="create-consultation-request",
    )
]
