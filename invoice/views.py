import datetime
from itertools import chain

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.cache import never_cache

# Create your views here.
from django.views import View

from invoice.forms import InvoiceForm
from invoice.models import Invoice
from notification.models import Notification


class ReadAbleInvoice:
    pass

@never_cache
def index(request):
    template = loader.get_template('invoice/index.html')

    context = {
        'invoices': Invoice.objects.filter()
    }

    if request.user.is_active:
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("<h1>UNAUTHORIZED</h1>")


class InvoiceFormView(View):
    form_class = InvoiceForm
    template_name = 'invoice/index.html'
    pid = 0

    @never_cache
    def get(self, request):
        form = self.form_class(None)

        if request.user is not None:
            if request.user.is_active:
                if request.user.is_staff:
                    result_list = Invoice.objects.all()
                else:
                    result_list = Invoice.objects.filter(receivingUser=request.user)

                context = {
                    'invoices': result_list,
                    'form': form,
                    'user': request.user
                }

                return render(request=request, template_name=self.template_name, context=context)

        return HttpResponse("<h1>UNAUTHORIZED</h1>")

    @never_cache
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        active_user = request.user

        if active_user is not None:
            if active_user.is_active:
                if form.is_valid():
                    invoice = form.save(commit=False)

                    invoice.issuingUser = form.cleaned_data['issuingUser']
                    invoice.receivingUser = form.cleaned_data['receivingUser']
                    invoice.date = datetime.datetime.now()
                    invoice.invoice = form.cleaned_data['invoice']

                    if invoice.issuingUser is None:
                        return HttpResponse("<h1>UNAUTHORIZED</h1>")
                    if invoice.receivingUser is None:
                        return HttpResponse("<h1>UNAUTHORIZED</h1>")

                    invoice.save()
                    m = "New incoice!"
                    Notification.objects.create(target_user=invoice.receivingUser, message=m)

                    # wIssuer = Invoice.objects.filter(issuingUser=request.user)
                    # wReceiver = Invoice.objects.filter(receivingUser=request.user)
                    result_list = Invoice.objects.all()

                    # result_list = list(chain(wIssuer, wReceiver))

                    context = {
                        'invoices': result_list,
                        'form': form
                    }

                    return render(request=request, template_name=self.template_name, context=context)
                elif settings.DEBUG:
                    print(form.errors)
                    return HttpResponse("<h1>NOT form.is_valid()</h1>")

        return redirect('/')
