from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

from events.models import Event


# Create your views here.
def index(request):
    latest_events_list = Event.objects.order_by('-start_date')[:5]
    template = loader.get_template('events/index.html')
    context = {
        'latest_events_list': latest_events_list,
    }
    return HttpResponse(template.render(context, request))


def details(request, event_id):
    current_event = Event.objects.get(id=event_id)
    template = loader.get_template('events/details.html')
    context = {
        'current_event': current_event
    }
    return HttpResponse(template.render(context, request))

class SearchResultsView(ListView):
    model = Event
    template_name = 'events/search_results.html'

    def get_queryset(self):
        return Event.objects.filter(game_name__icontains='Pokemon')