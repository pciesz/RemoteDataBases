from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path(r'category/<int:id>/', views.category_view, name='category_view'),
    path(r'thread/<int:id>/', views.thread_view, name='thread_view'),
]
