from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.
import requests
import json

def get_currency(request):

    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url)
    if response:
        res = response.json()        
        countries = [res[i]['name'] for i in range(len(res))]
        countries_let = [res[i]['name'][0] for i in range(len(res))]
        first_let_set = {i for i in countries_let}
        first_let_list = sorted(list(first_let_set))

        return render(request,'countries.html', {'countries':countries , 'letter':first_let_list } )
    else:
        return HttpResponse('server is not response')



def get_currency_detail(request,country):

    url = f'https://restcountries.eu/rest/v2/name/{country}'

    response = requests.get(url)
    res = response.json()
    return render(request,'index.html', {'country':res[0]} )



