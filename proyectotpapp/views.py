from django.shortcuts import render
from django.http import HttpResponse

import random

def numero_al_azar_decimal(request):
    return HttpResponse(random.random())

def numero_al_azar_entero_en_rango(request,param1,param2):
    num = random.randint(param1,param2)
    return HttpResponse(num)



    

