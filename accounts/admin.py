from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Owner)
admin.site.register(Volunteer)
# admin.site.register(Tag)
# admin.site.register(Order)
admin.site.register(Dogs)