from __future__ import absolute_import

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from .models import ClockStyle


def index(request):
    try:
        clock = ClockStyle.objects.filter(active=True)[0]
    except ClockStyle.DoesNotExist:
        return HttpResponse("No clocks active. Please set a ClockStyle as active in the admin.")
        raise Http404
    return render(request, 'clocks/index.html', {'clock': clock})

def detail(request, clock_id):
    try:
        clock = ClockStyle.objects.get(pk=clock_id)
    except ClockStyle.DoesNotExist:
        raise Http404
    return render(request, 'clocks/index.html', {'clock': clock})