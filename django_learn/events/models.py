from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# creating tables 

class Attenders(models.Model):
    first_name = models.CharField('first name',max_length= 100)
    last_name = models.CharField('last name',max_length= 100)
    useremail = models.EmailField('userEmail')

    def __str__(self):
        return self.first_name+' '+self.last_name


class Venue(models.Model):
    name = models.CharField('Venue name',max_length= 100)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('zip code',max_length= 100)
    web = models.URLField('website address')
    email_address = models.EmailField('Email')
    owner = models.IntegerField("venue owner",blank=False,default=1)

    def __str__(self):
        return self.name




class Event(models.Model):
    name = models.CharField('Event name', max_length=100)
    event_date = models.DateTimeField('Event date')

    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)

    # Manager should be a ForeignKey to User, not a CharField
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(Attenders, blank=True)
    approval =  models.BooleanField("Approved",default=False,)

    def __str__(self):
        return self.name
    
    @property
    def Day_till(self):
        today = date.today()
        days_till = self.event_date.date()-today
        days_till_stripped = str(days_till).split(',',1)[0]
        return  days_till_stripped
    
    @property
    def Check(self):
        today = date.today()
        self.event_date.date()
       
        if self.event_date.date() > today:
            return 'Future'
        if self.event_date.date() < today:
            return 'Past'
        if self.event_date.date() == today:
            return 'Present'


        



