from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Домашка по 4 заданию")

