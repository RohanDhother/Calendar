from django.db import models
import datetime
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=254)
    dateTime = models.DateTimeField()

    def to_dict(self):
        return{
        'id': self.id,
        'name': self.name,
        'dateTime': self.dateTime.strftime("%H:%M")
        }
