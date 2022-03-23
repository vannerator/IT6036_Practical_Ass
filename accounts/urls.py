from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import *



urlpatterns = [
    path('change_password/', auth_views.PasswordChangeView.as_view(
            template_name='registration/change_password.html',
            success_url = reverse_lazy('change_password_done'),
        ),
        name='change_password'
    ),
    path('change_password_done/', change_password_done, name='change_password_done'),
]
