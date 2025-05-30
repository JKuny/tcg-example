from django.db.models import Q
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, TemplateView

from events.models import Event
from players.models import Player

def index(request):
    # Only get normal players, not superuser or staff
    latest_player_list = Player.objects.order_by('-user__date_joined').filter(
        user__is_superuser=False, user__is_staff=False)[:5]
    template = loader.get_template('players/index.html')
    context = {
        'latest_player_list': latest_player_list
    }
    return HttpResponse(template.render(context, request))


def details(request, player_id):
    current_player = Player.objects.get(id=player_id)
    template = loader.get_template('players/details.html')
    context = {
        'current_player': current_player
    }
    return HttpResponse(template.render(context, request))

class SearchResultsView(ListView):
    model = Event
    template_name = 'players/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Event.objects.filter(
            Q(event_name__icontains=query) | Q(state__icontains=query)
        )
        return object_list
