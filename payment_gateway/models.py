from django.db import models

class payments(models.Model):
    amount = models.CharField(max_length=100, blank=True,null=True)
    currency = models.CharField(max_length=100, blank=True,null=True)
    number = models.CharField(max_length=100, blank=True,null=True)
    status = models.CharField(max_length=100, blank=True,null=True)
    fname = models.CharField(max_length=100, blank=True,null=True)
    lname = models.CharField(max_length=100, blank=True,null=True)
    payee_email = models.CharField(max_length=100, blank=True,null=True)
    payee_merchant_id = models.CharField(max_length=100, blank=True,null=True)
    payer_email = models.CharField(max_length=100, blank=True,null=True)
    payer_id = models.CharField(max_length=100, blank=True,null=True)