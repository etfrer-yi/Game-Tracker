from django.shortcuts import render
from django.views.generic import ListView
from .models import Battlefield1Stats

# Create your views here.
class Battlefield1View(ListView):
    model = Battlefield1Stats
    template_name = "battlefield1/battlefield1.html"