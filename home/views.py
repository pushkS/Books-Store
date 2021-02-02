from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def popular(request):
    return render(request,'popular.html')

def sign(request):
    return render(request,'sign.html')