from django import forms
from django.contrib.auth.models import User

from invoice.models import Invoice


class InvoiceForm(forms.ModelForm):
    issuingUser = forms.ModelChoiceField(queryset=User.objects.all())
    receivingUser = forms.ModelChoiceField(queryset=User.objects.all())
    invoicePath = forms.CharField(max_length=500)

    class Meta:
        model = Invoice
        fields = ['issuingUser', 'receivingUser', 'invoicePath']
