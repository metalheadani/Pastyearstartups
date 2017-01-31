from django.conf.urls import include, url
from summit.views import pastyearstartup

urlpatterns = [
    url(r'^pastyearstartup/',pastyearstartup, name=pastyearstartup),
]