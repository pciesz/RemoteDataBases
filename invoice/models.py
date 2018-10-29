from django.db import models
from user.models import User


class VisitationState(models.Model):
    stateName = models.CharField(max_length=50)


class Visitation(models.Model):
    date = models.DateField()
    state = models.ForeignKey(VisitationState, on_delete=models.CASCADE)


class Invoice(models.Model):
    issuingUser = models.ForeignKey(User, related_name="issuer", on_delete=models.CASCADE)
    receivingUser = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)

    date = models.DateField()
    invoicePath = models.CharField(max_length=500)

    visitation = models.ForeignKey(Visitation, on_delete=models.CASCADE)
