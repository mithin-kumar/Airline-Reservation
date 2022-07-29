from django.db import models

# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=45)

    def __str__(self):
        return f"{self.city} ({self.code})"


def  routes(request):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="depature")
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="destination")
    stopover=models.ManyToManyField(flights,blank=True,related_name="stopover")

    def __str__(self):
        return f"routee {self.id}  is  from {self.origin} to  {self.destination}"




class flights(models.Model):

    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    duration = models.IntegerField()
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arraivals")
    seat_available=models.IntegerField(default=200)



    def __str__(self):
        return f"{self.id} : {self.origin} to  {self.destination} time {self.duration} available seats {self.seat_available}"

class Passenger(models.Model):
    first_name=models.CharField(max_length=64)
    age=models.IntegerField()
    sex=models.CharField(max_length=5)
    flights=models.ManyToManyField(flights,blank=True,related_name="passenger")

    def  __str__(self):
        return f"{self.first_name} is of age {self.age} "


    """def __init__(self,id,name,sex,age,fligt=None):
        self.first_name=name
        self.age=age
        self.sex=sex
        #self.flights.add(flight)
        self.id=id"""
