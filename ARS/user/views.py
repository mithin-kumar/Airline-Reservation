from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from  django.urls import reverse
from django.contrib.auth import authenticate,login ,logout
# Create your views here.

def  index(request):
   # return render(request,"user/index.html")
   if not request.user.is_authenticated:
       return HttpResponseRedirect(reverse("login"))
   #return render(request, "users/user.html")
   return  render(request,"user/index.html")

def login_view(request):
    return render(request,"user/login.html")

def check(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse("flight/index"))
            #return render(request,"user/user.html")
        else :
            return HttpResponse("not correct  user")
    return  HttpResponse("checking")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))