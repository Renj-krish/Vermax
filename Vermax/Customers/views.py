from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Customer
from django.contrib import messages
# Create your views here.
def signout(request):
     logout(request)
     return redirect('home')
def account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['login']= True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            #creates user accounts
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )


            #creates customer account
            customer = Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            success_message = "User registered successfully"
            messages.success(request, success_message)
        except Exception as e:
            error_message="duplicate name or invalid name"
            messages.error(request, error_message)

    if request.POST and 'login' in request.POST:
            context['register']= False
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect ('home')
            else:
                messages.error(request, 'invalid user name or password')

    return render(request, 'account.html', context)