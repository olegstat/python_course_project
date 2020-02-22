from django import forms
from .models import CarBase

class CarInputForm(forms.Form):
    car_make = forms.ModelChoiceField(queryset=CarBase.objects.order_by('make').values_list('make', flat=True).distinct(), empty_label="car make" )
    car_model = forms.ModelChoiceField(queryset=CarBase.objects.order_by('model').values_list('model', flat=True).distinct(), empty_label="car model")
    year_from = forms.ModelChoiceField(queryset=CarBase.objects.order_by('year').values_list('year', flat=True).distinct(), empty_label="year from")
    year_until = forms.ModelChoiceField(queryset=CarBase.objects.order_by('year').values_list('year', flat=True).distinct(), empty_label="year until")