from django.shortcuts import render
from .models import places
from .models import travelblog


# Create your views here.

def destination(request):
    destination_places = places.objects.all()
    blogs = travelblog.objects.all()
    return render(request, 'index.html', {'destinations': destination_places, 'posts': blogs})
