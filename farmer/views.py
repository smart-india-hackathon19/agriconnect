from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import datetime
# Create your views here.


def homepage(request):
	return render(request,'homepage/home.html')

def tender(request):
	return render(request,'farmer/tender_form.html')

def storage_add(request):
	return render(request,'farmer/storage_form.html')

def shipment(request):
	return render(request,'farmer/shipment_form.html')

def produce_add_form(request):
	if request.method == "GET":
		crops = Crop.objects.all()
		context = {
		"crops" : crops
		}
		return render(request,'farmer/produce_form.html',context)
	else:
		crop = Crop.objects.get(id=request.POST['crop'])
		expected_delivery_date = datetime.datetime.now()
		produce = Produce.objects.create(farmer=request.user,crop=crop,expected_delivery_date=expected_delivery_date,expected_yield=request.POST['yield'])
		produce.save()
		return redirect('farmer:produce_add_form')

def produce_list(request):
	produces = Produce.objects.filter(farmer=request.user)
	context = {
	"produces" : produces
	}
	return render(request,'farmer/produce_list.html',context)

def tender_list(request,produce_id):

	return render(request,'farmer/tender_list.html')