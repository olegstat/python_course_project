from django.urls import path
from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from auto_price import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main_page_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('details/', views.details_view),
    path('plot/', views.plot_view),
    path('top_20/', views.all_auto_plot_view),
    path('api/', views.CarBaseListView.as_view(), name='car-base-api')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

