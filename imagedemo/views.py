from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    products=Products.objects.all()
    context={'products':products}
    
    return render(request,'home.html',context)

def file(request):
    products=NewProducts.objects.all()
    context={'products':products}
    
    return render(request,'fileimage.html',context)
