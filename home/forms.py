from django.db import models
from .models import Agent
from django.forms import ModelForm

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'provider', 'email_address', 'phone_number']