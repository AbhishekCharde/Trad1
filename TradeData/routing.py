from django.urls import path
from .stockconsumer import stockConsumer

ws_urlpatterns = [
    path('ws/some_url/',stockConsumer.as_asgi())
]