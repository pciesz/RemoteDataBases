from django.db import models

from user.models import User


class Notification(models.Model):
    target_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_seen = models.BooleanField
