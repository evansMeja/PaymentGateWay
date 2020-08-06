from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', make_payment, name="make_payment"),
    path('request_payment_api/',request_payment_api,name="request_payment_api")
]
