from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('order-purchase/',order_purchase,name="order-purchase"),
    path('delete-orders/<int:id>/',delete_orders, name="delete-orders"), 
    path('order-purchase/<int:id>',bill_view,name="order-purchase"), 

    # path('edit-orders/<int:id>/',edit_orders,name="edit-orders"),

    path('binding_orders/',binding_orders,name="binding_orders"),
    path('binding_orders/<int:id>',binding_bill_view,name="binding_orders"),
    path('delete_binding/<int:id>/',delete_binding, name="delete_binding"),
    # path('edit_binding/<int:id>/',edit_binding,name="edit_binding"),
    path('approve_order/<int:id>',approve_order,name="approve_order"),

    path('bill_sundries/',bill_sundries,name="bill_sundries"),
    path('production_voucher/',production_voucher,name="production_voucher"),
    path('production_voucher/<int:id>/',production_voucher_view,name="production_voucher_view"),
    path('production_voucher_delete/<int:id>/',production_voucher_delete,name="production_voucher_delete"),

    path('bill_of_material/<int:id>/',bill_of_material_view,name="bill_of_material_view"), 

    

    path('bill_of_material/',bill_of_material,name="bill_of_material"),
    path('sale_voucher/',sale_voucher1,name="sale_voucher"),

    path('sale_voucher/<int:id>/',sale_voucher_view,name="sale_voucher_view"),
    path('delete_sale_voucher/<int:id>/',delete_sale_voucher, name="delete_sale_voucher"),
    path('delete_bill_of_material/<int:id>/',delete_bill_of_material, name="delete_bill_of_material"),




]