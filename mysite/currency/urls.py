from django.urls import path
from currency.views import get_currency,get_currency_detail


urlpatterns = [

    path('', get_currency, name='index'),
    path('countries/name/<str:country>/', get_currency_detail, name='detail'),

]