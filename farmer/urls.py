from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'farmer'


urlpatterns = [
    url(r'^produce_add_form/',views.produce_add_form,name="produce_add_form"),
    url(r'^storage_add/',views.storage_add,name="storage_add"),
    url(r'^shipment/',views.shipment,name="shipment"),
    url(r'^',views.homepage,name="homepage"),
]