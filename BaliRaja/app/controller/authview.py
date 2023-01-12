from multiprocessing import AuthenticationError
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import redirect, render,HttpResponse

from app.forms import costomuserform

def register(request):
    form=costomuserform()
    if request.method =='POST':
        form=costomuserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successfully! Login to continue")
            return redirect("/login")
    context={'form':form}
    return render(request, "auth/register.html",context )

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You Are Already Logged In")
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            passwd=request.POST.get('password')
            user=authenticate(request,username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully')
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("/login")

        return render(request, "auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"LOgged OUT successfully")
        return redirect("/")