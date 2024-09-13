from django import forms
from django.forms import ModelForm
from .models import Venue
from .models import Event 


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # Get all the columns present in Venue table
        fields = "__all__" # Gets all the columns
        # fields  = ('name','address') # Get only name , address column
        labels = {
             'name':'',
              'address':'',
               'zip_code':'',
                'web':'',
                 'email_address':'',

        }
        widgets = {
            'name':forms.TimeInput(attrs={'class':'form-control','placeholder':'venue name'}),
             'address':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter address'}),
             'zip_code':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter zip-code'}),
             'web':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter url'}),
             'email_address':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter email for venue'}),

        
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        # Get all the columns present in Venue table
        fields = "__all__" # Gets all the columns
        # fields  = ('name','address') # Get only name , address column
        labels = {
             'name':'',
              'event_date':'yyyy-mm-dd hh:mm:ss',
               'manager':'',
                'description':'',
                 'attendees':'attendees',
                  'venue':'venue',

        }
        widgets = {
            'name':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter name'}),
             'event_date':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter event_date'}),
             'manager':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter manager'}),
             'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description'}),
             'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Enter attendees'}),
             'venue':forms.Select(attrs={'class':'form-select','placeholder':'Enter  venue'}),

        
        }

