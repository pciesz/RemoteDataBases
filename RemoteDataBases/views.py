from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from notification.models import Notification


def index(request):
    template = loader.get_template('index.html')

    if request.user.is_active:
        context = {'notif': Notification.objects.filter(target_user=request.user, is_seen=False)}
    else:
        context = {'notif': Notification.objects.none()}

    return HttpResponse(template.render(context, request))
