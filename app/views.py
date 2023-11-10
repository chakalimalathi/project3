from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chaithu(request):
    return HttpResponse('<h1><marquee>beautifull girl</h1></marquee>')
def raji(request):
    return HttpResponse('<h1>raji is a good girl</h1>')