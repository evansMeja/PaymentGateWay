from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pay/', include('payment_gateway.urls')),
    path('', include('payment_gateway.urls')),
]
