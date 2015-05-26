from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def home(request):
	return render(request, 'home/home.html')
