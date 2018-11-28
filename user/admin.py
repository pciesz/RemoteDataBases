from django.contrib import admin

from notification.models import Notification
from .models import *
# Register your models here.

admin.site.register(Role)
admin.site.register(Notification)
admin.site.register(RoleGroup)