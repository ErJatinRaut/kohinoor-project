from django.contrib import admin



# Register your models here.
from .models import *
admin.site.register(Cover_record)
admin.site.register(Cover_texture)
admin.site.register(Cover_lamination)
admin.site.register(Topi)
admin.site.register(Topi_order)
admin.site.register(Cover_cutting)
admin.site.register(Sale_bill)
admin.site.register(Sale_return)
admin.site.register(Cost_production)
admin.site.register(Sale_type)
admin.site.register(Purchase_type)
admin.site.register(Cover_available)
admin.site.register(Topi_available)