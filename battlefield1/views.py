from django.views.generic import ListView
from .models import Battlefield1Stats

# Create your views here.
class Battlefield1View(ListView):
    model = Battlefield1Stats
    template_name = "battlefield1/battlefield1.html"
    context_object_name = "player_records"
    paginate_by = 20