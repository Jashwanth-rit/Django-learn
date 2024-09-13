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

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event name',max_length= 100)
    event_date = models.DateTimeField('Event date')

    #one-one connection using foriegn key with other table
    venue = models.ForeignKey(Venue,blank = True,null=True,on_delete=models.CASCADE)
    manager = models.CharField('manager name',max_length= 100)
    # TO add manager as User
    # manager = models.ForeignKey(User,blank = True,null=True,on_delete=models.SET_NULL)
    
    description = models.TextField(blank = True)

    #manytomany connection between Event and Attenders table
    attendees = models.ManyToManyField(Attenders,blank=True)

    def __str__(self):
        return self.name

