from django.db import models

class payments(models.Model):
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=100, blank=True,null=True)
    number = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=100)
    authorization_code = models.IntegerField()
    time = models.DateTimeField()