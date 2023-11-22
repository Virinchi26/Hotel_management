# weather/views.py

from django.shortcuts import render
import requests
from .forms import WeatherForm

def get_weather(location, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",
    }
    response = requests.get(base_url, params=params)
    return response.json()

def weather(request):
    form = WeatherForm(request.GET or None)
    weather_data = None

    if request.GET and form.is_valid():
        location = form.cleaned_data['location']
        api_key = "8619356e30e31e939d6eeaa58b65ff9b"  # Replace with your OpenWeatherMap API key

        weather_data = get_weather(location, api_key)

    context = {
        "form": form,
        "weather_data": weather_data,
    }
    return render(request, 'weather.html', context)
