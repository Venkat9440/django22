import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import *
from .models import *

from datetime import timedelta

# Create your views here.
def hello(request):
    return render(request, 'hello.html')


def hello123(request):
    return HttpResponse("<center style=color:blue>Welcome to TPM Homepage</center>")


def image(request):
    return render(request, 'image.html')


def Homepage(request):
    return render(request, 'Homepage.html')


def Travelpackage(request):
    return render(request, 'Travelpackage.html')


def console(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['aditya']
        print(f'user_input:{user_input}')
    # return HttpResponse('Form submitted is successfully')
    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html', a1)


def rando(request):
    return render(request, 'random123.html')


import random, string


def random123(request):
    b = {}  # Define the dictionary outside the if block
    if request.method == "POST":
        in1 = request.POST['otp']
        in2 = int(in1)
        result = ''.join(random.sample(string.digits, in2))
        print(f'result:{result}')
        b = {'result': result}
    return render(request, "random123.html", b)

from django.shortcuts import render
from .forms import IntegerDateForm
from datetime import timedelta

def getdate1(request):
    return render(request, 'getdate_template.html')


def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + timedelta(days=integer_value)
            return render(request, 'getdate_template.html', {'updated_date': updated_date})
        # Handle form invalid case, you were missing this part
    else:
        form = IntegerDateForm()

    return render(request, 'getdate_template.html', {'form': form})


from django.shortcuts import render
from django.shortcuts import render
from pytz import timezone
from datetime import datetime

def index(request):
    return render(request, 'pytzexample.html')

def current_time(request, city):
    # Mapping of city names to timezone strings
    city_timezones = {
        'New_York': 'America/New_York',
        'London': 'Europe/London',
        'Tokyo': 'Asia/Tokyo',
        'Sydney': 'Australia/Sydney'
    }

    # Get the timezone for the selected city
    timezone_str = city_timezones.get(city, None)
    if timezone_str is None:
        current_time = 'Invalid city'
    else:
        # Get the current time in the selected city's timezone
        city_timezone = timezone(timezone_str)
        current_time = datetime.now(city_timezone).strftime('%Y-%m-%d %H:%M:%S')

    context = {
        'city': city,
        'current_time': current_time
    }
    return render(request, 'pytzexample.html', context)

def time(request):
    return render(request, 'display_time.html')


from datetime import datetime
import pytz


def display_time(request):
    # Get current time in UTC
    utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)

    # Define time zones you want to display
    time_zones = ['America/New_York', 'Europe/London', 'Asia/Tokyo']

    # Create a list to store time in each time zone
    times_in_zones = []

    for tz_name in time_zones:
        # Convert UTC time to the desired time zone
        local_time = utc_time.astimezone(pytz.timezone(tz_name))
        times_in_zones.append({'zone': tz_name, 'time': local_time})

    return render(request, 'time_display.html', {'times_in_zones': times_in_zones})


def register(request):
    return render(request, 'register.html')


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        # check if email already exists
        if Register.objects.filter(email=email).exists():
            message1 = "Email already exists choose a different email"
            # return HttpsResponse("email already registered")
            return render(request, 'register.html', {'message1': message1})
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('Homepage')
    return render(request, 'register.html')


from django import forms


def piechartcall(request):
    return render(request, 'PieChart.html')


class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')


def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/PieChart.png')  # Save the chart image
            img1 = {'chart_image': '/static/images/PieChart.png'}
            return render(request, 'PieChart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'PieChart.html', {'form': form})


def slidecall(request):
    return render(request, 'SlideShow.html')


import requests


def weatherpagecall(request):
    return render(request, 'WeatherReport.html')


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '2736646289ac4d9eb0c4e8f52cb842c1'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'WeatherReport.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'WeatherReport.html', {'error_message': error_message})


from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'Homepage.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def singup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'oops! username already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:
            messages.info(request, 'password do not match')
            return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return render(request, 'Homepage.html')


def contact(request):
    return render(request, 'Feedback.html')


def contactmail(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '-----------this is just a comment'
        data = contactus(firstname=firstname, lastname=lastname, email=email)
        data.save()
        return HttpResponse('<h1><center> thankyou for feedback</center></h1>')
