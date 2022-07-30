from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from  django  import forms
from  .models  import flights,Airport,Passenger
# Create your views here.
"""def queryform(forms.Form):
     origin=forms."""

def  index(request):
    if  request.method=="POST":
        f2=flights.objects.get(origin=request.POST['origin'],destination=request.POST['destination'])
        return render(request,"flights/index.html",{
            "flight" :f2
        })
    return render(request,"flights/index.html",{
        "flights" :flights.objects.all(),
        "Airports" :Airport.objects.all()
    })

def search(request):
    if  request.method=="POST":
        f2=flights.objects.filter(origin=request.POST['origin'],destination=request.POST['destination'])
        return render(request,"flights/result.html",{
            "flight" :f2
        })


def flight(request,flight_id):
    f1=flights.objects.get(id=flight_id)
    return render(request,"flights/details.html",{
        "flight" :f1,
        "passengers" : f1.passenger.all()
    })

def book(request,flight_id):
    if  request.method =="POST":
        f1=flights.objects.get(id=flight_id)
        passenger=Passenger(first_name=request.POST['passenger_name'],age=request.POST['passenger_age'],sex=request.POST['passenger_sex'])
        #passenger=Passenger.objects.get(id=int(request.POST['passenger']))

        passenger.save()
        x = passenger.id
        passenger=Passenger.objects.get(id=x)
        passenger.flights.add(f1)
        f1.seat_available=f1.seat_available-1

        return HttpResponseRedirect(reverse("flight",args=(f1.id,)))

    return HttpResponseRedirect(reverse("flight/index"))



