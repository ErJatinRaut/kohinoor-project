from django.contrib import admin
from testapp.models import User,Role_data
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','mobile']

admin.site.register(User,UserAdmin)    
admin.site.register(Role_data)  