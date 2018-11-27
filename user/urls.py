from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path(r"register/", views.UserFormView.as_view(), name="register")
]
