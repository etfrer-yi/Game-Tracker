from django.views.generic import ListView
from .models import Battlefield4Stats

# Create your views here.
class Battlefield4View(ListView):
    model = Battlefield4Stats
    template_name = "battlefield4/battlefield4.html"
    context_object_name = "player_records"
    paginate_by = 20