from django.views.generic.base import TemplateView
from .models import Battlefield4Stats, Battlefield1Stats, Battlefieldhardlinestats
from django.http import HttpResponse
import pandas as pd
import plotly.express as px
from plotly.io import to_html

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
    graph_filter_on = request.GET.getlist("graph_filter_on")[0]
    x_axis_filter = request.GET.getlist("x-axis")[0]
    y_axis_filter = request.GET.getlist("y-axis")[0]

    fields = [field.get_attname_column() for field in Battlefield1Stats._meta.get_fields()]
    django_to_db_col_map = {}
    for django_col, db_col in fields:
        django_to_db_col_map[django_col] = db_col
    x_col = django_to_db_col_map[x_axis_filter]
    y_col = django_to_db_col_map[y_axis_filter]
    if x_col == y_col:
        x_col += "(x-axis)"
        y_col += "(y-axis)"

    df_list = []
    bf_game_to_model_dict = {"bf1": Battlefield1Stats.objects, "bf4": Battlefield4Stats.objects, "bf_hardline": Battlefieldhardlinestats.objects}
    for bf_game in bf_games:
        df_list.append(pd.DataFrame(list(bf_game_to_model_dict[bf_game].filter(platform__in=platforms).values_list(x_axis_filter, y_axis_filter, "platform", "game_title")),
                                          columns=[x_col, y_col, "Platform", "Game Title"]))
    df = pd.concat(df_list)
    df.sort_values(by=[x_col], inplace=True)
    symbol = None if graph_filter_on == "overall" else ""
    category_orders = None if graph_filter_on == "overall" else {}
    if isinstance(symbol, str) and isinstance(category_orders, dict):
        if "game-title" in graph_filter_on:
            symbol = "Game Title"
            category_orders["Platform"] = ["pc", "psn", "xbox"]
        elif "platform" in graph_filter_on:
            symbol = "Platform"
            category_orders["Game Title"] = ["Battlefield 1", "Battlefield Hardline", "Battlefield 4"]
    # symbol_sequence = None if graph_filter_on == "overall" else ["circle-open", "circle-dot", "circle-open-dot"]
    graph_features = {
        "data_frame": df,
        "x": x_col,
        "y": y_col,
        "color": symbol,
        "symbol": symbol,
        # "symbol_sequence": symbol_sequence,
        "category_orders": category_orders
    }
    if graph_type == "scatter":
        graph_features["trendline"] = "ols"
        graph_features["trendline_scope"] = "overall" if graph_filter_on == "overall" else "trace"
        fig = px.scatter(**graph_features)
    else:
        fig = px.line(**graph_features)

    return HttpResponse(to_html(fig, include_plotlyjs=False, full_html=False))
