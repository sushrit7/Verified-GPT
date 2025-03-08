from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "base.html")

def thread(request):
    return render(request, "thread.html")