from django.urls import path
from . import views
from .views import SearchResultsView

app_name = "events"

urlpatterns = [
    path("", views.index, name="events"),
    path("<int:event_id>/", views.details, name="detail"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]
