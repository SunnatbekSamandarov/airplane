from django.contrib import admin
from .models import Flight,Book,Hotel,Country,Contact
# Register your models here.
class FlightAdmin(admin.ModelAdmin):

    pass
class BookAdmin(admin.ModelAdmin):
    pass
class HotelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flight,FlightAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Contact)
admin.site.register(Country)

