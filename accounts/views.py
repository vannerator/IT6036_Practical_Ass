from django.shortcuts import render

# custom view for change password page
def change_password_done(request):
    return render(request, 'registration/change_password_done.html')