from django.urls import path
from .views import *

urlpatterns = [
    path('', show_main_page, name='main_page'),
]