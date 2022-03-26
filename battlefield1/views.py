from .models import Battlefield1Stats
import django_filters
from django_filters.views import FilterView

class Battlefield1StatsFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(Battlefield1StatsFilter, self).__init__(*args, **kwargs)
        self.filters["gamer__icontains"].label = "Gamer (inexact, partial):"
        self.filters["platform__icontains"].label = "Platform (inexact, partial):"
        self.filters['rank__gte'].label = "Rank >= than:"
        self.filters['rank__lte'].label = "Rank <= than:"
        self.filters['game_score__gte'].label = "Game score >= than:"
        self.filters['game_score__lte'].label = "Game score <= than:"
        self.filters['games__gte'].label = "Games >= than:"
        self.filters['games__lte'].label = "Games <= than:"

    class Meta:
        model = Battlefield1Stats
        fields = {
            "gamer": ["icontains"],
            "platform": ["icontains"],
            "rank": ["gte", "lte"],
            "game_score": ["gte", "lte"],
            "games": ["gte", "lte"],
        }


# Create your views here.
class Battlefield1View(FilterView):
    model = Battlefield1Stats
    template_name = "battlefield1/battlefield1.html"
    context_object_name = "player_records"
    filterset_class = Battlefield1StatsFilter
    paginate_by = 20


