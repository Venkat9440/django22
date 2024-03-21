
from django.urls import path

from . import admin
from .views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path("h2/",hello),
    path('hello/',hello123,name='hello123'),
    path('',Homepage,name='Homepage'),
    path('travelpackage/',Travelpackage,name='Travelpackage'),
    path('c/', print_to_console, name='print_to_console'),
    path('console/', console, name='console'),
    path('image/',image,name ='image'),
    path('r/',rando,name='rando'),
    path('ran1/',random123,name='random123'),
    path('d/',get_date,name='get_date'),
    path('current/', index, name='index'),
    path('current_time/<str:city>/', current_time, name='current_time'),
    path('reg/',register, name='register'),
    path('form/',registerloginfunction, name='registerloginfunction'),
    path('piecall/',piechartcall,name='piechartcall'),
    path('pie/',pie_chart,name='pie_chart'),
    path('s/',slidecall,name='slidecall'),
    path('w/',weatherpagecall,name='weatherpagecall'),
    path('wl/', weatherlogic, name='weatherlogic'),
    path('l/',login,name='login'),
    path('sign/',signup,name='signup'),
    path('login/', login1, name='login1'),
    path('signup/',singup1,name='singup1'),
    path('logout/',logout,name='logout'),
    path('time/',time,name='time'),
    path('timedisplay/',display_time,name='display_time'),
    path('f/',contact,name='contact'),
    path('feedback/',contactmail,name='contactmail'),

]

'''tzfunctionalcall'''