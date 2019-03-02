from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Crop(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Produce(models.Model):
	farmer = models.ForeignKey(User,on_delete = models.CASCADE)
	crop = models.ForeignKey(Crop,on_delete = models.CASCADE)
	expected_yield = models.IntegerField()
	expected_delivery_date = models.DateField()

	def __str__(self):
		return "{} is growing {} expected yield is {} tons and will deliver on {} ".format(self.farmer.username,self.crop.name,self.expected_yield,self.expected_delivery_date)


# class ProduceActivity(models.Model):
# 	produce = models.ForeignKey(Produce,on_delete=models.CASCADE)
# 	date = models.DateField


class ProduceTender(models.Model):
	produce = models.ForeignKey(Produce, on_delete = models.CASCADE)
	location =  models.CharField(max_length=100)
	quantity = models.IntegerField()
	added_on = models.DateTimeField()
	tender_type = ( ('transport','transport'), 
				  ('storage', 'storage'),('sell',"sell")
	)
	t_type = models.CharField(max_length=20,choices=tender_type)

	def __str__(self):
		return "{} want to {} his {} tons crop to near {} location ".format(self.produce.farmer.username,self.quantity,self.t_type,self.location)

class TenderBid(models.Model):
	tender =  models.ForeignKey(ProduceTender, on_delete= models.CASCADE)
	accepted = models.BooleanField(default=False)

