from django.urls import path

from . import admin
from .views import *

urlpatterns = [
    path('', url_shortener, name='url_shortener'),
    path('<str:short_url>/', redirect_to_org, name='redirect_to_org'),
]