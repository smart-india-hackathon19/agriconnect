from django.conf.urls import url
from . import views

app_name = 'farmer'


urlpatterns = [
    url(r'',views.homepage,name="homepage"),
]