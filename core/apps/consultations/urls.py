from django.urls import path
from . import views

urlpatterns = [
    path(
        "v1/consultations/consultation-request/",
        views.ConsulationRequestCreateView.as_view(),
        name="create-consultation-request",
    ),
    path(
        "v1/consultations/contact-request/",
        views.ContactRequestCreateView.as_view(),
        name="create-contact-request",
    ),
    path(
        "v1/consultations/next-step-request/",
        views.NextStepRequestCreateView.as_view(),
        name="create-next-step-request",
    ),
]
