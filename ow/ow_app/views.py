from django.shortcuts import render
from django.http import HttpResponse
from ow_app.models import Category, Service


# Create your views here.

def index(request):
    return HttpResponse("<h1>страница</h1>")

def base(request):
    return render(request,'ow_app/base.html')

def base(request):
    data = Category.objects.all()
    #data2 = Service.objects.all()
    #data2 = Service.objects.filter(category=request.category)
    data2 = Service.objects.filter().order_by('category')
    return render(request, 'ow_app/base.html', {'data': data, 'data2': data2})
