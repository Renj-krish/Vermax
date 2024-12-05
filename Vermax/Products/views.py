from django.shortcuts import render
from Products.models import Product

# Create your views here.
def index(request):
    return render(request,'index.html')

def product_list(request):
    return render(request,'product.html')

def detail_product(request):
    return render(request,'product_detail.html')