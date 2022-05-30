from django.http import HttpResponse
from django.shortcuts import render

def taskList(request):
  return HttpResponse('To Do List')