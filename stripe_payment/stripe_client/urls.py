from django.urls import path
from .views import *

urlpatterns = [
    path('payment/', Payment.as_view(), name="payment"),
    path('bankdetail/', BankDetail.as_view(), name="bankdetail"),
]