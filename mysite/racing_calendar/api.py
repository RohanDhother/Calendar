from .models import *
import datetime
from django.http import JsonResponse

def events_api(request):
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
