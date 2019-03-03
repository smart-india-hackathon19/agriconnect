from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import datetime
import csv
# Create your views here.


def homepage(request):
	commoditity = Commodity.objects.order_by().values('name').distinct()
	context = {"crops" : commoditity}
	return render(request,'homepage/home.html',context)

def tender(request,produce_id):
	if request.method == "GET":
		return render(request,'farmer/tender_form.html',{"produce_id" : produce_id})
	else:
		produce=Produce.objects.get(id=produce_id)
		added_on = datetime.datetime.now()
		tender = ProduceTender.objects.create(produce=produce,location=request.POST['location'],quantity=request.POST['quantity'],added_on=added_on,t_type=request.POST['t_type'])
		tender.save()
		return redirect('farmer:tender_list',produce_id=produce.id)

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
		return redirect('farmer:produce_list')

def produce_list(request):
	produces = Produce.objects.filter(farmer=request.user)
	context = {
	"produces" : produces
	}
	return render(request,'farmer/produce_list.html',context)

def tender_list(request,produce_id):
	tenders = ProduceTender.objects.filter(produce=produce_id)
	context = {
		"sells" : tenders.filter(t_type="sell"),
		"storages" : tenders.filter(t_type="storage"),
		"transports" : tenders.filter(t_type="transport")
	}
	return render(request,'farmer/tender_list.html',context)

def predict_crop_price(request,name):
	return render(request,'farmer/predict.html',{"name" : name})

def csv_process(request,name):
	response = HttpResponse()
	writer = csv.writer(response)
	writer.writerow(["date","close"])
	if name == "random":
		name = Commodity.objects.all().order_by('?').first().name
		print (name)
	commodities = Commodity.objects.filter(name=name).order_by('date')
	for commoditity	in commodities:
		row = writer.writerow([commoditity.date,commoditity.price])
	return response

