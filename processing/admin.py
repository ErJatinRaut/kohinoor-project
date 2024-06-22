from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Manual_binding)
admin.site.register(transfer_printing_module)
admin.site.register(cover_transfer)
admin.site.register(transfer_topi)


