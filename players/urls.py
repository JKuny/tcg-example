from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('', views.index, name='players'),
    path('<int:player_id>', views.details, name='detail'),
    path('search/', views.SearchResultsView.as_view(), name="search_results"),
]