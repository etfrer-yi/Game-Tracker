from django.urls import path
from .views import Battlefield1View
from . import views

urlpatterns = [
    path("", Battlefield1View.as_view(), name="battlefield1")
]