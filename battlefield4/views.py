from django.shortcuts import render
from django.views.generic import ListView
from .models import Battlefield4Stats

# Create your views here.
class Battlefield4View(ListView):
    model = Battlefield4Stats
    template_name = "battlefield4/battlefield4.html"