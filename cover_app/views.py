from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
import datetime
from cover_app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from brand_app.models import *
from django.http import JsonResponse
import secrets
import sweetify
from django.http import HttpResponseBadRequest

from datetime import datetime

def cover_recoding(request):
    if request.method=="POST":

      plate_record= request.POST.get("plate_record")
      date_record=  datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
      quantity_record= request.POST.get("quantity_record")
      unit_record= request.POST.get("unit_record")
      vender_record= request.POST.get("vender_record")
      data1 = Cover_record(
                
                plate_record= plate_record,
                date_record=date_record,
                quantity_record=quantity_record,
                unit_record=unit_record,
                vender_record=vender_record,
                
      )
      data1.save()
      sweetify.success(request, " Created Successfully.", timer=6000, button='OK')
    
    data=Cover_record.objects.all().order_by('-id')
    obj3=Cover_Printing.objects.all()
    obj=Bindingvender.objects.all()
    return render(request, 'cover/cover_record.html', {'data':data,'obj3':obj3,'obj':obj})



def delete_cover_record(request, id):
    cus = Cover_record.objects.get(id=id)
    cus.delete()
    return redirect('/cover_recoding/')


def edit_cover_record(request, id):
    data = Cover_record.objects.get(id=id)
    if request.method == 'POST':
            data.plate_record = request.POST.get('plate_record')
            data.date_record = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
            data.quantity_record = request.POST.get('quantity_record')
            data.unit_record = request.POST.get('unit_record')
            data.vender_record = request.POST.get('vender_record')
            
            data.save()
           
            return redirect('/cover_recoding/')
    
    print("datanew", data.plate_record)
    context = {'data':data,}
    return render(request, 'cover/edit_cover_record.html', context)
    

def view_cover_cutting(request,id):
    data = Cover_cutting.objects.get(id=id)
    
    print("4444444444",data.cutting_quantity)
    data2=Cover_Printing.objects.filter(plate_no=data.cutting_plate_no)
    print("111",data2)
    for i in data2:
       print("333333",i.subject1)
    context = {'data':data,'data2':data2,}
    return render(request, 'cover/view_cover_cutting.html', context)






def cover_lamination(request):
    if request.method=="POST":

      plate_lamination1= request.POST.get("plate_lamination1")
      date_lamination=  datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
      quantity_lamination1= request.POST.get("quantity_lamination1")
      unit_lamination1= request.POST.get("unit_lamination1")
      vender_lamination= request.POST.get("vender_lamination")

      plate_lamination2 =request.POST.get("plate_lamination2")
      quantity_lamination2 = request.POST.get("quantity_lamination2")
      unit_lamination2 =request.POST.get("unit_lamination2")

      plate_lamination3= request.POST.get("plate_lamination3")
      quantity_lamination3= request.POST.get("quantity_lamination3")
      unit_lamination3= request.POST.get("unit_lamination3")

      plate_lamination4= request.POST.get("plate_lamination4")
      quantity_lamination4= request.POST.get("quantity_lamination4")
      unit_lamination4= request.POST.get("unit_lamination4")
      
      plate_lamination5= request.POST.get("plate_lamination5")
      quantity_lamination5= request.POST.get("quantity_lamination5")
      unit_lamination5= request.POST.get("unit_lamination5")

      plate_lamination6= request.POST.get("plate_lamination6")
      quantity_lamination6= request.POST.get("quantity_lamination6")
      unit_lamination6= request.POST.get("unit_lamination6")

      plate_lamination7= request.POST.get("plate_lamination7")
      quantity_lamination7= request.POST.get("quantity_lamination7")
      unit_lamination7= request.POST.get("unit_lamination7")

      plate_lamination8= request.POST.get("plate_lamination8")
      quantity_lamination8= request.POST.get("quantity_lamination8")
      unit_lamination8= request.POST.get("unit_lamination8")

      plate_lamination9= request.POST.get("plate_lamination9")
      quantity_lamination9= request.POST.get("quantity_lamination9")
      unit_lamination9= request.POST.get("unit_lamination9")

      plate_lamination10= request.POST.get("plate_lamination10")
      quantity_lamination10= request.POST.get("quantity_lamination10")
      unit_lamination10= request.POST.get("unit_lamination10")





      data1 = Cover_lamination(
                
                plate_lamination1= plate_lamination1,
                date_lamination=date_lamination,
                quantity_lamination1=quantity_lamination1,
                unit_lamination1=unit_lamination1,
                vender_lamination=vender_lamination,

                plate_lamination2= plate_lamination2,
                quantity_lamination2=quantity_lamination2,
                unit_lamination2=unit_lamination2,

                plate_lamination3= plate_lamination3,
                quantity_lamination3=quantity_lamination3,
                unit_lamination3=unit_lamination3,

                plate_lamination4= plate_lamination4,
                quantity_lamination4=quantity_lamination4,
                unit_lamination4=unit_lamination4,

                plate_lamination5= plate_lamination5,
                quantity_lamination5=quantity_lamination5,
                unit_lamination5=unit_lamination5,

                plate_lamination6= plate_lamination6,
                quantity_lamination6=quantity_lamination6,
                unit_lamination6=unit_lamination6,

                plate_lamination7= plate_lamination7,
                quantity_lamination7=quantity_lamination7,
                unit_lamination7=unit_lamination7,

                plate_lamination8= plate_lamination8,
                quantity_lamination8=quantity_lamination8,
                unit_lamination8=unit_lamination8,

                plate_lamination9= plate_lamination9,
                quantity_lamination9=quantity_lamination9,
                unit_lamination9=unit_lamination9,

                plate_lamination10= plate_lamination10,
                quantity_lamination10=quantity_lamination10,
                unit_lamination10=unit_lamination10,
                
      )
      data1.save()
      sweetify.success(request, " Created Successfully.", timer=6000, button='OK')
    
    data=Cover_lamination.objects.all().order_by('-id')
    obj3=Cover_Printing.objects.all()
    obj=Bindingvender.objects.all()
    return render(request, 'cover/cover_lamination.html', {'data':data,'obj3':obj3,'obj':obj})




def delete_cover_lamination(request, id):
    cus = Cover_lamination.objects.get(id=id)
    cus.delete()
    return redirect('/cover_lamination/')


def edit_cover_lamination(request, id):
    data = Cover_lamination.objects.get(id=id)
    if request.method == 'POST':
            data.plate_lamination = request.POST.get('plate_lamination')
            data.date_lamination = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
            data.quantity_lamination = request.POST.get('quantity_lamination')
            data.unit_lamination = request.POST.get('unit_lamination')
            data.vender_lamination = request.POST.get('vender_lamination')
            
            data.save()
           
            return redirect('/cover_lamination/')
    
    print("datanew", data.plate_lamination)
    context = {'data':data,}
    return render(request, 'cover/edit_cover_lamination.html', context)


def cover_lami_bill_view(request, id):
    data = Cover_lamination.objects.get(id=id)
    print('data', data)
    a = float(data.plate_lamination) if data.plate_lamination else 0.0
    print('a', a)
    b = float(data.quantity_lamination) if data.quantity_lamination else 0.0
    print("b", b)

    # Define the maximum number of orders
    max_orders = 49 # Maximum number of orders to consider

    order_data = []
    total_quantity = 0

    for i in range(1, max_orders + 1):
        
        quantity_field = 'quantity_lamination{}'.format(i)
        quantity = getattr(data, quantity_field, None)

        if quantity:
            order_data.append({
                'medium': request.POST.get('midium_{}'.format(i)),
                'subject': request.POST.get('bsubject_{}'.format(i)),
                'quantity': float(quantity),
                'ord_rate3': request.POST.get('ord_rate3{}'.format(i))
            })

            # Calculate the sum of quantities
            total_quantity += float(quantity)
            print('total_quantity', total_quantity)

    # Update the total_quantity field of the Bindingorder object
    data.binding_order_total = total_quantity
    print("1111111111", data.binding_order_total)
    data.save()

    context = {
        'data': data,
        'order_data': order_data,
        'binding_order_total': total_quantity,
        'a': a,
    }

    return render(request, 'cover/cover_lami_bill_view.html', context)




def cover_texture(request):
    if request.method=="POST":

      plate_texture1= request.POST.get("plate_texture1")
      date_texture=  datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
      quantity_texture1= request.POST.get("quantity_texture1")
      unit_texture1= request.POST.get("unit_texture1")
      vender_texture= request.POST.get("vender_texture")

      plate_texture2= request.POST.get("plate_texture2")
      quantity_texture2= request.POST.get("quantity_texture2")
      unit_texture2= request.POST.get("unit_texture2")

      plate_texture3= request.POST.get("plate_texture3")
      quantity_texture3= request.POST.get("quantity_texture3")
      unit_texture3= request.POST.get("unit_texture3")

      plate_texture4= request.POST.get("plate_texture4")
      quantity_texture4= request.POST.get("quantity_texture4")
      unit_texture4= request.POST.get("unit_texture4")


      plate_texture5= request.POST.get("plate_texture5")
      quantity_texture5= request.POST.get("quantity_texture5")
      unit_texture5= request.POST.get("unit_texture5")

      plate_texture6= request.POST.get("plate_texture6")
      quantity_texture6= request.POST.get("quantity_texture6")
      unit_texture6= request.POST.get("unit_texture6")

      plate_texture7= request.POST.get("plate_texture7")
      quantity_texture7= request.POST.get("quantity_texture7")
      unit_texture7= request.POST.get("unit_texture7")

      plate_texture8= request.POST.get("plate_texture8")
      quantity_texture8= request.POST.get("quantity_texture8")
      unit_texture8= request.POST.get("unit_texture8")

      plate_texture9= request.POST.get("plate_texture9")
      quantity_texture9= request.POST.get("quantity_texture9")
      unit_texture9= request.POST.get("unit_texture9")

      plate_texture10= request.POST.get("plate_texture10")
      quantity_texture10= request.POST.get("quantity_texture10")
      unit_texture10= request.POST.get("unit_texture10")
      data1 = Cover_texture(
                
                plate_texture1= plate_texture1,
                date_texture=date_texture,
                quantity_texture1=quantity_texture1,
                unit_texture1=unit_texture1,
                vender_texture=vender_texture,

                plate_texture2= plate_texture2,
                quantity_texture2=quantity_texture2,
                unit_texture2=unit_texture2,
                
                plate_texture3= plate_texture3,
                quantity_texture3=quantity_texture3,
                unit_texture3=unit_texture3,

                plate_texture4= plate_texture4,
                quantity_texture4=quantity_texture4,
                unit_texture4=unit_texture4,

                plate_texture5= plate_texture5,
                quantity_texture5=quantity_texture5,
                unit_texture5=unit_texture5,

                plate_texture6= plate_texture6,
                quantity_texture6=quantity_texture6,
                unit_texture6=unit_texture6,

                plate_texture7= plate_texture7,
                quantity_texture7=quantity_texture7,
                unit_texture7=unit_texture7,

                plate_texture8= plate_texture8,
                quantity_texture8=quantity_texture8,
                unit_texture8=unit_texture8,

                plate_texture9= plate_texture9,
                quantity_texture9=quantity_texture9,
                unit_texture9=unit_texture9,

                plate_texture10= plate_texture10,
                quantity_texture10=quantity_texture10,
                unit_texture10=unit_texture10,



                
      )
      data1.save()
      sweetify.success(request, " Created Successfully.", timer=6000, button='OK')
    
    data=Cover_texture.objects.all().order_by('-id')
    obj3=Cover_Printing.objects.all()
    obj=Bindingvender.objects.all()
    return render(request, 'cover/cover_texture.html', {'data':data,'obj3':obj3,'obj':obj})




def delete_cover_texture(request, id):
    cus = Cover_texture.objects.get(id=id)
    cus.delete()
    return redirect('/cover_texture/')


def edit_cover_texture(request, id):
    data = Cover_texture.objects.get(id=id)
    if request.method == 'POST':
            data.plate_texture = request.POST.get('plate_texture')
            data.date_texture = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
            data.quantity_texture = request.POST.get('quantity_texture')
            data.unit_texture = request.POST.get('unit_texture')
            data.vender_texture = request.POST.get('vender_texture')
            
            data.save()
           
            return redirect('/cover_lamination/')
    
    print("datanew", data.plate_texture)
    context = {'data':data,}
    return render(request, 'cover/edit_cover_texture.html', context)




def topi(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        t_plate_no = request.POST.get('t_plate_no')
        t_plate_rate = request.POST.get('t_plate_rate')
        t_printing_rate = request.POST.get('t_printing_rate')
        t_paper_to_be_used = request.POST.get('t_paper_to_be_used')  # Convert to float
        
        t_no_of_ups= request.POST.get('t_no_of_ups')
        print("1111111111111",t_no_of_ups)
        t_subject1=request.POST.get('t_subject1') 
        print("1111111111111",t_subject1)
        t_subject2= request.POST.get('t_subject2')
        t_subject3= request.POST.get('t_subject3')
        t_subject4= request.POST.get('t_subject4')
        t_subject5= request.POST.get('t_subject5')
        t_subject6= request.POST.get('t_subject6')
        t_subject7= request.POST.get('t_subject7')
        t_subject8= request.POST.get('t_subject8')
        t_subject9= request.POST.get('t_subject9')
        t_subject10= request.POST.get('t_subject10')
        t_subject11= request.POST.get('t_subject11')
        t_subject12= request.POST.get('t_subject12')
        t_subject13= request.POST.get('t_subject13')
        t_subject14= request.POST.get('t_subject14')
        t_subject15= request.POST.get('t_subject15')
        t_subject16= request.POST.get('t_subject16')
        t_subject17= request.POST.get('t_subject17')
        t_subject18= request.POST.get('t_subject18')
        t_subject19= request.POST.get('t_subject19')
        t_subject20= request.POST.get('t_subject20')
        t_subject21= request.POST.get('t_subject21')
        t_subject22= request.POST.get('t_subject22')
        t_subject23= request.POST.get('t_subject23')
        t_subject24= request.POST.get('t_subject24')
        t_subject25= request.POST.get('t_subject25')
        t_subject26= request.POST.get('t_subject26')
        t_subject27= request.POST.get('t_subject27')
        t_subject28= request.POST.get('t_subject28')
        t_subject29= request.POST.get('t_subject29')
        t_subject30= request.POST.get('t_subject30')
        t_subject31= request.POST.get('t_subject31')
        t_subject32= request.POST.get('t_subject32')
        t_quantity = request.POST.get('t_quantity')
        book_data = Topi(
            
            t_plate_no=t_plate_no,
            t_paper_to_be_used=t_paper_to_be_used,
            t_plate_rate=t_plate_rate,
            t_printing_rate=t_printing_rate,
            
            t_no_of_ups= t_no_of_ups,
            t_subject1=t_subject1,
            t_subject2=t_subject2,
            t_subject3=t_subject3,
            t_subject4=t_subject4,
            t_subject5=t_subject5,
            t_subject6=t_subject6,
            t_subject7=t_subject7,
            t_subject8=t_subject8,
            t_subject9=t_subject9,
            t_subject10=t_subject10,
            t_subject11=t_subject11,
            t_subject12=t_subject12,
            t_subject13=t_subject13,
            t_subject14=t_subject14,
            t_subject15=t_subject15,
            t_subject16=t_subject16,
            t_subject17=t_subject17,
            t_subject18= t_subject18,
            t_subject19= t_subject19,
            t_subject20= t_subject20,
            t_subject21= t_subject21,
            t_subject22= t_subject22,
            t_subject23= t_subject23,
            t_subject24= t_subject24,
            t_subject25= t_subject25,
            t_subject26= t_subject26,
            t_subject27= t_subject27,
            t_subject28= t_subject28,
            t_subject29= t_subject29,
            t_subject30= t_subject30,
            t_subject31= t_subject31,
            t_subject32= t_subject32,
            t_quantity = t_quantity,
            

        )
        book_data.save()
    obj=books.objects.all()
    obj1=Company.objects.all()
    data = Topi.objects.all().order_by('-id')
    obj2 =forms.objects.all()
    return render(request, 'cover/topi.html', {'data': data,'obj':obj,'obj1':obj1,'obj2':obj2})  


def delete_topi(request, id):
    cus = Topi.objects.get(id=id)
    cus.delete()
    return redirect('/topi/')


def cover_tex_bill_view(request, id):
    
    data = Cover_texture.objects.get(id=id)
    print('data', data)
    a = float(data.plate_texture1) if data.plate_texture1 else 0.0
    print('a', a)
    b = float(data.quantity_texture1) if data.quantity_texture1 else 0.0
    print("b", b)

    # Define the maximum number of orders
    max_orders = 49 # Maximum number of orders to consider

    order_data = []
    total_quantity = 0

    for i in range(1, max_orders + 1):
        
        quantity_field = 'quantity_texture{}'.format(i)
        quantity = getattr(data, quantity_field, None)

        if quantity:
            order_data.append({
                'medium': request.POST.get('midium_{}'.format(i)),
                'subject': request.POST.get('bsubject_{}'.format(i)),
                'quantity': float(quantity),
                'ord_rate3': request.POST.get('ord_rate3{}'.format(i))
            })

            # Calculate the sum of quantities
            total_quantity += float(quantity)
            print('total_quantity', total_quantity)

    # Update the total_quantity field of the Bindingorder object
    data.binding_order_total = total_quantity
    print("1111111111", data.binding_order_total)
    data.save()

    context = {
        'data': data,
        'order_data': order_data,
        'binding_order_total': total_quantity,
        'a': a,
    }

    return render(request, 'cover/cover_tex_bill_view.html', context)



@login_required(login_url="")
def edit_topi(request, id):
    data = Topi.objects.get(id=id)
    if request.method == 'POST':
        # data.from_vend=request.POST.get("from_vend")
        # data.to_vend=request.POST.get("to_vend")
        data.t_plate_no= request.POST.get('t_plate_no')
        data.t_paper_to_be_used= request.POST.get('t_paper_to_be_used')
        data.t_quantity = request.POST.get('t_quantity')
        data.t_subject1=request.POST.get('t_subject1')
        data.t_subject2=request.POST.get('t_subject2')
        data.t_subject3=request.POST.get('t_subject3')
        data.t_subject4=request.POST.get('t_subject4')
        data.t_subject5=request.POST.get('t_subject5')
        data.t_subject6=request.POST.get('t_subject6')
        data.t_subject7=request.POST.get('t_subject7')
        data.t_subject8=request.POST.get('t_subject8')
        data.t_subject9=request.POST.get('t_subject9')
        data.t_subject10=request.POST.get('t_subject10')
        data.t_subject11=request.POST.get('t_subject11')
        data.t_subject12=request.POST.get('t_subject12')
        data.t_subject13=request.POST.get('t_subject13')
        data.t_subject14=request.POST.get('t_subject14')
        data.t_subject15=request.POST.get('t_subject15')
        data.t_subject16=request.POST.get('t_subject16')
        data.t_subject17=request.POST.get('t_subject17')
        data.t_subject18= request.POST.get('t_subject18')
        data.t_subject19= request.POST.get('t_subject19')
        data.t_subject20= request.POST.get('t_subject20')
        data.t_subject21= request.POST.get('t_subject21')
        data.t_subject22= request.POST.get('t_subject22')
        data.t_subject23= request.POST.get('t_subject23')
        data.t_subject24= request.POST.get('t_subject24')
        data.t_subject25= request.POST.get('t_subject25')
        data.t_subject26= request.POST.get('t_subject26')
        data.t_subject27= request.POST.get('t_subject27')
        data.t_subject28= request.POST.get('t_subject28')
        data.t_subject29= request.POST.get('t_subject29')
        data.t_subject30= request.POST.get('t_subject30')
        data.t_subject31= request.POST.get('t_subject31')
        data.t_subject32= request.POST.get('t_subject32')
       
        
        
        print("11111111111111",data.t_quantity)
        
        
        data.save()
        return redirect('/topi/')
    
        
                
    obj2 =forms.objects.all()
    context = {'data':data,'obj2':obj2}
    return render(request, 'cover/edit_topi.html', context)



def topi_order(request):
    if request.method == "POST":
        
        ord_vendor = request.POST.get("ord_vendor")
        material_center = request.POST.get("material_center")
        ord_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        ord_plate_no1 = request.POST.get("ord_plate_no1")
        ord_quantity1 = request.POST.get("ord_quantity1")
        ord_unit1 = request.POST.get("ord_unit1")
        ord_rate1 = request.POST.get("ord_rate1")
        ord_amount1 = request.POST.get("ord_amount1")
        printing_rate1 = request.POST.get("printing_rate1")
        print_rate1 = request.POST.get("print_rate1")
        material_centre1= request.POST.get('material_centre1')


        ord_plate_no2 = request.POST.get("ord_plate_no2")
        ord_quantity2 = request.POST.get("ord_quantity2")
        ord_unit2 = request.POST.get("ord_unit2")
        ord_rate2 = request.POST.get("ord_rate2")
        ord_amount2 = request.POST.get("ord_amount2")
        printing_rate2 = request.POST.get("printing_rate2")
        print_rate2 = request.POST.get("print_rate2")

        ord_plate_no3 = request.POST.get("ord_plate_no3")
        ord_quantity3 = request.POST.get("ord_quantity3")
        ord_unit3 = request.POST.get("ord_unit3")
        ord_rate3 = request.POST.get("ord_rate3")
        ord_amount3 = request.POST.get("ord_amount3")
        printing_rate3 = request.POST.get("printing_rate3")
        print_rate3 = request.POST.get("print_rate3")

        ord_plate_no4 = request.POST.get("ord_plate_no4")
        ord_quantity4 = request.POST.get("ord_quantity4")
        ord_unit4 = request.POST.get("ord_unit4")
        ord_rate4 = request.POST.get("ord_rate4")
        ord_amount4 = request.POST.get("ord_amount4")
        printing_rate4 = request.POST.get("printing_rate4")
        print_rate4 = request.POST.get("print_rate4")

        ord_plate_no5 = request.POST.get("ord_plate_no5")
        ord_quantity5 = request.POST.get("ord_quantity5")
        ord_unit5 = request.POST.get("ord_unit5")
        ord_rate5 = request.POST.get("ord_rate5")
        ord_amount5 = request.POST.get("ord_amount5")
        printing_rate5 = request.POST.get("printing_rate5")
        print_rate5 = request.POST.get("print_rate5")

        ord_plate_no6 = request.POST.get("ord_plate_no6")
        ord_quantity6 = request.POST.get("ord_quantity6")
        ord_unit6 = request.POST.get("ord_unit6")
        ord_rate6 = request.POST.get("ord_rate6")
        ord_amount6 = request.POST.get("ord_amount6")
        printing_rate6 = request.POST.get("printing_rate6")
        print_rate6 = request.POST.get("print_rate6")

        ord_plate_no7 = request.POST.get("ord_plate_no7")
        ord_quantity7 = request.POST.get("ord_quantity7")
        ord_unit7 = request.POST.get("ord_unit7")
        ord_rate7 = request.POST.get("ord_rate7")
        ord_amount7 = request.POST.get("ord_amount7")
        printing_rate7 = request.POST.get("printing_rate7")
        print_rate7 = request.POST.get("print_rate7")

        ord_plate_no8 = request.POST.get("ord_plate_no8")
        ord_quantity8 = request.POST.get("ord_quantity8")
        ord_unit8 = request.POST.get("ord_unit8")
        ord_rate8 = request.POST.get("ord_rate8")
        ord_amount8 = request.POST.get("ord_amount8")
        printing_rate8 = request.POST.get("printing_rate8")
        print_rate8 = request.POST.get("print_rate8")

        ord_plate_no9 = request.POST.get("ord_plate_no9")
        ord_quantity9 = request.POST.get("ord_quantity9")
        ord_unit9 = request.POST.get("ord_unit9")
        ord_rate9 = request.POST.get("ord_rate9")
        ord_amount9 = request.POST.get("ord_amount9")
        printing_rate9 = request.POST.get("printing_rate9")
        print_rate9 = request.POST.get("print_rate9")

        ord_plate_no10 = request.POST.get("ord_plate_no10")
        ord_quantity10 = request.POST.get("ord_quantity10")
        ord_unit10 = request.POST.get("ord_unit10")
        ord_rate10 = request.POST.get("ord_rate10")
        ord_amount10 = request.POST.get("ord_amount10")
        printing_rate10= request.POST.get("printing_rate10")
        print_rate10= request.POST.get("print_rate10")

        bill_sundries_1 = request.POST.get("bill_sundries_1")
        narration_1= request.POST.get("narration_1")
        amount_1= request.POST.get("amount_1")
        percent_1=request.POST.get("percent_1")

        bill_sundries_2 = request.POST.get("bill_sundries_2")
        narration_2= request.POST.get("narration_2")
        amount_2= request.POST.get("amount_2")
        percent_2=request.POST.get("percent_2")

        bill_sundries_3 = request.POST.get("bill_sundries_3")
        narration_3= request.POST.get("narration_3")
        amount_3= request.POST.get("amount_3")
        percent_3=request.POST.get("percent_3")

        bill_sundries_4 = request.POST.get("bill_sundries_4")
        narration_4= request.POST.get("narration_4")
        amount_4= request.POST.get("amount_4")
        percent_4=request.POST.get("percent_4")

        bill_sundries_5 = request.POST.get("bill_sundries_5")
        narration_5= request.POST.get("narration_5")
        amount_5= request.POST.get("amount_5")
        percent_5=request.POST.get("percent_5")
        totalAmount=request.POST.get("totalAmount")

        

        # Calculate cutting_amount
        quantities = []
        rates = []

        # Loop through the range 1 to 11 to get quantities and rates
        for i in range(1, 11):
            quantity_field = f"ord_quantity{i}"
            rate_field = f"ord_rate{i}"

            quantity = request.POST.get(quantity_field)
            rate = request.POST.get(rate_field)

            # Check if either quantity or rate is not empty before calculating amount
            if quantity and rate:
                quantities.append(float(quantity))
                rates.append(float(rate))

        # Calculate the corresponding amounts
        amounts = [quantity * rate for quantity, rate in zip(quantities, rates)]
        print("1234444444",amounts)

        # Create a dictionary to map fields and values for the Topi_order model
        field_values = {
            "ord_vendor": ord_vendor,
            "ord_date": ord_date,
        }

        for i in range(1, 11):
            field_values[f"ord_quantity{i}"] = request.POST.get(f"ord_quantity{i}")
            field_values[f"ord_rate{i}"] = request.POST.get(f"ord_rate{i}")
            field_values[f"ord_amount{i}"] = amounts[i - 1] if i <= len(amounts) else None
            print("1111111111",field_values[f"ord_amount{i}"])
            

        data1 = Topi_order(
            material_center=material_center,
            ord_vendor=ord_vendor,
            ord_date=ord_date,
            ord_plate_no1=ord_plate_no1,
            ord_quantity1=ord_quantity1,
            ord_unit1=ord_unit1,
            ord_rate1=ord_rate1,
            ord_amount1=ord_amount1,

            ord_plate_no2=ord_plate_no2,
            ord_quantity2=ord_quantity2,
            ord_unit2=ord_unit2,
            ord_rate2=ord_rate2,
            ord_amount2=ord_amount2,

            ord_plate_no3=ord_plate_no3,
            ord_quantity3=ord_quantity3,
            ord_unit3=ord_unit3,
            ord_rate3=ord_rate3,
            ord_amount3=ord_amount3,

            ord_plate_no4=ord_plate_no4,
            ord_quantity4=ord_quantity4,
            ord_unit4=ord_unit4,
            ord_rate4=ord_rate4,
            ord_amount4=ord_amount4,

            ord_plate_no5=ord_plate_no5,
            ord_quantity5=ord_quantity5,
            ord_unit5=ord_unit5,
            ord_rate5=ord_rate5,
            ord_amount5=ord_amount5,


            ord_plate_no6=ord_plate_no6,
            ord_quantity6=ord_quantity6,
            ord_unit6=ord_unit6,
            ord_rate6=ord_rate6,
            ord_amount6=ord_amount6,


            ord_plate_no7=ord_plate_no7,
            ord_quantity7=ord_quantity7,
            ord_unit7=ord_unit7,
            ord_rate7=ord_rate7,
            ord_amount7=ord_amount7,

            ord_plate_no8=ord_plate_no8,
            ord_quantity8=ord_quantity8,
            ord_unit8=ord_unit8,
            ord_rate8=ord_rate8,
            ord_amount8=ord_amount8,

            ord_plate_no9=ord_plate_no9,
            ord_quantity9=ord_quantity9,
            ord_unit9=ord_unit9,
            ord_rate9=ord_rate9,
            ord_amount9=ord_amount9,

            ord_plate_no10=ord_plate_no10,
            ord_quantity10=ord_quantity10,
            ord_unit10=ord_unit10,
            ord_rate10=ord_rate10,
            ord_amount10=ord_amount10,
            material_centre1=material_centre1,
            printing_rate1=printing_rate1,
            printing_rate2=printing_rate2,
            printing_rate3=printing_rate3,
            printing_rate4=printing_rate4,
            printing_rate5=printing_rate5,
            printing_rate6=printing_rate6,
            printing_rate7=printing_rate7,
            printing_rate8=printing_rate8,
            printing_rate9=printing_rate9,
            printing_rate10=printing_rate10,

            print_rate1=print_rate1,
            print_rate2= print_rate2,
            print_rate3= print_rate3,
            print_rate4= print_rate4,
            print_rate5= print_rate5,
            print_rate6= print_rate6,
            print_rate7= print_rate7,
            print_rate8=print_rate8,
            print_rate9= print_rate9,
            print_rate10= print_rate10,

            bill_sundries_1=bill_sundries_1,
            narration_1=narration_1,
            amount_1=amount_1,
            percent_1=percent_1,


            bill_sundries_2=bill_sundries_2,
            narration_2=narration_2,
            amount_2=amount_2,
            percent_2=percent_2,


            bill_sundries_3=bill_sundries_3,
            narration_3=narration_3,
            amount_3=amount_3,
            percent_3=percent_3,


            bill_sundries_4=bill_sundries_4,
            narration_4=narration_4,
            amount_4=amount_4,
            percent_4=percent_4,


            bill_sundries_5=bill_sundries_5,
            narration_5=narration_5,
            amount_5=amount_5,
            percent_5=percent_5,

            totalAmount=totalAmount,
           



           
            
        )
        data1.save()
        sweetify.success(request, " Created Successfully.", timer=6000, button='OK')

    data = Topi_order.objects.all().order_by('-id')
    comp = Company.objects.all()
    vend= Bindingvender.objects.all()
    obj3=Topi.objects.all()
    for i in obj3:
        print("111111111",i.t_printing_rate)
    data3=material_centre.objects.all()
    return render(request, 'cover/topi_order.html', {'data': data,'comp':comp,'obj3':obj3,'vend':vend,'data3':data3, })


def topi_bill_view(request, id):
    data = Topi_order.objects.get(id=id)
    print('data', data)
    a = float(data.ord_amount1) if data.ord_amount1 else 0.0
    print('a', a)
    b = float(data.ord_plate_no1) if data.ord_plate_no1 else 0.0
    print("b", b)

    # Define the maximum number of orders
    max_orders = 50  # Maximum number of orders to consider

    order_data = []
    total_quantity = 0

    for i in range(1, max_orders + 1):
        quantity_field = 'ord_amount{}'.format(i)
        quantity = getattr(data, quantity_field, None)

        if quantity:
            order_data.append({
                'medium': request.POST.get('midium_{}'.format(i)),
                'subject': request.POST.get('bsubject_{}'.format(i)),
                'quantity': float(quantity),
                'ord_rate3': request.POST.get('ord_rate3{}'.format(i))
            })

            # Calculate the sum of quantities
            total_quantity += float(quantity)
            print('total_quantity', total_quantity)

    # Update the total_quantity field of the Bindingorder object
    data.binding_order_total = total_quantity
    print("1111111111", data.binding_order_total)
    data.save()

    context = {
        'data': data,
        'order_data': order_data,
        'binding_order_total': total_quantity,
        'a': a,
    }

    return render(request, 'cover/topi_order_bill_view.html', context)






@login_required(login_url="") 
def delete_topi_order(request, id):
    cus = Topi_order.objects.get(id=id)
    cus.delete()
    sweetify.success(request, title="Success", icon='success', text='Order Deleted successfully...', timer=1500)
    return redirect('/topi_order/')





def cover_cutting(request):
    if request.method == "POST":
        cutting_plate_no = request.POST.get("cutting_plate_no")
        cutting_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        cutting_quantity = request.POST.get("cutting_quantity")
        cutting_rate = request.POST.get("cutting_rate")
        cutting_sheet_quantity = request.POST.get("cutting_sheet_quantity")
        cutting_Gruce_quantity = request.POST.get("cutting_Gruce_quantity")
        cutting_rim_quantity = request.POST.get("cutting_rim_quantity")
        cutting_vendor = request.POST.get("cutting_vendor")
        cutting_voucher_no = request.POST.get("cutting_voucher_no")

        # Calculate cutting_amount
        cutting_amount = request.POST.get("cutting_amount")
        print("11111111",cutting_amount)

        data1 = Cover_cutting(
            cutting_plate_no=cutting_plate_no,
            cutting_date=cutting_date,
            cutting_quantity=cutting_quantity,
            cutting_sheet_quantity=cutting_sheet_quantity,
            cutting_Gruce_quantity=cutting_Gruce_quantity,
            cutting_rim_quantity=cutting_rim_quantity,
            cutting_rate=cutting_rate,
            cutting_amount=cutting_amount,
            cutting_vendor=cutting_vendor,
            cutting_voucher_no=cutting_voucher_no,
        )
        data1.save()
        sweetify.success(request, " Created Successfully.", timer=6000, button='OK')

    data = Cover_cutting.objects.all().order_by('-id')
    obj3 = Cover_Printing.objects.all()
    obj = Bindingvender.objects.all()
    return render(request, 'cover/cover_cutting.html', {'data': data, 'obj3': obj3, 'obj': obj})


def delete_cover_cutting(request, id):
    cus = Cover_cutting.objects.get(id=id)
    cus.delete()
    return redirect('/cover_cutting/')


def edit_cover_cutting(request, id):
    data = Cover_cutting.objects.get(id=id)
    if request.method == 'POST':
            data.cutting_plate_no = request.POST.get('cutting_plate_no')
            data.cutting_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
            data.cutting_quantity = request.POST.get('cutting_quantity')
            data.cutting_sheet_quantity = request.POST.get('cutting_sheet_quantity')
            data.cutting_Gruce_quantity = request.POST.get('cutting_Gruce_quantity')
            data.cutting_rim_quantity = request.POST.get('cutting_rim_quantity')
            data.cutting_rate = request.POST.get('cutting_rate')
            data.cutting_amount = request.POST.get('cutting_amount')
            data.cutting_vendor = request.POST.get('cutting_vendor')
            data.cutting_voucher_no = request.POST.get('cutting_voucher_no')
            
            
            data.save()
           
            return redirect('/cover_cutting/')
    
    print("datanew", data.cutting_plate_no)
    context = {'data':data,}
    return render(request, 'cover/edit_cover_cutting.html', context)

from itertools import chain
def sale_bill(request):
    if request.method == "POST":
        material_center = request.POST.get("material_center")
        company = request.POST.get("company")
        sale_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        sale_vendor = request.POST.get("sale_vendor")
        voucher_no = request.POST.get("voucher_no")
        sale_quantity1 = request.POST.get("sale_quantity1")
        qty_per_bitti1 = request.POST.get("qty_per_bitti1")
        no_of_bitti1 = request.POST.get("no_of_bitti1")
        rate1 = request.POST.get("rate1")
        print('222222222222',rate1)
        vend_category=request.POST.get("vend_category")

        sale_amount1 = request.POST.get("sale_amount1")
        plate_no1 = request.POST.get("plate_no1")
        sale_price1 = request.POST.get("sale_price1")
        discount1 = request.POST.get("discount1")
        extra_discount1=request.POST.get("extra_discount1")

        plate_no2 = request.POST.get("plate_no2")
        sale_quantity2 = request.POST.get("sale_quantity2")
        qty_per_bitti2 = request.POST.get("qty_per_bitti2")
        no_of_bitti2 = request.POST.get("no_of_bitti2")
        rate2 = request.POST.get("rate2")
        sale_amount2 = request.POST.get("sale_amount2")
        sale_price2 = request.POST.get("sale_price2")
        discount2 = request.POST.get("discount2")
        extra_discount2=request.POST.get("extra_discount2")

        plate_no3 = request.POST.get("plate_no3")
        sale_quantity3 = request.POST.get("sale_quantity3")
        qty_per_bitti3 = request.POST.get("qty_per_bitti3")
        no_of_bitti3 = request.POST.get("no_of_bitti3")
        rate3 = request.POST.get("rate3")
        sale_amount3 = request.POST.get("sale_amount3")
        sale_price3 = request.POST.get("sale_price3")
        discount3 = request.POST.get("discount3")
        extra_discount3=request.POST.get("extra_discount3")

        plate_no4 = request.POST.get("plate_no4")
        sale_quantity4 = request.POST.get("sale_quantity4")
        qty_per_bitti4 = request.POST.get("qty_per_bitti4")
        no_of_bitti4 = request.POST.get("no_of_bitti4")
        rate4 = request.POST.get("rate4")
        sale_amount4 = request.POST.get("sale_amount4")
        sale_price4 = request.POST.get("sale_price4")
        discount4= request.POST.get("discount4")
        extra_discount4=request.POST.get("extra_discount4")

        plate_no5 = request.POST.get("plate_no5")
        sale_quantity5 = request.POST.get("sale_quantity5")
        qty_per_bitti5 = request.POST.get("qty_per_bitti5")
        no_of_bitti5 = request.POST.get("no_of_bitti5")
        rate5 = request.POST.get("rate5")
        sale_amount5 = request.POST.get("sale_amount5")
        sale_price5= request.POST.get("sale_price5")
        discount5= request.POST.get("discount5")
        extra_discount5=request.POST.get("extra_discount5")

        plate_no6 = request.POST.get("plate_no6")
        sale_quantity6 = request.POST.get("sale_quantity6")
        qty_per_bitti6 = request.POST.get("qty_per_bitti6")
        no_of_bitti6 = request.POST.get("no_of_bitti6")
        rate6 = request.POST.get("rate6")
        sale_amount6 = request.POST.get("sale_amount6")
        sale_price6= request.POST.get("sale_price6")
        discount6 = request.POST.get("discount6")
        extra_discount6=request.POST.get("extra_discount6")


        plate_no7 = request.POST.get("plate_no7")
        sale_quantity7 = request.POST.get("sale_quantity7")
        qty_per_bitti7 = request.POST.get("qty_per_bitti7")
        no_of_bitti7 = request.POST.get("no_of_bitti7")
        rate7 = request.POST.get("rate7")
        sale_amount7 = request.POST.get("sale_amount7")

        sale_price7= request.POST.get("sale_price7")
        discount7 = request.POST.get("discount7")
        extra_discount7=request.POST.get("extra_discount7")

        plate_no8 = request.POST.get("plate_no8")
        sale_quantity8 = request.POST.get("sale_quantity8")
        qty_per_bitti8 = request.POST.get("qty_per_bitti8")
        no_of_bitti8 = request.POST.get("no_of_bitti8")
        rate8 = request.POST.get("rate8")
        sale_amount8 = request.POST.get("sale_amount8")
        sale_price8= request.POST.get("sale_price8")
        discount8 = request.POST.get("discount8")
        extra_discount8=request.POST.get("extra_discount8")

        plate_no9= request.POST.get("plate_no9")
        sale_quantity9 = request.POST.get("sale_quantity9")
        qty_per_bitti9 = request.POST.get("qty_per_bitti9")
        no_of_bitti9 = request.POST.get("no_of_bitti9")
        rate9 = request.POST.get("rate9")
        sale_amount9 = request.POST.get("sale_amount9")
        sale_price9= request.POST.get("sale_price9")
        discount9 = request.POST.get("discount9")
        extra_discount9=request.POST.get("extra_discount9")

        plate_no10 = request.POST.get("plate_no10")
        sale_quantity10 = request.POST.get("sale_quantity10")
        qty_per_bitti10 = request.POST.get("qty_per_bitti10")
        no_of_bitti10 = request.POST.get("no_of_bitti10")
        rate10 = request.POST.get("rate10")
        sale_amount10 = request.POST.get("sale_amount10")
        sale_price10= request.POST.get("sale_price10")
        discount10= request.POST.get("discount10")
        extra_discount10=request.POST.get("extra_discount10")
        total_sale_amount = request.POST.get("total_sale_amount")
        bill_sundries_1 = request.POST.get("bill_sundries_1")
        narration_1= request.POST.get("narration_1")
        amount_1= request.POST.get("amount_1")
        percent_1=request.POST.get("percent_1")

        bill_sundries_2 = request.POST.get("bill_sundries_2")
        narration_2= request.POST.get("narration_2")
        amount_2= request.POST.get("amount_2")
        percent_2=request.POST.get("percent_2")

        bill_sundries_3 = request.POST.get("bill_sundries_3")
        narration_3= request.POST.get("narration_3")
        amount_3= request.POST.get("amount_3")
        percent_3=request.POST.get("percent_3")

        bill_sundries_4 = request.POST.get("bill_sundries_4")
        narration_4= request.POST.get("narration_4")
        amount_4= request.POST.get("amount_4")
        percent_4=request.POST.get("percent_4")

        bill_sundries_5 = request.POST.get("bill_sundries_5")
        narration_5= request.POST.get("narration_5")
        amount_5= request.POST.get("amount_5")
        percent_5=request.POST.get("percent_5")
        total_amount = request.POST.get("total_amount")
        print("ssssssssssssssssssssssss",total_amount)

        print("23",15555555)
        category1 = request.POST.get("category1")
        category2 = request.POST.get("category2")
        category3 = request.POST.get("category3")
        category4 = request.POST.get("category4")
        category5 = request.POST.get("category5")
        category6 = request.POST.get("category6")
        category7 = request.POST.get("category7")
        category8 = request.POST.get("category8")
        category9 = request.POST.get("category9")
        category10 = request.POST.get("category10")
        subject1 = request.POST.get("subject1")
        subject2 = request.POST.get("subject2")
        subject3 = request.POST.get("subject3")
        subject4 = request.POST.get("subject4")
        subject5 = request.POST.get("subject5")
        subject6 = request.POST.get("subject6")
        subject7 = request.POST.get("subject7")
        subject8 = request.POST.get("subject8")
        subject9 = request.POST.get("subject9")
        subject10 = request.POST.get("subject10")

        brand_name1 = request.POST.get("brand_name1")
        brand_name2= request.POST.get("brand_name2")
        brand_name3 = request.POST.get("brand_name3")
        brand_name4 = request.POST.get("brand_name4")
        brand_name5 = request.POST.get("brand_name5")
        brand_name6 = request.POST.get("brand_name6")
        brand_name7 = request.POST.get("brand_name7")
        brand_name8 = request.POST.get("brand_name8")
        brand_name9 = request.POST.get("brand_name9")
        brand_name10 = request.POST.get("brand_name10")
        
        

        # Calculate cutting_amount
        quantities = []
        rates = []
        total_sale_amount = 0
        # Loop through the range 1 to 11 to get quantities and rates
        for i in range(1, 11):
            quantity_field = f"sale_quantity{i}"
            rate_field = f"rate{i}"
            sale_amount_field = f"sale_amount{i}"

            quantity = request.POST.get(quantity_field)
            rate = request.POST.get(rate_field)
            sale_amount = request.POST.get(sale_amount_field)

            # Check if either quantity or rate is not empty before calculating amount
            if quantity and rate:
                quantities.append(float(quantity))
                rates.append(float(rate))
                if sale_amount:
                    total_sale_amount += float(sale_amount)

        print("Total Sale Amount:", total_sale_amount)
        # Calculate the corresponding amounts
        amounts = [quantity * rate for quantity, rate in zip(quantities, rates)]
        print("1234444444",amounts)
       
            # field_values[f"sundries_operation{i}"] = request.POST.get(f"operation_{i}")
            # # sale_bill_obj = SaleBill(**field_values)


        # Create a dictionary to map fields and values for the Topi_order model
        field_values = {
            "sale_vendor": sale_vendor,
            "sale_date": sale_date,
        }

        for i in range(1, 11):
            field_values[f"sale_quantity{i}"] = request.POST.get(f"sale_quantity{i}")
            field_values[f"rate{i}"] = request.POST.get(f"rate{i}")
            field_values[f"sale_amount{i}"] = amounts[i - 1] if i <= len(amounts) else None
            print("1111111111",field_values[f"sale_amount{i}"])
        for i in range(1, 5):
            field_values[f"bill_sundries_{i}"] = request.POST.get(f"bill_sundries_{i}")
            field_values[f"narration_{i}"] = request.POST.get(f"narration_{i}")
            field_values[f"amount_{i}"] = request.POST.get(f"amount_{i}")
            print("666666666", field_values[f"narration_{i}"])

        data1 = Sale_bill(
            material_center=material_center,
            company=company,
            sale_date=sale_date,
            sale_vendor=sale_vendor,
            plate_no1=plate_no1,
            sale_quantity1=sale_quantity1,
            qty_per_bitti1=qty_per_bitti1,
            no_of_bitti1=no_of_bitti1,
            rate1=rate1,
            sale_amount1=sale_amount1,
            sale_price1=sale_price1,
            extra_discount1=extra_discount1,
            discount1=discount1,
            voucher_no=voucher_no,
            vend_category=vend_category,
            
            
            sale_quantity2=sale_quantity2,
            qty_per_bitti2=qty_per_bitti2,
            no_of_bitti2=no_of_bitti2,
            rate2=rate2,
            sale_amount2=sale_amount2,
            plate_no2=plate_no2,
            sale_price2=sale_price2,
            extra_discount2=extra_discount2,
            discount2=discount2,

            sale_quantity3=sale_quantity3,
            qty_per_bitti3=qty_per_bitti3,
            no_of_bitti3=no_of_bitti3,
            rate3=rate3,
            sale_amount3=sale_amount3,
            plate_no3=plate_no3,
            sale_price3=sale_price3,
            extra_discount3=extra_discount3,
            discount3=discount3,

            sale_quantity4=sale_quantity4,
            qty_per_bitti4=qty_per_bitti4,
            no_of_bitti4=no_of_bitti4,
            rate4=rate4,
            sale_amount4=sale_amount4,
            plate_no4=plate_no4,
            sale_price4=sale_price4,
            extra_discount4=extra_discount4,
            discount4=discount4,


            sale_quantity5=sale_quantity5,
            qty_per_bitti5=qty_per_bitti5,
            no_of_bitti5=no_of_bitti5,
            rate5=rate5,
            sale_amount5=sale_amount5,
            plate_no5=plate_no5,
            sale_price5=sale_price5,
            extra_discount5=extra_discount5,
            discount5=discount5,


            sale_quantity6=sale_quantity6,
            qty_per_bitti6=qty_per_bitti6,
            no_of_bitti6=no_of_bitti6,
            rate6=rate6,
            sale_amount6=sale_amount6,
            plate_no6=plate_no6,
            sale_price6=sale_price6,
            extra_discount6=extra_discount6,
            discount6=discount6,


            sale_quantity7=sale_quantity7,
            qty_per_bitti7=qty_per_bitti7,
            no_of_bitti7=no_of_bitti7,
            rate7=rate7,
            sale_amount7=sale_amount7,
            plate_no7=plate_no7,
            sale_price7=sale_price7,
            extra_discount7=extra_discount7,
            discount7=discount7,

            sale_quantity8=sale_quantity8,
            qty_per_bitti8=qty_per_bitti8,
            no_of_bitti8=no_of_bitti8,
            rate8=rate8,
            sale_amount8=sale_amount8,
            plate_no8=plate_no8,
            sale_price8=sale_price8,
            extra_discount8=extra_discount8,
            discount8=discount8,

            sale_quantity9=sale_quantity9,
            qty_per_bitti9=qty_per_bitti9,
            no_of_bitti9=no_of_bitti9,
            rate9=rate9,
            sale_amount9=sale_amount9,
            plate_no9=plate_no9,
            sale_price9=sale_price9,
            extra_discount9=extra_discount9,
            discount9=discount9,

            sale_quantity10=sale_quantity10,
            qty_per_bitti10=qty_per_bitti10,
            no_of_bitti10=no_of_bitti10,
            rate10=rate10,
            sale_amount10=sale_amount10,
            plate_no10=plate_no10,
            sale_price10=sale_price10,
            extra_discount10=extra_discount10,
            discount10=discount10,
            total_sale_amount=total_sale_amount,
            total_amount=total_amount,

            bill_sundries_1=bill_sundries_1,
            narration_1=narration_1,
            amount_1=amount_1,
            percent_1=percent_1,


            bill_sundries_2=bill_sundries_2,
            narration_2=narration_2,
            amount_2=amount_2,
            percent_2=percent_2,


            bill_sundries_3=bill_sundries_3,
            narration_3=narration_3,
            amount_3=amount_3,
            percent_3=percent_3,


            bill_sundries_4=bill_sundries_4,
            narration_4=narration_4,
            amount_4=amount_4,
            percent_4=percent_4,


            bill_sundries_5=bill_sundries_5,
            narration_5=narration_5,
            amount_5=amount_5,
            percent_5=percent_5,
            category1=category1,
            category2=category2,
            category3=category3,
            category4=category4,
            category5=category5,
            category6=category6,
            category7=category7,
            category8=category8,
            category9=category9,
            category10=category10,
            subject1 = subject1,
            subject2 = subject2,
            subject3 = subject3,
            subject4 = subject4,
            subject5 = subject5,
            subject6 = subject6,
            subject7 = subject7,
            subject8 = subject8,
            subject9 = subject9,
            subject10 = subject10,

            brand_name1 = brand_name1,
            brand_name2 = brand_name2,
            brand_name3 = brand_name3,
            brand_name4 = brand_name4,
            brand_name5 = brand_name5,
            brand_name6 = brand_name6,
            brand_name7 = brand_name7,
            brand_name8 = brand_name8,
            brand_name9 = brand_name9,
            brand_name10 = brand_name10,





           

            
        )
        data1.save()
        sweetify.success(request, " Created Successfully.", timer=6000, button='OK')

    data = Sale_bill.objects.all().order_by('-id')
    comp = Company.objects.all()
    vend = Customer_ledger.objects.all()
    data10 = Customer_ledger.objects.all()
    data3 = Subbrand.objects.all()
    
    data_combined = list(chain(books.objects.all(), data3))

    result_data = []
    data4 = books.objects.all()
    combined_data = []

    for subbrand in data3:
        matching_books = books.objects.filter(books_name=subbrand.brand_combine)
        matching_categories = Customer_ledger.objects.filter(price_category__in=[
            subbrand.category_1, subbrand.category_2, subbrand.category_3,
            subbrand.category_4, subbrand.category_5, subbrand.category_6,
            subbrand.category_7, subbrand.category_8, subbrand.category_9,
            subbrand.category_10
        ])
        # for i in matching_categories:

        print("111111",matching_categories)

        for book in matching_books:
            for category in matching_categories:
                if book.books_name == subbrand.brand_combine and category.price_category in [
                    subbrand.category_1, subbrand.category_2, subbrand.category_3,
                    subbrand.category_4, subbrand.category_5, subbrand.category_6,
                    subbrand.category_7, subbrand.category_8, subbrand.category_9,
                    subbrand.category_10
                ]:
                    combined_data.append({
                        'subbrand_value': subbrand.brand_combine,
                        'book_name': book.books_name,
                        'code': book.code,
                        'subject': book.subject,
                        "bitti_pack_size": book.bitti_pack_size,
                        "selling_price": book.selling_price,
                        'cust_name': category.cust_name,
                        'price_category': category.price_category,  # Replace with actual selling_price from Customer_ledger
                        'category': subbrand.category_1,
                        'main_discount': subbrand.mainDiscount_1,
                        'extra_discount': subbrand.extraDiscount_1,
                        'category_1': subbrand.category_2,
                        'main_discount_1': subbrand.mainDiscount_2,
                        'extra_discount_1': subbrand.extraDiscount_2,
                        'category_2': subbrand.category_3,
                        'main_discount_2': subbrand.mainDiscount_3,
                        'extra_discount_2': subbrand.extraDiscount_3,
                        'category_3': subbrand.category_4,
                        'main_discount_3': subbrand.mainDiscount_4,
                        'extra_discount_3': subbrand.extraDiscount_4,
                        'category_4': subbrand.category_5,
                        'main_discount_4': subbrand.mainDiscount_5,
                        'extra_discount_4': subbrand.extraDiscount_5,
                        'category_5': subbrand.category_6,
                        'main_discount_5': subbrand.mainDiscount_6,
                        'extra_discount_5': subbrand.extraDiscount_6,
                        'category_6': subbrand.category_7,
                        'main_discount_6': subbrand.mainDiscount_7,
                        'extra_discount_6': subbrand.extraDiscount_7,
                        'category_7': subbrand.category_8,
                        'main_discount_7': subbrand.mainDiscount_8,
                        'extra_discount_7': subbrand.extraDiscount_8,
                        'category_8': subbrand.category_9,
                        'main_discount_8': subbrand.mainDiscount_9,
                        'extra_discount_8': subbrand.extraDiscount_9,
                        'category_9': subbrand.category_10,
                        'main_discount_9': subbrand.mainDiscount_10,
                        'extra_discount_9': subbrand.extraDiscount_10,
                    })

    print("8888888", combined_data)


    
    

    
    data4=material_centre.objects.all()
    return render(request, 'cover/sale_bill.html', {'data4':data4,'data': data,'comp':comp,'data3':data3,'vend':vend, 'data_combined': data_combined, 'data10':data10, "combined_data": combined_data })


def sale_bill_view(request, id):
    data = Sale_bill.objects.get(id=id)
    print('data', data)
    a = float(data.sale_amount1) if data.sale_amount1 else 0.0
    print('a', a)
    b = str(data.plate_no1) if data.plate_no1 else 0.0
    print("b", b)

    # Define the maximum number of orders
    max_orders = 50  # Maximum number of orders to consider

    order_data = []
    total_quantity = 0

    for i in range(1, max_orders + 1):
        quantity_field = 'sale_amount{}'.format(i)
        quantity = getattr(data, quantity_field, None)

        if quantity:
            order_data.append({
                'medium': request.POST.get('midium_{}'.format(i)),
                'subject': request.POST.get('bsubject_{}'.format(i)),
                'quantity': float(quantity),
                'rate': request.POST.get('rate{}'.format(i))
            })

            # Calculate the sum of quantities
            total_quantity += float(quantity)
            print('total_quantity', total_quantity)

    # Update the total_quantity field of the Bindingorder object
    data.binding_order_total = total_quantity
    print("1111111111", data.binding_order_total)
    data.save()

    context = {
        'data': data,
        'order_data': order_data,
        'binding_order_total': total_quantity,
        'a': a,
    }

    return render(request, 'cover/sale_bill_view.html', context)



def delete_sale_bill(request, id):
    cus = Sale_bill.objects.get(id=id)
    cus.delete()
    return redirect('/sale_bill/')



def sale_return(request):
  if request.method=="POST":
    
        r_company = request.POST.get("r_company")
        vend_category = request.POST.get("vend_category")
        r_sale_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        r_sale_vendor = request.POST.get("r_sale_vendor")
        r_voucher_no = request.POST.get("r_voucher_no")
        r_sale_quantity1 = request.POST.get("r_sale_quantity1")
        r_qty_per_bitti1 = request.POST.get("r_qty_per_bitti1")
        r_no_of_bitti1 = request.POST.get("r_no_of_bitti1")
        r_rate1 = request.POST.get("r_rate1")
        print('222222222222',r_rate1)
        r_sale_amount1 = request.POST.get("r_sale_amount1")
        r_plate_no1 = request.POST.get("r_plate_no1")

        r_plate_no2 = request.POST.get("r_plate_no2")
        r_sale_quantity2 = request.POST.get("r_sale_quantity2")
        r_qty_per_bitti2 = request.POST.get("r_qty_per_bitti2")
        r_no_of_bitti2 = request.POST.get("r_no_of_bitti2")
        r_rate2 = request.POST.get("r_rate2")
        r_sale_amount2 = request.POST.get("r_sale_amount2")

        r_plate_no3 = request.POST.get("r_plate_no3")
        r_sale_quantity3 = request.POST.get("r_sale_quantity3")
        r_qty_per_bitti3 = request.POST.get("r_qty_per_bitti3")
        r_no_of_bitti3 = request.POST.get("r_no_of_bitti3")
        r_rate3 = request.POST.get("r_rate3")
        r_sale_amount3 = request.POST.get("r_sale_amount3")

        r_plate_no4 = request.POST.get("r_plate_no4")
        r_sale_quantity4 = request.POST.get("r_sale_quantity4")
        r_qty_per_bitti4 = request.POST.get("r_qty_per_bitti4")
        r_no_of_bitti4 = request.POST.get("r_no_of_bitti4")
        r_rate4 = request.POST.get("r_rate4")
        r_sale_amount4 = request.POST.get("r_sale_amount4")

        r_plate_no5 = request.POST.get("r_plate_no5")
        r_sale_quantity5 = request.POST.get("r_sale_quantity5")
        r_qty_per_bitti5 = request.POST.get("r_qty_per_bitti5")
        r_no_of_bitti5 = request.POST.get("r_no_of_bitti5")
        r_rate5 = request.POST.get("r_rate5")
        r_sale_amount5 = request.POST.get("r_sale_amount5")

        r_plate_no6 = request.POST.get("r_plate_no6")
        r_sale_quantity6 = request.POST.get("r_sale_quantity6")
        r_qty_per_bitti6 = request.POST.get("r_qty_per_bitti6")
        r_no_of_bitti6 = request.POST.get("r_no_of_bitti6")
        r_rate6 = request.POST.get("r_rate6")
        r_sale_amount6 = request.POST.get("r_sale_amount6")


        r_plate_no7 = request.POST.get("r_plate_no7")
        r_sale_quantity7 = request.POST.get("r_sale_quantity7")
        r_qty_per_bitti7 = request.POST.get("r_qty_per_bitti7")
        r_no_of_bitti7 = request.POST.get("r_no_of_bitti7")
        r_rate7 = request.POST.get("r_rate7")
        r_sale_amount7 = request.POST.get("r_sale_amount7")

        r_plate_no8 = request.POST.get("r_plate_no8")
        r_sale_quantity8 = request.POST.get("r_sale_quantity8")
        r_qty_per_bitti8 = request.POST.get("r_qty_per_bitti8")
        r_no_of_bitti8 = request.POST.get("r_no_of_bitti8")
        r_rate8 = request.POST.get("r_rate8")
        r_sale_amount8 = request.POST.get("r_sale_amount8")

        r_plate_no9= request.POST.get("r_plate_no9")
        r_sale_quantity9 = request.POST.get("r_sale_quantity9")
        r_qty_per_bitti9 = request.POST.get("r_qty_per_bitti9")
        r_no_of_bitti9 = request.POST.get("r_no_of_bitti9")
        r_rate9 = request.POST.get("r_rate9")
        r_sale_amount9 = request.POST.get("r_sale_amount9")

        r_plate_no10 = request.POST.get("r_plate_no10")
        r_sale_quantity10 = request.POST.get("r_sale_quantity10")
        r_qty_per_bitti10 = request.POST.get("r_qty_per_bitti10")
        r_no_of_bitti10 = request.POST.get("r_no_of_bitti10")
        r_rate10 = request.POST.get("r_rate10")
        r_sale_amount10 = request.POST.get("r_sale_amount10")
        r_total_sale_amount = request.POST.get("r_total_sale_amount")

        category1 = request.POST.get("category1")
        category2 = request.POST.get("category2")
        category3 = request.POST.get("category3")
        category4 = request.POST.get("category4")
        category5 = request.POST.get("category5")
        category6 = request.POST.get("category6")
        category7 = request.POST.get("category7")
        category8 = request.POST.get("category8")
        category9 = request.POST.get("category9")
        category10 = request.POST.get("category10")

        subject1 = request.POST.get("subject1")
        subject2 = request.POST.get("subject2")
        subject3 = request.POST.get("subject3")
        subject4 = request.POST.get("subject4")
        subject5 = request.POST.get("subject5")
        subject6 = request.POST.get("subject6")
        subject7 = request.POST.get("subject7")
        subject8 = request.POST.get("subject8")
        subject9 = request.POST.get("subject9")
        subject10 = request.POST.get("subject10")

        brand_name1 = request.POST.get("brand_name1")
        brand_name2= request.POST.get("brand_name2")
        brand_name3 = request.POST.get("brand_name3")
        brand_name4 = request.POST.get("brand_name4")
        brand_name5 = request.POST.get("brand_name5")
        brand_name6 = request.POST.get("brand_name6")
        brand_name7 = request.POST.get("brand_name7")
        brand_name8 = request.POST.get("brand_name8")
        brand_name9 = request.POST.get("brand_name9")
        brand_name10 = request.POST.get("brand_name10")


        sale_price1= request.POST.get("sale_price1")
        discount1 = request.POST.get("discount1")
        extra_discount1= request.POST.get("extra_discount1")

        sale_price2= request.POST.get("sale_price2")
        discount2 = request.POST.get("discount2")
        extra_discount2= request.POST.get("extra_discount2")

        sale_price3= request.POST.get("sale_price3")
        discount3 = request.POST.get("discount3")
        extra_discount3= request.POST.get("extra_discount3")

        sale_price4= request.POST.get("sale_price4")
        discount4 = request.POST.get("discount4")
        extra_discount4= request.POST.get("extra_discount4")

        sale_price5= request.POST.get("sale_price5")
        discount5 = request.POST.get("discount5")
        extra_discount5= request.POST.get("extra_discount5")

        sale_price6= request.POST.get("sale_price6")
        discount6= request.POST.get("discount6")
        extra_discount6= request.POST.get("extra_discount6")

        sale_price7= request.POST.get("sale_price7")
        discount7 = request.POST.get("discount7")
        extra_discount7= request.POST.get("extra_discount7")

        sale_price8= request.POST.get("sale_price8")
        discount8 = request.POST.get("discount8")
        extra_discount8= request.POST.get("extra_discount8")

        sale_price9= request.POST.get("sale_price9")
        discount9 = request.POST.get("discount9")
        extra_discount9= request.POST.get("extra_discount9")

        sale_price10 = request.POST.get("sale_price10")
        discount10 = request.POST.get("discount10")
        extra_discount10= request.POST.get("extra_discount10")
        
        

        # Calculate cutting_amount
        quantities = []
        rates = []
        r_total_sale_amount = 0
        # Loop through the range 1 to 11 to get quantities and rates
        for i in range(1, 11):
            quantity_field = f"r_sale_quantity{i}"
            rate_field = f"r_rate{i}"
            sale_amount_field = f"r_sale_amount{i}"

            quantity = request.POST.get(quantity_field)
            rate = request.POST.get(rate_field)
            sale_amount = request.POST.get(sale_amount_field)

            # Check if either quantity or rate is not empty before calculating amount
            if quantity and rate:
                quantities.append(float(quantity))
                rates.append(float(rate))
                if sale_amount:
                    r_total_sale_amount += float(sale_amount)

        print("Total Sale Amount:", r_total_sale_amount)
        # Calculate the corresponding amounts
        amounts = [quantity * rate for quantity, rate in zip(quantities, rates)]
        print("1234444444",amounts)

        # Create a dictionary to map fields and values for the Topi_order model
        field_values = {
            "r_sale_vendor": r_sale_vendor,
            "r_sale_date": r_sale_date,
        }

        for i in range(1, 11):
            field_values[f"r_sale_quantity{i}"] = request.POST.get(f"r_sale_quantity{i}")
            field_values[f"r_rate{i}"] = request.POST.get(f"r_rate{i}")
            field_values[f"r_sale_amount{i}"] = amounts[i - 1] if i <= len(amounts) else None
            print("1111111111",field_values[f"r_sale_amount{i}"])
            

        data1 = Sale_return(
            r_company=r_company,
            r_sale_date=r_sale_date,
            r_sale_vendor=r_sale_vendor,
            r_plate_no1=r_plate_no1,
            r_sale_quantity1=r_sale_quantity1,
            r_qty_per_bitti1=r_qty_per_bitti1,
            r_no_of_bitti1=r_no_of_bitti1,
            r_rate1=r_rate1,
            r_sale_amount1=r_sale_amount1,
            r_voucher_no=r_voucher_no,
            
            
            r_sale_quantity2=r_sale_quantity2,
            r_qty_per_bitti2=r_qty_per_bitti2,
            r_no_of_bitti2=r_no_of_bitti2,
            r_rate2=r_rate2,
            r_sale_amount2=r_sale_amount2,
            r_plate_no2=r_plate_no2,

            r_sale_quantity3=r_sale_quantity3,
            r_qty_per_bitti3=r_qty_per_bitti3,
            r_no_of_bitti3=r_no_of_bitti3,
            r_rate3=r_rate3,
            r_sale_amount3=r_sale_amount3,
            r_plate_no3=r_plate_no3,

            r_sale_quantity4=r_sale_quantity4,
            r_qty_per_bitti4=r_qty_per_bitti4,
            r_no_of_bitti4=r_no_of_bitti4,
            r_rate4=r_rate4,
            r_sale_amount4=r_sale_amount4,
            r_plate_no4=r_plate_no4,

            r_sale_quantity5=r_sale_quantity5,
            r_qty_per_bitti5=r_qty_per_bitti5,
            r_no_of_bitti5=r_no_of_bitti5,
            r_rate5=r_rate5,
            r_sale_amount5=r_sale_amount5,
            r_plate_no5=r_plate_no5,


            r_sale_quantity6=r_sale_quantity6,
            r_qty_per_bitti6=r_qty_per_bitti6,
            r_no_of_bitti6=r_no_of_bitti6,
            r_rate6=r_rate6,
            r_sale_amount6=r_sale_amount6,
            r_plate_no6=r_plate_no6,


            r_sale_quantity7=r_sale_quantity7,
            r_qty_per_bitti7=r_qty_per_bitti7,
            r_no_of_bitti7=r_no_of_bitti7,
            r_rate7=r_rate7,
            r_sale_amount7=r_sale_amount7,
            r_plate_no7=r_plate_no7,

            r_sale_quantity8=r_sale_quantity8,
            r_qty_per_bitti8=r_qty_per_bitti8,
            r_no_of_bitti8=r_no_of_bitti8,
            r_rate8=r_rate8,
            r_sale_amount8=r_sale_amount8,
            r_plate_no8=r_plate_no8,

            r_sale_quantity9=r_sale_quantity9,
            r_qty_per_bitti9=r_qty_per_bitti9,
            r_no_of_bitti9=r_no_of_bitti9,
            r_rate9=r_rate9,
            r_sale_amount9=r_sale_amount9,
            r_plate_no9=r_plate_no9,

            r_sale_quantity10=r_sale_quantity10,
            r_qty_per_bitti10=r_qty_per_bitti10,
            r_no_of_bitti10=r_no_of_bitti10,
            r_rate10=r_rate10,
            r_sale_amount10=r_sale_amount10,
            r_plate_no10=r_plate_no10,
            r_total_sale_amount=r_total_sale_amount,

            category1 = category1,
            category2 = category2,
            category3 = category3,
            category4 = category4,
            category5 = category5,
            category6 = category6,
            category7 = category7,
            category8 = category8,
            category9 = category9,
            category10 = category10,

            subject1 = subject1,
            subject2 = subject2,
            subject3 = subject3,
            subject4 = subject4,
            subject5 = subject5,
            subject6 = subject6,
            subject7 = subject7,
            subject8 = subject8,
            subject9 = subject9,
            subject10 = subject10,

            brand_name1 = brand_name1,
            brand_name2 = brand_name2,
            brand_name3 = brand_name3,
            brand_name4 = brand_name4,
            brand_name5 = brand_name5,
            brand_name6 = brand_name6,
            brand_name7 = brand_name7,
            brand_name8 = brand_name8,
            brand_name9 = brand_name9,
            brand_name10 = brand_name10,

            sale_price1= sale_price1,
            discount1 = discount1,
            extra_discount1= extra_discount1,

            sale_price2= sale_price2,
            discount2 = discount2,
            extra_discount2= extra_discount2,

            sale_price3= sale_price3,
            discount3 = discount3,
            extra_discount3= extra_discount3,

            sale_price4= sale_price4,
            discount4 = discount4,
            extra_discount4= extra_discount4,

            sale_price5= sale_price5,
            discount5 = discount5,
            extra_discount5= extra_discount5,

            sale_price6= sale_price6,
            discount6 = discount6,
            extra_discount6= extra_discount6,

            sale_price7= sale_price7,
            discount7 = discount7,
            extra_discount7= extra_discount7,

            sale_price8= sale_price8,
            discount8 = discount8,
            extra_discount8= extra_discount8,

            sale_price9= sale_price9,
            discount9 = discount9,
            extra_discount9= extra_discount9,

            sale_price10= sale_price10,
            discount10 = discount10,
            extra_discount10= extra_discount10,
            vend_category=vend_category,



            
        )
        data1.save()
        sweetify.success(request, " Created Successfully.", timer=6000, button='OK')

  data2 = Sale_return.objects.all().order_by('-id')
  
  comp = Company.objects.all()
  vend= Customer_ledger.objects.all()
  obj3=books.objects.all()
  data4=material_centre.objects.all()

  data3 = Subbrand.objects.all()

  combined_data = []

  for subbrand in data3:
    matching_books = books.objects.filter(books_name=subbrand.brand_combine)
    matching_categories = Customer_ledger.objects.filter(price_category__in=[
        subbrand.category_1, subbrand.category_2, subbrand.category_3,
        subbrand.category_4, subbrand.category_5, subbrand.category_6,
        subbrand.category_7, subbrand.category_8, subbrand.category_9,
        subbrand.category_10
    ])
    # for i in matching_categories:

    print("111111",matching_categories)

    for book in matching_books:
        for category in matching_categories:
            if book.books_name == subbrand.brand_combine and category.price_category in [
                subbrand.category_1, subbrand.category_2, subbrand.category_3,
                subbrand.category_4, subbrand.category_5, subbrand.category_6,
                subbrand.category_7, subbrand.category_8, subbrand.category_9,
                subbrand.category_10
            ]:
                combined_data.append({
                    'subbrand_value': subbrand.brand_combine,
                    'book_name': book.books_name,
                    'code': book.code,
                    'subject': book.subject,
                    "bitti_pack_size": book.bitti_pack_size,
                    "selling_price": book.selling_price,
                    'cust_name': category.cust_name,
                    'price_category': category.price_category,  # Replace with actual selling_price from Customer_ledger
                    'category': subbrand.category_1,
                    'main_discount': subbrand.mainDiscount_1,
                    'extra_discount': subbrand.extraDiscount_1,
                    'category_1': subbrand.category_2,
                    'main_discount_1': subbrand.mainDiscount_2,
                    'extra_discount_1': subbrand.extraDiscount_2,
                    'category_2': subbrand.category_3,
                    'main_discount_2': subbrand.mainDiscount_3,
                    'extra_discount_2': subbrand.extraDiscount_3,
                    'category_3': subbrand.category_4,
                    'main_discount_3': subbrand.mainDiscount_4,
                    'extra_discount_3': subbrand.extraDiscount_4,
                    'category_4': subbrand.category_5,
                    'main_discount_4': subbrand.mainDiscount_5,
                    'extra_discount_4': subbrand.extraDiscount_5,
                    'category_5': subbrand.category_6,
                    'main_discount_5': subbrand.mainDiscount_6,
                    'extra_discount_5': subbrand.extraDiscount_6,
                    'category_6': subbrand.category_7,
                    'main_discount_6': subbrand.mainDiscount_7,
                    'extra_discount_6': subbrand.extraDiscount_7,
                    'category_7': subbrand.category_8,
                    'main_discount_7': subbrand.mainDiscount_8,
                    'extra_discount_7': subbrand.extraDiscount_8,
                    'category_8': subbrand.category_9,
                    'main_discount_8': subbrand.mainDiscount_9,
                    'extra_discount_8': subbrand.extraDiscount_9,
                    'category_9': subbrand.category_10,
                    'main_discount_9': subbrand.mainDiscount_10,
                    'extra_discount_9': subbrand.extraDiscount_10,
                })

    print("8888888", combined_data)


  return render(request, 'cover/sale_return.html', {'combined_data':combined_data,'data2': data2,'comp':comp,"vend":vend,"obj3":obj3,'data4':data4})


def delete_sale_return(request, id):
    cus = Sale_return.objects.get(id=id)
    cus.delete()
    return redirect('/sale_return/')



def sale_return_view(request, id):
    data = Sale_return.objects.get(id=id)
    print('data', data)
    a = float(data.r_sale_amount1) if data.r_sale_amount1 else 0.0
    print('a', a)
    b = str(data.r_plate_no1) if data.r_plate_no1 else 0.0
    print("b", b)

    # Define the maximum number of orders
    max_orders = 50  # Maximum number of orders to consider

    order_data = []
    total_quantity = 0

    for i in range(1, max_orders + 1):
        quantity_field = 'r_sale_amount{}'.format(i)
        quantity = getattr(data, quantity_field, None)

        if quantity:
            order_data.append({
                'medium': request.POST.get('midium_{}'.format(i)),
                'subject': request.POST.get('bsubject_{}'.format(i)),
                'quantity': float(quantity),
                'r_rate': request.POST.get('r_rate{}'.format(i))
            })

            # Calculate the sum of quantities
            total_quantity += float(quantity)
            print('total_quantity', total_quantity)

    # Update the total_quantity field of the Bindingorder object
    data.binding_order_total = total_quantity
    print("1111111111", data.binding_order_total)
    data.save()

    context = {
        'data': data,
        'order_data': order_data,
        'binding_order_total': total_quantity,
        'a': a,
    }

    return render(request, 'cover/sale_return_view.html', context)



def cost_production(request):
    if request.method == "POST":
        sale = int(request.POST.get("sale", 0))
        production_date= datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        closing_stock = int(request.POST.get("closing_stock", 0))
        total = request.POST.get("total")
        opening_stock = int(request.POST.get("opening_stock", 0))
        total_production = request.POST.get("total_production")
        

        # Calculate cutting_amount
        total = sale + closing_stock
        print("11111111",total)
        total_production= total - opening_stock
        print("11111111",total_production)

        data1 = Cost_production(
            sale=sale,
            closing_stock=closing_stock,
            total=total,
            opening_stock=opening_stock,
            total_production=total_production,
            production_date=production_date,
            
        )
        data1.save()
        sweetify.success(request, " Created Successfully.", timer=6000, button='OK')

    data1 = Cost_production.objects.all().order_by('-id')
    obj3 = Cover_Printing.objects.all()
    obj = Covervender.objects.all()
    return render(request, 'cover/cost_production.html', {'data1': data1, 'obj3': obj3, 'obj': obj})


def edit_cost_production(request, id):
    data = Cost_production.objects.get(id=id)
    if request.method == 'POST':
            data.sale = int(request.POST.get('sale',0))
            data.production_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
            data.closing_stock = int(request.POST.get('closing_stock',0))
            data.total = float(request.POST.get('total',0))
            data.opening_stock = int(request.POST.get('opening_stock',0))
            data.total_production =float( request.POST.get('total_production',0))
            
            data.total = data.sale + data.closing_stock
            print("11111111",data.total)
            data.total_production= data.total - data.opening_stock
            print("11111111",data.total_production)
            data.save()
           
            return redirect('/cost_production/')

    
    print("datanew", data.sale)
    context = {'data':data,}
    return render(request, 'cover/edit_cost_production.html', context)

def delete_cost_production(request, id):
    cus = Cost_production.objects.get(id=id)
    cus.delete()
    return redirect('/cost_production/')



def sale_type(request):
    if request.method == "POST":
        
        sale_type = request.POST.get("sale_type")
        t_sale_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        sale_account = request.POST.get("sale_account")
        taxation_type = request.POST.get("taxation_type")
        tax_invoice = request.POST.get("tax_invoice")


        specify_here = request.POST.get("specify_here")
        specify_voucher = request.POST.get("specify_voucher")
        taxable_voucher = request.POST.get("taxable_voucher")
        t_exempt = request.POST.get("t_exempt")
        taxable_item = request.POST.get("taxable_item")
        reverse_charge = request.POST.get("reverse_charge")
        non_gst = request.POST.get("non_gst")
        zero_rated = request.POST.get("zero_rated")
        nil_rated = request.POST.get("nil_rated")
        local = request.POST.get("local")
        central = request.POST.get("central")
        others = request.POST.get("others")
        deemed_export = request.POST.get("deemed_export")
        multi_rate = request.POST.get("multi_rate")
        single_tax = request.POST.get("single_tax")
        stock_transfer= request.POST.get("stock_transfer")
        
        

        
        data1 = Sale_type(
            sale_type=sale_type,
            t_sale_date=t_sale_date,
            sale_account=sale_account,
            taxation_type=taxation_type,
            tax_invoice=tax_invoice,
            specify_here=specify_here,
            specify_voucher=specify_voucher,
            taxable_voucher=taxable_voucher,
            t_exempt=t_exempt,
            taxable_item=taxable_item,
            reverse_charge=reverse_charge,
            non_gst=non_gst,
            zero_rated=zero_rated,
            nil_rated=nil_rated,
            local=local,
            central=central,
            stock_transfer=stock_transfer,
            others=others,
            deemed_export=deemed_export,
            multi_rate=multi_rate,
            single_tax=single_tax,
            
            
        )
        data1.save()
        sweetify.success(request, " Created Successfully.", timer=6000, button='OK')

    data = Sale_type.objects.all().order_by('-id')
    comp = Company.objects.all()
    vend= Covervender.objects.all()
    obj3=Topi.objects.all()
    return render(request, 'cover/sale_type.html', {'data': data,'comp':comp,'obj3':obj3,'vend':vend })




def purchase_type(request):
    if request.method == "POST":
        
        material_center = request.POST.get("material_center")
        name = request.POST.get("name")
        p_sale_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        alias = request.POST.get("alias")
        print_name = request.POST.get("print_name")
        default_value = request.POST.get("default_value")


        sub_total_heading = request.POST.get("sub_total_heading")
        bill_sundry_nature = request.POST.get("bill_sundry_nature")
        affected_good = request.POST.get("affected_good")
        adjust_amount = request.POST.get("adjust_amount")
        account_past = request.POST.get("account_past")
        affected_good_purchase = request.POST.get("affected_good_purchase")
        adjust_purchase_account = request.POST.get("adjust_purchase_account")
        account_heat = request.POST.get("account_heat")
        affected_material_issue = request.POST.get("affected_material_issue")
        affected_material_receipt = request.POST.get("affected_material_receipt")
        affected_stock_transfer = request.POST.get("affected_stock_transfer")
        p_specify_here = request.POST.get("p_specify_here")
        p_taxable_voucher = request.POST.get("p_taxable_voucher")
        p_local = request.POST.get("p_local")
        p_stock_transfer = request.POST.get("p_stock_transfer")
        p_single_tax= request.POST.get("p_single_tax")
        
        

        
        data1 = Purchase_type(
            material_center=material_center,
            name=name,
            p_sale_date=p_sale_date,
            alias=alias,
            print_name=print_name,
            default_value=default_value,
            sub_total_heading=sub_total_heading,
            bill_sundry_nature=bill_sundry_nature,
            affected_good=affected_good,
            adjust_amount=adjust_amount,
            account_past=account_past,
            affected_good_purchase=affected_good_purchase,
            adjust_purchase_account=adjust_purchase_account,
            account_heat=account_heat,
            affected_material_issue=affected_material_issue,
            affected_material_receipt=affected_material_receipt,
            affected_stock_transfer=affected_stock_transfer,
            p_specify_here=p_specify_here,
            p_taxable_voucher=p_taxable_voucher,
            p_local=p_local,
            p_stock_transfer=p_stock_transfer,
            p_single_tax=p_single_tax,
            
            
        )
        data1.save()
        sweetify.success(request, " Created Successfully.", timer=6000, button='OK')

    data = Purchase_type.objects.all().order_by('-id')
    comp = Company.objects.all()
    vend= Covervender.objects.all()
    obj3=Topi.objects.all()
    data2=material_centre.objects.all()
    return render(request, 'cover/purchase_type.html', {'data2':data2,'data': data,'comp':comp,'obj3':obj3,'vend':vend })



def cover_available(request):
    if request.method == 'POST' :
        obj = Cover_available()
        

        obj.opening_stock_of_cover_1 = request.POST.get('opening_stock_of_cover_1')
        obj.cover_recived_after_cutting_1 = request.POST.get('cover_recived_after_cutting_1')
        obj.cover_issued_for_pasting_1 = request.POST.get('cover_issued_for_pasting_1')
        obj.cover_returned_by_paster_1 = request.POST.get('cover_returned_by_paster_1')
        obj.cover_balance_1 = request.POST.get('cover_balance_1')
        obj.particular_1 = request.POST.get('particular_1')
        
        obj.opening_stock_of_cover_2 = request.POST.get('opening_stock_of_cover_2')
        obj.cover_recived_after_cutting_2 = request.POST.get('cover_recived_after_cutting_2')
        obj.cover_issued_for_pasting_2 = request.POST.get('cover_issued_for_pasting_2')
        obj.cover_returned_by_paster_2 = request.POST.get('cover_returned_by_paster_2')
        obj.cover_balance_2 = request.POST.get('cover_balance_2')
        obj.particular_2 = request.POST.get('particular_2')

        obj.opening_stock_of_cover_3 = request.POST.get('opening_stock_of_cover_3')
        obj.cover_recived_after_cutting_3 = request.POST.get('cover_recived_after_cutting_3')
        obj.cover_issued_for_pasting_3 = request.POST.get('cover_issued_for_pasting_3')
        obj.cover_returned_by_paster_3 = request.POST.get('cover_returned_by_paster_3')
        obj.cover_balance_3 = request.POST.get('cover_balance_3')
        obj.particular_3 = request.POST.get('particular_3')

        obj.opening_stock_of_cover_4 = request.POST.get('opening_stock_of_cover_4')
        obj.cover_recived_after_cutting_4 = request.POST.get('cover_recived_after_cutting_4')
        obj.cover_issued_for_pasting_4 = request.POST.get('cover_issued_for_pasting_4')
        obj.cover_returned_by_paster_4 = request.POST.get('cover_returned_by_paster_4')
        obj.cover_balance_4 = request.POST.get('cover_balance_4')
        obj.particular_4 = request.POST.get('particular_4')

        obj.opening_stock_of_cover_5 = request.POST.get('opening_stock_of_cover_5')
        obj.cover_recived_after_cutting_5 = request.POST.get('cover_recived_after_cutting_5')
        obj.cover_issued_for_pasting_5 = request.POST.get('cover_issued_for_pasting_5')
        obj.cover_returned_by_paster_5 = request.POST.get('cover_returned_by_paster_5')
        obj.cover_balance_5 = request.POST.get('cover_balance_5')
        obj.particular_5 = request.POST.get('particular_5')

        obj.opening_stock_of_cover_6 = request.POST.get('opening_stock_of_cover_6')
        obj.cover_recived_after_cutting_6 = request.POST.get('cover_recived_after_cutting_6')
        obj.cover_issued_for_pasting_6 = request.POST.get('cover_issued_for_pasting_6')
        obj.cover_returned_by_paster_6 = request.POST.get('cover_returned_by_paster_6')
        obj.cover_balance_6 = request.POST.get('cover_balance_6')
        obj.particular_6 = request.POST.get('particular_6')

        obj.opening_stock_of_cover_7 = request.POST.get('opening_stock_of_cover_7')
        obj.cover_recived_after_cutting_7 = request.POST.get('cover_recived_after_cutting_7')
        obj.cover_issued_for_pasting_7 = request.POST.get('cover_issued_for_pasting_7')
        obj.cover_returned_by_paster_7 = request.POST.get('cover_returned_by_paster_7')
        obj.cover_balance_7 = request.POST.get('cover_balance_7')
        obj.particular_7 = request.POST.get('particular_7')

        obj.opening_stock_of_cover_8 = request.POST.get('opening_stock_of_cover_8')
        obj.cover_recived_after_cutting_8 = request.POST.get('cover_recived_after_cutting_8')
        obj.cover_issued_for_pasting_8 = request.POST.get('cover_issued_for_pasting_8')
        obj.cover_returned_by_paster_8 = request.POST.get('cover_returned_by_paster_8')
        obj.cover_balance_8 = request.POST.get('cover_balance_8')
        obj.particular_8 = request.POST.get('particular_8')

        obj.opening_stock_of_cover_9 = request.POST.get('opening_stock_of_cover_9')
        obj.cover_recived_after_cutting_9 = request.POST.get('cover_recived_after_cutting_9')
        obj.cover_issued_for_pasting_9 = request.POST.get('cover_issued_for_pasting_9')
        obj.cover_returned_by_paster_9 = request.POST.get('cover_returned_by_paster_9')
        obj.cover_balance_9 = request.POST.get('cover_balance_9')
        obj.particular_9 = request.POST.get('particular_9')

        # Fetch the corresponding books object
        particular_value = obj.particular_1  # Use the appropriate field from your form
        book_instances = books.objects.filter(subject=particular_value)

        # Update the cover_balance field in each books model instance
        for book_instance in book_instances:
            book_instance.cover = obj.cover_balance_1  # Use the appropriate field from your form
            book_instance.save()



        obj.save()


    data = Cover_available.objects.all().order_by("-id")
    data2=books.objects.all()

    options =  Cover_Printing.objects.all()

    context = {
        'data' : data,
        'options': options,
        'data2':data2
    }
    return render(request, 'cover/cover_available.html',context=context )


def delete_cover_available(request, id):
    cus = Cover_available.objects.get(id=id)
    cus.delete()
    return redirect('/cover_available/')


def view_cover_available(request, id):
    data = Cover_available.objects.get(id=id)
    
    
    max_orders = 10  # Maximum number of orders to consider

    order_data = []
    total_quantity = 0

    for i in range(1, max_orders + 1):
        quantity_field = 'cover_balance_{}'.format(i)
        quantity = getattr(data, quantity_field, None)

        if quantity:
            order_data.append({
                'medium': request.POST.get('midium_{}'.format(i)),
                'subject': request.POST.get('bsubject_{}'.format(i)),
                'quantity': float(quantity),
                'ord_rate3': request.POST.get('ord_rate3{}'.format(i))
            })

            # Calculate the sum of quantities
            total_quantity += float(quantity)
            print('total_quantity', total_quantity)

    # Update the total_quantity field of the Bindingorder object
    data.binding_order_total = total_quantity
    print("1111111111", data.binding_order_total)
    data.save()
    
    context = {
        'data': data,
        
    }

    return render(request, 'cover/cover_available_bill_view.html',context)



# def edit_cover_available(request,id):
#     data = Cover_available.objects.get(id=id)
#     if request.method == 'POST':
#             data.opening_stock_of_cover_1 = request.POST.get('opening_stock_of_cover_1')
#             data.cover_recived_after_cutting_1 = request.POST.get('cover_recived_after_cutting_1')
#             data.cover_issued_for_pasting_1 = request.POST.get('cover_issued_for_pasting_1')
#             data.cover_returned_by_paster_1 = request.POST.get('cover_returned_by_paster_1')
#             data.cover_balance_1 = request.POST.get('cover_balance_1')
#             data.particular_1 = request.POST.get('particular_1')

#             data.save()
           
#             return redirect('/customer_ledger/')
#     context = {'data':data,}
#     return render(request,'cover/edit_cover_available.html')



def topi_available(request):
    if request.method == 'POST':
        obj = Topi_available()
        obj.opening_stock_of_topi_1 = request.POST.get('opening_stock_of_topi_1')
        obj.topi_recived_after_cutting_1 = request.POST.get('topi_recived_after_cutting_1')
        obj.topi_issued_for_pasting_1 = request.POST.get('topi_issued_for_pasting_1')
        obj.topi_returned_by_paster_1 = request.POST.get('topi_returned_by_paster_1')
        obj.topi_balance_1 = request.POST.get('topi_balance_1')
        obj.particular_1 = request.POST.get('particular_1')

        
        obj.opening_stock_of_topi_2 = request.POST.get('opening_stock_of_topi_2')
        obj.topi_recived_after_cutting_2 = request.POST.get('topi_recived_after_cutting_2')
        obj.topi_issued_for_pasting_2 = request.POST.get('topi_issued_for_pasting_2')
        obj.topi_returned_by_paster_2 = request.POST.get('topi_returned_by_paster_2')
        obj.topi_balance_2 = request.POST.get('topi_balance_2')
        obj.particular_2 = request.POST.get('particular_2')

        obj.opening_stock_of_topi_3 = request.POST.get('opening_stock_of_topi_3')
        obj.topi_recived_after_cutting_3 = request.POST.get('topi_recived_after_cutting_3')
        obj.topi_issued_for_pasting_3 = request.POST.get('topi_issued_for_pasting_3')
        obj.topi_returned_by_paster_3 = request.POST.get('topi_returned_by_paster_3')
        obj.topi_balance_3 = request.POST.get('topi_balance_3')
        obj.particular_3 = request.POST.get('particular_3')

        obj.opening_stock_of_topi_4 = request.POST.get('opening_stock_of_topi_4')
        obj.topi_recived_after_cutting_4 = request.POST.get('topi_recived_after_cutting_4')
        obj.topi_issued_for_pasting_4 = request.POST.get('topi_issued_for_pasting_4')
        obj.topi_returned_by_paster_4 = request.POST.get('topi_returned_by_paster_4')
        obj.topi_balance_4 = request.POST.get('topi_balance_4')
        obj.particular_4 = request.POST.get('particular_4')

        obj.opening_stock_of_topi_5 = request.POST.get('opening_stock_of_topi_5')
        obj.topi_recived_after_cutting_5 = request.POST.get('topi_recived_after_cutting_5')
        obj.topi_issued_for_pasting_5 = request.POST.get('topi_issued_for_pasting_5')
        obj.topi_returned_by_paster_5 = request.POST.get('topi_returned_by_paster_5')
        obj.topi_balance_5 = request.POST.get('topi_balance_5')
        obj.particular_5 = request.POST.get('particular_5')

        obj.opening_stock_of_topi_6 = request.POST.get('opening_stock_of_topi_6')
        obj.topi_recived_after_cutting_6 = request.POST.get('topi_recived_after_cutting_6')
        obj.topi_issued_for_pasting_6 = request.POST.get('topi_issued_for_pasting_6')
        obj.topi_returned_by_paster_6 = request.POST.get('topi_returned_by_paster_6')
        obj.topi_balance_6 = request.POST.get('topi_balance_6')
        obj.particular_6 = request.POST.get('particular_6')

        obj.opening_stock_of_topi_7 = request.POST.get('opening_stock_of_topi_7')
        obj.topi_recived_after_cutting_7 = request.POST.get('topi_recived_after_cutting_7')
        obj.topi_issued_for_pasting_7 = request.POST.get('topi_issued_for_pasting_7')
        obj.topi_returned_by_paster_7 = request.POST.get('topi_returned_by_paster_7')
        obj.topi_balance_7 = request.POST.get('topi_balance_7')
        obj.particular_7 = request.POST.get('particular_7')

        obj.opening_stock_of_topi_8 = request.POST.get('opening_stock_of_topi_8')
        obj.topi_recived_after_cutting_8 = request.POST.get('topi_recived_after_cutting_8')
        obj.topi_issued_for_pasting_8 = request.POST.get('topi_issued_for_pasting_8')
        obj.topi_returned_by_paster_8 = request.POST.get('topi_returned_by_paster_8')
        obj.topi_balance_8 = request.POST.get('topi_balance_8')
        obj.particular_8 = request.POST.get('particular_8')

        obj.opening_stock_of_topi_9 = request.POST.get('opening_stock_of_topi_9')
        obj.topi_recived_after_cutting_9 = request.POST.get('topi_recived_after_cutting_9')
        obj.topi_issued_for_pasting_9 = request.POST.get('topi_issued_for_pasting_9')
        obj.topi_returned_by_paster_9 = request.POST.get('topi_returned_by_paster_9')
        obj.topi_balance_9 = request.POST.get('topi_balance_9')
        obj.particular_9 = request.POST.get('particular_9')

        obj.opening_stock_of_topi_10 = request.POST.get('opening_stock_of_topi_10')
        obj.topi_recived_after_cutting_10 = request.POST.get('topi_recived_after_cutting_10')
        obj.topi_issued_for_pasting_10 = request.POST.get('topi_issued_for_pasting_10')
        obj.topi_returned_by_paster_10 = request.POST.get('topi_returned_by_paster_10')
        obj.topi_balance_10 = request.POST.get('topi_balance_10')
        obj.particular_10 = request.POST.get('particular_10')


        obj.save()


    data = Topi_available.objects.all()

    options =Cover_Printing.objects.all()

    context = {
        'data' : data,
        'options': options
    }
    return render(request, 'cover/topi_available.html',context=context )


def delete_topi_available(request, id):
    cus = Topi_available.objects.get(id=id)
    cus.delete()
    return redirect('/cover_available/')

def view_topi_available(request,id):
    data = Topi_available.objects.get(id=id)

    max_orders = 10  # Maximum number of orders to consider

    order_data = []
    total_quantity = 0

    for i in range(1, max_orders + 1):
        quantity_field = 'topi_balance_{}'.format(i)
        quantity = getattr(data, quantity_field, None)

        if quantity:
            order_data.append({
                'medium': request.POST.get('midium_{}'.format(i)),
                'subject': request.POST.get('bsubject_{}'.format(i)),
                'quantity': float(quantity),
                'ord_rate3': request.POST.get('ord_rate3{}'.format(i))
            })

            # Calculate the sum of quantities
            total_quantity += float(quantity)
            print('total_quantity', total_quantity)

    # Update the total_quantity field of the Bindingorder object
    data.binding_order_total = total_quantity
    data.save()
    context = {
        'data': data,
        
    }

    return render(request,'cover/topi_available_bill_view.html',context)