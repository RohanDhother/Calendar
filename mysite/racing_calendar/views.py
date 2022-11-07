from django.shortcuts import render, redirect
from django.http import HttpResponse

def mainPage(request):
    return render(request, 'racing_calendar/pages/mainPage.html')

def admin(request):
    return render(request, 'racing_calendar/pages/admin.html')
# Create your views here.
