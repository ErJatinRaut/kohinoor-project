from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('shrink-packing/',packing_view,name="shrink-data"),
    path('bitti-packing/',bitti_packing,name="packing-data"),
    path('delete-packing/<int:id>/',delete_packing, name="delete-packing"),
    path('edit-packing/<int:id>/',edit_packing, name="edit-packing"),
    path('edit-bitti/<int:id>/',edit_bitti,name="edit-bitti"),
    path('delete-bitti/<int:id>/',delete_bitti, name="delete-bitti"),
    path('shrink-transfer/<int:id>',shrink_transfer,name="shrink-transfer"),
    path('shrink_transfer_to/',shrink_transfer_to,name="shrink_transfer_to"),

    path('pending-shrink-transfer/<int:id>/',pending_shrink_transfer,name="pending-shrink-transfer"),
   
]
