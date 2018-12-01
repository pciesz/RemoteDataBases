from django.contrib.auth.models import User
from django.db import models


class VisitationState(models.Model):
    stateName = models.CharField(max_length=50)


class Visitation(models.Model):
    date = models.DateField()
    state = models.ForeignKey(VisitationState, on_delete=models.CASCADE)


class Invoice(models.Model):
    issuingUser = models.ForeignKey(User, related_name="issuer", on_delete=models.DO_NOTHING)
    receivingUser = models.ForeignKey(User, related_name="receiver", on_delete=models.DO_NOTHING)

    date = models.DateField()
    invoice = models.FileField()

