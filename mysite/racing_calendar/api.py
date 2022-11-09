from .models import *
import datetime
from django.http import JsonResponse
import json

def events_api(request): #send the next three days of events to frontend
    if(request.method=="GET"):
        events = Event.objects.all().filter(dateTime__range=[datetime.datetime.today().date(), datetime.datetime.today().date() + datetime.timedelta(days=2)])
        day1 = [datetime.datetime.today().strftime("%A")]
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
        eventsList = Event.objects.all().order_by('-dateTime')
        events = []
        for i in range(len(eventsList)):
            try:
                index = events.index(eventsList[i].dateTime.strftime("%A(%d:%m:%y)"))
                events[index][1].append(eventsList[i].to_dict())
            except:
                events.append([eventsList[i].dateTime.strftime("%A(%d:%m:%y)"), eventsList[i].to_dict()])
        return JsonResponse({
        'events': events
        })

def DeleteEvent_api(request): #deletes an event
    if(request.method=="DELETE"):
        body = json.loads(request.body.decode('utf-8'))
        id=body['id']
        e = Event.objects.get(id=id)
        e.delete()
    return JsonResponse({})
