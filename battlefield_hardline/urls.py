from django.urls import path
from .views import BattlefieldHardlineView, BattlefieldHardlineDetailView
from . import views

urlpatterns = [
    path("", BattlefieldHardlineView.as_view(), name="battlefield_hardline"),
    path("<int:pk>/", BattlefieldHardlineDetailView.as_view(), name="battlefield_hardline_detailview"),
]