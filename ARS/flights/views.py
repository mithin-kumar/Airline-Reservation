from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from  .models  import flights,Airport,Passenger
# Create your views here.

def  index(request):
    return render(request,"flights/index.html",{
        "flights" :flights.objects.all()
    })

def flight(request,flight_id):
    flight=flights.objects.get(id=flight_id)
    return render(request,"flights/details.html",{
        "flight" : flight,
        "passengers" : flight.passenger.all()
    })

def book(request,flight_id):
    if  request.method =="POST":
        f1=flights.objects.get(id=flight_id)
        passenger=Passenger(id=request.POST['passenger_id'],first_name=request.POST['passenger_name'],age=request.POST['passenger_age'],sex=request.POST['passenger_sex'])
        #passenger=Passenger.objects.get(id=int(request.POST['passenger']))
        passenger.save()
        passenger=Passenger.objects.get(id=int(request.POST['passenger_id']))
        passenger.flights.add(f1)
        f1.seat_available=f1.seat_available-1

        return HttpResponseRedirect(reverse("flight",args=(f1.id,)))

    return HttpResponseRedirect(reverse("flight/index"))



