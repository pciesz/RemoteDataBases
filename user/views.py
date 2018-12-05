from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.views.generic import View

from notification.models import Notification
from .forms import UserForm, UserLoginForm


# Create your views here.
def index(request):
    template = loader.get_template('user/index.html')
    context = {
        'notif': Notification.objects.all()
    }
    return HttpResponse(template.render(context, request))


def List(request):
    template = loader.get_template('user/list.html')
    user_list = User.objects.all()
    context = {
        'users': user_list
    }

    if request.user.is_active:
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("<h1>UNAUTHORIZED</h1>")




class UserFormView(View):
    form_class = UserForm
    template_name = 'user/user_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        else:
            #return render(request, 'user/user_exist.html')
            return HttpResponse("<h2>This user exist!</h2>")


def Logout(request):
    logout(request)
    return redirect('/')


class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'user/user_login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(username + ' ' + password)

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        else:
            return HttpResponse(str(form.errors))
