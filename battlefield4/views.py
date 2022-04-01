from .models import Battlefield4Stats
import django_filters
from django_filters.views import FilterView
from django.views.generic.detail import DetailView

class Battlefield4StatsFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(Battlefield4StatsFilter, self).__init__(*args, **kwargs)
        self.filters["gamer__icontains"].label = "Gamer (inexact, partial):"
        self.filters["platform__icontains"].label = "Platform (inexact, partial):"
        self.filters['rank__gte'].label = "Rank >= than:"
        self.filters['rank__lte'].label = "Rank <= than:"
        self.filters['game_score__gte'].label = "Game score >= than:"
        self.filters['game_score__lte'].label = "Game score <= than:"
        self.filters['games__gte'].label = "Games >= than:"
        self.filters['games__lte'].label = "Games <= than:"

    class Meta:
        model = Battlefield4Stats
        fields = {
            "gamer": ["icontains"],
            "platform": ["icontains"],
            "rank": ["gte", "lte"],
            "game_score": ["gte", "lte"],
            "games": ["gte", "lte"],
        }

class Battlefield4View(FilterView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        return context

    model = Battlefield4Stats
    template_name = "battlefield4/battlefield4.html"
    context_object_name = "player_records"
    filterset_class = Battlefield4StatsFilter
    paginate_by = 100

class Battlefield4DetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        original_player_record_url_root = "https://battlefieldtracker.com/bf4/stats/"
        record = self.object
        context['original_player_record_url'] = original_player_record_url_root + record.original_platform + "/" + record.gamer
        context['original_player_list_url'] = "https://battlefieldtracker.com/bf4/leaderboards/all"
        return context

    model = Battlefield4Stats
    context_object_name = "player_record"
    template_name = "battlefield4/battlefield4_detailview.html"




