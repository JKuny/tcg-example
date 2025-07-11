from django.db.models import Q
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

from events.models import Event


# Create your views here.
def index(request):
    latest_events_list = Event.objects.order_by("-start_date")[:9]
    if len(latest_events_list) == 0:
        latest_events_list = Event.objects.all()

    template = loader.get_template("events/index.html")
    context = {
        "latest_events_list": latest_events_list,
    }
    return HttpResponse(template.render(context, request))


def details(request, event_id):
    current_event = Event.objects.get(id=event_id)
    template = loader.get_template("events/details.html")
    context = {"current_event": current_event}
    return HttpResponse(template.render(context, request))


class SearchResultsView(ListView):
    model = Event
    template_name = "events/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("event_search")
        object_list = Event.objects.filter(
            Q(game_name__icontains=query)
        )
        return object_list
