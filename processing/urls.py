from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('printing-data/',printing_data,name="printing-data"),
    path('edit-printing/<int:order_id>/',edit_printing,name="edit-printing"),
    path('view-printing/<int:order_id>/',view_printing,name="view-printing"),
    path('bindings-data/',binding_data,name="bindings-data"),
    path('edit-bindings/<int:order_id>/',edit_binding,name="edit-bindings"),
    path('cutting-data/',cutting_form,name="cutting-data"),
    path('edit-cutting/<int:order_id>/',edit_cutting,name="edit-cutting"),
    path('gathering-info/',gathering_info,name='gathering-info'),
    path('edit-gathering/<int:order_id>/',view_gathering_info,name='edit-gathering'),
    path('manual-binding/',new_binding_spark,name="binding_spark"),
    path('edit-spark-bindings/<int:order_id>/',newedit_spark_binding,name="edit_spark_binding"),

    path('printing_transfer/',printing_transfer,name="printing_transfer"),
    path('edit_printing_transfer/<int:id>/', edit_printing_transfer, name="edit_printing_transfer"),
    path('delete_printing_transfer/<int:id>/', delete_printing_transfer, name="delete_printing_transfer"),

    path('transfer_cover/',transfer_cover,name="transfer_cover"),
    path('delete_cover_transfer/<int:id>/', delete_cover_transfer, name="delete_cover_transfer"),
    path('edit_cover_transfer/<int:id>/', edit_cover_transfer, name="edit_cover_transfer"),

    path('topi_transfer/',topi_transfer,name="topi_transfer"),
    path('delete_topi_transfer/<int:id>/', delete_topi_transfer, name="delete_topi_transfer"),
    path('edit_topi_transfer/<int:id>/', edit_topi_transfer, name="edit_topi_transfer"),
    
    
    


]


