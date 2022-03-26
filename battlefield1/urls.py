from django.urls import path
from .views import Battlefield1View, Battlefield1DetailView
from . import views

urlpatterns = [
    path("", Battlefield1View.as_view(), name="battlefield1"),
    path("<int:pk>/", Battlefield1DetailView.as_view(), name="battlefield1_detailview"),
]