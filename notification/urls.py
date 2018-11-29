from django.urls import path
from . import views

urlpatterns = [
    path(r'read/<int:id>/', views.index, name="index"),
]
