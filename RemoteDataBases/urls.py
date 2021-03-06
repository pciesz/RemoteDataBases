"""RemoteDataBases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path(r'', views.index),
    path(r'admin/', admin.site.urls),
    path(r"user/", include("user.urls"), name="user"),
    path(r"invoices/", include("invoice.urls"), name="invoices"),
    path(r"forum/", include("forum.urls"), name="forum"),
    path(r"notification/", include("notification.urls"), name="notifications"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
