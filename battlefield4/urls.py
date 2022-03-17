from django.urls import path
from .views import Battlefield4View
from . import views

urlpatterns = [
    path("", Battlefield4View.as_view(), name="battlefield4")
]