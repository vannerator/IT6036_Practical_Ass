from django.shortcuts import render

def change_password_done(request):
    return render(request, 'registration/change_password_done.html')