from django.shortcuts import render
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    products=Products.objects.all()
    context={'products':products}
    
    return render(request,'home.html',context)

def file(request):
    products=NewProducts.objects.all()
    context={'products':products}
    
    return render(request,'fileimage.html',context)

def addproducts(request):
    if request.method=="POST":
        prod_name=request.POST['name']
        price=request.POST['price']
        images=request.FILES.getlist('images')
        for image in images:
            product=Products(name=prod_name,price=price,image=image).save()
        messages.success(request,"product inserted successfully")
        

    return render(request,'addproducts.html')
