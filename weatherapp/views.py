from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
import requests
from django import forms
from django.views import View

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_weather_info(lat, long):
    api_url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}".format(lat, long)
    print(api_url)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        print(response.json()["properties"]["meta"]["updated_at"])
        return response.json()
    else:
        return "Error"


# class WeatherForm(forms.Form):
#     lat = forms.NumberInput()
#     long = forms.NumberInput()


class WeatherView(View):
    def get(self, request, *args, **kwargs):
        # form = WeatherForm()
        context = {
            # "weather_form": form,
        }
        template = get_template('weather.html')
        return HttpResponse(template.render(context, request))

    def post(self, request, *args, **kwargs):
        # form = WeatherForm(request.POST)
        context = {
            # "weather_form": form
        }
        # if form.is_valid():
            # print(request.POST)
        lat = request.POST['lat']
        long = request.POST['long']
        context['weather_info'] = get_weather_info(lat, long)
        template = get_template('weather.html')
        return HttpResponse(template.render(context, request))