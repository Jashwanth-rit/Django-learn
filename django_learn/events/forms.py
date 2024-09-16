from django import forms
from django.forms import ModelForm
from .models import Venue
from .models import Event 


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','zip_code','web','email_address','image')  # Gets all the columns
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'web': '',
            'email_address': '',
            'image':"",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter zip code'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter website URL'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            

        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date','description','attendees','venue')
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            # 'manager': 'Manager',
            'description': '',
            'attendees': 'Attendees',
            'venue': 'Venue',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'event_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            # 'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select manager'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Select attendees'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select venue'}),
        }

class EventAdminForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'manager': 'Manager',
            'description': '',
            'attendees': 'Attendees',
            'venue': 'Venue',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'event_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select manager'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Select attendees'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select venue'}),
        }
