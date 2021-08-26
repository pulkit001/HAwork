from django.contrib import admin
from .models import Lost , Found , ContactOffice
# Register your models here.

admin.site.site_header = "IIT Bombay Security"

class LostAdmin(admin.ModelAdmin):
    list_display = ('Article' , 'Date' , 'Contact')

class FoundAdmin(admin.ModelAdmin):
    list_display = ('Article' , 'Date' , 'Contact')

admin.site.register(Lost , LostAdmin)
admin.site.register(Found , FoundAdmin)
admin.site.register(ContactOffice)
