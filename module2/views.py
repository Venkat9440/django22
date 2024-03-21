from django.shortcuts import render, redirect

import random
import string

from .models import URL


def url_shortener(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_url = generate_short_url()
        URL.objects.create(long_url=long_url, short_url=short_url)
        return render(request, 'url_shortener.html', {'short_url': short_url})
    return render(request, 'url_shortener.html')


def redirect_to_org(request, short_url):
    url = URL.objects.get(short_url=short_url)
    return redirect(url.long_url)


def generate_short_url():
    characters = string.ascii_letters + string.digits
    # k = print('www.',characters,'.com')
    www = 'www.'
    com = ".com"
    randomstr = ''.join(random.choice(characters) for i in range(8))
    return www + randomstr + com