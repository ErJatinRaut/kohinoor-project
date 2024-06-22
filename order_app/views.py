from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from multiprocessing import context
from os import system
from django.shortcuts import render, redirect
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from brand_app.models import *
from django.http import JsonResponse
from order_app.models import *
from order_app.models import orders
from brand_app.models import venders
import time
import random
import sweetify
from brand_app.models import *
from django.db.models import Q




from processing.models import *

from processing.models import *
from django.core.mail import send_mail
from django.db.models import Q
def order_purchase(request):
    # brands = {
    #     'Kohinoor': {'pages_per_form': 64},
    #     'Spark': {'pages_per_form': 128},
    #     'Vidya Mitra': {'pages_per_form': 32},
    #     'Abhiyashika': {'pages_per_form': 64},
    #     'Kohinoor Abhyashika':{'pages_per_form': 64},
    # }
    brands= books.objects.all()
    order = orders.objects.all()
    book = books.objects.all()
    data = orders.objects.all().order_by('-purchase_date')
    vendor = venders.objects.all()
    if request.method == 'POST':
        if request.POST.get("create_form_btn") == "save_cashmemo_btn":
            order_id = str(int(time.time())) + str(random.randint(1, 9))
            single_1, double_1,four_1,rate1,single_2,double_2,four_2,rate2, = [request.POST.get(i) for i in ['single_1', 'double_1', 'four_1','rate1', 'single_2', 'double_2','four_2','rate2']]
            id, no_of_pages, gst, purchase_date, forms = [request.POST.get(i) for i in ['id', 'no_of_pages', 'gst', 'purchase_date', 'forms']]
            vender_name, vender_address, vender_mob, vender_email = [request.POST.get(i) for i in ['vender_name', 'vender_address', 'vender_mob', 'vender_email']]
            vedd= request.POST.get('vender_name')
            material_center= request.POST.get('material_center'),
            print('uuuuuuuuuu',vedd)
            vender=venders.objects.get(id=vedd)
            print('cvbnm',vender)
            print('ghdrgtfrgr',vender.organization_name, vender.vender_address, vender.vender_email)
            items = []
            for i in range(1, 51):
                item = []
                for j in ['brand_name', 'class_name', 'medium', 'subject', 'quantity', 'rim']:
                    value = request.POST.get(f'{j}_{i}')
                    if value:
                        item.append(str(value))
                items.append(','.join(item))
            total_quantity = sum([float(request.POST.get(f'quantity_{i}')) for i in range(1, 51) if request.POST.get(f'quantity_{i}')])
            order = orders.objects.create(purchase_date=datetime.datetime.now(),
            vender_name=vender.organization_name, vender_mob=vender_mob, vender_address=vender_address, 
            item1=items[0],item11=items[10],item21=items[20],item31=items[30],item41=items[40],
            item2=items[1],item12=items[11],item22=items[21],item32=items[31],item42=items[41],
            item3=items[2],item13=items[12],item23=items[22],item33=items[32],item43=items[42],
            item4=items[3],item14=items[13],item24=items[23],item34=items[33],item44=items[43],
            item5=items[4],item15=items[14],item25=items[24],item35=items[34],item45=items[44],
            item6=items[5],item16=items[15],item26=items[25],item36=items[35],item46=items[45],
            item7=items[6],item17=items[16],item27=items[26],item37=items[36],item47=items[46],
            item8=items[7],item18=items[17],item28=items[27],item38=items[37],item48=items[47],
            item9=items[8],item19=items[18],item29=items[28],item39=items[38],item49=items[48],
            item10=items[9],item20=items[19],item30=items[29],item40=items[39],item50=items[49],
            vender_email=vender.vender_email,
            no_of_pages=no_of_pages, gst=gst, order_id=order_id, total_quantity=total_quantity,single_1=single_1,double_1=double_1,four_1=four_1,rate1=rate1,single_2=single_2,double_2=double_2,four_2=four_2,rate2=rate2,
                
            brand_name_1=request.POST.get('brand_name_1'), class_name_1=request.POST.get('class_name_1'), medium_1=request.POST.get('medium_1'), subject_1=request.POST.get('subject_1'), quantity_1=request.POST.get('quantity_1'), pages_1=request.POST.get('pages_1'),
            brand_name_2=request.POST.get('brand_name_2'), class_name_2=request.POST.get('class_name_2'), medium_2=request.POST.get('medium_2'), subject_2=request.POST.get('subject_2'), quantity_2=request.POST.get('quantity_2'), pages_2=request.POST.get('pages_2'),
            brand_name_3=request.POST.get('brand_name_3'), class_name_3=request.POST.get('class_name_3'), medium_3=request.POST.get('medium_3'), subject_3=request.POST.get('subject_3'), quantity_3=request.POST.get('quantity_3'), pages_3=request.POST.get('pages_3'),
            brand_name_4=request.POST.get('brand_name_4'), class_name_4=request.POST.get('class_name_4'), medium_4=request.POST.get('medium_4'), subject_4=request.POST.get('subject_4'),quantity_4=request.POST.get('quantity_4'), pages_4=request.POST.get('pages_4'),
            brand_name_5=request.POST.get('brand_name_5'), class_name_5=request.POST.get('class_name_5'), medium_5=request.POST.get('medium_5'), subject_5=request.POST.get('subject_5'),quantity_5=request.POST.get('quantity_5'), pages_5=request.POST.get('pages_5'),
            brand_name_6=request.POST.get('brand_name_6'), class_name_6=request.POST.get('class_name_6'), medium_6=request.POST.get('medium_6'), subject_6=request.POST.get('subject_6'),quantity_6=request.POST.get('quantity_6'), pages_6=request.POST.get('pages_6'),
            brand_name_7=request.POST.get('brand_name_7'), class_name_7=request.POST.get('class_name_7'), medium_7=request.POST.get('medium_7'), subject_7=request.POST.get('subject_7'),quantity_7=request.POST.get('quantity_7'), pages_7=request.POST.get('pages_7'),
            brand_name_8=request.POST.get('brand_name_8'), class_name_8=request.POST.get('class_name_8'), medium_8=request.POST.get('medium_8'), subject_8=request.POST.get('subject_8'),quantity_8=request.POST.get('quantity_8'), pages_8=request.POST.get('pages_8'),
            brand_name_9=request.POST.get('brand_name_9'), class_name_9=request.POST.get('class_name_9'), medium_9=request.POST.get('medium_9'), subject_9=request.POST.get('subject_9'),quantity_9=request.POST.get('quantity_9'), pages_9=request.POST.get('pages_9'),
            brand_name_10=request.POST.get('brand_name_10'), class_name_10=request.POST.get('class_name_10'), medium_10=request.POST.get('medium_10'), subject_10=request.POST.get('subject_10'),quantity_10=request.POST.get('quantity_10'), pages_10=request.POST.get('pages_10'),
            brand_name_11=request.POST.get('brand_name_11'), class_name_11=request.POST.get('class_name_11'), medium_11=request.POST.get('medium_11'), subject_11=request.POST.get('subject_11'),quantity_11=request.POST.get('quantity_11'), pages_11=request.POST.get('pages_11'),
            brand_name_12=request.POST.get('brand_name_12'), class_name_12=request.POST.get('class_name_12'), medium_12=request.POST.get('medium_12'), subject_12=request.POST.get('subject_12'),quantity_12=request.POST.get('quantity_12'), pages_12=request.POST.get('pages_12'),
            brand_name_13=request.POST.get('brand_name_13'), class_name_13=request.POST.get('class_name_13'), medium_13=request.POST.get('medium_13'), subject_13=request.POST.get('subject_13'),quantity_13=request.POST.get('quantity_13'), pages_13=request.POST.get('pages_13'),
            brand_name_14=request.POST.get('brand_name_14'), class_name_14=request.POST.get('class_name_14'), medium_14=request.POST.get('medium_14'), subject_14=request.POST.get('subject_14'),quantity_14=request.POST.get('quantity_14'), pages_14=request.POST.get('pages_14'),
            brand_name_15=request.POST.get('brand_name_15'), class_name_15=request.POST.get('class_name_15'), medium_15=request.POST.get('medium_15'), subject_15=request.POST.get('subject_15'),quantity_15=request.POST.get('quantity_15'), pages_15=request.POST.get('pages_15'),
            brand_name_16=request.POST.get('brand_name_16'), class_name_16=request.POST.get('class_name_16'), medium_16=request.POST.get('medium_16'), subject_16=request.POST.get('subject_16'),quantity_16=request.POST.get('quantity_16'), pages_16=request.POST.get('pages_16'),
            brand_name_17=request.POST.get('brand_name_17'), class_name_17=request.POST.get('class_name_17'), medium_17=request.POST.get('medium_17'), subject_17=request.POST.get('subject_17'),quantity_17=request.POST.get('quantity_17'), pages_17=request.POST.get('pages_17'),
            brand_name_18=request.POST.get('brand_name_18'), class_name_18=request.POST.get('class_name_18'), medium_18=request.POST.get('medium_18'), subject_18=request.POST.get('subject_18'),quantity_18=request.POST.get('quantity_18'), pages_18=request.POST.get('pages_18'),
            brand_name_19=request.POST.get('brand_name_19'), class_name_19=request.POST.get('class_name_19'), medium_19=request.POST.get('medium_19'), subject_19=request.POST.get('subject_19'),quantity_19=request.POST.get('quantity_19'), pages_19=request.POST.get('pages_19'),
            brand_name_20=request.POST.get('brand_name_20'), class_name_20=request.POST.get('class_name_20'), medium_20=request.POST.get('medium_20'), subject_20=request.POST.get('subject_20'),quantity_20=request.POST.get('quantity_20'), pages_20=request.POST.get('pages_20'),
            brand_name_21=request.POST.get('brand_name_21'), class_name_21=request.POST.get('class_name_21'), medium_21=request.POST.get('medium_21'), subject_21=request.POST.get('subject_21'),quantity_21=request.POST.get('quantity_21'), pages_21=request.POST.get('pages_21'),
            brand_name_22=request.POST.get('brand_name_22'), class_name_22=request.POST.get('class_name_22'), medium_22=request.POST.get('medium_22'), subject_22=request.POST.get('subject_22'),quantity_22=request.POST.get('quantity_22'), pages_22=request.POST.get('pages_22'),
            brand_name_23=request.POST.get('brand_name_23'), class_name_23=request.POST.get('class_name_23'), medium_23=request.POST.get('medium_23'), subject_23=request.POST.get('subject_23'),quantity_23=request.POST.get('quantity_23'), pages_23=request.POST.get('pages_23'),
            brand_name_24=request.POST.get('brand_name_24'), class_name_24=request.POST.get('class_name_24'), medium_24=request.POST.get('medium_24'), subject_24=request.POST.get('subject_24'),quantity_24=request.POST.get('quantity_24'), pages_24=request.POST.get('pages_24'),
            brand_name_25=request.POST.get('brand_name_25'), class_name_25=request.POST.get('class_name_25'), medium_25=request.POST.get('medium_25'), subject_25=request.POST.get('subject_25'),quantity_25=request.POST.get('quantity_25'), pages_25=request.POST.get('pages_25'),
            brand_name_26=request.POST.get('brand_name_26'), class_name_26=request.POST.get('class_name_26'), medium_26=request.POST.get('medium_26'), subject_26=request.POST.get('subject_26'),quantity_26=request.POST.get('quantity_26'), pages_26=request.POST.get('pages_26'),
            brand_name_27=request.POST.get('brand_name_27'), class_name_27=request.POST.get('class_name_27'), medium_27=request.POST.get('medium_27'), subject_27=request.POST.get('subject_27'),quantity_27=request.POST.get('quantity_27'), pages_27=request.POST.get('pages_27'),
            brand_name_28=request.POST.get('brand_name_28'), class_name_28=request.POST.get('class_name_28'), medium_28=request.POST.get('medium_28'), subject_28=request.POST.get('subject_28'),quantity_28=request.POST.get('quantity_28'), pages_28=request.POST.get('pages_28'),
            brand_name_29=request.POST.get('brand_name_29'), class_name_29=request.POST.get('class_name_29'), medium_29=request.POST.get('medium_29'), subject_29=request.POST.get('subject_29'),quantity_29=request.POST.get('quantity_29'), pages_29=request.POST.get('pages_29'),
            brand_name_30=request.POST.get('brand_name_30'), class_name_30=request.POST.get('class_name_30'), medium_30=request.POST.get('medium_30'), subject_30=request.POST.get('subject_30'),quantity_30=request.POST.get('quantity_30'), pages_30=request.POST.get('pages_30'),
            brand_name_31=request.POST.get('brand_name_31'), class_name_31=request.POST.get('class_name_31'), medium_31=request.POST.get('medium_31'), subject_31=request.POST.get('subject_31'),quantity_31=request.POST.get('quantity_31'), pages_31=request.POST.get('pages_31'),
            brand_name_32=request.POST.get('brand_name_32'), class_name_32=request.POST.get('class_name_32'), medium_32=request.POST.get('medium_32'), subject_32=request.POST.get('subject_32'),quantity_32=request.POST.get('quantity_32'), pages_32=request.POST.get('pages_32'),
            brand_name_33=request.POST.get('brand_name_33'), class_name_33=request.POST.get('class_name_33'), medium_33=request.POST.get('medium_33'), subject_33=request.POST.get('subject_33'),quantity_33=request.POST.get('quantity_33'), pages_33=request.POST.get('pages_33'),
            brand_name_34=request.POST.get('brand_name_34'), class_name_34=request.POST.get('class_name_34'), medium_34=request.POST.get('medium_34'), subject_34=request.POST.get('subject_34'),quantity_34=request.POST.get('quantity_34'), pages_34=request.POST.get('pages_34'),
            brand_name_35=request.POST.get('brand_name_35'), class_name_35=request.POST.get('class_name_35'), medium_35=request.POST.get('medium_35'), subject_35=request.POST.get('subject_35'),quantity_35=request.POST.get('quantity_35'), pages_35=request.POST.get('pages_35'),
            brand_name_36=request.POST.get('brand_name_36'), class_name_36=request.POST.get('class_name_36'), medium_36=request.POST.get('medium_36'), subject_36=request.POST.get('subject_36'),quantity_36=request.POST.get('quantity_36'), pages_36=request.POST.get('pages_36'),
            brand_name_37=request.POST.get('brand_name_37'), class_name_37=request.POST.get('class_name_37'), medium_37=request.POST.get('medium_37'), subject_37=request.POST.get('subject_37'),quantity_37=request.POST.get('quantity_37'), pages_37=request.POST.get('pages_37'),
            brand_name_38=request.POST.get('brand_name_38'), class_name_38=request.POST.get('class_name_38'), medium_38=request.POST.get('medium_38'), subject_38=request.POST.get('subject_38'),quantity_38=request.POST.get('quantity_38'), pages_38=request.POST.get('pages_38'),
            brand_name_39=request.POST.get('brand_name_39'), class_name_39=request.POST.get('class_name_39'), medium_39=request.POST.get('medium_39'), subject_39=request.POST.get('subject_39'),quantity_39=request.POST.get('quantity_39'), pages_39=request.POST.get('pages_39'),
            brand_name_40=request.POST.get('brand_name_40'), class_name_40=request.POST.get('class_name_40'), medium_40=request.POST.get('medium_40'), subject_40=request.POST.get('subject_40'),quantity_40=request.POST.get('quantity_40'), pages_40=request.POST.get('pages_40'),
            brand_name_41=request.POST.get('brand_name_41'), class_name_41=request.POST.get('class_name_41'), medium_41=request.POST.get('medium_41'), subject_41=request.POST.get('subject_41'),quantity_41=request.POST.get('quantity_41'), pages_41=request.POST.get('pages_41'),
            brand_name_42=request.POST.get('brand_name_42'), class_name_42=request.POST.get('class_name_42'), medium_42=request.POST.get('medium_42'), subject_42=request.POST.get('subject_42'),quantity_42=request.POST.get('quantity_42'), pages_42=request.POST.get('pages_42'),
            brand_name_43=request.POST.get('brand_name_43'), class_name_43=request.POST.get('class_name_43'), medium_43=request.POST.get('medium_43'), subject_43=request.POST.get('subject_43'),quantity_43=request.POST.get('quantity_43'), pages_43=request.POST.get('pages_43'),
            brand_name_44=request.POST.get('brand_name_44'), class_name_44=request.POST.get('class_name_44'), medium_44=request.POST.get('medium_44'), subject_44=request.POST.get('subject_44'),quantity_44=request.POST.get('quantity_44'), pages_44=request.POST.get('pages_44'),
            brand_name_45=request.POST.get('brand_name_45'), class_name_45=request.POST.get('class_name_45'), medium_45=request.POST.get('medium_45'), subject_45=request.POST.get('subject_45'),quantity_45=request.POST.get('quantity_45'), pages_45=request.POST.get('pages_45'),
            brand_name_46=request.POST.get('brand_name_46'), class_name_46=request.POST.get('class_name_46'), medium_46=request.POST.get('medium_46'), subject_46=request.POST.get('subject_46'),quantity_46=request.POST.get('quantity_46'), pages_46=request.POST.get('pages_46'),
            brand_name_47=request.POST.get('brand_name_47'), class_name_47=request.POST.get('class_name_47'), medium_47=request.POST.get('medium_47'), subject_47=request.POST.get('subject_47'),quantity_47=request.POST.get('quantity_47'), pages_47=request.POST.get('pages_47'),
            brand_name_48=request.POST.get('brand_name_48'), class_name_48=request.POST.get('class_name_48'), medium_48=request.POST.get('medium_48'), subject_48=request.POST.get('subject_48'),quantity_48=request.POST.get('quantity_48'), pages_48=request.POST.get('pages_48'),
            brand_name_49=request.POST.get('brand_name_49'), class_name_49=request.POST.get('class_name_49'), medium_49=request.POST.get('medium_49'), subject_49=request.POST.get('subject_49'),quantity_49=request.POST.get('quantity_49'), pages_49=request.POST.get('pages_49'),
            brand_name_50=request.POST.get('brand_name_50'), class_name_50=request.POST.get('class_name_50'), medium_50=request.POST.get('medium_50'), subject_50=request.POST.get('subject_50'),quantity_50=request.POST.get('quantity_50'), pages_50=request.POST.get('pages_50'),
            code_1 = request.POST.get('code_1'),
            code_2 = request.POST.get('code_2'),
            code_3 = request.POST.get('code_3'),
            code_4 = request.POST.get('code_4'),
            code_5 = request.POST.get('code_5'),
            rim_1 = request.POST.get('rim_1'),
            pform_1 = request.POST.get('pform_1'),
            rim_2= request.POST.get('rim_2'),
            pform_2 = request.POST.get('pform_2'),
            rim_3 = request.POST.get('rim_3'),
            pform_3 = request.POST.get('pform_3'),
            rim_4 = request.POST.get('rim_4'),
            pform_4 = request.POST.get('pform_4'),
            rim_5 = request.POST.get('rim_5'),
            pform_5 = request.POST.get('pform_5'),
            rim_6 = request.POST.get('rim_6'),
            pform_6 = request.POST.get('pform_6'),
            rim_7 = request.POST.get('rim_7'),
            pform_7 = request.POST.get('pform_7'),
            rim_8 = request.POST.get('rim_8'),
            pform_8 = request.POST.get('pform_8'),
            rim_9 = request.POST.get('rim_9'),
            pform_9 = request.POST.get('pform_9'),
            rim_10 = request.POST.get('rim_10'),
            pform_10 = request.POST.get('pform_10'),

            rim_11 = request.POST.get('rim_11'),
            pform_11 = request.POST.get('pform_11'),
            rim_12 = request.POST.get('rim_12'),
            pform_12 = request.POST.get('pform_12'),
            rim_13 = request.POST.get('rim_13'),
            pform_13 = request.POST.get('pform_13'),
            rim_14 = request.POST.get('rim_14'),
            pform_14 = request.POST.get('pform_14'),
            rim_15 = request.POST.get('rim_15'),
            pform_15 = request.POST.get('pform_15'),
            rim_16 = request.POST.get('rim_16'),
            pform_16 = request.POST.get('pform_16'),
            rim_17 = request.POST.get('rim_17'),
            pform_17 = request.POST.get('pform_17'),
            rim_18 = request.POST.get('rim_18'),
            pform_18 = request.POST.get('pform_18'),
            rim_19 = request.POST.get('rim_19'),
            pform_19 = request.POST.get('pform_19'),
            rim_20 = request.POST.get('rim_20'),
            pform_20 = request.POST.get('pform_20'),
            rim_21 = request.POST.get('rim_21'),
            pform_21 = request.POST.get('pform_21'),
            rim_22 = request.POST.get('rim_22'),
            pform_22 = request.POST.get('pform_22'),
            rim_23= request.POST.get('rim_23'),
            pform_23 = request.POST.get('pform_23'),
            rim_24 = request.POST.get('rim_24'),
            pform_24 = request.POST.get('pform_24'),
            rim_25 = request.POST.get('rim_25'),
            pform_25= request.POST.get('pform_25'),
            rim_26 = request.POST.get('rim_26'),
            pform_26 = request.POST.get('pform_26'),
            rim_27 = request.POST.get('rim_27'),
            pform_27 = request.POST.get('pform_27'),
            rim_28 = request.POST.get('rim_28'),
            pform_28 = request.POST.get('pform_28'),
            rim_29 = request.POST.get('rim_29'),
            pform_29 = request.POST.get('pform_29'),
            rim_30 = request.POST.get('rim_30'),
            pform_30 = request.POST.get('pform_30'),
            rim_31 = request.POST.get('rim_31'),
            pform_31 = request.POST.get('pform_31'),
            rim_32 = request.POST.get('rim_32'),
            pform_32 = request.POST.get('pform_32'),
            rim_33 = request.POST.get('rim_33'),
            pform_33 = request.POST.get('pform_33'),
            rim_34 = request.POST.get('rim_34'),
            pform_34 = request.POST.get('pform_34'),
            rim_35 = request.POST.get('rim_35'),
            pform_35 = request.POST.get('pform_35'),
            rim_36 = request.POST.get('rim_36'),
            pform_36 = request.POST.get('pform_36'),
            rim_37 = request.POST.get('rim_37'),
            pform_37 = request.POST.get('pform_37'),
            rim_38 = request.POST.get('rim_38'),
            pform_38 = request.POST.get('pform_38'),
            rim_39 = request.POST.get('rim_39'),
            pform_39 = request.POST.get('pform_39'),
            rim_40 = request.POST.get('rim_40'),
            pform_40 = request.POST.get('pform_40'),
            rim_41 = request.POST.get('rim_41'),
            pform_41 = request.POST.get('pform_41'),
            rim_42 = request.POST.get('rim_42'),
            pform_42 = request.POST.get('pform_42'),
            rim_43 = request.POST.get('rim_43'),
            pform_43 = request.POST.get('pform_43'),
            rim_44 = request.POST.get('rim_44'),
            pform_44 = request.POST.get('pform_44'),
            rim_45 = request.POST.get('rim_45'),
            pform_45 = request.POST.get('pform_45'),
            rim_46 = request.POST.get('rim_46'),
            pform_46 = request.POST.get('pform_46'),
            rim_47 = request.POST.get('rim_47'),
            pform_47 = request.POST.get('pform_47'),
            rim_48 = request.POST.get('rim_48'),
            pform_48 = request.POST.get('pform_48'),
            rim_49 = request.POST.get('rim_49'),
            pform_49 = request.POST.get('pform_49'),
            rim_50 = request.POST.get('rim_50'),
            pform_50 = request.POST.get('pform_50'),
            
            amount_1=request.POST.get('amount_1'), amount_2=request.POST.get('amount_2'),
            amount_3=request.POST.get('amount_3'), amount_4=request.POST.get('amount_4'),
            amount_5=request.POST.get('amount_5'),  amount_6=request.POST.get('amount_6'),
            amount_7=request.POST.get('amount_7'),  amount_8=request.POST.get('amount_8'),
            amount_9=request.POST.get('amount_9'),  amount_10=request.POST.get('amount_10'),
            amount_11=request.POST.get('amount_11'), amount_12=request.POST.get('amount_12'),
            amount_13=request.POST.get('amount_13'), amount_14=request.POST.get('amount_14'),
            amount_15=request.POST.get('amount_15'), amount_16=request.POST.get('amount_16'),
            amount_17=request.POST.get('amount_17'), amount_18=request.POST.get('amount_18'),
            amount_19=request.POST.get('amount_19'), amount_20=request.POST.get('amount_20'),
            amount_21=request.POST.get('amount_21'), amount_22=request.POST.get('amount_22'),
            amount_23=request.POST.get('amount_23'), amount_24=request.POST.get('amount_24'),
            amount_25=request.POST.get('amount_25'),  amount_26=request.POST.get('amount_26'),
            amount_27=request.POST.get('amount_27'), amount_28=request.POST.get('amount_28'),
            amount_29=request.POST.get('amount_29'), amount_30=request.POST.get('amount_30'),
            amount_31=request.POST.get('amount_31'),  amount_32=request.POST.get('amount_32'),
            amount_33=request.POST.get('amount_33'), amount_34=request.POST.get('amount_34'),
            amount_35=request.POST.get('amount_35'), amount_36=request.POST.get('amount_36'),
            amount_37=request.POST.get('amount_37'), amount_38=request.POST.get('amount_38'),
            amount_39=request.POST.get('amount_39'), amount_40=request.POST.get('amount_40'),
            amount_41=request.POST.get('amount_41'), amount_42=request.POST.get('amount_42'),
            amount_43=request.POST.get('amount_43'), amount_44=request.POST.get('amount_44'),
            amount_45=request.POST.get('amount_45'), amount_46=request.POST.get('amount_46'),
            amount_47=request.POST.get('amount_47'), amount_48=request.POST.get('amount_48'),
            amount_49=request.POST.get('amount_49'), amount_50=request.POST.get('amount_50'),

            
            company_name1= request.POST.get('company_name1'),
            )
            
            data = orders.objects.filter().order_by('-purchase_date')
            rim = []
            form = []
            amount = []
            for i in range(1, 51):
                rim_value = float(request.POST.get(f'rim_{i}', 0))  # Convert to integer, default to 0 if value is None
                rim.append(rim_value)
                quantity = request.POST.get(f'quantity_{i}')
                brand = request.POST.get(f'brand_name_{i}')
                form_value= float( request.POST.get(f'pform_{i}',0))
                total_value= float( request.POST.get(f'amount_{i}',0))
                
                form.append(form_value)
                amount.append(total_value)
            total_rim = sum(rim)
            total_form =sum(form)
            total_amount =sum(amount)
            print("Total Form:", total_form)
            print("Total Rim:", total_rim)
            print("Total Rim:", total_amount)
           
            order.total_rim = total_rim
            order.total_form = total_form
            order.total_amount = total_amount
            order.save()



            
           

            manual_bind=Manual_binding(order_id=order_id,brand_name1= order.brand_name_1,class_name1=order.class_name_1,medium1= order.medium_1,subject1 = order.subject_1, quantity1 = order.quantity_1,pages1=order.pages_1,brand_name2 = order.brand_name_2,class_name2 = order.class_name_2,medium2 = order.medium_2,
                                        subject2 = order.subject_2,
                                        quantity2 = order.quantity_2,
                                        pages2 = order.pages_2,

                                        brand_name3 = order.brand_name_3,
                                        class_name3 = order.class_name_3,
                                        medium3 = order.medium_3,
                                        subject3 = order.subject_3,
                                        quantity3 = order.quantity_3,
                                        pages3 = order.pages_3,

                                        brand_name4 = order.brand_name_4,
                                        class_name4 = order.class_name_4,
                                        medium4 = order.medium_4,
                                        subject4 = order.subject_4,
                                        quantity4 = order.quantity_4,
                                        pages4 = order.pages_4,

                                        brand_name5 = order.brand_name_5,
                                        class_name5 = order.class_name_5,
                                        medium5 = order.medium_5,
                                        subject5 = order.subject_5,
                                        quantity5 = order.quantity_5,
                                        pages5 = order.pages_5,


                                        brand_name6 = order.brand_name_6,
                                        class_name6 = order.class_name_6,
                                        medium6 = order.medium_6,
                                        subject6 = order.subject_6,
                                        quantity6 = order.quantity_6,
                                        pages6 = order.pages_6,

                                        brand_name7 = order.brand_name_7,
                                        class_name7 = order.class_name_7,
                                        medium7 = order.medium_7,
                                        subject7 = order.subject_7,
                                        quantity7 = order.quantity_7,
                                        pages7 = order.pages_7,

                                        brand_name8 = order.brand_name_8,
                                        class_name8 = order.class_name_8,
                                        medium8 = order.medium_8,
                                        subject8 = order.subject_8,
                                        quantity8 = order.quantity_8,
                                        pages8 = order.pages_8,

                                        brand_name9 = order.brand_name_9,
                                        class_name9 = order.class_name_9,
                                        medium9 = order.medium_9,
                                        subject9 = order.subject_9,
                                        quantity9 = order.quantity_9,
                                        pages9 = order.pages_9,

                                        brand_name10 = order.brand_name_10,
                                        class_name10 = order.class_name_10,
                                        medium10 = order.medium_10,
                                        subject10 = order.subject_10,
                                        quantity10 = order.quantity_10,
                                        pages10 = order.pages_10,
                                        
                                        material_center = material_center,
                                        
                                        
                                        
                                        
                                        )

            manual_bind.save()

            data1 = orders.objects.get(order_id=order_id)
            print('ddddeee',data1)

            if request.method == 'POST':
                if request.POST.get("order_approved") == "approval_button":
                    orders.objects.filter(Q(order_id=order_id) & Q(order_approved=False)).update(order_approved=True)
                else:
                    pass  


    book1 = Company.objects.all()       
    vend = venders.objects.all()
    book = books.objects.all() 
    for i in book:
       print(i.subbrand_printing_form_size)
    data8 = orders.objects.all().order_by('-order_id')
    obj = books.objects.values('code').distinct().order_by('code')
    obj1 = books.objects.values('books_name').distinct().order_by('books_name')
    obj2 = books.objects.values('books_class').distinct().order_by('books_class')
    obj3 = books.objects.values('medium').distinct().order_by('medium')
    obj4 = books.objects.values('subject').distinct().order_by('subject')
    obj5 = books.objects.values('no_of_pages').distinct().order_by('no_of_pages') 
    x=[i for i in range(1, 51)]
    

   

    data3 = material_centre.objects.all()
    return render(request, 'orders/neword.html', { 'data3':data3,'x':x,'vendor':vendor, 'orders':data, 'book':book, 'vend':vend, 'data8':data8,'obj1':obj1,'obj2':obj2,'obj3':obj3,'obj4':obj4,'obj5':obj5,'obj':obj,'book1':book1})


    
from django.core.mail import send_mail
from django.http import HttpResponse
from django.db import IntegrityError
def approve_order(request,id):
    student = orders.objects.get(id=id)        
    print('eerrrrrrrrrrrrrrrrrrrrrrrrr',student.vender_email)
    

    try:
        student = orders.objects.get(id=id)        
        print(student.vender_email)
        student.order_approved = False
        student.order_approved = True  # Disable the auditor
        order_approve = orders.objects.filter(order_approved=True)
        print('////////////////////',order_approve)
        student.save()
        eeee = orders.objects.get(id=id)
        print('kkkkkkkkkkk',eeee.vender_email)
        subject = 'Order Placed Sucessfully'
        message =  f"Dear {eeee.vender_name},\n\nA new order has been placed from Kohinoor Tez. Please see the attached Order Form for more details.\n\nBest Regards,\nTeam Kohinoor Tez"
        sender_email = 'pbambulkar9924@gmail.com'
        recipient_list = [eeee.vender_email]
        send_mail(subject, message, sender_email, recipient_list)
    
        
        return redirect('/order-purchase/')
    except IntegrityError:
        return HttpResponse("An error occurred while disabling the student", status=500)









    # vend = venders.objects.all()
    # book = books.objects.all()
    # data1 = venders.objects.values(
    #     'organization_name').distinct().order_by('organization_name')
    # data2 = venders.objects.values(
    #     'vender_address').distinct().order_by('vender_address')
    # data3 = brands.objects.values(
    #     'brand_name').distinct().order_by('brand_name')
    # data4 = books .objects.values(
    #     'books_name').distinct().order_by('books_name')
    # data5 = books .objects.values(
    #     'books_class').distinct().order_by('books_class')
    # data6 = books.objects.values('subject').distinct().order_by('subject')
    # data7 = mediums.objects.values('medium').distinct().order_by('medium')
    # data8 = orders.objects.filter().order_by('-purchase_date')
    # data9 = classes.objects.values('class_name').distinct().order_by('class_name')
    
    # vend = venders.objects.all()
    # book = books.objects.all()
    # data8 = orders.objects.all()
    # data9 = classes.objects.values('class_name').distinct().order_by('class_name')
    # x=[i for i in range(1, 51)]
    # return render(request, 'orders/neword.html', { 'x':x,'vendor':vendor, 'orders':data, 'book':book, 'vend':vend, 'data8':data8,'data9':data9,'data1':data1,'data2':data2,'data3':data3,
    #                                               'data4':data4,'data5':data5,'data6':data6,'data7':data7})





# def order_purchase(request):
#     order, book, vendor = orders.objects.all(), books.objects.all(), venders.objects.all()
#     data = order.order_by('-purchase_date')

#     if request.method == 'POST' and request.POST.get("create_form_btn") == "save_cashmemo_btn":
#         order_id = str(int(time.time())) + str(random.randint(1, 9))
#         fields = ['brand_name', 'class_name', 'medium', 'subject', 'quantity', 'rim']
#         items = []
#         for i in range(1, 51):
#             item = []
#             for field in fields:
#                 value = request.POST.get(f'{field}_{i}')
#                 item.append(value or '')
#             items.append(",".join(item))

#         vender_data = {f'vender_{field}': request.POST.get(f'vender_{field}') for field in ['name', 'address', 'mob', 'email']}
#         order_data = {**vender_data, 'order_id': order_id, 'no_of_pages': request.POST.get('no_of_pages'),
#                       'gst': request.POST.get('gst'), 'purchase_date': request.POST.get('purchase_date'),
#                       'forms': request.POST.get('forms')}
#         for i in range(1, 51):
#             order_data[f'item_{i}'] = items[i-1]
#         orders.objects.create(**order_data)

#         # Extracting item quantities and computing the total amount
#         temp_amnt = [request.POST.get(f"quantity_{i}", '') for i in range(1, 51)]
#         temp_amnt = [str(i or '') for i in temp_amnt]
#         total_amount = sum([float(i) for i in temp_amnt if i])

#         # Creating the order entry
#         item_fields = ['brand_name', 'class_name', 'medium', 'subject', 'quantity', 'rim']
#         item_data = {}
#         for i in range(1, 51):
#             for field in item_fields:
#                 item_data[f'{field}_{i}'] = request.POST.get(f'{field}_{i}')
#         orders.objects.create(
#             purchase_date=datetime.datetime.now(),
#             vender_name=request.POST.get('vender_name'),
#             vender_mob=request.POST.get('vender_mob'),
#             vender_address=request.POST.get('vender_address'),
#             vender_email=request.POST.get('vender_email'),
#             no_of_pages=request.POST.get('no_of_pages'),
#             gst=request.POST.get('gst'),
#             order_id=order_id,
#             total_quantity=total_amount,
#             **item_data
#         )


#         brd_app = brands.objects.all()
#         book = books.objects.all()
#         data = orders.objects.filter().order_by('-purchase_date')

#         rim = [0] * 50

#         for i in range(1, 51):
#             quantity = locals().get(f"quantity_{i}")
#             if quantity is not None:
#                 data = orders.objects.last()
#                 for j in book:
#                     item = getattr(data, f"item{i}")
#                     if j.books_name in item:
#                         rim[i-1] = (float(quantity)*float(j.per_book_forms))/500


#         temp_rim = [vars()[f'rim_{i}'] for i in range(1, 51) if vars()[f'quantity_{i}']]
#         rim = temp_rim
#         total_rim = sum(map(float, temp_rim))

#         for i in range(1, 51):
#             setattr(actual_data, f'rim_{i}', vars()[f'rim_{i}'])


#     return render(request, 'orders/neword.html', {'order': order, 'book': book, 'vendor': vendor, 'data': data})



# def order_purchase(request):
#     order = orders.objects.all()
#     book = books.objects.all()
#     data = orders.objects.all().order_by('-purchase_date')
#     vendor = venders.objects.all()
#     if request.method == 'POST':
#         if request.POST.get("create_form_btn") == "save_cashmemo_btn":
#             order_id = str(int(time.time())) + str(random.randint(1, 9))
#             id, no_of_pages, gst, purchase_date, forms = [request.POST.get(i) for i in ['id', 'no_of_pages', 'gst', 'purchase_date', 'forms']]
#             vender_name, vender_address, vender_mob, vender_email = [request.POST.get(i) for i in ['vender_name', 'vender_address', 'vender_mob', 'vender_email']]
#             items = []
#             for i in range(1, 51):
#                 item = []
#                 for j in ['brand_name', 'class_name', 'medium', 'subject', 'quantity', 'rim']:
#                     value = request.POST.get(f'{j}_{i}')
#                     if value:
#                         item.append(str(value))
#                 items.append(','.join(item))
#             total_quantity = sum([float(request.POST.get(f'quantity_{i}')) for i in range(1, 3) if request.POST.get(f'quantity_{i}')])
#             order = orders.objects.create(purchase_date=datetime.datetime.now(), vender_name=vender_name, vender_mob=vender_mob,
#                                            vender_address=vender_address, item1=items[0], item2=items[1], vender_email=vender_email,
#                                            no_of_pages=no_of_pages, gst=gst, order_id=order_id, total_quantity=total_quantity,
#                                            brand_name_1=request.POST.get('brand_name_1'), class_name_1=request.POST.get('class_name_1'),
#                                            medium_1=request.POST.get('medium_1'), subject_1=request.POST.get('subject_1'),
#                                            quantity_1=request.POST.get('quantity_1'), rim_1=request.POST.get('rim_1'),
#                                            brand_name_2=request.POST.get('brand_name_2'), class_name_2=request.POST.get('class_name_2'),
#                                            medium_2=request.POST.get('medium_2'), subject_2=request.POST.get('subject_2'),
#                                            quantity_2=request.POST.get('quantity_2'), rim_2=request.POST.get('rim_2'))
#             book = books.objects.all()
#             data = orders.objects.filter().order_by('-purchase_date')
#             rims = []
#             for i in range(1, 51):
#                 quantity = request.POST.get(f'quantity_{i}')
#                 if quantity:
#                     data = orders.objects.filter().last()
#                     for j in book:
#                         if j.books_name in getattr(data, f'item{i}'):
#                             rim = (float(quantity)*float(j.per_book_forms))/500
#                             rims.append(rim)
#             total_rim = sum(rims)
#             order.rim_1 = rims[0] if len(rims) > 0 else 0
#             order.rim_2 = rims[1] if len(rims) > 1 else 0
#             order.total_rim = total_rim
#             order.save()
#     vend = venders.objects.all()
#     book = books.objects.all()
#     data8 = orders.objects.all()
#     return render(request, 'orders/neword.html', {'vendor':vendor, 'orders':data, 'book':book, 'vend':vend, 'data8':data8})




@login_required(login_url="") 
def delete_orders(request, id):
    cus = orders.objects.get(id=id)
    cus.delete()
    sweetify.success(request, title="Success", icon='success', text=' Order Deleted successfully...', timer=1500)
    return redirect('/order-purchase/')

@login_required(login_url="") 
def edit_orders(request, id):
    data1 = orders.objects.get(id=id)
    if request.method == 'POST':
        data1.vender_name = request.POST.get('vender_name')
        data1.vender_address = request.POST.get('vender_address')
        data1.vender_mob = request.POST.get('vender_mob')
        data1.total_quantity = request.POST.get('total_quantity')
        data1.save()
        messages.success(request, "Updated Successfully...!!")
        return redirect('/order-purchase/')
    
    context = {'data1':data1,}
    return render(request, 'orders/edit_orders.html', context)

# def delete_orders(request, id):
#     cus = orders.objects.get(id=id)
#     if cus.delete():
#         cus = orders.objects.get(id=id)
#         cus.delete()
#         sweetify.success(request, title="Success 1...", icon='success', text='Deleted successfully...', timer=1500)
#         return redirect('/order-purchase/')
#     else:
#         sweetify.error(request, title="Success 2...", icon='success', text='error', timer=1500)
#         return redirect('/order-purchase/')
    




def bill_view(request,id):
    data = orders.objects.get(order_id=id)
    print('data', data)
    context = {
        'data': data,
    }    
    return render(request, 'orders/order_bill_view.html',context)



def Orderlist(request, id):    
    list1 = []
    filtered_order_list = []
    user_order_name = venders.objects.filter(organization_name= id)
    print("organization_name", user_order_name)
    for organization_name in user_order_name:
        list1.append({
            "c_order": organization_name.organization_name,
            })
    for x in list1:
        if x['c_order'] not in filtered_order_list:
            if x['c_order'] != '':
                filtered_order_list.append(x['c_order'])
            filtered_order_list.sort()
    return JsonResponse({"data": filtered_order_list})

def Addresslist(request, id):    
    list1 = []
    filtered_address_list = []
    address_vender = venders.objects.filter(vender_address= id)
    print("vender_address", address_vender)
    for address in address_vender:
        list1.append({
            "c_address": address.vender_address,
            })
    for x in list1:
        if x['c_address'] not in filtered_address_list:
            if x['c_address'] != '':
                filtered_address_list.append(x['c_address'])
            filtered_address_list.sort()
    return JsonResponse({"data": filtered_address_list})




















# def order_purchase(request):
#     order = orders.objects.all()
#     book = books.objects.all()
#     data = orders.objects.all().order_by('-purchase_date')
#     vendor = venders.objects.all()
#     if request.method == 'POST':
#         if request.POST.get("create_form_btn") == "save_cashmemo_btn":
#             order_id = str(int(time.time())) + str(random.randint(1, 9))
#             id = request.POST.get('id')
#             vender_name = request.POST.get('vender_name')
#             vender_address = request.POST.get('vender_address')
#             vender_mob = request.POST.get('vender_mob')
#             vender_email = request.POST.get('vender_email')
#             no_of_pages = request.POST.get('no_of_pages')
#             gst = request.POST.get('gst')
#             # order_id=request.POST.get('order_id')
#             purchase_date = request.POST.get('purchase_date')
#             forms = request.POST.get('forms')
#             brand_name_1 = request.POST.get('brand_name_1')
#             class_name_1 = request.POST.get('class_name_1')
#             medium_1 = request.POST.get('medium_1')
#             subject_1 = request.POST.get('subject_1')
#             quantity_1 = request.POST.get('quantity_1')
#             rim_1 = request.POST.get('rim_1')
#             temp_item1 = []
#             if brand_name_1:
#                 temp_item1.append(brand_name_1)
#             if class_name_1:
#                 temp_item1.append(class_name_1)
#             if medium_1:
#                 temp_item1.append(medium_1)
#             if subject_1:
#                 temp_item1.append(subject_1)
#             if quantity_1:
#                 temp_item1.append(quantity_1)
#             if rim_1:
#                 temp_item1.append(rim_1)    
#             temp_item1 = [str(i or '') for i in temp_item1]
#             item1 = ",".join(temp_item1)
#             brand_name_2 = request.POST.get('brand_name_2')
#             class_name_2 = request.POST.get('class_name_2')
#             medium_2 = request.POST.get('medium_2')
#             subject_2 = request.POST.get('subject_2')
#             quantity_2 = request.POST.get('quantity_2')
#             rim_2 = request.POST.get('rim_2')
#             temp_item2 = []
#             if brand_name_2:
#                 temp_item2.append(brand_name_2)
#             if class_name_2:
#                 temp_item2.append(class_name_2)
#             if medium_2:
#                 temp_item2.append(medium_2)
#             if subject_2:
#                 temp_item2.append(subject_2)
#             if quantity_2:
#                 temp_item2.append(quantity_2)
#             if rim_2:
#                 temp_item2.append(rim_2)    
#             temp_item2 = [str(i or '') for i in temp_item2]
#             item2 = ",".join(temp_item2)
#             temp_amnt = []
#             if quantity_1:
#                 temp_amnt.append(quantity_1)
#             if quantity_2:
#                 temp_amnt.append(quantity_2)
#             temp_amnt = [str(i or '') for i in temp_amnt]
#             print(temp_amnt)
#             total_amount = 0
#             for i in temp_amnt:
#                 total_amount = total_amount + float(i)
#             actual_data = orders.objects.create(purchase_date=datetime.datetime.now(),vender_name=vender_name,
#                     vender_mob=vender_mob,vender_address=vender_address, item1=item1,item2=item2,
#                     vender_email=vender_email,no_of_pages=no_of_pages,gst=gst, order_id=order_id, total_quantity=total_amount,
#                     brand_name_1=brand_name_1,class_name_1=class_name_1,medium_1=medium_1,subject_1=subject_1,quantity_1=quantity_1,rim_1=rim_1,
#                     brand_name_2=brand_name_2,class_name_2=class_name_2,medium_2=medium_2,subject_2=subject_2,quantity_2=quantity_2,rim_2=rim_2,)
#             brd_app = brands.objects.all()
#             book = books.objects.all()
#             data = orders.objects.filter().order_by('-purchase_date')
#             rim_1 = 0
#             rim_2 = 0
#             if quantity_1 != None:
#                 data = orders.objects.filter().last()
#                 for j in book:
#                     if j.books_name in data.item1:
#                         rim_1 = (float(quantity_1)*float(j.per_book_forms))/500
#             if quantity_2 != None:
#                 data = orders.objects.filter().last()
#                 for j in book:
#                     if j.books_name in data.item2:
#                         rim_2 = (float(quantity_2)*float(j.per_book_forms))/500
#             temp_rim = []
#             if quantity_1:
#                 temp_rim.append(rim_1)
#             if quantity_2:
#                 temp_rim.append(rim_2)
#             temp_rim = [(i) for i in temp_rim]
#             rim = (temp_rim)
#             print(temp_rim)

#             total_rim = 0
#             for i in temp_rim:
#                 total_rim = total_rim + float(i)
#             actual_data.rim_1=rim_1
#             actual_data.rim_2=rim_2
#             actual_data.total_rim = total_rim
#             actual_data.save()
#     vend = venders.objects.all()
#     book = books.objects.all()
#     data1 = venders.objects.values(
#         'organization_name').distinct().order_by('organization_name')
#     data2 = venders.objects.values(
#         'vender_address').distinct().order_by('vender_address')
#     data3 = brands.objects.values(
#         'brand_name').distinct().order_by('brand_name')
#     data4 = books .objects.values(
#         'books_name').distinct().order_by('books_name')
#     data5 = books .objects.values(
#         'books_class').distinct().order_by('books_class')
#     data6 = books.objects.values('subject').distinct().order_by('subject')
#     data7 = mediums.objects.values('medium').distinct().order_by('medium')
#     data8 = orders.objects.filter().order_by('-purchase_date')
#     context ={
#         'vend': vend,
#         'data8': data8,
#         'book': book,
#         'data': data,
#         'data1': data1,
#         'data2': data2,
#         'data3': data3,
#         'data4': data4,
#         'data5': data5,
#         'data6': data6,
#         'data7': data7,
#         'order': order,
#         'vendor': vendor,
#     }
#     return render(request, 'orders/neword.html',context)



# def binding_orders(request):
#     data1 = Bindingorder.objects.filter().order_by('-date')
#     if request.method =='POST':
       
#         # date =request.POST.get('date')
#         vender_name =request.POST.get('vender_name')
       
#         subject =request.POST.get('subject')
#         quantity =request.POST.get('quantity')
#         rate_binding =request.POST.get('rate_binding')
 
#         binding_data = Bindingorder(vender_name=vender_name,subject=subject,quantity=quantity,rate_binding=rate_binding)
#         binding_data.save()
 
#     data = Bindingorder.objects.all()
#     vend = venders.objects.all()
#     print('vendor',vend)   
#     book=books.objects.all().distinct()
#     print("book",book)
#     context = {
        
#         'data':data,
#         'vend':vend,
#         'book':book,
#         'data1':data1,
#     }


#     return render(request,'orders/binding_order_1.html',context)




# Working code
def binding_orders(request):
    data1 = Bindingorder.objects.filter().order_by('-date')
    if request.method == 'POST':
        material_center = request.POST.get('material_center')
        vender_name = request.POST.get('vender_name')
        company_binding = request.POST.get('company_binding')
        border_id = str(random.randint(2, 9)) + str(int(time.time()))
       
        # Retrieve data for the first item
        subject_1 = request.POST.get('subject')
        quantity_1 = request.POST.get('quantity')
        rate_binding_1 = request.POST.get('rate_binding')
        midium_1 = request.POST.get('midium_bind')
        class_1 =  request.POST.get('class_bind')
        code_1 = request.POST.get('code_bind')
        brand_1 = request.POST.get('brand_bind')
        # Retrieve data for the second item
        subject_2 = request.POST.get('bsubject_1')
        quantity_2 = request.POST.get('bquantity_1')
        rate_binding_2 = request.POST.get('brate_binding_1')
        midium_2 = request.POST.get('midium_1')
        class_2 =  request.POST.get('class_1')
        code_2 = request.POST.get('code_1')
        brand_2 = request.POST.get('brand_1')

        # Retrieve data for the third item
        subject_3 = request.POST.get('bsubject_2')
        quantity_3 = request.POST.get('bquantity_2')
        rate_binding_3 = request.POST.get('brate_binding_2')
        midium_3 = request.POST.get('midium_2')
        class_3 =  request.POST.get('class_2')
        code_3 = request.POST.get('code_2')
        brand_3 = request.POST.get('brand_2')


        subject_4 = request.POST.get('bsubject_3')
        quantity_4 = request.POST.get('bquantity_3')
        rate_binding_4 = request.POST.get('brate_binding_3')
        midium_4 = request.POST.get('midium_3')
        class_4 =  request.POST.get('class_3')
        code_4 = request.POST.get('code_3')
        brand_4 = request.POST.get('brand_3')


        subject_5 = request.POST.get('bsubject_4')
        quantity_5 = request.POST.get('bquantity_4')
        rate_binding_5 = request.POST.get('brate_binding_4')
        midium_5 = request.POST.get('midium_4')
        class_5 =  request.POST.get('class_4')
        code_5 = request.POST.get('code_4')
        brand_5 = request.POST.get('brand_4')

        # Retrieve data for the third item
        subject_6 = request.POST.get('bsubject_5')
        quantity_6 = request.POST.get('bquantity_5')
        rate_binding_6 = request.POST.get('brate_binding_5')
        midium_6 = request.POST.get('midium_5')
        class_6 =  request.POST.get('class_5')
        code_6 = request.POST.get('code_5')
        brand_6 = request.POST.get('brand_5')

        subject_7 = request.POST.get('bsubject_6')
        quantity_7 = request.POST.get('bquantity_6')
        rate_binding_7 = request.POST.get('brate_binding_6')
        midium_7 = request.POST.get('midium_6')
        class_7 =  request.POST.get('class_6')
        code_7 = request.POST.get('code_6')
        brand_7 = request.POST.get('brand_6')



        subject_8 = request.POST.get('bsubject_7')
        quantity_8 = request.POST.get('bquantity_7')
        rate_binding_8 = request.POST.get('brate_binding_7')
        midium_8 = request.POST.get('midium_7')
        class_8 =  request.POST.get('class_7')
        code_8 = request.POST.get('code_7')
        brand_8 = request.POST.get('brand_7')



        subject_9 = request.POST.get('bsubject_8')
        quantity_9 = request.POST.get('bquantity_8')
        rate_binding_9 = request.POST.get('brate_binding_8')
        midium_9 = request.POST.get('midium_8')
        class_9 =  request.POST.get('class_8')
        code_9 = request.POST.get('code_8')
        brand_9 = request.POST.get('brand_8')


        subject_10 = request.POST.get('bsubject_9')
        quantity_10 = request.POST.get('bquantity_9')
        rate_binding_10 = request.POST.get('brate_binding_9')
        midium_10 = request.POST.get('midium_9')
        class_10 =  request.POST.get('class_9')
        code_10 = request.POST.get('code_9')
        brand_10 = request.POST.get('brand_9')



        subject_11 = request.POST.get('bsubject_10')
        quantity_11 = request.POST.get('bquantity_10')
        rate_binding_11 = request.POST.get('brate_binding_10')
        midium_11 = request.POST.get('midium_10')
        class_11 =  request.POST.get('class_10')
        code_11 = request.POST.get('code_10')
        brand_11 = request.POST.get('brand_10')



        subject_12 = request.POST.get('bsubject_11')
        quantity_12 = request.POST.get('bquantity_11')
        rate_binding_12 = request.POST.get('brate_binding_11')
        midium_12 = request.POST.get('midium_11')
        class_12 =  request.POST.get('class_11')
        code_12 = request.POST.get('code_11')
        brand_12 = request.POST.get('brand_11')


        subject_13 = request.POST.get('bsubject_12')
        quantity_13 = request.POST.get('bquantity_12')
        rate_binding_13 = request.POST.get('brate_binding_12')
        midium_13 = request.POST.get('midium_12')
        class_13 =  request.POST.get('class_12')
        code_13 = request.POST.get('code_12')
        brand_13 = request.POST.get('brand_12')



        subject_14 = request.POST.get('bsubject_13')
        quantity_14 = request.POST.get('bquantity_13')
        rate_binding_14 = request.POST.get('brate_binding_13')
        midium_14 = request.POST.get('midium_13')
        class_14 =  request.POST.get('class_13')
        code_14 = request.POST.get('code_13')
        brand_14 = request.POST.get('brand_13')


        subject_15 = request.POST.get('bsubject_14')
        quantity_15 = request.POST.get('bquantity_14')
        rate_binding_15 = request.POST.get('brate_binding_14')
        midium_15 = request.POST.get('midium_14')
        class_15 =  request.POST.get('class_14')
        code_15 = request.POST.get('code_14')
        brand_15 = request.POST.get('brand_14')



        subject_16 = request.POST.get('bsubject_15')
        quantity_16 = request.POST.get('bquantity_15')
        rate_binding_16 = request.POST.get('brate_binding_15')
        midium_16 = request.POST.get('midium_15')
        class_16 =  request.POST.get('class_15')
        code_16 = request.POST.get('code_15')
        brand_16 = request.POST.get('brand_15')



        subject_17 = request.POST.get('bsubject_16')
        quantity_17 = request.POST.get('bquantity_16')
        rate_binding_17 = request.POST.get('brate_binding_16')
        midium_17 = request.POST.get('midium_16')
        class_17 =  request.POST.get('class_16')
        code_17 = request.POST.get('code_16')
        brand_17 = request.POST.get('brand_16')



        subject_18 = request.POST.get('bsubject_17')
        quantity_18 = request.POST.get('bquantity_17')
        rate_binding_18 = request.POST.get('brate_binding_17')
        midium_18 = request.POST.get('midium_17')
        class_18 =  request.POST.get('class_17')
        code_18 = request.POST.get('code_17')
        brand_18 = request.POST.get('brand_17')



        subject_19 = request.POST.get('bsubject_18')
        quantity_19 = request.POST.get('bquantity_18')
        rate_binding_19 = request.POST.get('brate_binding_18')
        midium_19 = request.POST.get('midium_18')
        class_19 =  request.POST.get('class_18')
        code_19 = request.POST.get('code_18')
        brand_19 = request.POST.get('brand_18')



        subject_20 = request.POST.get('bsubject_19')
        quantity_20 = request.POST.get('bquantity_19')
        rate_binding_20 = request.POST.get('brate_binding_19')
        midium_20 = request.POST.get('midium_19')
        class_20 =  request.POST.get('class_19')
        code_20 = request.POST.get('code_19')
        brand_20 = request.POST.get('brand_19')



        subject_21 = request.POST.get('bsubject_20')
        quantity_21 = request.POST.get('bquantity_20')
        rate_binding_21 = request.POST.get('brate_binding_20')
        midium_21 = request.POST.get('midium_20')
        class_21 =  request.POST.get('class_20')
        code_21 = request.POST.get('code_20')
        brand_21 = request.POST.get('brand_20')



        subject_22 = request.POST.get('bsubject_21')
        quantity_22 = request.POST.get('bquantity_21')
        rate_binding_22 = request.POST.get('brate_binding_21')
        midium_22 = request.POST.get('midium_21')
        class_22 =  request.POST.get('class_21')
        code_22 = request.POST.get('code_21')
        brand_22 = request.POST.get('brand_21')



        subject_23 = request.POST.get('bsubject_22')
        quantity_23 = request.POST.get('bquantity_22')
        rate_binding_23 = request.POST.get('brate_binding_22')
        midium_23 = request.POST.get('midium_22')
        class_23 =  request.POST.get('class_22')
        code_23 = request.POST.get('code_22')
        brand_23 = request.POST.get('brand_22')



        subject_24 = request.POST.get('bsubject_23')
        quantity_24 = request.POST.get('bquantity_23')
        rate_binding_24 = request.POST.get('brate_binding_23')
        midium_24 = request.POST.get('midium_23')
        class_24 =  request.POST.get('class_23')
        code_24 = request.POST.get('code_23')
        brand_24 = request.POST.get('brand_23')



        subject_25 = request.POST.get('bsubject_24')
        quantity_25 = request.POST.get('bquantity_24')
        rate_binding_25 = request.POST.get('brate_binding_24')
        midium_25 = request.POST.get('midium_24')
        class_25 =  request.POST.get('class_24')
        code_25 = request.POST.get('code_24')
        brand_25 = request.POST.get('brand_24')




        subject_26 = request.POST.get('bsubject_25')
        quantity_26 = request.POST.get('bquantity_25')
        rate_binding_26 = request.POST.get('brate_binding_25')
        midium_26 = request.POST.get('midium_25')
        class_26 =  request.POST.get('class_25')
        code_26 = request.POST.get('code_25')
        brand_26 = request.POST.get('brand_25')



        subject_27 = request.POST.get('bsubject_26')
        quantity_27 = request.POST.get('bquantity_26')
        rate_binding_27 = request.POST.get('brate_binding_26')
        midium_27 = request.POST.get('midium_26')
        class_27 =  request.POST.get('class_26')
        code_27 = request.POST.get('code_26')
        brand_27 = request.POST.get('brand_26')



        subject_28 = request.POST.get('bsubject_27')
        quantity_28 = request.POST.get('bquantity_27')
        rate_binding_28 = request.POST.get('brate_binding_27')
        midium_28 = request.POST.get('midium_27')
        class_28 =  request.POST.get('class_27')
        code_28 = request.POST.get('code_27')
        brand_28 = request.POST.get('brand_27')



        subject_29 = request.POST.get('bsubject_28')
        quantity_29 = request.POST.get('bquantity_28')
        rate_binding_29 = request.POST.get('brate_binding_28')
        midium_29 = request.POST.get('midium_28')
        class_29 =  request.POST.get('class_28')
        code_29 = request.POST.get('code_28')
        brand_29 = request.POST.get('brand_28')



        subject_30 = request.POST.get('bsubject_29')
        quantity_30 = request.POST.get('bquantity_29')
        rate_binding_30 = request.POST.get('brate_binding_29')
        midium_30 = request.POST.get('midium_29')
        class_30 =  request.POST.get('class_29')
        code_30 = request.POST.get('code_29')
        brand_30 = request.POST.get('brand_29')



        subject_31 = request.POST.get('bsubject_30')
        quantity_31 = request.POST.get('bquantity_30')
        rate_binding_31 = request.POST.get('brate_binding_30')
        midium_31 = request.POST.get('midium_30')
        class_31 =  request.POST.get('class_30')
        code_31 = request.POST.get('code_30')
        brand_31 = request.POST.get('brand_30')



        subject_32 = request.POST.get('bsubject_31')
        quantity_32 = request.POST.get('bquantity_31')
        rate_binding_32 = request.POST.get('brate_binding_31')
        midium_32 = request.POST.get('midium_31')
        class_32 =  request.POST.get('class_31')
        code_32 = request.POST.get('code_31')
        brand_32 = request.POST.get('brand_31')



        subject_33 = request.POST.get('bsubject_32')
        quantity_33 = request.POST.get('bquantity_32')
        rate_binding_33 = request.POST.get('brate_binding_32')
        midium_33 = request.POST.get('midium_32')
        class_33 =  request.POST.get('class_32')
        code_33 = request.POST.get('code_32')
        brand_33 = request.POST.get('brand_32')



        subject_34 = request.POST.get('bsubject_33')
        quantity_34 = request.POST.get('bquantity_33')
        rate_binding_34 = request.POST.get('brate_binding_33')
        midium_34 = request.POST.get('midium_33')
        class_34 =  request.POST.get('class_33')
        code_34 = request.POST.get('code_33')
        brand_34 = request.POST.get('brand_33')



        subject_35 = request.POST.get('bsubject_34')
        quantity_35 = request.POST.get('bquantity_34')
        rate_binding_35 = request.POST.get('brate_binding_34')
        midium_35 = request.POST.get('midium_34')
        class_35 =  request.POST.get('class_34')
        code_35 = request.POST.get('code_34')
        brand_35 = request.POST.get('brand_34')



        subject_36 = request.POST.get('bsubject_35')
        quantity_36 = request.POST.get('bquantity_35')
        rate_binding_36 = request.POST.get('brate_binding_35')
        midium_36 = request.POST.get('midium_35')
        class_36 =  request.POST.get('class_35')
        code_36 = request.POST.get('code_35')
        brand_36 = request.POST.get('brand_35')



        subject_37 = request.POST.get('bsubject_36')
        quantity_37 = request.POST.get('bquantity_36')
        rate_binding_37 = request.POST.get('brate_binding_36')
        midium_37 = request.POST.get('midium_36')
        class_37 =  request.POST.get('class_36')
        code_37 = request.POST.get('code_36')
        brand_37 = request.POST.get('brand_36')



        subject_38 = request.POST.get('bsubject_37')
        quantity_38 = request.POST.get('bquantity_37')
        rate_binding_38 = request.POST.get('brate_binding_37')
        midium_38 = request.POST.get('midium_37')
        class_38 =  request.POST.get('class_37')
        code_38 = request.POST.get('code_37')
        brand_38 = request.POST.get('brand_37')


        subject_39 = request.POST.get('bsubject_38')
        quantity_39 = request.POST.get('bquantity_38')
        rate_binding_39 = request.POST.get('brate_binding_38')
        midium_39 = request.POST.get('midium_38')
        class_39 =  request.POST.get('class_38')
        code_39 = request.POST.get('code_38')
        brand_39 = request.POST.get('brand_38')



        subject_40 = request.POST.get('bsubject_39')
        quantity_40 = request.POST.get('bquantity_39')
        rate_binding_40 = request.POST.get('brate_binding_39')
        midium_40 = request.POST.get('midium_39')
        class_40 =  request.POST.get('class_39')
        code_40 = request.POST.get('code_39')
        brand_40 = request.POST.get('brand_39')



        subject_41 = request.POST.get('bsubject_40')
        quantity_41 = request.POST.get('bquantity_40')
        rate_binding_41 = request.POST.get('brate_binding_40')
        midium_41 = request.POST.get('midium_40')
        class_41 =  request.POST.get('class_40')
        code_41 = request.POST.get('code_40')
        brand_41 = request.POST.get('brand_40')



        subject_42 = request.POST.get('bsubject_41')
        quantity_42 = request.POST.get('bquantity_41')
        rate_binding_42 = request.POST.get('brate_binding_41')
        midium_42 = request.POST.get('midium_41')
        class_42 =  request.POST.get('class_41')
        code_42 = request.POST.get('code_41')
        brand_42 = request.POST.get('brand_41')




        subject_43 = request.POST.get('bsubject_42')
        quantity_43 = request.POST.get('bquantity_42')
        rate_binding_43 = request.POST.get('brate_binding_42')
        midium_43 = request.POST.get('midium_42')
        class_43 =  request.POST.get('class_42')
        code_43 = request.POST.get('code_42')
        brand_43 = request.POST.get('brand_42')



        subject_44 = request.POST.get('bsubject_43')
        quantity_44 = request.POST.get('bquantity_43')
        rate_binding_44 = request.POST.get('brate_binding_43')
        midium_44 = request.POST.get('midium_43')
        class_44 =  request.POST.get('class_43')
        code_44 = request.POST.get('code_43')
        brand_44 = request.POST.get('brand_43')



        subject_45 = request.POST.get('bsubject_44')
        quantity_45 = request.POST.get('bquantity_44')
        rate_binding_45 = request.POST.get('brate_binding_44')
        midium_45 = request.POST.get('midium_44')
        class_45 =  request.POST.get('class_44')
        code_45 = request.POST.get('code_44')
        brand_45 = request.POST.get('brand_44')



        subject_46 = request.POST.get('bsubject_45')
        quantity_46 = request.POST.get('bquantity_45')
        rate_binding_46 = request.POST.get('brate_binding_45')
        midium_46 = request.POST.get('midium_45')
        class_46 =  request.POST.get('class_45')
        code_46 = request.POST.get('code_45')
        brand_46 = request.POST.get('brand_45')




        subject_47 = request.POST.get('bsubject_46')
        quantity_47 = request.POST.get('bquantity_46')
        rate_binding_47 = request.POST.get('brate_binding_46')
        midium_47 = request.POST.get('midium_46')
        class_47 =  request.POST.get('class_46')
        code_47 = request.POST.get('code_46')
        brand_47 = request.POST.get('brand_46')



        subject_48 = request.POST.get('bsubject_47')
        quantity_48 = request.POST.get('bquantity_47')
        rate_binding_48 = request.POST.get('brate_binding_47')
        midium_48 = request.POST.get('midium_47')
        class_48 =  request.POST.get('class_47')
        code_48 = request.POST.get('code_47')
        brand_48 = request.POST.get('brand_47')



        subject_49 = request.POST.get('bsubject_48')
        quantity_49 = request.POST.get('bquantity_48')
        rate_binding_49 = request.POST.get('brate_binding_48')
        midium_49 = request.POST.get('midium_48')
        class_49 =  request.POST.get('class_48')
        code_49 = request.POST.get('code_48')
        brand_49 = request.POST.get('brand_48')



        subject_50 = request.POST.get('bsubject_49')
        quantity_50 = request.POST.get('bquantity_49')
        rate_binding_50 = request.POST.get('brate_binding_49')
        midium_50 = request.POST.get('midium_49')
        class_50 =  request.POST.get('class_49')
        code_50 = request.POST.get('code_49')
        brand_50 = request.POST.get('brand_49')



        subject_51 = request.POST.get('bsubject_50')
        quantity_51 = request.POST.get('bquantity_50')
        rate_binding_51 = request.POST.get('brate_binding_50')
        midium_51 = request.POST.get('midium_50')
        class_51 =  request.POST.get('class_50')
        code_51 = request.POST.get('code_50')
        brand_51 = request.POST.get('brand_50')

        b_amount= request.POST.get('b_amount')
        b_amount1= request.POST.get('b_amount')
        b_amount2= request.POST.get('b_amount1')
        b_amount3= request.POST.get('b_amount2')
        b_amount4= request.POST.get('b_amount3')
        b_amount5= request.POST.get('b_amount4')
        b_amount6= request.POST.get('b_amount5')
        b_amount7= request.POST.get('b_amount6')
        b_amount8= request.POST.get('b_amount7')
        b_amount9= request.POST.get('b_amount8')
        b_amount10= request.POST.get('b_amount9')
        b_amount11= request.POST.get('b_amount10')
        b_amount12= request.POST.get('b_amount11')
        b_amount13= request.POST.get('b_amount12')
        b_amount14= request.POST.get('b_amount13')
        b_amount15= request.POST.get('b_amount14')
        b_amount16= request.POST.get('b_amount15')
        b_amount17= request.POST.get('b_amount16')
        b_amount18= request.POST.get('b_amount17')
        b_amount19= request.POST.get('b_amount18')
        b_amount20= request.POST.get('b_amount19')
        b_amount21= request.POST.get('b_amount20')
        b_amount22= request.POST.get('b_amount21')
        b_amount23= request.POST.get('b_amount22')
        b_amount24= request.POST.get('b_amount23')
        b_amount25= request.POST.get('b_amount24')
        b_amount26= request.POST.get('b_amount25')
        b_amount27= request.POST.get('b_amount26')
        b_amount28= request.POST.get('b_amount27')
        b_amount29= request.POST.get('b_amount28')
        b_amount30= request.POST.get('b_amount29')
        b_amount31= request.POST.get('b_amount30')
        b_amount32= request.POST.get('b_amount31')
        b_amount33= request.POST.get('b_amount32')
        b_amount34= request.POST.get('b_amount33')
        b_amount35= request.POST.get('b_amount34')
        b_amount36= request.POST.get('b_amount35')
        b_amount37= request.POST.get('b_amount36')
        b_amount38= request.POST.get('b_amount37')
        b_amount39= request.POST.get('b_amount38')
        b_amount40= request.POST.get('b_amount39')
        b_amount41= request.POST.get('b_amount40')
        b_amount42= request.POST.get('b_amount41')
        b_amount43= request.POST.get('b_amount42')
        b_amount44= request.POST.get('b_amount43')
        b_amount45= request.POST.get('b_amount44')
        b_amount46= request.POST.get('b_amount45')
        b_amount47= request.POST.get('b_amount46')
        b_amount48= request.POST.get('b_amount47')
        b_amount49= request.POST.get('b_amount48')
        b_amount50= request.POST.get('b_amount49')
        b_amount51= request.POST.get('b_amount50')




        
            
        # Save data for all three items
        binding_data = Bindingorder(
            material_center=material_center,
            vender_name=vender_name,
            company_binding=company_binding,
            border_id=border_id,
            subject=subject_1,
            quantity=quantity_1,
            rate_binding=rate_binding_1,
            code_bind=code_1,
            class_bind=class_1,
            midium_bind=midium_1,
            brand_bind=brand_1,

            bsubject_1=subject_2,
            bquantity_1=quantity_2,
            brate_binding_1=rate_binding_2,
            code_1=code_2,
            class_1=class_2,
            midium_1=midium_2,
            brand_1=brand_2,

            bsubject_2=subject_3,
            bquantity_2=quantity_3,
            brate_binding_2=rate_binding_3,
            code_2=code_3,
            class_2=class_3,
            midium_2=midium_3,
            brand_2=brand_3,


            bsubject_3=subject_4,
            bquantity_3=quantity_4,
            brate_binding_3=rate_binding_4,
            code_3=code_4,
            class_3=class_4,
            midium_3=midium_4,
            brand_3=brand_4,

            bsubject_4=subject_5,
            bquantity_4=quantity_5,
            brate_binding_4=rate_binding_5,
            code_4=code_5,
            class_4=class_5,
            midium_4=midium_5,
            brand_4=brand_5,

            bsubject_5=subject_6,
            bquantity_5=quantity_6,
            brate_binding_5=rate_binding_6,
            code_5=code_6,
            class_5=class_6,
            midium_5=midium_6,
            brand_5=brand_6,


            bsubject_6=subject_7,
            bquantity_6=quantity_7,
            brate_binding_6=rate_binding_7,
            code_6=code_7,
            class_6=class_7,
            midium_6=midium_7,
            brand_6=brand_7,


            bsubject_7=subject_8,
            bquantity_7=quantity_8,
            brate_binding_7=rate_binding_8,
            code_7=code_8,
            class_7=class_8,
            midium_7=midium_8,
            brand_7=brand_8,

            bsubject_8=subject_9,
            bquantity_8=quantity_9,
            brate_binding_8=rate_binding_9,
            code_8=code_9,
            class_8=class_9,
            midium_8=midium_9,
            brand_8=brand_9,


            bsubject_9=subject_10,
            bquantity_9=quantity_10,
            brate_binding_9=rate_binding_10,
            code_9=code_10,
            class_9=class_10,
            midium_9=midium_10,
            brand_9=brand_10,

            bsubject_10=subject_11,
            bquantity_10=quantity_11,
            brate_binding_10=rate_binding_11,
            code_10=code_11,
            class_10=class_11,
            midium_10=midium_11,
            brand_10=brand_11,

            #----------- 
            bsubject_11=subject_12,
            bquantity_11=quantity_12,
            brate_binding_11=rate_binding_12,
            code_11=code_12,
            class_11=class_12,
            midium_11=midium_12,
            brand_11=brand_12,


            bsubject_12=subject_13,
            bquantity_12=quantity_13,
            brate_binding_12=rate_binding_13,
            code_12=code_13,
            class_12=class_13,
            midium_12=midium_13,
            brand_12=brand_13,

            bsubject_13=subject_14,
            bquantity_13=quantity_14,
            brate_binding_13=rate_binding_14,
            code_13=code_14,
            class_13=class_14,
            midium_13=midium_14,
            brand_13=brand_14,

            bsubject_14=subject_15,
            bquantity_14=quantity_15,
            brate_binding_14=rate_binding_15,
            code_14=code_15,
            class_14=class_15,
            midium_14=midium_15,
            brand_14=brand_15,


            bsubject_15=subject_16,
            bquantity_15=quantity_16,
            brate_binding_15=rate_binding_16,
            code_15=code_16,
            class_15=class_16,
            midium_15=midium_16,
            brand_15=brand_16,

            bsubject_16=subject_17,
            bquantity_16=quantity_17,
            brate_binding_16=rate_binding_17,
            code_16=code_17,
            class_16=class_17,
            midium_16=midium_17,
            brand_16=brand_17,


            bsubject_17=subject_18,
            bquantity_17=quantity_18,
            brate_binding_17=rate_binding_18,
            code_17=code_18,
            class_17=class_18,
            midium_17=midium_18,
            brand_17=brand_18,

            bsubject_18=subject_19,
            bquantity_18=quantity_19,
            brate_binding_18=rate_binding_19,
            code_18=code_19,
            class_18=class_19,
            midium_18=midium_19,
            brand_18=brand_19,


            bsubject_19=subject_20,
            bquantity_19=quantity_20,
            brate_binding_19=rate_binding_20,
            code_19=code_20,
            class_19=class_20,
            midium_19=midium_20,
            brand_19=brand_20,

            bsubject_20=subject_21,
            bquantity_20=quantity_21,
            brate_binding_20=rate_binding_21,
            code_20=code_21,
            class_20=class_21,
            midium_20=midium_21,
            brand_20=brand_21,

            bsubject_21=subject_22,
            bquantity_21=quantity_22,
            brate_binding_21=rate_binding_22,
            code_21=code_22,
            class_21=class_22,
            midium_21=midium_22,
            brand_21=brand_22,

            bsubject_22=subject_23,
            bquantity_22=quantity_23,
            brate_binding_22=rate_binding_23,
            code_22=code_23,
            class_22=class_23,
            midium_22=midium_23,
            brand_22=brand_23,

            bsubject_23=subject_24,
            bquantity_23=quantity_24,
            brate_binding_23=rate_binding_24,
            code_23=code_24,
            class_23=class_24,
            midium_23=midium_24,
            brand_23=brand_24,

            bsubject_24=subject_25,
            bquantity_24=quantity_25,
            brate_binding_24=rate_binding_25,
            code_24=code_25,
            class_24=class_25,
            midium_24=midium_25,
            brand_24=brand_25,


            bsubject_25=subject_26,
            bquantity_25=quantity_26,
            brate_binding_25=rate_binding_26,
            code_25=code_26,
            class_25=class_26,
            midium_25=midium_26,
            brand_25=brand_26,

            bsubject_26=subject_27,
            bquantity_26=quantity_27,
            brate_binding_26=rate_binding_27,
            code_26=code_27,
            class_26=class_27,
            midium_26=midium_27,
            brand_26=brand_27,
           

            bsubject_27=subject_28,
            bquantity_27=quantity_28,
            brate_binding_27=rate_binding_28,
            code_27=code_28,
            class_27=class_28,
            midium_27=midium_28,
            brand_27=brand_28,

            bsubject_28=subject_29,
            bquantity_28=quantity_29,
            brate_binding_28=rate_binding_29,
            code_28=code_29,
            class_28=class_29,
            midium_28=midium_29,
            brand_28=brand_29,

            bsubject_29=subject_30,
            bquantity_29=quantity_30,
            brate_binding_29=rate_binding_30,
            code_29=code_30,
            class_29=class_30,
            midium_29=midium_30,
            brand_29=brand_30,

            bsubject_30=subject_31,
            bquantity_30=quantity_31,
            brate_binding_30=rate_binding_31,
            code_30=code_31,
            class_30=class_31,
            midium_30=midium_31,
            brand_30=brand_31,

            bsubject_31=subject_32,
            bquantity_31=quantity_32,
            brate_binding_31=rate_binding_32,
            code_31=code_32,
            class_31=class_32,
            midium_31=midium_32,
            brand_31=brand_32,

            bsubject_32=subject_33,
            bquantity_32=quantity_33,
            brate_binding_32=rate_binding_33,
            code_32=code_33,
            class_32=class_33,
            midium_32=midium_33,
            brand_32=brand_33,

            bsubject_33=subject_34,
            bquantity_33=quantity_34,
            brate_binding_33=rate_binding_34,
            code_33=code_34,
            class_33=class_34,
            midium_33=midium_34,
            brand_33=brand_34,

            bsubject_34=subject_35,
            bquantity_34=quantity_35,
            brate_binding_34=rate_binding_35,
            code_34=code_35,
            class_34=class_35,
            midium_34=midium_35,
            brand_34=brand_35,

            bsubject_35=subject_36,
            bquantity_35=quantity_36,
            brate_binding_35=rate_binding_36,
            code_35=code_36,
            class_35=class_36,
            midium_35=midium_36,
            brand_35=brand_36,

            bsubject_36=subject_37,
            bquantity_36=quantity_37,
            brate_binding_36=rate_binding_37,
            code_36=code_37,
            class_36=class_37,
            midium_36=midium_37,
            brand_36=brand_37,

            bsubject_37=subject_38,
            bquantity_37=quantity_38,
            brate_binding_37=rate_binding_38,
            code_37=code_38,
            class_37=class_38,
            midium_37=midium_38,
            brand_37=brand_38,


            bsubject_38=subject_39,
            bquantity_38=quantity_39,
            brate_binding_38=rate_binding_39,
            code_38=code_39,
            class_38=class_39,
            midium_38=midium_39,
            brand_38=brand_39,

            bsubject_39=subject_40,
            bquantity_39=quantity_40,
            brate_binding_39=rate_binding_40,
            code_39=code_40,
            class_39=class_40,
            midium_39=midium_40,
            brand_39=brand_40,

            bsubject_40=subject_41,
            bquantity_40=quantity_41,
            brate_binding_40=rate_binding_41,
            code_40=code_41,
            class_40=class_41,
            midium_40=midium_41,
            brand_40=brand_41,

            bsubject_41=subject_42,
            bquantity_41=quantity_42,
            brate_binding_41=rate_binding_42,
            code_41=code_42,
            class_41=class_42,
            midium_41=midium_42,
            brand_41=brand_42,

            bsubject_42=subject_43,
            bquantity_42=quantity_43,
            brate_binding_42=rate_binding_43,
            code_42=code_43,
            class_42=class_43,
            midium_42=midium_43,
            brand_42=brand_43,

            bsubject_43=subject_44,
            bquantity_43=quantity_44,
            brate_binding_43=rate_binding_44,
            code_43=code_44,
            class_43=class_44,
            midium_43=midium_44,
            brand_43=brand_44,

            bsubject_44=subject_45,
            bquantity_44=quantity_45,
            brate_binding_44=rate_binding_45,
            code_44=code_45,
            class_44=class_45,
            midium_44=midium_45,
            brand_44=brand_45,

            bsubject_45=subject_46,
            bquantity_45=quantity_46,
            brate_binding_45=rate_binding_46,
            code_45=code_46,
            class_45=class_46,
            midium_45=midium_46,
            brand_45=brand_46,

            bsubject_46=subject_47,
            bquantity_46=quantity_47,
            brate_binding_46=rate_binding_47,
            code_46=code_47,
            class_46=class_47,
            midium_46=midium_47,
            brand_46=brand_47,

            bsubject_47=subject_48,
            bquantity_47=quantity_48,
            brate_binding_47=rate_binding_48,
            code_47=code_48,
            class_47=class_48,
            midium_47=midium_48,
            brand_47=brand_48,

            bsubject_48=subject_49,
            bquantity_48=quantity_49,
            brate_binding_48=rate_binding_49,
            code_48=code_49,
            class_48=class_49,
            midium_48=midium_49,
            brand_48=brand_49,

            bsubject_49=subject_50,
            bquantity_49=quantity_50,
            brate_binding_49=rate_binding_50,
            code_49=code_50,
            class_49=class_50,
            midium_49=midium_50,
            brand_49=brand_50,

            bsubject_50=subject_51,
            bquantity_50=quantity_51,
            brate_binding_50=rate_binding_51,
            code_50=code_51,
            class_50=class_51,
            midium_50=midium_51,
            brand_50=brand_51,
            
            b_amount=b_amount1,
            b_amount1=b_amount2,
            b_amount2=b_amount3,
            b_amount3=b_amount4,
            b_amount4=b_amount5,
            b_amount5=b_amount6,
            b_amount6=b_amount7,
            b_amount7=b_amount8,
            b_amount8=b_amount9,
            b_amount9=b_amount10,
            b_amount10=b_amount11,
            b_amount11=b_amount12,
            b_amount12=b_amount13,
            b_amount13=b_amount14,
            b_amount14=b_amount15,
            b_amount15=b_amount16,
            b_amount16=b_amount17,
            b_amount17=b_amount18,
            b_amount18=b_amount19,
            b_amount19=b_amount20,
            b_amount20=b_amount21,
            b_amount21=b_amount22,
            b_amount22=b_amount23,
            b_amount23=b_amount24,
            b_amount24=b_amount25,
            b_amount25=b_amount26,
            b_amount26=b_amount27,
            b_amount27=b_amount28,
            b_amount28=b_amount29,
            b_amount29=b_amount30,
            b_amount30=b_amount31,
            b_amount31=b_amount32,
            b_amount32=b_amount33,
            b_amount33=b_amount34,
            b_amount34=b_amount35,
            b_amount35=b_amount36,
            b_amount36=b_amount37,
            b_amount37=b_amount38,
            b_amount38=b_amount39,
            b_amount39=b_amount40,
            b_amount40=b_amount41,
            b_amount41=b_amount42,
            b_amount42=b_amount43,
            b_amount43=b_amount44,
            b_amount44=b_amount45,
            b_amount45=b_amount46,
            b_amount46=b_amount47,
            b_amount47=b_amount48,
            b_amount48=b_amount49,
            b_amount49=b_amount50,
            b_amount50=b_amount51,
            


        )
        binding_data.save()

    data = Bindingorder.objects.all()
    vend = Bindingvender.objects.all()
    book = books.objects.all().distinct()
    comp = Company.objects.all()
    data3 = material_centre.objects.all()

    context = {
        'data': data,
        'vend': vend,
        'book': book,
        'data1': data1,
        'comp':comp,
        'data3':data3,
    }

    return render(request, 'orders/binding_order_1.html', context)







def binding_bill_view(request, id):
    data = Bindingorder.objects.get(border_id=id)
    print('data', data)
    a = int(data.quantity)
    print('a', a)
    b= str(data.midium_1)
    print("b",b) 
    c= float(data.b_amount)
    print("c",c) 
    

    # Define the maximum number of orders
    max_orders = 50  # Maximum number of orders to consider

    order_data = []
    total_quantity = 0
    total_amount=0

    for i in range(1, max_orders + 1):
        quantity_field = 'bquantity_{}'.format(i)
        quantity = getattr(data, quantity_field, None)
        amount_field = 'b_amount{}'.format(i)
        amount = getattr(data, amount_field, None)
        print("3333333",amount)


        if quantity:
            order_data.append({
                'medium': request.POST.get('midium_{}'.format(i)),
                'subject': request.POST.get('bsubject_{}'.format(i)),
                'quantity': quantity,
                'amount': amount,
                'rate_binding': request.POST.get('brate_binding_{}'.format(i))
            })

            # Calculate the sum of quantities
            total_quantity += int(quantity)
            print('total_quantity', total_quantity)
            total_amount += float(amount)
            print('total_amount', total_amount)


    # Update the total_quantity field of the Bindingorder object
    data.binding_order_total = total_quantity + a
    data.binding_total_amount = total_amount + c
    print("222222222",data.binding_total_amount)
    data.save()

    context = {
        'data': data,
        'order_data': order_data,
        'binding_order_total': total_quantity,
        'binding_total_amount': total_amount,
        'a': a,
    }

    return render(request, 'orders/binding_order_bill_view.html', context)






@login_required(login_url="") 
def delete_binding(request, id):
    cus = Bindingorder.objects.get(id=id)
    cus.delete()
    sweetify.success(request, title="Success", icon='success', text='Order Deleted successfully...', timer=1500)
    return redirect('/binding_orders/')





# @login_required(login_url="") 
# def edit_binding(request, id):
#     data1 = Bindingorder.objects.get(id=id)

#     if request.method == 'POST':
#         data1.vender_name = request.POST.get('vender_name')
#         data1.subject = request.POST.get('subject')
#         data1.quantity = request.POST.get('quantity')
#         data1.rate_binding = request.POST.get('rate_binding')
#         data1.save()
#         messages.success(request, "Updated Successfully...!!")
#         return redirect('/binding_orders/')
#     vend = venders.objects.all()
#     print('vendor',vend)
#     book=books.objects.all() 
#     print("book",book)
#     context = {
#         'data1':data1,
#         'vend':vend,
#         'book':book,
#     }
#     return render(request, 'orders/edit_binding.html', context)


def bill_sundries(request):
    if request.method =='POST':
        bil_sundries_name=request.POST.get('bil_sundries_name')
        bill_sundries_alias=request.POST.get('bill_sundries_alias')
        bill_sundry_type=request.POST.get('bill_sundry_type')
        bill_sundry_nature=request.POST.get('bill_sundry_nature')
        bill_sundry_default_value=request.POST.get('bill_sundry_default_value')
        bill_sundry_total=request.POST.get('bill_sundry_total')
        cost_good_sale=request.POST.get('cost_good_sale')
        cost_good_purchase=request.POST.get('cost_good_purchase')
        cost_good_material_receipt=request.POST.get('cost_good_material_receipt')
        cost_good_stock_transfer=request.POST.get('cost_good_stock_transfer')
        acc_affect_accounting=request.POST.get('acc_affect_accounting')
        sale_amount_accounting=request.POST.get('sale_amount_accounting')
        specify_acc=request.POST.get('specify_acc')
        account_head_post=request.POST.get('account_head_post')
        account_tax=request.POST.get('account_tax')
        adjust_party_amount=request.POST.get('adjust_party_amount')
        post_over_and_above=request.POST.get('post_over_and_above')
        purchase_affect=request.POST.get('purchase_affect')
        purchase_amount=request.POST.get('purchase_amount')
        purchase_account_head=request.POST.get('account_head_post')
        purchase_party_amount=request.POST.get('purchase_party_amount')
        zero_tax_item=request.POST.get('zero_tax_item')
        stock_affects_accounting=request.POST.get('stock_affects_accounting')
        stock_other_side=request.POST.get('stock_other_side')
        stock_account_head_to_post=request.POST.get('stock_account_head_to_post')
        stock_adjust_party=request.POST.get('stock_adjust_party')
        stock_specify_acc_here=request.POST.get('stock_specify_acc_here')
        stock_post_over_above=request.POST.get('stock_post_over_above')
        percent=request.POST.get('percent')
        selective_calculation=request.POST.get('selective_calculation')
        item_basic_amt=request.POST.get('item_basic_amt')
        consolidate_bill_sundry=request.POST.get('consolidate_bill_sundry')
        bill_sundry_amount=request.POST.get('bill_sundry_amount')
        round_off_bill=request.POST.get('round_off_bill')

        bill_sundry_data=Bill_sundry(bil_sundries_name=bil_sundries_name,
                                     bill_sundries_alias=bill_sundries_alias,
                                     bill_sundry_type=bill_sundry_type,
                                     bill_sundry_nature=bill_sundry_nature,
                                     bill_sundry_default_value=bill_sundry_default_value,
                                     bill_sundry_total=bill_sundry_total,
                                     cost_good_sale=cost_good_sale,
                                     cost_good_purchase=cost_good_purchase,
                                     cost_good_material_receipt=cost_good_material_receipt,
                                     cost_good_stock_transfer=cost_good_stock_transfer,
                                     acc_affect_accounting=acc_affect_accounting,
                                     sale_amount_accounting=sale_amount_accounting,
                                     specify_acc=specify_acc,
                                     account_head_post=account_head_post,
                                     account_tax=account_tax,
                                     adjust_party_amount=adjust_party_amount,
                                     post_over_and_above=post_over_and_above,
                                     purchase_affect=purchase_affect,
                                     purchase_amount=purchase_amount,
                                     purchase_account_head=purchase_account_head,
                                     purchase_party_amount=purchase_party_amount,
                                     zero_tax_item=zero_tax_item,
                                     stock_affects_accounting=stock_affects_accounting,
                                     stock_other_side=stock_other_side,
                                     stock_account_head_to_post=stock_account_head_to_post,
                                     stock_adjust_party=stock_adjust_party,
                                     stock_specify_acc_here=stock_specify_acc_here,
                                     stock_post_over_above=stock_post_over_above,
                                     percent=percent,
                                     selective_calculation=selective_calculation,
                                     item_basic_amt=item_basic_amt,
                                     consolidate_bill_sundry=consolidate_bill_sundry,
                                     bill_sundry_amount=bill_sundry_amount,
                                     round_off_bill=round_off_bill,)
        bill_sundry_data.save()

    return render(request,'orders/bill_sundries.html')








def production_voucher(request):
    if request.method == 'POST':
        pr_voucher_date = request.POST.get('pr_voucher_date')
        pr_voucher_series = request.POST.get('pr_voucher_series')
        pr_voucher_no = request.POST.get('pr_voucher_no')
        pr_voucher_bom_name = request.POST.get('pr_voucher_bom_name')
        pr_voucher_narration = request.POST.get('pr_voucher_narration')

        pr_voucher_item_name_1 = request.POST.get('pr_voucher_item_name_1')
        print("888888888888888",pr_voucher_item_name_1)
        pr_voucher_qty_1 = request.POST.get('pr_voucher_qty_1')
        pr_voucher_unit_1 = request.POST.get('pr_voucher_unit_1')
        pr_voucher_price_1 = request.POST.get('pr_voucher_price_1')
        pr_voucher_amount_1 = request.POST.get('pr_voucher_amount_1')
        consumed_voucher_item_name =request.POST.get('consumed_voucher_item_name')
        print("999999999999999",consumed_voucher_item_name)
        consumed_voucher_qty=request.POST.get('consumed_voucher_qty')
        print("999999999999999",consumed_voucher_qty)

        consumed_voucher_unit=request.POST.get('consumed_voucher_unit')
        print("999999999999999",consumed_voucher_unit)
        consumed_voucher_price=request.POST.get('consumed_voucher_price')
        print("999999999999999",consumed_voucher_price)
        consumed_voucher_amount=request.POST.get('consumed_voucher_amount')
        print("999999999999999",consumed_voucher_amount)

        consumed_voucher_item_name_1 =request.POST.get('consumed_voucher_item_name_1')
        print("999999999999999",consumed_voucher_item_name_1)
        consumed_voucher_qty_1=request.POST.get('consumed_voucher_qty_1')
        print("999999999999999",consumed_voucher_qty_1)

        consumed_voucher_unit_1=request.POST.get('consumed_voucher_unit_1')
        print("999999999999999",consumed_voucher_unit_1)
        consumed_voucher_price_1=request.POST.get('consumed_voucher_price_1')
        print("999999999999999",consumed_voucher_price_1)
        consumed_voucher_amount_1=request.POST.get('consumed_voucher_amount_1')
        print("999999999999999",consumed_voucher_amount_1)



        cloned_data_list = []
        for i in range(1, 11):  # Assuming a maximum of 10 clone fields
            item_name = request.POST.get(f'pr_voucher_item_name{i}')
            print("dfghj",item_name)
            item_qty = request.POST.get(f'pr_voucher_qty{i}')
            print("dfghj",item_qty)
            
            item_unit = request.POST.get(f'pr_voucher_unit{i}')
            print("dfghj",item_unit)
            
            item_price = request.POST.get(f'pr_voucher_price{i}')
            print("dfghj",item_price)
            item_amount = request.POST.get(f'pr_voucher_amount{i}')
            print("dfghj",item_amount)

            if item_name and item_qty and item_unit and item_price and item_amount:
                cloned_data_list.append({
                    'pr_voucher_item_name': item_name,
                    'pr_voucher_qty': item_qty,
                    'pr_voucher_unit': item_unit,
                    'pr_voucher_price':item_price,
                    'pr_voucher_amount':item_amount,
                })

        cloned_data_list1 = []
        for j in range(1, 11):  # Assuming a maximum of 10 clone fields
            item_name1 = request.POST.get(f'consumed_voucher_item_name{j}')
            print("dfghj",item_name1)
            item_qty1 = request.POST.get(f'consumed_voucher_qty{j}')
            print("dfghj",item_qty1)
            
            item_unit1 = request.POST.get(f'consumed_voucher_unit{j}')
            print("dfghj",item_unit1)
            
            item_price1= request.POST.get(f'consumed_voucher_price{j}')
            print("dfghj",item_price1)
            item_amount1 = request.POST.get(f'consumed_voucher_amount{j}')
            print("dfghj",item_amount1)

            if item_name1 and item_qty1 and item_unit1 and item_price1 and item_amount1:
                cloned_data_list1.append({
                    'consumed_voucher_item_name': item_name1,
                    'consumed_voucher_qty': item_qty1,
                    'consumed_voucher_unit': item_unit1,
                    'consumed_voucher_price':item_price1,
                    'consumed_voucher_amount':item_amount1,
                })

       

        # Create ProductionVoucher instance
        pr_voucher = product_voucher.objects.create(
            pr_voucher_date=pr_voucher_date,
            pr_voucher_series=pr_voucher_series,
            pr_voucher_no=pr_voucher_no,
            pr_voucher_bom_name=pr_voucher_bom_name,
            pr_voucher_narration=pr_voucher_narration,
            pr_voucher_item_name_1=pr_voucher_item_name_1,
            pr_voucher_qty_1=pr_voucher_qty_1,
            pr_voucher_unit_1=pr_voucher_unit_1,
            pr_voucher_price_1=pr_voucher_price_1,
            pr_voucher_amount_1=pr_voucher_amount_1,
            consumed_voucher_item_name=consumed_voucher_item_name,
            consumed_voucher_qty=consumed_voucher_qty,
            consumed_voucher_unit=consumed_voucher_unit,
            consumed_voucher_price=consumed_voucher_price,
            consumed_voucher_amount=consumed_voucher_amount,
            dynamic_data=json.dumps(cloned_data_list),
            dynamic_data1=json.dumps(cloned_data_list1),

            consumed_voucher_item_name_1=consumed_voucher_item_name_1,
            consumed_voucher_qty_1=consumed_voucher_qty_1,
            consumed_voucher_unit_1=consumed_voucher_unit_1,
            consumed_voucher_price_1=consumed_voucher_price_1,
            consumed_voucher_amount_1=consumed_voucher_amount_1,

        )

        # Handle up to 10 cloned fields
        
        pr_voucher.save()

        return redirect('/production_voucher/')  # Redirect to a success page
    data=product_voucher.objects.all()
    data1=books.objects.all()
    context={
        'data':data,
        'data1':data1,
    }

    return render(request, 'orders/production_voucher.html',context)


import json

def production_voucher_view(request, id):
    data = product_voucher.objects.filter(id=id).first()
    dynamic_data = json.loads(data.dynamic_data) if data and data.dynamic_data else []
    dynamic_data1 = json.loads(data.dynamic_data1) if data and data.dynamic_data1 else []
    total_amount = 0
    for item in dynamic_data:
        total_amount += float(item.get('pr_voucher_amount', 0))
    # total_amount = sum(float(item.get(f'pr_voucher_amount{i}', 0)) for i in range(1, 11) for item in dynamic_data)
        print("sdfghjkl",total_amount)
    total_amount += float(data.pr_voucher_amount_1)
    print("sdfghjkl",total_amount)
    total_amount1 = 0
    for item in dynamic_data1:
        total_amount1 += float(item.get('consumed_voucher_amount', 0))
    # total_amount = sum(float(item.get(f'pr_voucher_amount{i}', 0)) for i in range(1, 11) for item in dynamic_data)
        print("ttttttttt",total_amount1)
    total_amount1 += float(data.consumed_voucher_amount_1)
    print("hhhhhhhhhhhhhhhhhh",total_amount1)


    context = {
        'data': data,
        'dynamic_data': dynamic_data,
        'dynamic_data1': dynamic_data1,
        'total_amount': total_amount,
        'total_amount1':total_amount1,


    }

    return render(request, 'orders/production_voucher_view.html', context)

@login_required(login_url="") 
def production_voucher_delete(request, id):
    cus = product_voucher.objects.get(id=id)
    cus.delete()
    sweetify.success(request, title="Success", icon='success', text='Order Deleted successfully...', timer=1500)
    return redirect('/production_voucher/')





from itertools import chain

import json
def bill_of_material(request):
    if request.method=='POST':
        bom_name = request.POST.get('bom_name')
        bom_alias = request.POST.get('bom_alias')
        bom_item_produce = request.POST.get('bom_item_produce')
        bom_quantity= request.POST.get('bom_quantity')
        bom_unit1=  request.POST.get('bom_unit1')
        bom_exp= request.POST.get('bom_exp')
        bom_item_generated= request.POST.get('bom_item_generated')
        bom_item_consumed_1= request.POST.get('bom_item_consumed_1')
        
        bom_item_name= request.POST.get('bom_item_name')
        bom_qty= request.POST.get('bom_qty')
        bom_unit= request.POST.get('bom_unit')

        bom_item_name_1=request.POST.get('bom_item_name_1')
        bom_qty_1 =request.POST.get('bom_qty_1')
        bom_unit_1=request.POST.get('bom_unit_1')

        bom_generated_item= request.POST.get('bom_generated_item')
        bom_generated_unit= request.POST.get('bom_generated_unit')
        bom_generated_qty= request.POST.get('bom_generated_qty')

        bom_generated_item_1= request.POST.get('bom_generated_item_1')
        bom_generated_unit_1= request.POST.get('bom_generated_unit_1')
        bom_generated_qty_1= request.POST.get('bom_generated_qty_1')
       




        cloned_data_list = []
        for i in range(1, 11):  # Assuming a maximum of 10 clone fields
            item_name = request.POST.get(f'bom_item_name{i}')
           
            print("dfghj",item_name)
            qty = request.POST.get(f'bom_qty{i}')
           
            print("dfghj",qty)
            unit = request.POST.get(f'bom_unit{i}')
           
            print("dfghj",unit)

            if item_name and qty and unit:
                cloned_data_list.append({
                    'bom_item_name': item_name,
                    'bom_qty': qty,
                    'bom_unit': unit,
                })
        cloned_data_list1 = []
        for j in range(1, 11):
            item_name1 = request.POST.get(f'bom_generated_item{j}')
            qty1 = request.POST.get(f'bom_generated_qty{j}')
            unit1 = request.POST.get(f'bom_generated_unit{j}')

            print(f"Item {j} - Name: {item_name1}, Qty: {qty1}, Unit: {unit1}")

            if item_name1 and qty1 and unit1:
                cloned_data_list1.append({
                    'bom_generated_item': item_name1,
                    'bom_generated_qty': qty1,
                    'bom_generated_unit': unit1,
                })
        # Save data to the database
        bill = BOM(
            bom_name=bom_name,
            bom_alias=bom_alias,
            bom_item_produce=bom_item_produce,
            bom_quantity=bom_quantity,
            # bom_unit1=bom_unit1,
            bom_exp=bom_exp,
            bom_item_generated=bom_item_generated,
            bom_item_consumed_1=bom_item_consumed_1,

            bom_generated_qty=bom_generated_qty,
            bom_generated_unit=bom_generated_unit,
            bom_generated_item=bom_generated_item,

            bom_generated_qty_1=bom_generated_qty_1,
            bom_generated_unit_1=bom_generated_unit_1,
            bom_generated_item_1=bom_generated_item_1,

            bom_item_name=bom_item_name,
            bom_qty=bom_qty,
            bom_unit=bom_unit,
            
            bom_item_name_1=bom_item_name_1,
            bom_qty_1=bom_qty_1,
            bom_unit_1=bom_unit_1,

            dynamic_data=json.dumps(cloned_data_list),
            dynamic_data1=json.dumps(cloned_data_list1),
        )
        bill.save()

    data=BOM.objects.all()
    data1=books.objects.all()
    data2=material_centre.objects.all()
    data7=master_unit.objects.all()
    data_combined = list(chain(
        books.objects.all(),
        forms.objects.all(),
        
    ))
    print(data_combined)
    context={
        'data':data,
        'data1':data1,
        'data2':data2,
        'data7':data7,
        'data_combined':data_combined,
     }

    return render(request,'orders/bill_of_material.html',context)


def bill_of_material_view(request,id):
   data=BOM.objects.get(id=id)
   dynamic_data = json.loads(data.dynamic_data) if data and data.dynamic_data else []
   dynamic_data1 = json.loads(data.dynamic_data1) if data and data.dynamic_data1 else []
   print("sdfghjkl", dynamic_data)
   print("dsdfghjk", data.dynamic_data1)
   
   context={ 
    'data':data,
    'dynamic_data':dynamic_data,
    'dynamic_data1':dynamic_data1,
   }
   return render(request,'orders/bill_of_material_view.html',context)

@login_required(login_url="") 
def delete_bill_of_material(request, id):
    cus = BOM.objects.get(id=id)
    cus.delete()
    sweetify.success(request, title="Success", icon='success', text='Order Deleted successfully...', timer=1500)
    return redirect('/bill_of_material/')


def sale_voucher1(request):
    if request.method == 'POST':
        sl_voucher_date = request.POST.get('sl_voucher_date')
        sl_voucher_series = request.POST.get('sl_voucher_series')
        sl_vehicle_no = request.POST.get('sl_vehicle_no')
        sl_voucher_sale_type = request.POST.get('sl_voucher_sale_type')
        sl_voucher_party = request.POST.get('sl_voucher_party')
        sl_voucher_narration = request.POST.get('sl_voucher_narration')

        sl_voucher_item_name_1 = request.POST.get('sl_voucher_item_name_1')
        # print("888888888888888",sl_voucher_item_name_1)
        sl_voucher_qty_1 = request.POST.get('sl_voucher_qty_1')
        sl_voucher_unit_1 = request.POST.get('sl_voucher_unit_1')
        sl_voucher_price_1 = request.POST.get('sl_voucher_price_1')
        sl_voucher_amount_1 = request.POST.get('sl_voucher_amount_1')
        sl_voucher_item_name= request.POST.get('sl_voucher_item_name')
        sl_voucher_qty=request.POST.get('sl_voucher_qty')
        sl_voucher_unit=request.POST.get('sl_voucher_unit')
        sl_voucher_price=request.POST.get('sl_voucher_price')
        sl_voucher_amount=request.POST.get('sl_voucher_amount')

        sl_bill_sundries=request.POST.get('sl_bill_sundries')
        sl_narration=request.POST.get('sl_narration')
        sl_zero=request.POST.get('sl_zero')
        sl_ammount=request.POST.get('sl_ammount')

        sl_bill_sundries_1=request.POST.get('sl_bill_sundries_1')
        sl_narration_1=request.POST.get('sl_narration_1')
        sl_zero_1=request.POST.get('sl_zero_1')
        sl_ammount_1=request.POST.get('sl_ammount_1')
        

        cloned_data_list = []
        for i in range(1, 11):  # Assuming a maximum of 10 clone fields
            item_name = request.POST.get(f'sl_voucher_item_name{i}')
            print("dfghj",item_name)
            item_qty = request.POST.get(f'sl_voucher_qty{i}')
            print("dfghj",item_qty)
            
            item_unit = request.POST.get(f'sl_voucher_unit{i}')
            print("dfghj",item_unit)
            
            item_price = request.POST.get(f'sl_voucher_price{i}')
            print("dfghj",item_price)
            item_amount = request.POST.get(f'sl_voucher_amount{i}')
            print("dfghj",item_amount)
            print('6666666666666666666666666666',item_name,item_qty,item_unit,item_price,item_amount)
            if item_name and item_qty and item_unit and item_price and item_amount:
                cloned_data_list.append({
                    'sl_voucher_item_name': item_name,
                    'sl_voucher_qty': item_qty,
                    'sl_voucher_unit': item_unit,
                    'sl_voucher_price':item_price,
                    'sl_voucher_amount':item_amount,
                })
                

        cloned_data_list1 = []
        for j in range(1, 11):  # Assuming a maximum of 10 clone fields
            sale_bill_sundries = request.POST.get(f'sl_bill_sundries{j}')
            print("dfghj",sale_bill_sundries)
            sale_narration = request.POST.get(f'sl_narration{j}')
            print("dfghj",sale_narration)
            
            sale_zero = request.POST.get(f'sl_zero{j}')
            print("dfghj",sale_zero)
            
            sale_ammount= request.POST.get(f'sl_ammount{j}')
            print("dfghj",sale_ammount)
            

            if sale_bill_sundries and sale_narration and sale_zero and sale_ammount:
                cloned_data_list1.append({
                    'sl_bill_sundries': sale_bill_sundries,
                    'sl_narration': sale_narration,
                    'sl_zero': sale_zero,
                    'sl_ammount':sale_ammount,
                   
                })

        # Create ProductionVoucher instance
        sl_voucher = sale_voucher.objects.create(
            sl_voucher_date=sl_voucher_date,
            sl_voucher_series=sl_voucher_series,
            sl_vehicle_no=sl_vehicle_no,
            sl_voucher_sale_type= sl_voucher_sale_type,
            sl_voucher_party=sl_voucher_party,
            sl_voucher_narration=sl_voucher_narration,

            sl_voucher_item_name_1=sl_voucher_item_name_1,
            sl_voucher_qty_1=sl_voucher_qty_1,
            sl_voucher_unit_1=sl_voucher_unit_1,
            sl_voucher_price_1=sl_voucher_price_1,
            sl_voucher_amount_1=sl_voucher_amount_1,
            sl_voucher_item_name=sl_voucher_item_name,
            sl_voucher_qty=sl_voucher_qty,
            sl_voucher_unit=sl_voucher_unit,
            sl_voucher_price=sl_voucher_price,
            sl_voucher_amount=sl_voucher_amount,

            sl_bill_sundries_1 = sl_bill_sundries_1,
            sl_narration_1 = sl_narration_1,
            sl_zero_1 = sl_zero_1,
            sl_ammount_1 = sl_ammount_1,

            sl_bill_sundries = sl_bill_sundries,
            sl_narration = sl_narration,
            sl_zero = sl_zero,
            sl_ammount = sl_ammount,
            
            dynamic_data=json.dumps(cloned_data_list),
            dynamic_data1=json.dumps(cloned_data_list1),

        )

        # Handle up to 10 cloned fields
        
        sl_voucher.save()

        return redirect('/sale_voucher/')  # Redirect to a success page
    data=sale_voucher.objects.all()
    data1=books.objects.all()
    context={
        'data':data,
        'data1':data1,
    }

    
    return render(request,'orders/sale_voucher.html',context)



def sale_voucher_view(request,id):
    data = sale_voucher.objects.filter(id=id).first()
    dynamic_data = json.loads(data.dynamic_data) if data and data.dynamic_data else []
    dynamic_data1 = json.loads(data.dynamic_data1) if data and data.dynamic_data1 else []
    total_amount = 0
    total_amount2 = 0
    for item in dynamic_data:
        total_amount2 += float(item.get('sl_voucher_amount', 0))
    # total_amount = sum(float(item.get(f'pr_voucher_amount{i}', 0)) for i in range(1, 11) for item in dynamic_data)
        print("sdfghjkl",total_amount2)
    total_amount2 += float(data.sl_voucher_amount_1)
    print("sdfghjkl",total_amount2)

    total_amount1 = 0
    for item in dynamic_data1:
        total_amount1 += float(item.get('sl_ammount', 0))
    total_amount = sum(float(item.get(f'sl_voucher_amount{i}', 0)) for i in range(1, 11) for item in dynamic_data)
    print("ttttttttt",total_amount1)
    total_amount1 += float(data.sl_ammount_1)
    print("hhhhhhhhhhhhhhhhhh",total_amount1)

    print("99999999999999999",total_amount2)
    context = {
        'data': data,
        'dynamic_data': dynamic_data,
        'dynamic_data1': dynamic_data1,
        'total_amount2':total_amount2,
        'total_amount1':total_amount1,


    }

    return render(request, 'orders/sale_voucher_view.html', context)

@login_required(login_url="") 
def delete_sale_voucher(request, id):
    sale = sale_voucher.objects.get(id=id)
    sale.delete()
    sweetify.success(request, title="Success", icon='success', text='Order Deleted successfully...', timer=1500)
    return redirect('/sale_voucher/')

