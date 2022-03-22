from django.contrib import admin
from home.models import Agent
from home.models import Tour
from home.models import Duration


admin.site.register(Tour)
admin.site.register(Agent)
admin.site.register(Duration)
