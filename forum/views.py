import datetime

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.views import View

import user
from forum.forms import EntryForm, ThreadForm, CategoryForm
from forum.models import Thread, Category, Entry
from notification.models import Notification


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
                    post = form.save(commit=False)

                    post.user = active_user
                    post.content = form.cleaned_data['content']
                    post.thread = Thread.objects.get(pk=id)
                    post.date = datetime.datetime.now()
                    post.deleted = False

                    post.save()
                    m = "New post in " + post.thread.subject
                    Notification.objects.create(target_user=active_user, message=m)

                    return render(request=request, template_name=self.template_name, context=entry_context)


class ThreadFormView(View):
    form_class = ThreadForm
    template_name = 'forum/category.html'
    pid = 0

    def get(self, request, id):
        form = self.form_class(None)

        context = {
            'category': Category.objects.get(pk=id),
            'threads': Thread.objects.filter(category=id),
            'form': form
        }

        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request, id):
        form = self.form_class(request.POST)
        active_user = request.user

        context = {
            'category': self.pid,
            'threads': Thread.objects.filter(category=id),
            'form': form
        }

        if active_user is not None:
            if active_user.is_active:
                if form.is_valid():
                    thread = form.save(commit=False)

                    thread.subject = form.cleaned_data['subject']
                    thread.category = Category.objects.get(pk=id)
                    thread.lastModificationDate = datetime.datetime.now()

                    thread.save()

                    return render(request=request, template_name=self.template_name, context=context)

        redirect('/')


class CategoryFormView(View):
    form_class = CategoryForm
    template_name = 'forum/index.html'
    pid = 0

    def get(self, request):
        form = self.form_class(None)

        context = {
            'categories': Category.objects.all(),
            'form': form
        }

        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST)
        active_user = request.user

        context = {
            'categories': Category.objects.all(),
            'form': form
        }

        if active_user is not None:
            if active_user.is_active:
                if form.is_valid():
                    category = form.save(commit=False)

                    category.name = form.cleaned_data['name']
                    category.visibleForConsumer = True

                    category.save()

                    return render(request=request, template_name=self.template_name, context=context)

        redirect('/')
