from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'farmer'


urlpatterns = [
    url(r'^produce_add_form/',views.produce_add_form,name="produce_add_form"),
    url(r'^',views.homepage,name="homepage"),
]