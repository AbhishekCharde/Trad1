from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='index'),
    path('home', views.index, name="home"),
    path('telegramchannels',views.telegramchannels, name="telegramchannels"),
    path('portfolio',views.portfolio, name="portfolio"),
    path('profile',views.profile, name="profile"),
    path('stockdata',views.stockdata, name="stockdata"),
    path('contactus',views.contactus, name="contactus"),
    path('stockdetails',views.stockdetails, name="stockdetails"),
    
]