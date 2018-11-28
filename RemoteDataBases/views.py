from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from forum.models import Category
from notification.models import Notification


def index(request):
    template = loader.get_template('index.html')

    categories = Category.objects.all()
    print(categories[0].id)

    context = {
        'notif': Notification.objects.filter(target_user=request.user, is_seen=False)
    }
    return HttpResponse(template.render(context, request))
