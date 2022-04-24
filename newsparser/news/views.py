from django import views
from django.shortcuts import render
from .models import *


def show_main_page(request):
    info_pravda = PravdaSite.objects.all()[0:10]
    info_nv = NVSite.objects.all()[0:10]
    return render(request, 'news/main_page.html', {'info_pravda':info_pravda, 'info_nv':info_nv})


