from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Payment(TemplateView):
    template_name = 'stripe_payment_form.html'

class BankDetail(TemplateView):
    template_name = 'bank_detail.html'