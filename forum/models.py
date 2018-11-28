from django.db import models

from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    visibleForConsumer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Thread(models.Model):
    subject = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    lastModificationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    thread = models.ForeignKey(Thread, on_delete=models.PROTECT)
    content = models.TextField(max_length=2000, help_text="Enter your post here.")
    date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
