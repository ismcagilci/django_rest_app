from django.contrib import admin
from .models import vehicle,navigationRecord,Operation,Bin
# Register your models here.


admin.site.register(vehicle)
admin.site.register(navigationRecord)
admin.site.register(Operation)
admin.site.register(Bin)