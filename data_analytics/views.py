from django.http import HttpResponse
from django.views.generic import ListView
from .models import Battlefield4Stats, Battlefield1Stats

# Create your views here.
def index(request):
    return HttpResponse("abc")