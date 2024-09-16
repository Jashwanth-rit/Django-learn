"""
URL configuration for django_learn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
   
     path('',views.home,name="home"),

# manuplating url giving , pattren of url

# pattern in type 
# int
# str
# slug to pass hyphon that kind of stuff
# path - to pass whole url

     path('<int:year>/<str:month>',views.home,name="home"),

# display events - defining url
    
     path('events',views.events,name="event-list"),
     path('add-venue',views.add_venue,name="add-venue"),

     path('add-event',views.add_event,name="add-event"),

     path('venues',views.venues,name="venues"),

     path('venue_details/<venue_id>',views.venuedetails,name="venuedetailes"),
      path('update/<venue_id>',views.updatevenue,name="updatevenue"),
      path('update_event/<venue_id>',views.updateevent,name="updateevent"),
       path('delete_event/<venue_id>',views.deleteevent,name="deleteevent"),
        path('delete_venue/<venue_id>',views.deletevenue,name="deletevenue"),
     path('search',views.search,name="search"),
      path('searchEvent',views.searchEvent,name="searchEvent"),
 path('venue_csv',views.venuecsv,name="venuecsv"),

path('venue_text',views.venuetext,name="venuetext"),
path('venue_events/<venue_name>',views.venue_events,name="venue_events"),
path('myevents',views.myevents,name="myevents"),

path('venue_pdf',views.venuepdf,name="venuepdf"),
path('admin_approval',views.admin_aprove,name="admin_aprove"),
]
