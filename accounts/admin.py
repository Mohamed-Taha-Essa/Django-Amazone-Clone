from django.contrib import admin
from . models import Address , Profile ,ContactNumber
# Register your models here.

admin.site.register(Address)
admin.site.register(Profile)
admin.site.register(ContactNumber)