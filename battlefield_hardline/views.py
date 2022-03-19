from django.views.generic import ListView
from .models import Battlefieldhardlinestats

# Create your views here.
class BattlefieldHardlineView(ListView):
    model = Battlefieldhardlinestats
    template_name = "battlefield_hardline/battlefield_hardline.html"
    context_object_name = "player_records"
    paginate_by = 20