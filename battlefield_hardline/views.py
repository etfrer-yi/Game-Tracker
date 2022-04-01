from .models import Battlefieldhardlinestats
import django_filters
from django_filters.views import FilterView
from django.views.generic.detail import DetailView

class BattlefieldHardlineStatsFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(BattlefieldHardlineStatsFilter, self).__init__(*args, **kwargs)
        self.filters["gamer__icontains"].label = "Gamer (inexact, partial):"
        self.filters["platform__icontains"].label = "Platform (inexact, partial):"
        self.filters['rank__gte'].label = "Rank >= than:"
        self.filters['rank__lte'].label = "Rank <= than:"
        self.filters['game_score__gte'].label = "Game score >= than:"
        self.filters['game_score__lte'].label = "Game score <= than:"
        self.filters['games__gte'].label = "Games >= than:"
        self.filters['games__lte'].label = "Games <= than:"

    class Meta:
        model = Battlefieldhardlinestats
        fields = {
            "gamer": ["icontains"],
            "platform": ["icontains"],
            "rank": ["gte", "lte"],
            "game_score": ["gte", "lte"],
            "games": ["gte", "lte"],
        }

class BattlefieldHardlineView(FilterView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        return context

    model = Battlefieldhardlinestats
    template_name = "battlefield_hardline/battlefield_hardline.html"
    context_object_name = "player_records"
    filterset_class = BattlefieldHardlineStatsFilter
    paginate_by = 100


class BattlefieldHardlineDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        original_player_record_url_root = "https://battlefieldtracker.com/bfh/stats/"
        record = self.object
        context['original_player_record_url'] = original_player_record_url_root + record.original_platform + "/" + record.gamer
        context['original_player_list_url'] = "https://battlefieldtracker.com/bfh/leaderboards/all"
        return context

    model = Battlefieldhardlinestats
    context_object_name = "player_record"
    template_name = "battlefield_hardline/battlefield_hardline_detailview.html"
