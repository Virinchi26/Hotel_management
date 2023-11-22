# weather/forms.py

from django import forms

class WeatherForm(forms.Form):
    location = forms.CharField(max_length=100, label='Location')
    date = forms.DateField(widget=forms.SelectDateWidget(), label='Select Date')
