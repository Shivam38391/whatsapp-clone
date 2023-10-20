from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.


User = get_user_model()

def index(request):
    users = User.objects.exclude(username=request.user.username) # all user except the current user
    
    context= {"users": users}
    return render(request, "index.html", context)

def chatPage(request):
    
    users = User.objects.exclude(username=request.user.username) # all user except the current user
    
    context= {"users": users}
    return render(request, "main_chat.html", context)
    