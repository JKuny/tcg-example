from django.http import HttpResponse
from django.template import loader

from players.models import Player


def index(request):
    latest_player_list = Player.objects.order_by('-user__date_joined')[:5]
    template = loader.get_template('players/index.html')
    context = {
        'latest_player_list': latest_player_list
    }
    return HttpResponse(template.render(context, request))


def details(request, player_id):
    return HttpResponse("Viewing player %s" % player_id)