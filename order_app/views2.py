
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

@login_required(login_url="")
def order_purchase(request):
    order = orders.objects.all()
    book = books.objects.all()
    data = orders.objects.all().order_by('-purchase_date')
    vendor = venders.objects.all()
    
    if request.method == 'POST':
        if request.POST.get("create_form_btn") == "save_cashmemo_btn":
            order_id = str(int(time.time())) + str(random.randint(1, 9))
            id = request.POST.get('id')
            vender_name = request.POST.get('vender_name')
            vender_address = request.POST.get('vender_address')
            vender_mob = request.POST.get('vender_mob')
            vender_email = request.POST.get('vender_email')
            no_of_pages = request.POST.get('no_of_pages')
            gst = request.POST.get('gst')
            # order_id=request.POST.get('order_id')
            purchase_date = request.POST.get('purchase_date')
            forms = request.POST.get('forms')

            brand_name_1 = request.POST.get('brand_name_1')
            class_name_1 = request.POST.get('class_name_1')
            medium_1 = request.POST.get('medium_1')
            subject_1 = request.POST.get('subject_1')
            quantity_1 = request.POST.get('quantity_1')
            rim_1 = request.POST.get('rim_1')
            temp_item1 = []
            if brand_name_1:
                temp_item1.append(brand_name_1)
            if class_name_1:
                temp_item1.append(class_name_1)
            if medium_1:
                temp_item1.append(medium_1)
            if subject_1:
                temp_item1.append(subject_1)
            if quantity_1:
                temp_item1.append(quantity_1)
            if rim_1:
                temp_item1.append(rim_1)    

            temp_item1 = [str(i or '') for i in temp_item1]
            item1 = ",".join(temp_item1)

            brand_name_2 = request.POST.get('brand_name_2')
            class_name_2 = request.POST.get('class_name_2')
            medium_2 = request.POST.get('medium_2')
            subject_2 = request.POST.get('subject_2')
            quantity_2 = request.POST.get('quantity_2')
            rim_2 = request.POST.get('rim_2')
            temp_item2 = []
            if brand_name_2:
                temp_item2.append(brand_name_2)
            if class_name_2:
                temp_item2.append(class_name_2)
            if medium_2:
                temp_item2.append(medium_2)
            if subject_2:
                temp_item2.append(subject_2)
            if quantity_2:
                temp_item2.append(quantity_2)
            if rim_2:
                temp_item2.append(rim_2)    

            temp_item2 = [str(i or '') for i in temp_item2]
            item2 = ",".join(temp_item2)

            brand_name_3 = request.POST.get('brand_name_3')
            class_name_3 = request.POST.get('class_name_3')
            medium_3 = request.POST.get('medium_3')
            subject_3 = request.POST.get('subject_3')
            quantity_3 = request.POST.get('quantity_3')
            rim_3 = request.POST.get('rim_3')
            temp_item3 = []
            if brand_name_3:
                temp_item3.append(brand_name_3)
            if class_name_3:
                temp_item3.append(class_name_3)
            if medium_3:
                temp_item3.append(medium_3)
            if subject_3:
                temp_item3.append(subject_3)
            if quantity_3:
                temp_item3.append(quantity_3)
            if rim_3:
                temp_item3.append(rim_3)    

            temp_item3 = [str(i or '') for i in temp_item3]
            item3 = ",".join(temp_item3)

            brand_name_4 = request.POST.get('brand_name_4')
            class_name_4 = request.POST.get('class_name_4')
            medium_4 = request.POST.get('medium_4')
            subject_4 = request.POST.get('subject_4')
            quantity_4 = request.POST.get('quantity_4')
            rim_4 = request.POST.get('rim_4')
            temp_item4 = []
            if brand_name_4:
                temp_item4.append(brand_name_4)
            if class_name_4:
                temp_item4.append(class_name_4)
            if medium_4:
                temp_item4.append(medium_4)
            if subject_4:
                temp_item4.append(subject_4)
            if quantity_4:
                temp_item4.append(quantity_4)
            if rim_4:
                temp_item4.append(rim_4)    

            temp_item4 = [str(i or '') for i in temp_item4]
            item4 = ",".join(temp_item4)            

            brand_name_5 = request.POST.get('brand_name_5')
            class_name_5 = request.POST.get('class_name_5')
            medium_5 = request.POST.get('medium_5')
            subject_5 = request.POST.get('subject_5')
            quantity_5 = request.POST.get('quantity_5')
            rim_5 = request.POST.get('rim_5')
            temp_item5 = []
            if brand_name_5:
                temp_item5.append(brand_name_5)
            if class_name_5:
                temp_item5.append(class_name_5)
            if medium_5:
                temp_item5.append(medium_5)
            if subject_5:
                temp_item5.append(subject_5)
            if quantity_5:
                temp_item5.append(quantity_5)
            if rim_5:
                temp_item5.append(rim_5)    

            temp_item5 = [str(i or '') for i in temp_item5]
            item5 = ",".join(temp_item5)


            brand_name_6 = request.POST.get('brand_name_6')
            class_name_6 = request.POST.get('class_name_6')
            medium_6 = request.POST.get('medium_6')
            subject_6 = request.POST.get('subject_6')
            quantity_6 = request.POST.get('quantity_6')
            rim_6 = request.POST.get('rim_6')
            temp_item6 = []
            if brand_name_6:
                temp_item6.append(brand_name_6)
            if class_name_6:
                temp_item6.append(class_name_6)
            if medium_6:
                temp_item6.append(medium_6)
            if subject_6:
                temp_item6.append(subject_6)
            if quantity_6:
                temp_item6.append(quantity_6)
            if rim_6:
                temp_item6.append(rim_6)    

            temp_item6 = [str(i or '') for i in temp_item6]
            item6 = ",".join(temp_item6)



            brand_name_7 = request.POST.get('brand_name_7')
            class_name_7 = request.POST.get('class_name_7')
            medium_7 = request.POST.get('medium_7')
            subject_7 = request.POST.get('subject_7')
            quantity_7 = request.POST.get('quantity_7')
            rim_7 = request.POST.get('rim_7')
            temp_item7 = []
            if brand_name_7:
                temp_item7.append(brand_name_7)
            if class_name_7:
                temp_item7.append(class_name_7)
            if medium_7:
                temp_item7.append(medium_7)
            if subject_7:
                temp_item7.append(subject_7)
            if quantity_7:
                temp_item7.append(quantity_7)
            if rim_7:
                temp_item7.append(rim_7)    

            temp_item7 = [str(i or '') for i in temp_item7]
            item7 = ",".join(temp_item7)

            
            brand_name_8 = request.POST.get('brand_name_8')
            class_name_8 = request.POST.get('class_name_8')
            medium_8 = request.POST.get('medium_8')
            subject_8 = request.POST.get('subject_8')
            quantity_8 = request.POST.get('quantity_8')
            rim_8 = request.POST.get('rim_8')
            temp_item8 = []
            if brand_name_8:
                temp_item8.append(brand_name_8)
            if class_name_8:
                temp_item8.append(class_name_8)
            if medium_8:
                temp_item8.append(medium_8)
            if subject_8:
                temp_item8.append(subject_8)
            if quantity_8:
                temp_item8.append(quantity_8)
            if rim_8:
                temp_item8.append(rim_8)    

            temp_item8 = [str(i or '') for i in temp_item8]
            item8 = ",".join(temp_item8)  


            brand_name_9 = request.POST.get('brand_name_9')
            class_name_9 = request.POST.get('class_name_9')
            medium_9 = request.POST.get('medium_9')
            subject_9 = request.POST.get('subject_9')
            quantity_9 = request.POST.get('quantity_9')
            rim_9 = request.POST.get('rim_9')
            temp_item9 = []
            if brand_name_9:
                temp_item9.append(brand_name_9)
            if class_name_9:
                temp_item9.append(class_name_9)
            if medium_9:
                temp_item9.append(medium_9)
            if subject_9:
                temp_item9.append(subject_9)
            if quantity_9:
                temp_item9.append(quantity_9)
            if rim_9:
                temp_item9.append(rim_9)    

            temp_item9 = [str(i or '') for i in temp_item9]
            item9 = ",".join(temp_item9)


            brand_name_10 = request.POST.get('brand_name_10')
            class_name_10 = request.POST.get('class_name_10')
            medium_10 = request.POST.get('medium_10')
            subject_10 = request.POST.get('subject_10')
            quantity_10 = request.POST.get('quantity_10')
            rim_10 = request.POST.get('rim_10')
            temp_item10 = []
            if brand_name_10:
                temp_item10.append(brand_name_10)
            if class_name_10:
                temp_item10.append(class_name_10)
            if medium_10:
                temp_item10.append(medium_10)
            if subject_10:
                temp_item10.append(subject_10)
            if quantity_10:
                temp_item10.append(quantity_10)
            if rim_10:
                temp_item10.append(rim_10)    

            temp_item10 = [str(i or '') for i in temp_item10]
            item10 = ",".join(temp_item10)
            

            brand_name_11 = request.POST.get('brand_name_11')
            class_name_11 = request.POST.get('class_name_11')
            medium_11 = request.POST.get('medium_11')
            subject_11 = request.POST.get('subject_11')
            quantity_11 = request.POST.get('quantity_11')
            rim_11 = request.POST.get('rim_11')
            temp_item11 = []
            if brand_name_11:
                temp_item11.append(brand_name_11)
            if class_name_11:
                temp_item11.append(class_name_11)
            if medium_11:
                temp_item11.append(medium_11)
            if subject_11:
                temp_item11.append(subject_11)
            if quantity_11:
                temp_item11.append(quantity_11)
            if rim_11:
                temp_item11.append(rim_11)    

            temp_item11 = [str(i or '') for i in temp_item11]
            item11 = ",".join(temp_item11)


            brand_name_12 = request.POST.get('brand_name_12')
            class_name_12 = request.POST.get('class_name_12')
            medium_12 = request.POST.get('medium_12')
            subject_12 = request.POST.get('subject_12')
            quantity_12 = request.POST.get('quantity_12')
            rim_12 = request.POST.get('rim_12')
            temp_item12 = []
            if brand_name_12:
                temp_item12.append(brand_name_12)
            if class_name_12:
                temp_item12.append(class_name_12)
            if medium_12:
                temp_item12.append(medium_12)
            if subject_12:
                temp_item12.append(subject_12)
            if quantity_12:
                temp_item12.append(quantity_12)
            if rim_12:
                temp_item12.append(rim_12)    

            temp_item12 = [str(i or '') for i in temp_item12]
            item12 = ",".join(temp_item12)


            brand_name_13 = request.POST.get('brand_name_13')
            class_name_13 = request.POST.get('class_name_13')
            medium_13 = request.POST.get('medium_13')
            subject_13 = request.POST.get('subject_13')
            quantity_13 = request.POST.get('quantity_13')
            rim_13 = request.POST.get('rim_13')
            temp_item13 = []
            if brand_name_13:
                temp_item13.append(brand_name_13)
            if class_name_13:
                temp_item13.append(class_name_13)
            if medium_13:
                temp_item13.append(medium_13)
            if subject_13:
                temp_item13.append(subject_13)
            if quantity_13:
                temp_item13.append(quantity_13)
            if rim_13:
                temp_item13.append(rim_13)    

            temp_item13 = [str(i or '') for i in temp_item13]
            item13 = ",".join(temp_item13)


            brand_name_14 = request.POST.get('brand_name_14')
            class_name_14 = request.POST.get('class_name_14')
            medium_14 = request.POST.get('medium_14')
            subject_14 = request.POST.get('subject_14')
            quantity_14 = request.POST.get('quantity_14')
            rim_14 = request.POST.get('rim_14')
            temp_item14 = []
            if brand_name_14:
                temp_item14.append(brand_name_14)
            if class_name_14:
                temp_item14.append(class_name_14)
            if medium_14:
                temp_item14.append(medium_14)
            if subject_14:
                temp_item14.append(subject_14)
            if quantity_14:
                temp_item14.append(quantity_14)
            if rim_14:
                temp_item14.append(rim_14)    

            temp_item14 = [str(i or '') for i in temp_item14]
            item14 = ",".join(temp_item14)


            brand_name_15 = request.POST.get('brand_name_15')
            class_name_15 = request.POST.get('class_name_15')
            medium_15 = request.POST.get('medium_15')
            subject_15 = request.POST.get('subject_15')
            quantity_15 = request.POST.get('quantity_15')
            rim_15 = request.POST.get('rim_15')
            temp_item15 = []
            if brand_name_15:
                temp_item15.append(brand_name_15)
            if class_name_15:
                temp_item15.append(class_name_15)
            if medium_15:
                temp_item15.append(medium_15)
            if subject_15:
                temp_item15.append(subject_15)
            if quantity_15:
                temp_item15.append(quantity_15)
            if rim_15:
                temp_item15.append(rim_15)    

            temp_item15 = [str(i or '') for i in temp_item15]
            item15 = ",".join(temp_item15)


            brand_name_16 = request.POST.get('brand_name_16')
            class_name_16 = request.POST.get('class_name_16')
            medium_16 = request.POST.get('medium_16')
            subject_16 = request.POST.get('subject_16')
            quantity_16 = request.POST.get('quantity_16')
            rim_16 = request.POST.get('rim_16')
            temp_item16 = []
            if brand_name_16:
                temp_item16.append(brand_name_16)
            if class_name_16:
                temp_item16.append(class_name_16)
            if medium_16:
                temp_item16.append(medium_16)
            if subject_16:
                temp_item16.append(subject_16)
            if quantity_16:
                temp_item16.append(quantity_16)
            if rim_16:
                temp_item16.append(rim_16)    

            temp_item16 = [str(i or '') for i in temp_item16]
            item16 = ",".join(temp_item16)


            brand_name_17 = request.POST.get('brand_name_17')
            class_name_17 = request.POST.get('class_name_17')
            medium_17 = request.POST.get('medium_17')
            subject_17 = request.POST.get('subject_17')
            quantity_17 = request.POST.get('quantity_17')
            rim_17 = request.POST.get('rim_17')
            temp_item17 = []
            if brand_name_17:
                temp_item17.append(brand_name_17)
            if class_name_17:
                temp_item17.append(class_name_17)
            if medium_17:
                temp_item17.append(medium_17)
            if subject_17:
                temp_item17.append(subject_17)
            if quantity_17:
                temp_item17.append(quantity_17)
            if rim_17:
                temp_item17.append(rim_17)    

            temp_item17 = [str(i or '') for i in temp_item17]
            item17 = ",".join(temp_item17)


            brand_name_18 = request.POST.get('brand_name_18')
            class_name_18 = request.POST.get('class_name_18')
            medium_18 = request.POST.get('medium_18')
            subject_18 = request.POST.get('subject_18')
            quantity_18 = request.POST.get('quantity_18')
            rim_18 = request.POST.get('rim_18')
            temp_item18 = []
            if brand_name_18:
                temp_item18.append(brand_name_18)
            if class_name_18:
                temp_item18.append(class_name_18)
            if medium_18:
                temp_item18.append(medium_18)
            if subject_18:
                temp_item18.append(subject_18)
            if quantity_18:
                temp_item18.append(quantity_18)
            if rim_18:
                temp_item18.append(rim_18)    

            temp_item18 = [str(i or '') for i in temp_item18]
            item18 = ",".join(temp_item18)


            brand_name_19 = request.POST.get('brand_name_19')
            class_name_19 = request.POST.get('class_name_19')
            medium_19 = request.POST.get('medium_19')
            subject_19 = request.POST.get('subject_19')
            quantity_19 = request.POST.get('quantity_19')
            rim_19 = request.POST.get('rim_19')
            temp_item19 = []
            if brand_name_19:
                temp_item19.append(brand_name_19)
            if class_name_19:
                temp_item19.append(class_name_19)
            if medium_19:
                temp_item19.append(medium_19)
            if subject_19:
                temp_item19.append(subject_19)
            if quantity_19:
                temp_item19.append(quantity_19)
            if rim_19:
                temp_item19.append(rim_19)    

            temp_item19 = [str(i or '') for i in temp_item19]
            item19 = ",".join(temp_item19)


            brand_name_20 = request.POST.get('brand_name_20')
            class_name_20 = request.POST.get('class_name_20')
            medium_20 = request.POST.get('medium_20')
            subject_20 = request.POST.get('subject_20')
            quantity_20 = request.POST.get('quantity_20')
            rim_20 = request.POST.get('rim_20')
            temp_item20 = []
            if brand_name_20:
                temp_item20.append(brand_name_20)
            if class_name_20:
                temp_item20.append(class_name_20)
            if medium_20:
                temp_item20.append(medium_20)
            if subject_20:
                temp_item20.append(subject_20)
            if quantity_20:
                temp_item20.append(quantity_20)
            if rim_20:
                temp_item20.append(rim_20)    

            temp_item20 = [str(i or '') for i in temp_item20]
            item20 = ",".join(temp_item20)


            brand_name_21 = request.POST.get('brand_name_21')
            class_name_21 = request.POST.get('class_name_21')
            medium_21 = request.POST.get('medium_21')
            subject_21 = request.POST.get('subject_21')
            quantity_21 = request.POST.get('quantity_21')
            rim_21 = request.POST.get('rim_21')
            temp_item21 = []
            if brand_name_21:
                temp_item21.append(brand_name_21)
            if class_name_21:
                temp_item21.append(class_name_21)
            if medium_21:
                temp_item21.append(medium_21)
            if subject_21:
                temp_item21.append(subject_21)
            if quantity_21:
                temp_item21.append(quantity_21)
            if rim_21:
                temp_item21.append(rim_21)    

            temp_item21 = [str(i or '') for i in temp_item21]
            item21 = ",".join(temp_item21)


            brand_name_22 = request.POST.get('brand_name_22')
            class_name_22 = request.POST.get('class_name_22')
            medium_22 = request.POST.get('medium_22')
            subject_22 = request.POST.get('subject_22')
            quantity_22 = request.POST.get('quantity_22')
            rim_22 = request.POST.get('rim_22')
            temp_item22 = []
            if brand_name_22:
                temp_item22.append(brand_name_22)
            if class_name_22:
                temp_item22.append(class_name_22)
            if medium_22:
                temp_item22.append(medium_22)
            if subject_22:
                temp_item22.append(subject_22)
            if quantity_22:
                temp_item22.append(quantity_22)
            if rim_22:
                temp_item22.append(rim_22)    

            temp_item22 = [str(i or '') for i in temp_item22]
            item22 = ",".join(temp_item22)


            brand_name_23 = request.POST.get('brand_name_23')
            class_name_23 = request.POST.get('class_name_23')
            medium_23 = request.POST.get('medium_23')
            subject_23 = request.POST.get('subject_23')
            quantity_23 = request.POST.get('quantity_23')
            rim_23 = request.POST.get('rim_23')
            temp_item23 = []
            if brand_name_23:
                temp_item23.append(brand_name_23)
            if class_name_23:
                temp_item23.append(class_name_23)
            if medium_23:
                temp_item23.append(medium_23)
            if subject_23:
                temp_item23.append(subject_23)
            if quantity_23:
                temp_item23.append(quantity_23)
            if rim_23:
                temp_item23.append(rim_23)    

            temp_item23 = [str(i or '') for i in temp_item23]
            item23 = ",".join(temp_item23)


            brand_name_24 = request.POST.get('brand_name_24')
            class_name_24 = request.POST.get('class_name_24')
            medium_24 = request.POST.get('medium_24')
            subject_24 = request.POST.get('subject_24')
            quantity_24 = request.POST.get('quantity_24')
            rim_24 = request.POST.get('rim_24')
            temp_item24 = []
            if brand_name_24:
                temp_item24.append(brand_name_24)
            if class_name_24:
                temp_item24.append(class_name_24)
            if medium_24:
                temp_item24.append(medium_24)
            if subject_24:
                temp_item24.append(subject_24)
            if quantity_24:
                temp_item24.append(quantity_24)
            if rim_24:
                temp_item24.append(rim_24)    

            temp_item24 = [str(i or '') for i in temp_item24]
            item24 = ",".join(temp_item24)


            brand_name_25 = request.POST.get('brand_name_25')
            class_name_25 = request.POST.get('class_name_25')
            medium_25 = request.POST.get('medium_25')
            subject_25 = request.POST.get('subject_25')
            quantity_25 = request.POST.get('quantity_25')
            rim_25 = request.POST.get('rim_25')
            temp_item25 = []
            if brand_name_25:
                temp_item25.append(brand_name_25)
            if class_name_25:
                temp_item25.append(class_name_25)
            if medium_25:
                temp_item25.append(medium_25)
            if subject_25:
                temp_item25.append(subject_25)
            if quantity_25:
                temp_item25.append(quantity_25)
            if rim_25:
                temp_item25.append(rim_25)    

            temp_item25 = [str(i or '') for i in temp_item25]
            item25 = ",".join(temp_item25)


            brand_name_26 = request.POST.get('brand_name_26')
            class_name_26 = request.POST.get('class_name_26')
            medium_26 = request.POST.get('medium_26')
            subject_26 = request.POST.get('subject_26')
            quantity_26 = request.POST.get('quantity_26')
            rim_26 = request.POST.get('rim_26')
            temp_item26 = []
            if brand_name_26:
                temp_item26.append(brand_name_26)
            if class_name_26:
                temp_item26.append(class_name_26)
            if medium_26:
                temp_item26.append(medium_26)
            if subject_26:
                temp_item26.append(subject_26)
            if quantity_26:
                temp_item26.append(quantity_26)
            if rim_26:
                temp_item26.append(rim_26)    

            temp_item26 = [str(i or '') for i in temp_item26]
            item26 = ",".join(temp_item26)


            brand_name_27 = request.POST.get('brand_name_27')
            class_name_27 = request.POST.get('class_name_27')
            medium_27 = request.POST.get('medium_27')
            subject_27 = request.POST.get('subject_27')
            quantity_27 = request.POST.get('quantity_27')
            rim_27 = request.POST.get('rim_27')
            temp_item27 = []
            if brand_name_27:
                temp_item27.append(brand_name_27)
            if class_name_27:
                temp_item27.append(class_name_27)
            if medium_27:
                temp_item27.append(medium_27)
            if subject_27:
                temp_item27.append(subject_27)
            if quantity_27:
                temp_item27.append(quantity_27)
            if rim_27:
                temp_item27.append(rim_27)    

            temp_item27 = [str(i or '') for i in temp_item27]
            item27 = ",".join(temp_item27)


            brand_name_28 = request.POST.get('brand_name_28')
            class_name_28 = request.POST.get('class_name_28')
            medium_28 = request.POST.get('medium_28')
            subject_28 = request.POST.get('subject_28')
            quantity_28 = request.POST.get('quantity_28')
            rim_28 = request.POST.get('rim_28')
            temp_item28 = []
            if brand_name_28:
                temp_item28.append(brand_name_28)
            if class_name_28:
                temp_item28.append(class_name_28)
            if medium_28:
                temp_item28.append(medium_28)
            if subject_28:
                temp_item28.append(subject_28)
            if quantity_28:
                temp_item28.append(quantity_28)
            if rim_28:
                temp_item28.append(rim_28)    

            temp_item28 = [str(i or '') for i in temp_item28]
            item28 = ",".join(temp_item28)


            brand_name_29 = request.POST.get('brand_name_29')
            class_name_29 = request.POST.get('class_name_29')
            medium_29 = request.POST.get('medium_29')
            subject_29 = request.POST.get('subject_29')
            quantity_29 = request.POST.get('quantity_29')
            rim_29 = request.POST.get('rim_29')
            temp_item29 = []
            if brand_name_29:
                temp_item29.append(brand_name_29)
            if class_name_29:
                temp_item29.append(class_name_29)
            if medium_29:
                temp_item29.append(medium_29)
            if subject_29:
                temp_item29.append(subject_29)
            if quantity_29:
                temp_item29.append(quantity_29)
            if rim_29:
                temp_item29.append(rim_29)    

            temp_item29 = [str(i or '') for i in temp_item29]
            item29 = ",".join(temp_item29)


            brand_name_30 = request.POST.get('brand_name_30')
            class_name_30 = request.POST.get('class_name_30')
            medium_30 = request.POST.get('medium_30')
            subject_30 = request.POST.get('subject_30')
            quantity_30 = request.POST.get('quantity_30')
            rim_30 = request.POST.get('rim_30')
            temp_item30 = []
            if brand_name_30:
                temp_item30.append(brand_name_30)
            if class_name_30:
                temp_item30.append(class_name_30)
            if medium_30:
                temp_item30.append(medium_30)
            if subject_30:
                temp_item30.append(subject_30)
            if quantity_30:
                temp_item30.append(quantity_30)
            if rim_30:
                temp_item30.append(rim_30)    

            temp_item30 = [str(i or '') for i in temp_item30]
            item30 = ",".join(temp_item30)


            brand_name_31 = request.POST.get('brand_name_31')
            class_name_31 = request.POST.get('class_name_31')
            medium_31 = request.POST.get('medium_31')
            subject_31 = request.POST.get('subject_31')
            quantity_31 = request.POST.get('quantity_31')
            rim_31 = request.POST.get('rim_31')
            temp_item31 = []
            if brand_name_31:
                temp_item31.append(brand_name_31)
            if class_name_31:
                temp_item31.append(class_name_31)
            if medium_31:
                temp_item31.append(medium_31)
            if subject_31:
                temp_item31.append(subject_31)
            if quantity_31:
                temp_item31.append(quantity_31)
            if rim_31:
                temp_item31.append(rim_31)    

            temp_item31 = [str(i or '') for i in temp_item31]
            item31 = ",".join(temp_item31)


            brand_name_32 = request.POST.get('brand_name_32')
            class_name_32 = request.POST.get('class_name_32')
            medium_32 = request.POST.get('medium_32')
            subject_32 = request.POST.get('subject_32')
            quantity_32 = request.POST.get('quantity_32')
            rim_32 = request.POST.get('rim_32')
            temp_item32 = []
            if brand_name_32:
                temp_item32.append(brand_name_32)
            if class_name_32:
                temp_item32.append(class_name_32)
            if medium_32:
                temp_item32.append(medium_32)
            if subject_32:
                temp_item32.append(subject_32)
            if quantity_32:
                temp_item32.append(quantity_32)
            if rim_32:
                temp_item32.append(rim_32)    

            temp_item32 = [str(i or '') for i in temp_item32]
            item32 = ",".join(temp_item32)


            brand_name_33 = request.POST.get('brand_name_33')
            class_name_33 = request.POST.get('class_name_33')
            medium_33 = request.POST.get('medium_33')
            subject_33 = request.POST.get('subject_33')
            quantity_33 = request.POST.get('quantity_33')
            rim_33 = request.POST.get('rim_33')
            temp_item33 = []
            if brand_name_33:
                temp_item33.append(brand_name_33)
            if class_name_33:
                temp_item33.append(class_name_33)
            if medium_33:
                temp_item33.append(medium_33)
            if subject_33:
                temp_item33.append(subject_33)
            if quantity_33:
                temp_item33.append(quantity_33)
            if rim_33:
                temp_item33.append(rim_33)    

            temp_item33 = [str(i or '') for i in temp_item33]
            item33 = ",".join(temp_item33)


            brand_name_34 = request.POST.get('brand_name_34')
            class_name_34 = request.POST.get('class_name_34')
            medium_34 = request.POST.get('medium_34')
            subject_34 = request.POST.get('subject_34')
            quantity_34 = request.POST.get('quantity_34')
            rim_34 = request.POST.get('rim_34')
            temp_item34 = []
            if brand_name_34:
                temp_item34.append(brand_name_34)
            if class_name_34:
                temp_item34.append(class_name_34)
            if medium_34:
                temp_item34.append(medium_34)
            if subject_34:
                temp_item34.append(subject_34)
            if quantity_34:
                temp_item34.append(quantity_34)
            if rim_34:
                temp_item34.append(rim_34)    

            temp_item34 = [str(i or '') for i in temp_item34]
            item34 = ",".join(temp_item34)


            brand_name_35 = request.POST.get('brand_name_35')
            class_name_35 = request.POST.get('class_name_35')
            medium_35 = request.POST.get('medium_35')
            subject_35 = request.POST.get('subject_35')
            quantity_35 = request.POST.get('quantity_35')
            rim_35 = request.POST.get('rim_35')
            temp_item35 = []
            if brand_name_35:
                temp_item35.append(brand_name_35)
            if class_name_35:
                temp_item35.append(class_name_35)
            if medium_35:
                temp_item35.append(medium_35)
            if subject_35:
                temp_item35.append(subject_35)
            if quantity_35:
                temp_item35.append(quantity_35)
            if rim_35:
                temp_item35.append(rim_35)    

            temp_item35 = [str(i or '') for i in temp_item35]
            item35 = ",".join(temp_item35)


            brand_name_36 = request.POST.get('brand_name_36')
            class_name_36 = request.POST.get('class_name_36')
            medium_36 = request.POST.get('medium_36')
            subject_36 = request.POST.get('subject_36')
            quantity_36 = request.POST.get('quantity_36')
            rim_36 = request.POST.get('rim_36')
            temp_item36 = []
            if brand_name_36:
                temp_item36.append(brand_name_36)
            if class_name_36:
                temp_item36.append(class_name_36)
            if medium_36:
                temp_item36.append(medium_36)
            if subject_36:
                temp_item36.append(subject_36)
            if quantity_36:
                temp_item36.append(quantity_36)
            if rim_36:
                temp_item36.append(rim_36)    

            temp_item36 = [str(i or '') for i in temp_item36]
            item36 = ",".join(temp_item36)


            brand_name_37 = request.POST.get('brand_name_37')
            class_name_37 = request.POST.get('class_name_37')
            medium_37 = request.POST.get('medium_37')
            subject_37 = request.POST.get('subject_37')
            quantity_37 = request.POST.get('quantity_37')
            rim_37 = request.POST.get('rim_37')
            temp_item37 = []
            if brand_name_37:
                temp_item37.append(brand_name_37)
            if class_name_37:
                temp_item37.append(class_name_37)
            if medium_37:
                temp_item37.append(medium_37)
            if subject_37:
                temp_item37.append(subject_37)
            if quantity_37:
                temp_item37.append(quantity_37)
            if rim_37:
                temp_item37.append(rim_37)    

            temp_item37 = [str(i or '') for i in temp_item37]
            item37 = ",".join(temp_item37)


            brand_name_38 = request.POST.get('brand_name_38')
            class_name_38 = request.POST.get('class_name_38')
            medium_38 = request.POST.get('medium_38')
            subject_38 = request.POST.get('subject_38')
            quantity_38 = request.POST.get('quantity_38')
            rim_38 = request.POST.get('rim_38')
            temp_item38 = []
            if brand_name_38:
                temp_item38.append(brand_name_38)
            if class_name_38:
                temp_item38.append(class_name_38)
            if medium_38:
                temp_item38.append(medium_38)
            if subject_38:
                temp_item38.append(subject_38)
            if quantity_38:
                temp_item38.append(quantity_38)
            if rim_38:
                temp_item38.append(rim_38)    

            temp_item38 = [str(i or '') for i in temp_item38]
            item38 = ",".join(temp_item38)


            brand_name_39 = request.POST.get('brand_name_39')
            class_name_39 = request.POST.get('class_name_39')
            medium_39 = request.POST.get('medium_39')
            subject_39 = request.POST.get('subject_39')
            quantity_39 = request.POST.get('quantity_39')
            rim_39 = request.POST.get('rim_39')
            temp_item39 = []
            if brand_name_39:
                temp_item39.append(brand_name_39)
            if class_name_39:
                temp_item39.append(class_name_39)
            if medium_39:
                temp_item39.append(medium_39)
            if subject_39:
                temp_item39.append(subject_39)
            if quantity_39:
                temp_item39.append(quantity_39)
            if rim_39:
                temp_item39.append(rim_39)    

            temp_item39 = [str(i or '') for i in temp_item39]
            item39 = ",".join(temp_item39)


            brand_name_40 = request.POST.get('brand_name_40')
            class_name_40 = request.POST.get('class_name_40')
            medium_40 = request.POST.get('medium_40')
            subject_40 = request.POST.get('subject_40')
            quantity_40 = request.POST.get('quantity_40')
            rim_40 = request.POST.get('rim_40')
            temp_item40 = []
            if brand_name_40:
                temp_item40.append(brand_name_40)
            if class_name_40:
                temp_item40.append(class_name_40)
            if medium_40:
                temp_item40.append(medium_40)
            if subject_40:
                temp_item40.append(subject_40)
            if quantity_40:
                temp_item40.append(quantity_40)
            if rim_40:
                temp_item40.append(rim_40)    

            temp_item40 = [str(i or '') for i in temp_item40]
            item40 = ",".join(temp_item40)


            brand_name_41 = request.POST.get('brand_name_41')
            class_name_41 = request.POST.get('class_name_41')
            medium_41 = request.POST.get('medium_41')
            subject_41 = request.POST.get('subject_41')
            quantity_41 = request.POST.get('quantity_41')
            rim_41 = request.POST.get('rim_41')
            temp_item41 = []
            if brand_name_41:
                temp_item41.append(brand_name_41)
            if class_name_41:
                temp_item41.append(class_name_41)
            if medium_41:
                temp_item41.append(medium_41)
            if subject_41:
                temp_item41.append(subject_41)
            if quantity_41:
                temp_item41.append(quantity_41)
            if rim_41:
                temp_item41.append(rim_41)    

            temp_item41 = [str(i or '') for i in temp_item41]
            item41 = ",".join(temp_item41)


            brand_name_42 = request.POST.get('brand_name_42')
            class_name_42 = request.POST.get('class_name_42')
            medium_42 = request.POST.get('medium_42')
            subject_42 = request.POST.get('subject_42')
            quantity_42 = request.POST.get('quantity_42')
            rim_42 = request.POST.get('rim_42')
            temp_item42 = []
            if brand_name_42:
                temp_item42.append(brand_name_42)
            if class_name_42:
                temp_item42.append(class_name_42)
            if medium_42:
                temp_item42.append(medium_42)
            if subject_42:
                temp_item42.append(subject_42)
            if quantity_42:
                temp_item42.append(quantity_42)
            if rim_42:
                temp_item42.append(rim_42)    

            temp_item42 = [str(i or '') for i in temp_item42]
            item42 = ",".join(temp_item42)


            brand_name_43 = request.POST.get('brand_name_43')
            class_name_43 = request.POST.get('class_name_43')
            medium_43 = request.POST.get('medium_43')
            subject_43 = request.POST.get('subject_43')
            quantity_43 = request.POST.get('quantity_43')
            rim_43 = request.POST.get('rim_43')
            temp_item43 = []
            if brand_name_43:
                temp_item43.append(brand_name_43)
            if class_name_43:
                temp_item43.append(class_name_43)
            if medium_43:
                temp_item43.append(medium_43)
            if subject_43:
                temp_item43.append(subject_43)
            if quantity_43:
                temp_item43.append(quantity_43)
            if rim_43:
                temp_item43.append(rim_43)    

            temp_item43 = [str(i or '') for i in temp_item43]
            item43 = ",".join(temp_item43)


            brand_name_44 = request.POST.get('brand_name_44')
            class_name_44 = request.POST.get('class_name_44')
            medium_44 = request.POST.get('medium_44')
            subject_44 = request.POST.get('subject_44')
            quantity_44 = request.POST.get('quantity_44')
            rim_44 = request.POST.get('rim_44')
            temp_item44 = []
            if brand_name_44:
                temp_item44.append(brand_name_44)
            if class_name_44:
                temp_item44.append(class_name_44)
            if medium_44:
                temp_item44.append(medium_44)
            if subject_44:
                temp_item44.append(subject_44)
            if quantity_44:
                temp_item44.append(quantity_44)
            if rim_44:
                temp_item44.append(rim_44)    

            temp_item44 = [str(i or '') for i in temp_item44]
            item44 = ",".join(temp_item44)


            brand_name_45 = request.POST.get('brand_name_45')
            class_name_45 = request.POST.get('class_name_45')
            medium_45 = request.POST.get('medium_45')
            subject_45 = request.POST.get('subject_45')
            quantity_45 = request.POST.get('quantity_45')
            rim_45 = request.POST.get('rim_45')
            temp_item45 = []
            if brand_name_45:
                temp_item45.append(brand_name_45)
            if class_name_45:
                temp_item45.append(class_name_45)
            if medium_45:
                temp_item45.append(medium_45)
            if subject_45:
                temp_item45.append(subject_45)
            if quantity_45:
                temp_item45.append(quantity_45)
            if rim_45:
                temp_item45.append(rim_45)    

            temp_item45 = [str(i or '') for i in temp_item45]
            item45 = ",".join(temp_item45)


            brand_name_46 = request.POST.get('brand_name_46')
            class_name_46 = request.POST.get('class_name_46')
            medium_46 = request.POST.get('medium_46')
            subject_46 = request.POST.get('subject_46')
            quantity_46 = request.POST.get('quantity_46')
            rim_46 = request.POST.get('rim_46')
            temp_item46 = []
            if brand_name_46:
                temp_item46.append(brand_name_46)
            if class_name_46:
                temp_item46.append(class_name_46)
            if medium_46:
                temp_item46.append(medium_46)
            if subject_46:
                temp_item46.append(subject_46)
            if quantity_46:
                temp_item46.append(quantity_46)
            if rim_46:
                temp_item46.append(rim_46)    

            temp_item46 = [str(i or '') for i in temp_item46]
            item46 = ",".join(temp_item46)


            brand_name_47 = request.POST.get('brand_name_47')
            class_name_47 = request.POST.get('class_name_47')
            medium_47 = request.POST.get('medium_47')
            subject_47 = request.POST.get('subject_47')
            quantity_47 = request.POST.get('quantity_47')
            rim_47 = request.POST.get('rim_47')
            temp_item47 = []
            if brand_name_47:
                temp_item47.append(brand_name_47)
            if class_name_47:
                temp_item47.append(class_name_47)
            if medium_47:
                temp_item47.append(medium_47)
            if subject_47:
                temp_item47.append(subject_47)
            if quantity_47:
                temp_item47.append(quantity_47)
            if rim_47:
                temp_item47.append(rim_47)    

            temp_item47 = [str(i or '') for i in temp_item47]
            item47 = ",".join(temp_item47)


            brand_name_48 = request.POST.get('brand_name_48')
            class_name_48 = request.POST.get('class_name_48')
            medium_48 = request.POST.get('medium_48')
            subject_48 = request.POST.get('subject_48')
            quantity_48 = request.POST.get('quantity_48')
            rim_48 = request.POST.get('rim_48')
            temp_item48 = []
            if brand_name_48:
                temp_item48.append(brand_name_48)
            if class_name_48:
                temp_item48.append(class_name_48)
            if medium_48:
                temp_item48.append(medium_48)
            if subject_48:
                temp_item48.append(subject_48)
            if quantity_48:
                temp_item48.append(quantity_48)
            if rim_48:
                temp_item48.append(rim_48)    

            temp_item48 = [str(i or '') for i in temp_item48]
            item48 = ",".join(temp_item48)


            brand_name_49 = request.POST.get('brand_name_49')
            class_name_49 = request.POST.get('class_name_49')
            medium_49 = request.POST.get('medium_49')
            subject_49 = request.POST.get('subject_49')
            quantity_49 = request.POST.get('quantity_49')
            rim_49 = request.POST.get('rim_49')
            temp_item49 = []
            if brand_name_49:
                temp_item49.append(brand_name_49)
            if class_name_49:
                temp_item49.append(class_name_49)
            if medium_49:
                temp_item49.append(medium_49)
            if subject_49:
                temp_item49.append(subject_49)
            if quantity_49:
                temp_item49.append(quantity_49)
            if rim_49:
                temp_item49.append(rim_49)    

            temp_item49 = [str(i or '') for i in temp_item49]
            item49 = ",".join(temp_item49)


            brand_name_50 = request.POST.get('brand_name_50')
            class_name_50 = request.POST.get('class_name_50')
            medium_50 = request.POST.get('medium_50')
            subject_50 = request.POST.get('subject_50')
            quantity_50 = request.POST.get('quantity_50')
            rim_50 = request.POST.get('rim_50')
            temp_item50 = []
            if brand_name_50:
                temp_item50.append(brand_name_50)
            if class_name_50:
                temp_item50.append(class_name_50)
            if medium_50:
                temp_item50.append(medium_50)
            if subject_50:
                temp_item50.append(subject_50)
            if quantity_50:
                temp_item50.append(quantity_50)
            if rim_50:
                temp_item50.append(rim_50)    

            temp_item50 = [str(i or '') for i in temp_item50]
            item50 = ",".join(temp_item50)


            
            



# For adding quantity at the end of each items
            temp_amnt = []
            if quantity_1:
                temp_amnt.append(quantity_1)
            if quantity_2:
                temp_amnt.append(quantity_2)
            if quantity_3:
                temp_amnt.append(quantity_3)
            if quantity_4:
                temp_amnt.append(quantity_4)
            if quantity_5:
                temp_amnt.append(quantity_5)
            if quantity_6:
                temp_amnt.append(quantity_6)
            if quantity_7:
                temp_amnt.append(quantity_7)
            if quantity_8:
                temp_amnt.append(quantity_8)
            if quantity_9:
                temp_amnt.append(quantity_9)
            if quantity_10:
                temp_amnt.append(quantity_10)
            if quantity_11:
                temp_amnt.append(quantity_11)  
            if quantity_12:
                temp_amnt.append(quantity_12)
            if quantity_13:
                temp_amnt.append(quantity_13)
            if quantity_14:
                temp_amnt.append(quantity_14)
            if quantity_15:
                temp_amnt.append(quantity_15)
            if quantity_16:
                temp_amnt.append(quantity_16)
            if quantity_17:
                temp_amnt.append(quantity_17)
            if quantity_18:
                temp_amnt.append(quantity_18)
            if quantity_19:
                temp_amnt.append(quantity_19)
            if quantity_20:
                temp_amnt.append(quantity_20)
            if quantity_21:
                temp_amnt.append(quantity_21)
            if quantity_22:
                temp_amnt.append(quantity_22)
            if quantity_23:
                temp_amnt.append(quantity_23)
            if quantity_24:
                temp_amnt.append(quantity_24)
            if quantity_25:
                temp_amnt.append(quantity_25)
            if quantity_26:
                temp_amnt.append(quantity_26)
            if quantity_27:
                temp_amnt.append(quantity_27)
            if quantity_28:
                temp_amnt.append(quantity_28)
            if quantity_29:
                temp_amnt.append(quantity_29)
            if quantity_30:
                temp_amnt.append(quantity_30)
            if quantity_31:
                temp_amnt.append(quantity_31)
            if quantity_32:
                temp_amnt.append(quantity_32)
            if quantity_33:
                temp_amnt.append(quantity_33)
            if quantity_34:
                temp_amnt.append(quantity_34)
            if quantity_35:
                temp_amnt.append(quantity_35) 
            if quantity_36:
                temp_amnt.append(quantity_36)
            if quantity_37:
                temp_amnt.append(quantity_37) 
            if quantity_38:
                temp_amnt.append(quantity_38)
            if quantity_39:
                temp_amnt.append(quantity_39)
            if quantity_40:
                temp_amnt.append(quantity_40)
            if quantity_41:
                temp_amnt.append(quantity_41)
            if quantity_42:
                temp_amnt.append(quantity_42)
            if quantity_43:
                temp_amnt.append(quantity_43)
            if quantity_44:
                temp_amnt.append(quantity_44)
            if quantity_45:
                temp_amnt.append(quantity_45)
            if quantity_46:
                temp_amnt.append(quantity_46)
            if quantity_47:
                temp_amnt.append(quantity_47)
            if quantity_48:
                temp_amnt.append(quantity_48)
            if quantity_49:
                temp_amnt.append(quantity_49)
            if quantity_50:
                temp_amnt.append(quantity_50)                                                                                                                                                              



            temp_amnt = [str(i or '') for i in temp_amnt]
            print(temp_amnt)
            total_amount = 0
            for i in temp_amnt:
                total_amount = total_amount + float(i)

            actual_data = orders.objects.create(purchase_date=datetime.datetime.now(),vender_name=vender_name,
                        vender_mob=vender_mob,vender_address=vender_address, item1=item1,item2=item2, item3=item3,
                        item4=item4,item5= item5, item6=item6,item7=item7,item8=item8,item9=item9, item10= item10,
                        item11= item11,item12=item12,item13=item13,item14= item14,item15=item15,item16=item16,
                        item17=item17,item18=item18,item19= item19,item20=item20,item21=item21,item22=item22,
                        item23= item23,item24=item24,item25=item25,item26=item26,item27=item27,item28=item28,
                        item29=item29,item30=item30,item31=item31,item32=item32,item33=item33,item34=item34,
                        item35=item35,item36=item36,item37= item37,item38=item38,item39=item39,item40=item40,
                        item41=item41,item42=item42,item43=item43,item44=item44,item45=item45,item46=item46,
                        item47=item47,item48=item48,item49=item49,item50=item50,vender_email=vender_email,
                        no_of_pages=no_of_pages,gst=gst, order_id=order_id, total_quantity=total_amount,
                        brand_name_1=brand_name_1,class_name_1=class_name_1,medium_1=medium_1,subject_1=subject_1,quantity_1=quantity_1,rim_1=rim_1,
                        brand_name_2=brand_name_2,class_name_2=class_name_2,medium_2=medium_2,subject_2=subject_2,quantity_2=quantity_2,rim_2=rim_2,
                        brand_name_3=brand_name_3,class_name_3=class_name_3,medium_3=medium_3,subject_3=subject_3,quantity_3=quantity_3,rim_3=rim_3,
                        brand_name_4=brand_name_4,class_name_4=class_name_4,medium_4=medium_4,subject_4=subject_4,quantity_4=quantity_4,rim_4=rim_4,
                        brand_name_5=brand_name_5,class_name_5=class_name_5,medium_5=medium_5,subject_5=subject_5,quantity_5=quantity_5,rim_5=rim_5,
                        brand_name_6=brand_name_6,class_name_6=class_name_6,medium_6=medium_6,subject_6=subject_6,quantity_6=quantity_6,rim_6=rim_6,
                        brand_name_7=brand_name_7,class_name_7=class_name_7,medium_7=medium_7,subject_7=subject_7,quantity_7=quantity_7,rim_7=rim_7,
                        brand_name_8=brand_name_8,class_name_8=class_name_8,medium_8=medium_8,subject_8=subject_8,quantity_8=quantity_8,rim_8=rim_8,
                        brand_name_9=brand_name_9,class_name_9=class_name_9,medium_9=medium_9,subject_9=subject_9,quantity_9=quantity_9,rim_9=rim_9,
                        brand_name_10=brand_name_10,class_name_10=class_name_10,medium_10=medium_10,subject_10=subject_10,quantity_10=quantity_10,rim_10=rim_10,
                        brand_name_11=brand_name_11,class_name_11=class_name_11,medium_11=medium_11,subject_11=subject_11,quantity_11=quantity_11,rim_11=rim_11,
                        brand_name_12=brand_name_12,class_name_12=class_name_12,medium_12=medium_12,subject_12=subject_12,quantity_12=quantity_12,rim_12=rim_12,
                        brand_name_13=brand_name_13,class_name_13=class_name_13,medium_13=medium_13,subject_13=subject_13,quantity_13=quantity_13,rim_13=rim_13,
                        brand_name_14=brand_name_14,class_name_14=class_name_14,medium_14=medium_14,subject_14=subject_14,quantity_14=quantity_14,rim_14=rim_14,
                        brand_name_15=brand_name_15,class_name_15=class_name_15,medium_15=medium_15,subject_15=subject_15,quantity_15=quantity_15,rim_15=rim_15,
                        brand_name_16=brand_name_16,class_name_16=class_name_16,medium_16=medium_16,subject_16=subject_16,quantity_16=quantity_16,rim_16=rim_16,
                        brand_name_17=brand_name_17,class_name_17=class_name_17,medium_17=medium_17,subject_17=subject_17,quantity_17=quantity_17,rim_17=rim_17,
                        brand_name_18=brand_name_18,class_name_18=class_name_18,medium_18=medium_18,subject_18=subject_18,quantity_18=quantity_18,rim_18=rim_18,
                        brand_name_19=brand_name_19,class_name_19=class_name_19,medium_19=medium_19,subject_19=subject_19,quantity_19=quantity_19,rim_19=rim_19,
                        brand_name_20=brand_name_20,class_name_20=class_name_20,medium_20=medium_20,subject_20=subject_20,quantity_20=quantity_20,rim_20=rim_20,
                        brand_name_21=brand_name_21,class_name_21=class_name_21,medium_21=medium_21,subject_21=subject_21,quantity_21=quantity_21,rim_21=rim_21,
                        brand_name_22=brand_name_22,class_name_22=class_name_22,medium_22=medium_22,subject_22=subject_22,quantity_22=quantity_22,rim_22=rim_22,
                        brand_name_23=brand_name_23,class_name_23=class_name_23,medium_23=medium_23,subject_23=subject_23,quantity_23=quantity_23,rim_23=rim_23,
                        brand_name_24=brand_name_24,class_name_24=class_name_24,medium_24=medium_24,subject_24=subject_24,quantity_24=quantity_24,rim_24=rim_24,
                        brand_name_25=brand_name_25,class_name_25=class_name_25,medium_25=medium_25,subject_25=subject_25,quantity_25=quantity_25,rim_25=rim_25,
                        brand_name_26=brand_name_26,class_name_26=class_name_26,medium_26=medium_26,subject_26=subject_26,quantity_26=quantity_26,rim_26=rim_26,
                        brand_name_27=brand_name_27,class_name_27=class_name_27,medium_27=medium_27,subject_27=subject_27,quantity_27=quantity_27,rim_27=rim_27,
                        brand_name_28=brand_name_28,class_name_28=class_name_28,medium_28=medium_28,subject_28=subject_28,quantity_28=quantity_28,rim_28=rim_28,
                        brand_name_29=brand_name_29,class_name_29=class_name_29,medium_29=medium_29,subject_29=subject_29,quantity_29=quantity_29,rim_29=rim_29,
                        brand_name_30=brand_name_30,class_name_30=class_name_30,medium_30=medium_30,subject_30=subject_30,quantity_30=quantity_30,rim_30=rim_30,
                        brand_name_31=brand_name_31,class_name_31=class_name_31,medium_31=medium_31,subject_31=subject_31,quantity_31=quantity_31,rim_31=rim_31,
                        brand_name_32=brand_name_32,class_name_32=class_name_32,medium_32=medium_32,subject_32=subject_32,quantity_32=quantity_32,rim_32=rim_32,
                        brand_name_33=brand_name_33,class_name_33=class_name_33,medium_33=medium_33,subject_33=subject_33,quantity_33=quantity_33,rim_33=rim_33,
                        brand_name_34=brand_name_34,class_name_34=class_name_34,medium_34=medium_34,subject_34=subject_34,quantity_34=quantity_34,rim_34=rim_34,
                        brand_name_35=brand_name_35,class_name_35=class_name_35,medium_35=medium_35,subject_35=subject_35,quantity_35=quantity_35,rim_35=rim_35,
                        brand_name_36=brand_name_36,class_name_36=class_name_36,medium_36=medium_36,subject_36=subject_36,quantity_36=quantity_36,rim_36=rim_36,
                        brand_name_37=brand_name_37,class_name_37=class_name_37,medium_37=medium_37,subject_37=subject_37,quantity_37=quantity_37,rim_37=rim_37,
                        brand_name_38=brand_name_38,class_name_38=class_name_38,medium_38=medium_38,subject_38=subject_38,quantity_38=quantity_38,rim_38=rim_38,
                        brand_name_39=brand_name_39,class_name_39=class_name_39,medium_39=medium_39,subject_39=subject_39,quantity_39=quantity_39,rim_39=rim_39,
                        brand_name_40=brand_name_40,class_name_40=class_name_40,medium_40=medium_40,subject_40=subject_40,quantity_40=quantity_40,rim_40=rim_40,
                        brand_name_41=brand_name_41,class_name_41=class_name_41,medium_41=medium_41,subject_41=subject_41,quantity_41=quantity_41,rim_41=rim_41,
                        brand_name_42=brand_name_42,class_name_42=class_name_42,medium_42=medium_42,subject_42=subject_42,quantity_42=quantity_42,rim_42=rim_42,
                        brand_name_43=brand_name_43,class_name_43=class_name_43,medium_43=medium_43,subject_43=subject_43,quantity_43=quantity_43,rim_43=rim_43,
                        brand_name_44=brand_name_44,class_name_44=class_name_44,medium_44=medium_44,subject_44=subject_44,quantity_44=quantity_44,rim_44=rim_44,
                        brand_name_45=brand_name_45,class_name_45=class_name_45,medium_45=medium_45,subject_45=subject_45,quantity_45=quantity_45,rim_45=rim_45,
                        brand_name_46=brand_name_46,class_name_46=class_name_46,medium_46=medium_46,subject_46=subject_46,quantity_46=quantity_46,rim_46=rim_46,
                        brand_name_47=brand_name_47,class_name_47=class_name_47,medium_47=medium_47,subject_47=subject_47,quantity_47=quantity_47,rim_47=rim_47,
                        brand_name_48=brand_name_48,class_name_48=class_name_48,medium_48=medium_48,subject_48=subject_48,quantity_48=quantity_48,rim_48=rim_48,
                        brand_name_49=brand_name_49,class_name_49=class_name_49,medium_49=medium_49,subject_49=subject_49,quantity_49=quantity_49,rim_49=rim_49,
                        brand_name_50=brand_name_50,class_name_50=class_name_50,medium_50=medium_50,subject_50=subject_50,quantity_50=quantity_50,rim_50=rim_50,

                        )

            brd_app = brands.objects.all()
            book = books.objects.all()
            data = orders.objects.filter().order_by('-purchase_date')

            rim_1 = 0
            rim_2 = 0
            rim_3 = 0
            rim_4 = 0
            rim_5 = 0
            rim_6 = 0
            rim_7 = 0
            rim_8 = 0
            rim_9 = 0
            rim_10 = 0
            rim_11 = 0
            rim_12 = 0
            rim_13 = 0
            rim_14 = 0
            rim_15 = 0
            rim_16 = 0
            rim_17 = 0
            rim_18 = 0
            rim_19 = 0
            rim_20 = 0
            rim_21 = 0
            rim_22 = 0 
            rim_23 = 0
            rim_24 = 0
            rim_25 = 0
            rim_26 = 0
            rim_27 = 0
            rim_28 = 0
            rim_29 = 0
            rim_30 = 0
            rim_31 = 0
            rim_32 = 0
            rim_33 = 0
            rim_34 = 0
            rim_35 = 0
            rim_36 = 0 
            rim_37 = 0
            rim_38 = 0
            rim_39 = 0
            rim_40 = 0
            rim_41 = 0
            rim_42 = 0 
            rim_43 = 0
            rim_44 = 0
            rim_45 = 0
            rim_46 = 0
            rim_47 = 0
            rim_48 = 0
            rim_49 = 0
            rim_50 = 0

            if quantity_1 != None:
                data = orders.objects.filter().last()
                for j in book:
                    if j.books_name in data.item1:
                        rim_1 = (float(quantity_1)*float(j.per_book_forms))/500
            if quantity_2 != None:
                data = orders.objects.filter().last()
                for j in book:
                    if j.books_name in data.item2:
                        rim_2 = (float(quantity_2)*float(j.per_book_forms))/500
            if quantity_3 != None:   
                data = orders.objects.filter().last()
                for j in book:       
                    if j.books_name in data.item3:
                        rim_3 = (float(quantity_3)*float(j.per_book_forms))/500
            if quantity_4 != None:
                data = orders.objects.filter().last() 
                for j in book:                      
                    if j.books_name in data.item4:
                        rim_4 = (float(quantity_4)*float(j.per_book_forms))/500
            if quantity_5 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item5:
                        rim_5 = (float(quantity_5)*float(j.per_book_forms))/500

            if quantity_6 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item6:
                        rim_6 = (float(quantity_6)*float(j.per_book_forms))/500 

            if quantity_7 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item7:
                        rim_7 = (float(quantity_7)*float(j.per_book_forms))/500                       

            if quantity_8 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item8:
                        rim_8 = (float(quantity_8)*float(j.per_book_forms))/500

            if quantity_9 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item9:
                        rim_9 = (float(quantity_9)*float(j.per_book_forms))/500

            if quantity_10 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item10:
                        rim_10 = (float(quantity_10)*float(j.per_book_forms))/500

            if quantity_11 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item11:
                        rim_11 = (float(quantity_11)*float(j.per_book_forms))/500  

            if quantity_12 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item12:
                        rim_12 = (float(quantity_12)*float(j.per_book_forms))/500

            if quantity_13 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item13:
                        rim_13 = (float(quantity_13)*float(j.per_book_forms))/500

            if quantity_14 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item14:
                        rim_14 = (float(quantity_14)*float(j.per_book_forms))/500

            if quantity_15 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item15:
                        rim_15 = (float(quantity_15)*float(j.per_book_forms))/500

            if quantity_16 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item16:
                        rim_16 = (float(quantity_16)*float(j.per_book_forms))/500

            if quantity_17 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item17:
                        rim_17 = (float(quantity_17)*float(j.per_book_forms))/500

            if quantity_18 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item18:
                        rim_18 = (float(quantity_18)*float(j.per_book_forms))/500

            if quantity_19 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item19:
                        rim_19 = (float(quantity_19)*float(j.per_book_forms))/500

            if quantity_20 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item20:
                        rim_20 = (float(quantity_20)*float(j.per_book_forms))/500

            if quantity_21 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item21:
                        rim_21 = (float(quantity_21)*float(j.per_book_forms))/500

            if quantity_22 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item22:
                        rim_22 = (float(quantity_22)*float(j.per_book_forms))/500

            if quantity_23 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item23:
                        rim_23 = (float(quantity_23)*float(j.per_book_forms))/500

            if quantity_24 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item24:
                        rim_24 = (float(quantity_24)*float(j.per_book_forms))/500

            if quantity_25 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item25:
                        rim_25 = (float(quantity_25)*float(j.per_book_forms))/500

            if quantity_26 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item26:
                        rim_26 = (float(quantity_26)*float(j.per_book_forms))/500

            if quantity_27 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item27:
                        rim_27 = (float(quantity_27)*float(j.per_book_forms))/500

            if quantity_28 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item28:
                        rim_28 = (float(quantity_28)*float(j.per_book_forms))/500

            if quantity_29 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item29:
                        rim_29 = (float(quantity_29)*float(j.per_book_forms))/500

            if quantity_30 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item30:
                        rim_30 = (float(quantity_30)*float(j.per_book_forms))/500

            if quantity_31 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item31:
                        rim_31 = (float(quantity_31)*float(j.per_book_forms))/500

            if quantity_32 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item32:
                        rim_32 = (float(quantity_32)*float(j.per_book_forms))/500

            if quantity_33 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item33:
                        rim_33 = (float(quantity_33)*float(j.per_book_forms))/500

            if quantity_34 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item34:
                        rim_34 = (float(quantity_34)*float(j.per_book_forms))/500

            if quantity_35 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item35:
                        rim_35 = (float(quantity_35)*float(j.per_book_forms))/500

            if quantity_36 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item36:
                        rim_36 = (float(quantity_36)*float(j.per_book_forms))/500

            if quantity_37 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item37:
                        rim_37 = (float(quantity_37)*float(j.per_book_forms))/500

            if quantity_38 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item38:
                        rim_38 = (float(quantity_38)*float(j.per_book_forms))/500

            if quantity_39 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item39:
                        rim_39 = (float(quantity_39)*float(j.per_book_forms))/500

            if quantity_40 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item40:
                        rim_40 = (float(quantity_40)*float(j.per_book_forms))/500

            if quantity_41 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item41:
                        rim_41 = (float(quantity_41)*float(j.per_book_forms))/500

            if quantity_42 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item42:
                        rim_42 = (float(quantity_42)*float(j.per_book_forms))/500

            if quantity_43 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item43:
                        rim_43 = (float(quantity_43)*float(j.per_book_forms))/500

            if quantity_44 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item44:
                        rim_44 = (float(quantity_44)*float(j.per_book_forms))/500

            if quantity_45 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item45:
                        rim_45 = (float(quantity_45)*float(j.per_book_forms))/500

            if quantity_46 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item46:
                        rim_46 = (float(quantity_46)*float(j.per_book_forms))/500 


            if quantity_47 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item47:
                        rim_47 = (float(quantity_47)*float(j.per_book_forms))/500 


            if quantity_48 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item48:
                        rim_48 = (float(quantity_48)*float(j.per_book_forms))/500

            if quantity_49 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item49:
                        rim_49 = (float(quantity_49)*float(j.per_book_forms))/500 

            if quantity_50 != None:
                data = orders.objects.filter().last() 
                for j in book:           
                    if j.books_name in data.item50:
                        rim_50 = (float(quantity_50)*float(j.per_book_forms))/500                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     




            temp_rim = []
            if quantity_1:
                temp_rim.append(rim_1)
            if quantity_2:
                temp_rim.append(rim_2)
            if quantity_3:
                temp_rim.append(rim_3)
            if quantity_4:
                temp_rim.append(rim_4)
            if quantity_5:
                temp_rim.append(rim_5)
            if quantity_6:
                temp_rim.append(rim_6)
            if quantity_7:
                temp_rim.append(rim_7)  
            if quantity_8:
                temp_rim.append(rim_8)
            if quantity_9:
                temp_rim.append(rim_9)
            if quantity_10:
                temp_rim.append(rim_10)
            if quantity_11:
                temp_rim.append(rim_11)  
            if quantity_12:
                temp_rim.append(rim_12)
            if quantity_13:
                temp_rim.append(rim_13)
            if quantity_14:
                temp_rim.append(rim_14)
            if quantity_15:
                temp_rim.append(rim_15)
            if quantity_16:
                temp_rim.append(rim_16)
            if quantity_17:
                temp_rim.append(rim_17)
            if quantity_18:
                temp_rim.append(rim_18)
            if quantity_19:
                temp_rim.append(rim_19)
            if quantity_20:
                temp_rim.append(rim_20)
            if quantity_21:
                temp_rim.append(rim_21)
            if quantity_22:
                temp_rim.append(rim_22)
            if quantity_23:
                temp_rim.append(rim_23)
            if quantity_24:
                temp_rim.append(rim_24)
            if quantity_25:
                temp_rim.append(rim_25)
            if quantity_26:
                temp_rim.append(rim_26)
            if quantity_27:
                temp_rim.append(rim_27)
            if quantity_28:
                temp_rim.append(rim_28)
            if quantity_29:
                temp_rim.append(rim_29)
            if quantity_30:
                temp_rim.append(rim_30)
            if quantity_31:
                temp_rim.append(rim_31)
            if quantity_32:
                temp_rim.append(rim_32) 
            if quantity_33:
                temp_rim.append(rim_33)
            if quantity_34:
                temp_rim.append(rim_34)
            if quantity_35:
                temp_rim.append(rim_35)
            if quantity_36:
                temp_rim.append(rim_36)
            if quantity_37:
                temp_rim.append(rim_37)
            if quantity_38:
                temp_rim.append(rim_38) 
            if quantity_39:
                temp_rim.append(rim_39)
            if quantity_40:
                temp_rim.append(rim_40)
            if quantity_41:
                temp_rim.append(rim_41)
            if quantity_42:
                temp_rim.append(rim_42)
            if quantity_43:
                temp_rim.append(rim_43)
            if quantity_44:
                temp_rim.append(rim_44)
            if quantity_45:
                temp_rim.append(rim_45)
            if quantity_46:
                temp_rim.append(rim_46)
            if quantity_47:
                temp_rim.append(rim_47)
            if quantity_48:
                temp_rim.append(rim_48)
            if quantity_49:
                temp_rim.append(rim_49)
            if quantity_50:
                temp_rim.append(rim_50)                    
                                                                                                                                                      



            temp_rim = [(i) for i in temp_rim]
            rim = (temp_rim)
            print(temp_rim)

            total_rim = 0
            for i in temp_rim:
                total_rim = total_rim + float(i)
            
                
                
            
                
                
            actual_data.rim_1=rim_1
            actual_data.rim_2=rim_2
            actual_data.rim_3=rim_3
            actual_data.rim_4=rim_4
            actual_data.rim_5=rim_5
            actual_data.rim_6=rim_6
            actual_data.rim_7=rim_7
            actual_data.rim_8=rim_8
            actual_data.rim_9=rim_9
            actual_data.rim_10=rim_10
            actual_data.rim_11=rim_11
            actual_data.rim_12=rim_12
            actual_data.rim_13=rim_13
            actual_data.rim_14=rim_14
            actual_data.rim_15=rim_15
            actual_data.rim_16=rim_16
            actual_data.rim_17=rim_17
            actual_data.rim_18=rim_18
            actual_data.rim_19=rim_19
            actual_data.rim_20=rim_20
            actual_data.rim_21=rim_21
            actual_data.rim_22=rim_22
            actual_data.rim_23=rim_23
            actual_data.rim_24=rim_24
            actual_data.rim_25=rim_25
            actual_data.rim_26=rim_26
            actual_data.rim_27=rim_27
            actual_data.rim_28=rim_28
            actual_data.rim_29=rim_29
            actual_data.rim_30=rim_30
            actual_data.rim_31=rim_31
            actual_data.rim_32=rim_32
            actual_data.rim_33=rim_33
            actual_data.rim_34=rim_34
            actual_data.rim_35=rim_35
            actual_data.rim_36=rim_36
            actual_data.rim_37=rim_37
            actual_data.rim_38=rim_38
            actual_data.rim_39=rim_39
            actual_data.rim_40=rim_40
            actual_data.rim_41=rim_41
            actual_data.rim_42=rim_42
            actual_data.rim_43=rim_43
            actual_data.rim_44=rim_44
            actual_data.rim_45=rim_45
            actual_data.rim_46=rim_46
            actual_data.rim_47=rim_47
            actual_data.rim_48=rim_48
            actual_data.rim_49=rim_49
            actual_data.rim_50=rim_50
            actual_data.total_rim = total_rim
            actual_data.save()
            print('actual_data.total_rim', actual_data.total_rim)


    vend = venders.objects.all()
    book = books.objects.all()
    data1 = venders.objects.values(
        'organization_name').distinct().order_by('organization_name')
    data2 = venders.objects.values(
        'vender_address').distinct().order_by('vender_address')
    data3 = brands.objects.values(
        'brand_name').distinct().order_by('brand_name')
    data4 = books .objects.values(
        'books_name').distinct().order_by('books_name')
    data5 = books .objects.values(
        'books_class').distinct().order_by('books_class')
    data6 = books.objects.values('subject').distinct().order_by('subject')
    data7 = mediums.objects.values('medium').distinct().order_by('medium')
    data8 = orders.objects.filter().order_by('-purchase_date')
    context ={
        'vend': vend,
        'data8': data8,
        'book': book,
        'data': data,
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        'data5': data5,
        'data6': data6,
        'data7': data7,
        'order': order,
        'vendor': vendor,
    }
    return render(request, 'orders/neword.html',context)

@login_required(login_url="") 
def delete_orders(request, id):
    cus = orders.objects.get(id=id)
    cus.delete()
    sweetify.success(request, title="Success 1...", icon='success', text='Deleted successfully...', timer=1500)
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
