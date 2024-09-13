from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event
from .models import Venue
from .forms import VenueForm
from .forms import EventForm
from django.http import HttpResponseRedirect,HttpResponse
import csv

from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas 
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# importing paginator

from django.core.paginator import Paginator


# View for displaying events on the home page

# Generating pdf file of venue

def venuepdf(req):
  
  # creating Bytestream buffer
  buf = io.BytesIO()

  # Create a canvas 
  c = canvas.Canvas(buf,pagesize = letter,bottomup = 0)
  # create a text object

  textob = c.beginText()
  textob.setTextOrigin(inch,inch)
  textob.setFont('Helvetica',14)

  venues = Venue.objects.all()
  lines = []
  for venue in venues:
        
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(" ")
        
        


  for line in lines:
       textob.textLine(line)

  c.drawText(textob)
  c.showPage()
  c.save()
  buf.seek(0)

  return FileResponse(buf,as_attachment=True,filename='venue.pdf')



  # Add some lines of text
  

# Generating a csv file to excel

def venuecsv(req):
    response  = HttpResponse(content_type = 'text/csv')
    response['content-Disposition'] = 'attachment;filaname=venues.csv'
    writer = csv.writer(response)
    writer.writerow(['venue name','venue address','venue zip_code','venue web','venue email_address'])
    venues = Venue.objects.all()
  
    for venue in venues:
        writer.writerow([venue.name,venue.address,venue.zip_code,venue.web,venue.email_address])
       

    # lines=["this are the lines"]
    
    return response



# Generating a text file of venue 

def venuetext(req):
    response  = HttpResponse(content_type = 'text/plain')
    response['content-Disposition'] = 'attachment;filaname=venues.txt'
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.web}\n{venue.email_address}\n\n\n')

    # lines=["this are the lines"]
    response.writelines(lines)
    return response



def search(req):
    if req.method == 'POST':
        search = req.POST['search']
        venues = Venue.objects.filter(name__contains = search)
        return render(req, "events/search.html", {
        
        'search':search,
        'venues':venues
       
    })
    else:
         return render(req, "events/search.html", {
        
        'search':search
       
    })

def deleteevent(req,venue_id):
    venue  = Event.objects.get(pk = venue_id)
    venue.delete()

    return redirect('event-list')

def deletevenue(req,venue_id):
    venue  = Venue.objects.get(pk = venue_id)
    venue.delete()

    return redirect('venues')

def venuedetails(req,venue_id):
    venue  = Venue.objects.get(pk = venue_id)
    return render(req, "events/venuedetails.html", {
        'venue':venue

        
       
    })
def updatevenue(req,venue_id):
    venue  = Venue.objects.get(pk = venue_id)
    form  = VenueForm(req.POST or None,instance=venue)
    if form.is_valid():
            form.save()
            return redirect('venues')
    return render(req, "events/update.html", {
        'venue':venue,
        'form':form

        
       
    })

def updateevent(req,venue_id):
    venue  = Event.objects.get(pk = venue_id)
    form  = EventForm(req.POST or None,instance=venue)
    if form.is_valid():
            form.save()
            return redirect('event-list')
    return render(req, "events/update_event.html", {
        'venue':venue,
        'form':form

        
       
    })


def venues(req):
    # Set up paginator
    p = Paginator(Venue.objects.all(),3)
    page = req.GET.get('page')
    venue_list = p.get_page(page)

    # venue_list  = Venue.objects.all().order_by('name')



    return render(req, "events/venues.html", {

        'venue_list':venue_list
       
    })

def add_venue(req):
    submitted = False
    if req.method == "POST":
        form = VenueForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-venue?submitted=True')
    else:
        form  = VenueForm
        if 'submitted' in req.GET:
            submitted = True;
    return render(req,'events/add_venue.html',{
        'form':form,
        'submitted':submitted
        

        })

def add_event(req):
    submitted = False
    if req.method == "POST":
        form = EventForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-event?submitted=True')
    else:
        form  = EventForm
        if 'submitted' in req.GET:
            submitted = True;
    return render(req,'events/add_events.html',{
        'form':form,
        'submitted':submitted
        

        })


def home(req, year=datetime.now().year, month=datetime.now().strftime('%B')):

    # Variables passed to the template
    name = "jk"
    month = month.title()  # Capitalizing the month name
    try:
        month_num = list(calendar.month_name).index(month)  # Get the month number
    except ValueError:
        month_num = 1  # Default to January if invalid month name is given

    cal = HTMLCalendar().formatmonth(year, month_num)  # Get the calendar for the given year and month

    now = datetime.now()  # Get the current datetime
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')  # Format time as a 12-hour clock with AM/PM

    # Render the template and pass the variables
    return render(req, "events/home.html", {
        "name": name,
        "year": year,
        "month": month,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })


def events(req):
    event_list = Event.objects.all().order_by('name')
    return render(req,'events/events.html',{
        'event_list': event_list

    })
