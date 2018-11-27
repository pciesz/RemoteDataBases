from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path(r"list/", views.List, name="list"),
    path(r"register/", views.UserFormView.as_view(), name="register"),
    path(r"login/", views.UserLoginFormView.as_view(), name="login"),
    path(r"logout/", views.Logout, name="logout")
]
