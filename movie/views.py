from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html', {'name': 'Esneider Zapata'})

# Create your views here.
