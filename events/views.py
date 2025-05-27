from django.http import HttpResponse
from django.template import loader

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
    return HttpResponse("You're looking at event %s" % event_id)