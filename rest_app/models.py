from django.db import models

# Create your models here.


class vehicle(models.Model):
    plate = models.CharField(max_length=100)
    def __str__(self):
        return self.plate
    

class navigationRecord(models.Model):
    vehicle = models.ForeignKey(vehicle, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True,verbose_name="Register Date",null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    def __str__(self):
        return self.vehicle.plate



class Operation(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Bin(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    last_collection = models.DateTimeField(auto_now_add=True,null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    collection_frequency = models.IntegerField(null=True)
    def __str__(self):
        return self.operation.name


    

    