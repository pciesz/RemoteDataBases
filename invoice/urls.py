from django.urls import path
from . import views

urlpatterns = [
    path('', views.InvoiceFormView.as_view(), name="index"),
]
