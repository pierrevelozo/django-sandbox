from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    date = timezone.localdate()
    return render(request, "newyear.html", {
	"newyear" : (date.day == 1 and date.month == 1)
    })
