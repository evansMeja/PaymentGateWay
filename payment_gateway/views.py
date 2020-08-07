from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import requests
from payment_app.settings import PAYMENT_BACKENDS_SETTINGS

def make_payment(request):
    template_name="payment_gateway/index.html"
    context={}
    return render(request,template_name,context)


def js_approach(request):
    template_name="payment_gateway/javascript_approach.html"
    context={}
    return render(request,template_name,context)

def request_payment_api(request):
    cardNumber = request.POST.get("cardNumber")
    cardExpiryMonth = request.POST.get("cardExpiryMonth")
    cardExpiryYear = request.POST.get("cardExpiryYear")
    cardCVC = request.POST.get("cardCVC")
    Amount = request.POST.get("Amount")
    data = {'success':False}
    url = PAYMENT_BACKENDS_SETTINGS['paypal']['url']
    try:
        task = {
        "amount": Amount,
        "currency": "USD",
        "type": "creditcard",
        "card": {
            "number": cardNumber,
            "expirationMonth": cardExpiryMonth,
            "expirationYear": cardExpiryYear,
            "cvv": cardCVC
            }
        }
        response = requests.post(url, json=task)
        if response.json()['status'] == "success":
            data ['success']=True
            amount = response.json()['amount']
            currency = response.json()['currency']
            number = response.json()['card']['number']
            status = response.json()['status']
            authorization_code = response.json()['authorization_code']
            time = response.json()['time']
            payments_obj = payments()
            payments_obj.amount = amount
            payments_obj.currency = currency
            payments_obj.number=number
            payments_obj.status=status
            payments_obj.authorization_code = authorization_code
            payments_obj.time= time
            payments_obj.save()
        data ['success']=True
    except:
            data ['success']=False
    return JsonResponse(data)
