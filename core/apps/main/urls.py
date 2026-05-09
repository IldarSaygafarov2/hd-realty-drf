from django.urls import path
from . import views

urlpatterns = [
    path("v1/faqs/", views.FAQListView.as_view(), name="faq-list"),
    path("v1/services/", views.ServiceListView.as_view(), name="service-list"),
    path("v1/portfolio/", views.PortfolioListView.as_view(), name="portfolio-list"),
]
