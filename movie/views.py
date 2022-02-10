from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Welcome, this page was made by Esneider Zapata Arias</h1>')

# Create your views here.
