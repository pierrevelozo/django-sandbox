from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    date = timezone.localdate()
    isnewyear = (date.day == 1 and date.month == 1)

    context = {"isnewyear": "Yes" if isnewyear == True else "No"}

    return render(request, "newyear.html", context)
