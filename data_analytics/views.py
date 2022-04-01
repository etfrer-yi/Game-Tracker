from django.views.generic.base import TemplateView
from .models import Battlefield4Stats, Battlefield1Stats, Battlefieldhardlinestats
from django.http import HttpResponse
import pandas as pd

class DataAnalyticsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Note that Battlefield1Stats is taken, but it could've been any of the other two BF games;
        # the important thing is to grab the different columns from them.
        context['numeric_fields'] = [field.get_attname_column() for field in Battlefield1Stats._meta.get_fields() if
                                      ("Integer" in field.get_internal_type() or "Float" in field.get_internal_type()) and not
                                      field.get_attname_column()[1] == "index"]
        return context

    template_name = "data_analytics/data_analytics.html"

def get_graph(request):
    bf_games = request.GET.getlist("bf_games")
    platforms = request.GET.getlist("platforms")
    graph_type = request.GET.getlist("graph_type")[0]
    x_axis_filter = request.GET.getlist("x-axis")[0]
    y_axis_filter = request.GET.getlist("y-axis")[0]

    df_list = []
    bf_game_to_model_dict = {"bf1": Battlefield1Stats.objects, "bf4": Battlefield4Stats.objects, "bf_hardline": Battlefieldhardlinestats.objects}
    for bf_game in bf_games:
        df_list.append(pd.DataFrame(list(bf_game_to_model_dict[bf_game].filter(platform__in=platforms).values_list(x_axis_filter, y_axis_filter, "platform")),
                                          columns=[x_axis_filter, y_axis_filter]))
    df = pd.concat(df_list)
    return HttpResponse("abc")
