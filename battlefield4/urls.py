from django.urls import path, re_path
from .views import Battlefield4View, Battlefield4DetailView

urlpatterns = [
    path("", Battlefield4View.as_view(), name="battlefield4"),
    path("<slug:pk>", Battlefield4DetailView.as_view(), name="battlefield4_detailview"),
    # re_path(r'^<slug:pk>/$', Battlefield4DetailView.as_view(), name="battlefield4_paginated_detailview")
]