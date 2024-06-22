from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(orders)
admin.site.register(Bindingorder)
admin.site.register(Bill_sundry)
admin.site.register(product_voucher)
admin.site.register(BOM)
admin.site.register(sale_voucher)