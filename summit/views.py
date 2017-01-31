from django.shortcuts import render
from django.http import HttpResponse


def pastyearstartup(request):
    context = {}
    return render(request, 'pastyearstartup.html', context)
