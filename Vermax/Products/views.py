from django.shortcuts import render
from Products.models import Product

# Create your views here.
def index(request):
    return render(request,'index.html')