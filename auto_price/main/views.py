from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, FileResponse
from .forms import CarInputForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarBaseSerializer
from .models import CarBase
from django_pandas.io import read_frame
from django.utils.html import escape
from django.urls import reverse
import pandas as pd
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

#main page view with form
def main_page_view(request):
    if request.method == "GET":
        form = CarInputForm()
        return render(request, 'index.html', {'form': form})
    return redirect(details_view)

#details page view
def details_view(request):
    form = CarInputForm(request.POST)
    qs = CarBase.objects.all()
    df = read_frame(qs)
    selected_make = request.POST.get('car_make')
    selected_model = request.POST.get('car_model')
    selected_year_from = request.POST.get('year_from')
    selected_year_until = request.POST.get('year_until')
    df = df[(df.make == selected_make) & (df.model == selected_model) & (df.year >= int(selected_year_from)) & (df.year <= int(selected_year_until))]
    if df['id'].count() > 0:
        total_ad_num = df['id'].count()
        avg_price = df['price'].mean().round()
        min_price = df['price'].min().round()
        max_price = df['price'].max().round()
        min_ad_url = df[(df.price == min_price)]['ad_url'].values[0]
        max_ad_url = df[(df.price == max_price)]['ad_url'].values[0]
        top_5 = df.sort_values(by='price', ascending=True)[:5].rename(columns={
            'price': 'Price',
            'year': 'Year',
            'engine': 'Engine',
            'gearbox': 'Gearbox',
            'ad_url': 'Link',
            'ad_date': 'Date added'
            }).filter(['Price', 'Year', 'Engine', 'Gearbox', 'Link', 'Date added']).to_html(render_links=True, escape=False, index=False)
        df_plot = read_frame(qs)
        df_plot = df_plot[(df_plot.make == selected_make)]
        plot = pd.crosstab(df_plot['model'], df_plot['make'], margins=False, normalize=False).sort_values(by='{}'.format(selected_make))
        barh = plot.plot(kind='barh', title=f'Popularity of all {selected_make} models (in number of ads)')
        barh.get_figure().savefig('plot1.png')
        return render(request, 'detail.html', {
            'avg_price': avg_price, 
            'selected_make': selected_make, 
            'selected_model': selected_model,
            'selected_year_from': selected_year_from,
            'selected_year_until': selected_year_until, 
            'min_price': min_price, 
            'max_price': max_price, 
            'min_ad_url': min_ad_url, 
            'max_ad_url': max_ad_url,
            'total_ad_num': total_ad_num,
            'top_5': top_5,
            })
    else:
        return render(request, 'no_ads.html')

#plot view
def plot_view(request):
    with open('plot1.png', "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")

#sign up view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#api view
class CarBaseListView(APIView):
    permission_classes = (AllowGetMethod,)
    def get(self, request, format=None):
        cars = CarBase.objects.all()[:50]
        serializer = CarBaseSerializer(cars, many=True)
        return Response(serializer.data)
