from django.contrib import admin
from .models import Lost , Found , ContactOffice
# Register your models here.
admin.site.register(Lost)
admin.site.register(Found)
admin.site.register(ContactOffice)
