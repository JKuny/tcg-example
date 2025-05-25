from django.http import HttpResponse
from django.template import loader

from events.models import Tournament


# Create your views here.
def index(request):
    latest_tournaments_list = Tournament.objects.order_by('-start_date')[:5]
    template = loader.get_template('tournaments/index.html')
    context = {
        'latest_tournaments_list': latest_tournaments_list,
    }
    return HttpResponse(template.render(context, request))
