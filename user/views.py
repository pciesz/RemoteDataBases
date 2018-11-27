from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.views.generic import View
from .forms import UserForm


# Create your views here.
def index(request):
    template = loader.get_template('user/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def list(request):
    template = loader.get_template('user/list.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

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
                    return redirect('index.html')
