from django.contrib.auth.models import User
from django.db import models



class Notification(models.Model):
    target_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=250, default="")
    is_seen = models.BooleanField(default=False)
