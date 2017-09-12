from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userchats.models import Chat, ChatLine
from django.core.mail import send_mail
# Create your views here.
def dashboard_view(request):
    """
    This view renders the dashboard page
    with url accounts/profile on login

    """
    print(request.meta)
    html_message = "<p style='background-color: blue'>This is a sample html message</p>"
    send_mail(
        "Welcome to Dashoard",
        "html message",
        "tesabunor@gmail.com",
        ["tegaesabunor@gmail.com"],
        fail_silently=True,
        html_message=html_message,
    )
    return render(request, "dashboard.html")

def profile_view(request):
    """
    This view renders the profile page
    
    """
    return render(request, "profile.html")

def search_view(request):
    """
    This view renders the search page

    """
    return render(request, "search.html")

def settings_view(request):
    """
    This view renders the settings page

    """
    return render(request, "settings.html")

@login_required
def inbox(request):
    heartuser = request.user.heartuser
    users = []
    last_messages = []
    chats = Chat.objects.filter(users__id=heartuser.id)
    for chat in chats:
        users += [chat.users.all().exclude(heartuser__id=heartuser.id)[0]]
        last_messages += [chat.chatline_set.all().order_by('-created_at')[0].message]
        print(users)
        print(last_messages)
    users_and_messages = zip(users, last_messages)
    users_and_messages = list(users_and_messages)
    print(users_and_messages)
    print(type(users_and_messages))
    return render(request, "inbox.html", {'users_and_messages':users_and_messages})