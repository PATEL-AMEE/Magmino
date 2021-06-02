from django.shortcuts import render
# from app1.forms import LogForm
from app1.models import LogMessage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def hours(request):
    return render(request, "hours.html")
def gallery(request):
    return render(request, "gallery.html")
def booking(request):
    return render(request, "booking.html")
def contact(request):
    return render(request, "contact.html")


