from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.home,name="home"),
    path('file/',views.file,name="file"),
    path('addproducts/',views.addproducts,name="addproducts"),
]