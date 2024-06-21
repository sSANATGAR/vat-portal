from django.contrib import admin
from .models import Cards, Firmware, Cars
from .forms import FirmwareAdminForm

class CarsAdmin(admin.ModelAdmin):
    list_display = ('license_plate_max', 'mac_address', 'firmware_version', 'rfids')

admin.site.register(Cars, CarsAdmin)

class FirmwareAdmin(admin.ModelAdmin):
    form = FirmwareAdminForm
    list_display = ['version', 'firmware_file']


admin.site.register(Firmware, FirmwareAdmin)
admin.site.register(Cards)