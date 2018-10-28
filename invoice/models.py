from django.db import models
from user.models import User


# Create your models here.

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateField()
    invoicePath = models.CharField(max_length=500)
