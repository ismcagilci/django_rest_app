from django.shortcuts import render
from .models import vehicle,navigationRecord,Operation,Bin
import pytz
from datetime import datetime,timedelta
import json
from django.http import JsonResponse
# Create your views here.



def getlastPoints(request):
    if request.method == "GET":
        now = datetime.now(pytz.utc)
        nr = navigationRecord.objects.filter(time__gte = now-timedelta(hours=48))
        new_list = []
        for data in nr:
            new = {}
            new["latitude"] = data.latitude
            new["longitude"] = data.longitude
            new["vehicle_plate"] = data.vehicle.plate
            new["datetime"] = str(data.time.day) +"."+ str(data.time.month) +"."+ str(data.time.year) +" "+ str(data.time.hour) +":"+ str(data.time.minute) +"."+ str(data.time.second)
            new_list.append(new)
        #json_data = json.dumps(new)
        return JsonResponse(new_list,safe=False)


def getOperations(request):
    if request.method == "GET":
        all_bin = Bin.objects.all()
        new_list = []
        for data in all_bin:
            new = {}
            new["operation_name"] = data.operation.name
            new["collection_frequency"] = data.collection_frequency
            new_list.append(new)
        return JsonResponse(new_list,safe=False)