from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from forum.models import Category
from notification.models import Notification


def index(request):
    template = loader.get_template('index.html')

    # user_notif = Notification.objects.filter(target_user=request.user, is_seen=False)

    if request.user.is_active:
        context = {
            'notif': Notification.objects.filter(target_user=request.user, is_seen=False)
        }
    else:
        context = {'logged_status': "You are not logged in!"}

    return HttpResponse(template.render(context, request))
