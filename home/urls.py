from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('account/', account, name='account'),
    path('tours/', TourListView.as_view(), name='tours'),
    path('tours_by_agent/', ToursByAgentListView.as_view(), name='tours_by_agent'),
    path('agents/', AgentListView.as_view(), name='agents'),
    path('tours/<int:pk>/', TourDetailView.as_view(), name='tour_detail'),
    path('agents/<int:pk>/', AgentDetailView.as_view(), name='agent_detail'),
    path('agents/<int:pk>/edit', AgentUpdateView.as_view(), name='agent_edit'),
]