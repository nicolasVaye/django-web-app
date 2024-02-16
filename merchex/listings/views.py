from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Title


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})


def contact_us(request):
    return render(request, 'listings/contact_us.html')