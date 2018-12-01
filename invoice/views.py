import datetime
from itertools import chain

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

# Create your views here.
from django.views import View

from invoice.forms import InvoiceForm
from invoice.models import Invoice


class ReadAbleInvoice:
    pass


def index(request):
    template = loader.get_template('invoice/index.html')

    context = {
        'invoices': Invoice.objects.filter()
    }

    return HttpResponse(template.render(context, request))


class InvoiceFormView(View):
    form_class = InvoiceForm
    template_name = 'invoice/index.html'
    pid = 0

    def get(self, request):
        form = self.form_class(None)

        if request.user is not None:
            if request.user.is_active:
                wIssuer = Invoice.objects.filter(issuingUser=request.user)
                wReceiver = Invoice.objects.filter(receivingUser=request.user)

                result_list = list(chain(wIssuer, wReceiver))

                context = {
                    'invoices': result_list,
                    'form': form
                }

                return render(request=request, template_name=self.template_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST)
        active_user = request.user

        if active_user is not None:
            if active_user.is_active:
                if form.is_valid():
                    invoice = form.save(commit=False)

                    invoice.issuingUser = form.cleaned_data['issuingUser']
                    invoice.receivingUser = form.cleaned_data['receivingUser']
                    invoice.date = datetime.datetime.now()
                    invoice.invoicePath = form.cleaned_data['invoicePath']

                    if invoice.issuingUser is None:
                        redirect('/')
                    if invoice.receivingUser is None:
                        redirect('/')

                    invoice.save()

                    wIssuer = Invoice.objects.filter(issuingUser=request.user)
                    wReceiver = Invoice.objects.filter(receivingUser=request.user)

                    result_list = list(chain(wIssuer, wReceiver))

                    context = {
                        'invoices': result_list,
                        'form': form
                    }

                    return render(request=request, template_name=self.template_name, context=context)

        redirect('/')
