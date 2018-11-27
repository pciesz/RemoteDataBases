from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)


class RoleGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
