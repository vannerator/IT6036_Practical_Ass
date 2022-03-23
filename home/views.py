from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

from .models import Tour, Agent
from .forms import AgentForm



"""
The classes defined below are function based view (FBV).
"""
def home(request):
    return render(request, 'index.html')

def account(request):
    return render(request, 'account.html')


def login(request):
    return render(request, 'login.html')

"""
The classes defined below are class based view (CBV).

if you use ListView, you have to define the corresponding model
(declared in models.py under home). As ListView is used to do the
interaction with Database.
"""

class TourListView(ListView):
    queryset = Tour.objects.all().order_by('tour_name')

    # setup template file
    template_name = 'tours.html'

    # setup “friendly” template context
    # if not set up, 'tour_list' used as default
    # setting 'context_object_name' is always a good idea
    context_object_name = 'tours'

    # setup how many data to display per page
    paginate_by = 10

class ToursByAgentListView(ListView):
    queryset = Tour.objects.all().order_by('tour_name')

    template_name = 'tours_by_agent.html'

    context_object_name = 'tours'

    paginate_by = 10

class AgentListView(ListView):
    queryset = Agent.objects.all().order_by('provider')

    # setup template file
    template_name = 'agents.html'

    context_object_name = 'agents'

    # setup how many data to display per page
    paginate_by = 10


class TourDetailView(DetailView):
    queryset = Tour.objects.all().order_by('tour_name')

    template_name = 'tour_detail.html'

    context_object_name = 'tour'

class AgentDetailView(DetailView):
    queryset = Agent.objects.all()

    template_name = 'agent_detail.html'

    context_object_name = 'agent'

# view for Agent form
class AgentUpdateView(UpdateView):
    queryset = Agent.objects.all()
    form_class = AgentForm
    template_name = "agent_edit.html"
    context_object_name = 'agent'

