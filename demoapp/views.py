from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Place2

# Create your views here
def home(request):
    obj=Place.objects.all()
    obj2=Place2.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})



