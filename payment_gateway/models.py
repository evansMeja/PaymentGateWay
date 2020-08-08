from django.db import models

class payments(models.Model):
    amount = models.CharField(max_length=100, blank=True,null=True)
    currency = models.CharField(max_length=100, blank=True,null=True)
    number = models.CharField(max_length=100, blank=True,null=True)
    status = models.CharField(max_length=100, blank=True,null=True)