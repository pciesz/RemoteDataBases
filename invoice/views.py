from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from invoice.models import Invoice


class ReadAbleInvoice:
    pass


def index(request):
    template = loader.get_template('invoice/index.html')

    context = {
        'invoices': Invoice.objects.filter()
    }

    return HttpResponse(template.render(context, request))
