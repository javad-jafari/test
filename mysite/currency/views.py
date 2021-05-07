from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

import requests
import time
from binance.client import Client

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


api_key = "jd6ZVf62EOYKdUaNDwPfCSB9ndH303ePzBGeSJxgfEzvIMzBEtKahXw7eFnV55EG"
secret_key = "dQWwP1oMJe1vuopXF4mykLyk9ZKeUQWXM1ORiuFyYPbSD45bxdvfRkMjuIBXKJft"

def get_currency(request):

    url = 'https://api.binance.com/api/v3/ticker/price'
    symbol = "BTCUSDT"

    response = ''
    while response == '':
        try:
            response = requests.get(url, params=dict(symbol=symbol), headers=headers)
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    response = response.json()
    return HttpResponse(str(response))


def get_currency_detail(request,coin):

    url = 'https://api.binance.com/api/v3/ticker/price'
    response = ''
    while response == '':
        try:
            response = requests.get(url, params=dict(symbol=coin), headers=headers)
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    response = response.json()
    return HttpResponse(str(response))




