from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'farmer'


urlpatterns = [
    url(r'^tender_list/(?P<produce_id>[0-9]+)/$',views.tender_list,name="tender_list"),
    url(r'^produce_add_form/',views.produce_add_form,name="produce_add_form"),
    url(r'^produce_list/',views.produce_list,name="produce_list"),
    url(r'^tender_form/$',views.tender,name="tender_form"),
    url(r'^storage_add/',views.storage_add,name="storage_add"),
    url(r'^shipment/',views.shipment,name="shipment"),
    url(r'^$',views.homepage,name="homepage"),
]