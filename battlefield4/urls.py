from django.urls import path, re_path
from .views import Battlefield4View, Battlefield4DetailView

urlpatterns = [
    path("", Battlefield4View.as_view(), name="battlefield4"),
    path("<int:pk>/", Battlefield4DetailView.as_view(), name="battlefield4_detailview"),
]