from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.views import View

import user
from forum.forms import EntryForm
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


class EntryFormView(View):
    form_class = EntryForm
    template_name = 'forum/thread.html'

    def get(self, request, id):
        form = self.form_class(None)

        entry_context = {
            'thread': Thread.objects.filter(id=id)[0],
            'posts': Entry.objects.filter(thread=id),
            'form': form
        }

        print("size")
        print(len(entry_context['posts']))

        return render(request=request, template_name=self.template_name, context=entry_context)

    def post(self, request, id):
        form = self.form_class(request.POST)
        active_user = request.user

        entry_context = {
            'thread': Thread.objects.filter(id=id)[0],
            'posts': Entry.objects.filter(thread=id),
            'form': form
        }

        if active_user is not None:
            if active_user.is_active:
                if form.is_valid():
                    content = form.cleaned_data['content']

                    print(content)
                    return render(request=request, template_name=self.template_name, context=entry_context)
