from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cover_recoding/',cover_recoding,name="cover_recoding"),
    path('delete_cover_record/<int:id>/',delete_cover_record,name="delete_cover_record"),
    path('edit_cover_record/<int:id>/',edit_cover_record,name="edit_cover_record"),


    path('cover_lamination/',cover_lamination,name="cover_lamination"),
    path('delete_cover_lamination/<int:id>/',delete_cover_lamination,name="delete_cover_lamination"),
    path('edit_cover_lamination/<int:id>/',edit_cover_lamination,name="edit_cover_lamination"),
    
    path('cover_lami_bill_view/<int:id>/',cover_lami_bill_view,name="cover_lami_bill_view"),



    path('cover_texture/',cover_texture,name="cover_texture"),
    path('delete_cover_texture/<int:id>/',delete_cover_texture,name="delete_cover_texture"),
    path('edit_cover_texture/<int:id>/',edit_cover_texture,name="edit_cover_texture"),
    path('cover_tex_bill_view/<int:id>/',cover_tex_bill_view,name="cover_tex_bill_view"),

    path('topi/',topi,name="topi"),
    path('delete_topi/<int:id>/',delete_topi,name="delete_topi"),
    path('edit_topi/<int:id>/',edit_topi,name="edit_topi"),


    path('topi_order/',topi_order,name="topi_order"),
    path('topi_order/<int:id>/',topi_bill_view,name="topi_bill_view"),
    path('delete_topi_order/<int:id>/',delete_topi_order,name="delete_topi_order"),


    path('cover_cutting/',cover_cutting,name="cover_cutting"),
    path('delete_cover_cutting/<int:id>/',delete_cover_cutting,name="delete_cover_cutting"),
    path('edit_cover_cutting/<int:id>/',edit_cover_cutting,name="edit_cover_cutting"),
    path('view_cover_cutting/<int:id>/',view_cover_cutting,name="view_cover_cutting"),


    path('sale_bill/',sale_bill,name="sale_bill"),
    path('sale_bill/<int:id>/',sale_bill_view,name="sale_bill_view"),
    path('delete_sale_bill/<int:id>/',delete_sale_bill,name="delete_sale_bill"),


    path('sale_return/',sale_return,name="sale_return"),
    path('delete_sale_return/<int:id>/',delete_sale_return,name="delete_sale_return"),
    path('sale_return/<int:id>/',sale_return_view,name="sale_return_view"),
    

    path('cost_production/',cost_production,name="cost_production"),
    path('edit_cost_production/<int:id>/',edit_cost_production,name="edit_cost_production"),
    path('delete_cost_production/<int:id>/',delete_cost_production,name="delete_cost_production"),

    path('sale_type/',sale_type,name="sale_type"),
    
    path('purchase_type/',purchase_type,name="purchase_type"),

    path('cover_available/',cover_available,name="cover_available"),
    path('view_cover_available/<int:id>/',view_cover_available,name="view_cover_available"),
    path('delete_cover_available/<int:id>/',delete_cover_available,name="delete_cover_available"),

    path('topi_available/',topi_available,name = "topi_available"),
    path('delete_topi_available/<int:id>/',delete_topi_available,name="delete_topi_available"),
    path('view_topi_available/<int:id>/',view_topi_available,name="view_topi_available"),


]