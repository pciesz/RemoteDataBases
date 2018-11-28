from django import forms

from forum.models import Entry, Thread, Category


class EntryForm(forms.Form):
    content = forms.TextInput()

    class Meta:
        model = Entry
        fields = ['content']


class ThreadForm(forms.Form):
    subject = forms.CharField(max_length=120)

    class Meta:
        model = Thread
        fields = ['subject']


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=120)

    class Meta:
        model = Category
        fields = ['name']
