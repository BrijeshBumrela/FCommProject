from django.shortcuts import render

import requests
import json
from . import api

def index(request):


    # url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid={}".format(api.api_key)
    # r = requests.get(url)

    # r = r.json()

    # print(r)

    return render(request, 'weather/index.html')