from django.urls import path
from .views import DataAnalyticsView
from . import views

urlpatterns = [
    path("", DataAnalyticsView.as_view(), name="data_analytics")
]