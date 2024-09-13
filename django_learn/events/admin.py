from django.contrib import admin
from .models import Event
from .models import Venue
from .models import Attenders


# Register your models here.


admin.site.register(Event)
# admin.site.register(Venue)
admin.site.register(Attenders)

# process of changing interface of venue table display in admin interface

@admin.register(Venue)

class VenueAdmin(admin.ModelAdmin):
    # To display this columns in interface 
    list_display = ('name','address','web')
    # To sort table in order of alphabet A-Z
    ordering = ('name',)
    # TO search by name or address
    search_fields = ('name','address')
    # To filter by address or to add filters bar
    list_filter = ('name','address')
    # To gruop by fields
    fields = (('name','address'),('web','email_address'),'zip_code')

