from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("We are at about us")

def contact(request):
    return HttpResponse("We are at contact us")

def tracker(request):
    return HttpResponse("We are at Tracking Status")

def search(request):
    return HttpResponse("We are at Search")

def productview(request):
    return HttpResponse("We are at Product View")
def checkout(request):
    return HttpResponse("We are at Checkout Page")