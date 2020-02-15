from django.urls import path
from main import views

urlpatterns = [
    path('', views.main_page_view),
    path('details/', views.details_view),
    path('api/', views.CarBaseListView.as_view(), name='car-base-api')
]

