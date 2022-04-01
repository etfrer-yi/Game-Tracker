from django.urls import path
from .views import DataAnalyticsView, get_graph

urlpatterns = [
    path("", DataAnalyticsView.as_view(), name="data_analytics"),
    path("graph", get_graph, name="get_graph")
]