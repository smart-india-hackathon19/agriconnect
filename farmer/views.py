from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def homepage(request):
	return render(request,'homepage/home.html')

def storage_add(request):
	return render(request,'farmer/storage_form.html')

def shipment(request):
	return render(request,'farmer/shipment_form.html')

def produce_add_form(request):
	crops = Crop.objects.all()
	print (crops)
	context = {
	"crops" : crops
	}
	return render(request,'farmer/produce_form.html',context)
