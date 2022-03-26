from django.urls import path
from .views import BattlefieldHardlineView
from . import views

urlpatterns = [
    path("", BattlefieldHardlineView.as_view(), name="battlefield_hardline")
]