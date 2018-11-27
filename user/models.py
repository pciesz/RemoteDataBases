from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=250)


class Role(models.Model):
    name = models.CharField(max_length=100)


class RoleGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
