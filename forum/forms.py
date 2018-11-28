from django import forms

from forum.models import Entry, Thread, Category


class EntryForm(forms.ModelForm):
    content = forms.CharField(max_length=500)

    class Meta:
        model = Entry
        fields = ['content']


class ThreadForm(forms.ModelForm):
    subject = forms.CharField(max_length=120)

    class Meta:
        model = Thread
        fields = ['subject']


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=120)

    class Meta:
        model = Category
        fields = ['name']
