from .models import *
import datetime
from django.http import JsonResponse
import json

def Events_api(request): #send the next three days of events to frontend
    if(request.method=="GET"):
        events = Event.objects.all().filter(dateTime__range=[datetime.datetime.today().date(), datetime.datetime.today().date() + datetime.timedelta(days=2)])
        day1 = []
        day2 = []
        day3 = []
        for i in range(len(events)):
            if(events[i].dateTime.date()==datetime.datetime.today().date()):
                day1.append(events[i].to_dict())
            elif(events[i].dateTime.date()==datetime.datetime.today().date() + datetime.timedelta(days=1)):
                day2.append(events[i].to_dict())
            else:
                day3.append(events[i].to_dict())
        print("\n\nday1:", day1, "\n\n")
        return JsonResponse({'day1': day1, 'day2': day2, 'day3': day3})
    return JsonResponse({})

def Allevents_api(request): #sends all events to frontend
    if(request.method=="GET"):
        eventsList = Event.objects.all().order_by('dateTime')
        days = []
        numDays = 0
        for i in range(len(eventsList)):
            j = 0
            found = False
            while(j<len(days) and found == False):
                if(days[j][0]['date']==eventsList[i].dateTime.strftime("%A(%d:%m:%y)")):
                    days[j].append(eventsList[i].to_dict())
                    found = True
                j = j + 1
            if(found==False):
                days.append([eventsList[i].to_dict()])
                numDays = numDays + 1
        return JsonResponse({
        'days': days,
        'numDays': numDays
        })

def DeleteEvent_api(request): #deletes an event
    if(request.method=="DELETE"):
        body = json.loads(request.body.decode('utf-8'))
        id=body['id']
        e = Event.objects.get(id=id)
        e.delete()
    return JsonResponse({})

def AddEvent_api(request):
    if(request.method=="POST"):
        body = json.loads(request.body.decode('utf-8'))
        name=body['name']
        dateTime=body['dateTime']
        date = [int(x) for x in dateTime.split("T")[0].split("-")]
        time = [int(x) for x in dateTime.split("T")[1].split(":")]
        e = Event(name=name, dateTime=datetime.datetime(date[0], date[1], date[2], time[0], time[1]))
        e.save()
        return JsonResponse({'event': [e.to_dict()]})
    return JsonResponse({})
