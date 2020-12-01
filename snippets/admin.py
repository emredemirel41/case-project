from django.contrib import admin
from .models import DeviceLog, Device


admin.site.register(DeviceLog)
admin.site.register(Device)