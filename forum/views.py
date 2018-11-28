from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from forum.models import Thread, Category, Entry


def index(request):
    template = loader.get_template('forum/index.html')

    context = {
        'categories': Category.objects.all()
    }

    return HttpResponse(template.render(context, request))


def category_view(request, id):
    template = loader.get_template('forum/category.html')

    context = {
        'threads': Thread.objects.filter(category=id)  # .order_by(lastModificationDate)
    }

    return HttpResponse(template.render(context, request))


def thread_view(request, id):
    template = loader.get_template('forum/thread.html')

    context = {
        'thread': Thread.objects.filter(id=id)[0],
        'posts': Entry.objects.filter(thread=id)
    }

    return HttpResponse(template.render(context, request))
