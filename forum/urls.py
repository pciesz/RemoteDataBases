from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryFormView.as_view(), name="index"),
    path(r'category/<int:id>/', views.ThreadFormView.as_view(), name='category_view'),
    path(r'thread/<int:id>/', views.EntryFormView.as_view(), name='thread_view'),
]
