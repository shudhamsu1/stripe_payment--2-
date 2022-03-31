from django.urls import path

from payment.api.v1.viewsets import AddCash, BankDetailViewSet

from payment.api.v1.viewsets import SignInView

urlpatterns = [
    path('add-cash/', AddCash.as_view(), name='add_cash'),
    path('add-bank/', BankDetailViewSet.as_view(), name='add_cash'),
    path('users/sign-in', SignInView.as_view(), name='user_sign_in'),

]
