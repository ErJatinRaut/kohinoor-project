from django.shortcuts import render
from multiprocessing import context
from os import system
from django.shortcuts import render, redirect
import datetime
from processing.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from brand_app.models import mediums
from django.http import JsonResponse
from django.contrib.auth.models import User
from order_app.models import orders
from brand_app.models import *
# Create your views here.

def printing_transfer(request):
    if request.method=='POST':
        date = request.POST.get('date')
        vender_transfer_from = request.POST.get('vender_transfer_from')
        vender_transfer_to = request.POST.get('vender_transfer_to')
        print_transfer_voucher_no = request.POST.get('print_transfer_voucher_no')
        print_transfer_subject = request.POST.get('print_transfer_subject')
        print_transfer_form_no1 = request.POST.get('print_transfer_form_no1')
        print_transfer_qty1 = request.POST.get('print_transfer_qty1')
        print_transfer_form_no2 = request.POST.get('print_transfer_form_no2')
        print_transfer_qty2 = request.POST.get('print_transfer_qty2')

        print_transfer_form_no3 = request.POST.get('print_transfer_form_no3')
        print_transfer_qty3 = request.POST.get('print_transfer_qty3')

        print_transfer_form_no4 = request.POST.get('print_transfer_form_no4')
        print_transfer_qty4 = request.POST.get('print_transfer_qty4')
        print_transfer_form_no5 = request.POST.get('print_transfer_form_no5')
        print_transfer_qty5 = request.POST.get('print_transfer_qty5')
        print_transfer_form_no6 = request.POST.get('print_transfer_form_no6')
        print_transfer_qty6 = request.POST.get('print_transfer_qty6')

        print_transfer_form_no7 = request.POST.get('print_transfer_form_no7')
        print_transfer_qty7 = request.POST.get('print_transfer_qty7')
        print_transfer_form_no8 = request.POST.get('print_transfer_form_no8')
        print_transfer_qty8 = request.POST.get('print_transfer_qty8')
        print_transfer_form_no9 = request.POST.get('print_transfer_form_no9')
        print_transfer_qty9 = request.POST.get('print_transfer_qty9')
        
        print_transfer_form_no10 = request.POST.get('print_transfer_form_no10')
        print_transfer_qty10 = request.POST.get('print_transfer_qty10')
        print_transfer_form_no11 = request.POST.get('print_transfer_form_no11')
        print_transfer_qty11 = request.POST.get('print_transfer_qty11')
        print_transfer_form_no12 = request.POST.get('print_transfer_form_no12')
        print_transfer_qty12 = request.POST.get('print_transfer_qty12')

        main_group_data =transfer_printing_module(date=date,
                                                  vender_transfer_from=vender_transfer_from,
                                                  vender_transfer_to=vender_transfer_to,
                                                  print_transfer_voucher_no=print_transfer_voucher_no,
                                                  print_transfer_subject=print_transfer_subject,
                                                  print_transfer_form_no1=print_transfer_form_no1,
                                                  print_transfer_qty1=print_transfer_qty1,
                                                  print_transfer_form_no2=print_transfer_form_no2,
                                                  print_transfer_qty2=print_transfer_qty2,
                                                  print_transfer_form_no3=print_transfer_form_no3,
                                                  print_transfer_qty3=print_transfer_qty3,
                                                  print_transfer_form_no4=print_transfer_form_no4,
                                                  print_transfer_qty4=print_transfer_qty4,
                                                  print_transfer_form_no5=print_transfer_form_no5,
                                                  print_transfer_qty5=print_transfer_qty5,
                                                  print_transfer_form_no6=print_transfer_form_no6,
                                                  print_transfer_qty6=print_transfer_qty6,
                                                  print_transfer_form_no7=print_transfer_form_no7,
                                                  print_transfer_qty7=print_transfer_qty7,
                                                  print_transfer_form_no8=print_transfer_form_no8,
                                                  print_transfer_qty8=print_transfer_qty8,
                                                  print_transfer_form_no9=print_transfer_form_no9,
                                                  print_transfer_qty9=print_transfer_qty9,
                                                  print_transfer_form_no10=print_transfer_form_no10,
                                                  print_transfer_qty10=print_transfer_qty10,
                                                  print_transfer_form_no11=print_transfer_form_no11,
                                                  print_transfer_qty11=print_transfer_qty11,
                                                  print_transfer_form_no12=print_transfer_form_no12,
                                                  print_transfer_qty12=print_transfer_qty12,)
        main_group_data.save()

    
    data=transfer_printing_module.objects.all()
    data26=books.objects.all()
    data1=venders.objects.all()
    data2=Gatheringvender.objects.all()
    context={
        'data26':data26,
        'data':data,
        'data1':data1,
        'data2':data2,
    }

    return render(request,'transfer/prinitng_transfer.html',context)

def edit_printing_transfer(request,id):
    data=transfer_printing_module.objects.get(id=id)
    if request.method=='POST':
        data.vender_transfer_from=request.POST.get('vender_transfer_from')
        data.vender_transfer_to=request.POST.get('vender_transfer_to')
        data.print_transfer_voucher_no=request.POST.get('print_transfer_voucher_no')
        data.print_transfer_subject=request.POST.get('print_transfer_subject')
        data.print_transfer_form_no1=request.POST.get('print_transfer_form_no1')
        data.print_transfer_qty1=request.POST.get('print_transfer_qty1')
        data.print_transfer_form_no2=request.POST.get('print_transfer_form_no2')
        data.print_transfer_qty2=request.POST.get('print_transfer_qty2')
        data.print_transfer_form_no3=request.POST.get('print_transfer_form_no3')
        data.print_transfer_qty3=request.POST.get('print_transfer_qty3')
        data.print_transfer_form_no4=request.POST.get('print_transfer_form_no4')
        data.print_transfer_qty4=request.POST.get('print_transfer_qty4')
        data.print_transfer_form_no5=request.POST.get('print_transfer_form_no5')
        data.print_transfer_qty5=request.POST.get('print_transfer_qty5')

        data.print_transfer_form_no6=request.POST.get('print_transfer_form_no6')
        data.print_transfer_qty6=request.POST.get('print_transfer_qty6')
        data.print_transfer_form_no7=request.POST.get('print_transfer_form_no7')
        data.print_transfer_qty7=request.POST.get('print_transfer_qty7')
        data.print_transfer_form_no8=request.POST.get('print_transfer_form_no8')
        data.print_transfer_qty8=request.POST.get('print_transfer_qty8')
        data.print_transfer_form_no9=request.POST.get('print_transfer_form_no9')
        data.print_transfer_qty9=request.POST.get('print_transfer_qty9')
        data.print_transfer_form_no10=request.POST.get('print_transfer_form_no10')
        data.print_transfer_qty10=request.POST.get('print_transfer_qty10')
        data.print_transfer_form_no11=request.POST.get('print_transfer_form_no11')
        data.print_transfer_qty11=request.POST.get('print_transfer_qty11')
        data.print_transfer_form_no12=request.POST.get('print_transfer_form_no12')
        data.print_transfer_qty12=request.POST.get('print_transfer_qty12')
        data.save()

        return redirect('/printing_transfer/')
    
    data26=books.objects.all()
    data1=venders.objects.all()
    data2=Gatheringvender.objects.all()
    context={
        'data26':data26,
        'data':data,
        'data1':data1,
        'data2':data2,
    }

       
    return render(request,'transfer/edit_printing_transfer.html',context)

def delete_printing_transfer(request,id):
    cus = transfer_printing_module.objects.get(id=id)
    cus.delete()
    return redirect('/printing_transfer/')


def transfer_cover(request):
    if request.method=='POST':
        date=request.POST.get('date')
        vender_transfer_from = request.POST.get('vender_transfer_from')
        vender_transfer_to = request.POST.get('vender_transfer_to')
        cover_transfer_voucher_no = request.POST.get('cover_transfer_voucher_no')
        cover_transfer_subject1 = request.POST.get('cover_transfer_subject1')

        cover_transfer_qty1 = request.POST.get('cover_transfer_qty1')
        cover_transfer_unit1 = request.POST.get('cover_transfer_unit1')
        cover_transfer_subject2 = request.POST.get('cover_transfer_subject2')
        cover_transfer_qty2 = request.POST.get('cover_transfer_qty2')

        cover_transfer_unit2 = request.POST.get('cover_transfer_unit2')
        cover_transfer_subject3 = request.POST.get('cover_transfer_subject3')
        cover_transfer_qty3 = request.POST.get('cover_transfer_qty3')
        cover_transfer_unit3 = request.POST.get('cover_transfer_unit3')

        cover_transfer_subject4 = request.POST.get('cover_transfer_subject4')
        cover_transfer_qty4 = request.POST.get('cover_transfer_qty4')
        cover_transfer_unit4 = request.POST.get('cover_transfer_unit4')

        cover_transfer_subject5 = request.POST.get('cover_transfer_subject5')
        cover_transfer_qty5 = request.POST.get('cover_transfer_qty5')
        cover_transfer_unit5 = request.POST.get('cover_transfer_unit5')

        data_transfer_cover=cover_transfer(date=date,
                                           vender_transfer_from=vender_transfer_from,
                                           vender_transfer_to=vender_transfer_to,
                                           cover_transfer_voucher_no=cover_transfer_voucher_no,
                                           cover_transfer_subject1=cover_transfer_subject1,
                                           cover_transfer_qty1=cover_transfer_qty1,
                                           cover_transfer_unit1=cover_transfer_unit1,
                                           cover_transfer_subject2=cover_transfer_subject2,
                                           cover_transfer_qty2=cover_transfer_qty2,
                                           cover_transfer_unit2=cover_transfer_unit2,
                                           cover_transfer_subject3=cover_transfer_subject3,
                                           cover_transfer_qty3=cover_transfer_qty3,
                                           cover_transfer_unit3=cover_transfer_unit3,
                                           cover_transfer_subject4=cover_transfer_subject4,
                                           cover_transfer_qty4=cover_transfer_qty4,
                                           cover_transfer_unit4=cover_transfer_unit4,
                                           cover_transfer_subject5=cover_transfer_subject5,
                                           cover_transfer_qty5=cover_transfer_qty5,
                                           cover_transfer_unit5=cover_transfer_unit5,)
        data_transfer_cover.save()
    data=cover_transfer.objects.all()
    data26=books.objects.all()
    data1=venders.objects.all()
    data2=Gatheringvender.objects.all()
    context={
        'data26':data26,
        'data':data,
        'data1':data1,
        'data2':data2,
    }
    return render(request,'transfer/cover_transfer1.html',context)

def delete_cover_transfer(request,id):
    cus = cover_transfer.objects.get(id=id)
    cus.delete()
    return redirect('/transfer_cover/')

def edit_cover_transfer(request,id):
    data=cover_transfer.objects.get(id=id)
    if request.method=='POST':
        data.vender_transfer_from = request.POST.get('vender_transfer_from')
        data.vender_transfer_to = request.POST.get('vender_transfer_to')
        data.cover_transfer_voucher_no = request.POST.get('cover_transfer_voucher_no')
        data.cover_transfer_subject1 = request.POST.get('cover_transfer_subject1')

        data.cover_transfer_qty1 = request.POST.get('cover_transfer_qty1')
        data.cover_transfer_unit1 = request.POST.get('cover_transfer_unit1')
        data.cover_transfer_subject2 = request.POST.get('cover_transfer_subject2')
        data.cover_transfer_qty2 = request.POST.get('cover_transfer_qty2')

        data.cover_transfer_unit2 = request.POST.get('cover_transfer_unit2')
        data.cover_transfer_subject3 = request.POST.get('cover_transfer_subject3')
        data.cover_transfer_qty3 = request.POST.get('cover_transfer_qty3')
        data.cover_transfer_unit3 = request.POST.get('cover_transfer_unit3')

        data.cover_transfer_subject4 = request.POST.get('cover_transfer_subject4')
        data.cover_transfer_qty4 = request.POST.get('cover_transfer_qty4')
        data.cover_transfer_unit4 = request.POST.get('cover_transfer_unit4')

        data.cover_transfer_subject5 = request.POST.get('cover_transfer_subject5')
        data.cover_transfer_qty5 = request.POST.get('cover_transfer_qty5')
        data.cover_transfer_unit5 = request.POST.get('cover_transfer_unit5')
        
        data.save()



    data26=books.objects.all()
    data1=venders.objects.all()
    data2=Gatheringvender.objects.all()
    context={
        'data':data,
        'data26':data26,
        'data1':data1,
        'data2':data2,
    }
    return render(request,'transfer/edit_cover_transfer.html',context)


def topi_transfer(request):
    if request.method =='POST':
        date=request.POST.get('date')
        vender_transfer_from = request.POST.get('vender_transfer_from')
        vender_transfer_to = request.POST.get('vender_transfer_to')
        topi_transfer_voucher_no = request.POST.get('topi_transfer_voucher_no')
        topi_transfer_subject1 = request.POST.get('topi_transfer_subject1')

        topi_transfer_qty1 = request.POST.get('topi_transfer_qty1')

        xyz=transfer_topi(date=date,
                          vender_transfer_from=vender_transfer_from,
                          vender_transfer_to=vender_transfer_to,
                          topi_transfer_voucher_no=topi_transfer_voucher_no,
                          topi_transfer_subject1=topi_transfer_subject1,
                          topi_transfer_qty1=topi_transfer_qty1,)
        xyz.save()
        
    data=transfer_topi.objects.all()
    data26=books.objects.all()
    data1=venders.objects.all()
    data2=Gatheringvender.objects.all()
    context={
        'data26':data26,
        'data1':data1,
        'data2':data2,
        'data':data,
        }
    return render(request,'transfer/topi_transfer.html',context)

def delete_topi_transfer(request,id):
    cus = transfer_topi.objects.get(id=id)
    cus.delete()
    return redirect('/topi_transfer/')


def edit_topi_transfer(request,id):
    data=transfer_topi.objects.get(id=id)

    if request.method =='POST':
       
        data.vender_transfer_from = request.POST.get('vender_transfer_from')
        data.vender_transfer_to = request.POST.get('vender_transfer_to')
        data.topi_transfer_voucher_no = request.POST.get('topi_transfer_voucher_no')
        data.topi_transfer_subject1 = request.POST.get('topi_transfer_subject1')

        data.topi_transfer_qty1 = request.POST.get('topi_transfer_qty1')

        data.save()
        return redirect('/topi_transfer/')

    
    data26=books.objects.all()
    data1=venders.objects.all()
    data2=Gatheringvender.objects.all()

    context={
        'data26':data26,
        'data1':data1,
        'data2':data2,
        'data':data
    }
    return render(request,'transfer/edit_topi_transfer.html',context)

# @login_required(login_url="")
# def printing_data(request):
#     if request.method =='POST':
#         id = request.POST.get('id')
#         printing_received_form=request.POST.get('printing_received_form')
#         print_wastage_form = request.POST.get('print_wastage_form')

#         printing_received_form_1 =request.POST.get('printing_received_form_1')
#         print_wastage_form_1 = request.POST.get('print_wastage_form_1')
#         printing_received_form_2 =request.POST.get('printing_received_form_2')
#         print_wastage_form_2 = request.POST.get('print_wastage_form_2')
#         printing_received_form_3 =request.POST.get('printing_received_form_3')
#         print_wastage_form_3 = request.POST.get('print_wastage_form_3')
#         printing_received_form_4 =request.POST.get('printing_received_form_4')
#         print_wastage_form_4 = request.POST.get('print_wastage_form_4')
#         printing_received_form_5 =request.POST.get('printing_received_form_5')
#         print_wastage_form_5 = request.POST.get('print_wastage_form_5')
#         printing_received_form_6 =request.POST.get('printing_received_form_6')
#         print_wastage_form_6 = request.POST.get('print_wastage_form_6')
#         printing_received_form_7 =request.POST.get('printing_received_form_7')
#         print_wastage_form_7 = request.POST.get('print_wastage_form_7')
#         printing_received_form_8 =request.POST.get('printing_received_form_8')
#         print_wastage_form_8 = request.POST.get('print_wastage_form_8')
#         printing_received_form_9 =request.POST.get('printing_received_form_9')
#         print_wastage_form_9 = request.POST.get('print_wastage_form_9')
#         printing_received_form_10 =request.POST.get('printing_received_form_10')
#         print_wastage_form_10 = request.POST.get('print_wastage_form_10')
        
#         printing_received_form_11 =request.POST.get('printing_received_form_11')
#         print_wastage_form_11 = request.POST.get('print_wastage_form_11')
#         printing_received_form_12 =request.POST.get('printing_received_form_12')
#         print_wastage_form_12 = request.POST.get('print_wastage_form_12')
#         printing_received_form_13 =request.POST.get('printing_received_form_13')
#         print_wastage_form_13 = request.POST.get('print_wastage_form_13')
#         printing_received_form_14 =request.POST.get('printing_received_form_14')
#         print_wastage_form_14 = request.POST.get('print_wastage_form_14')
#         printing_received_form_15 =request.POST.get('printing_received_form_15')
#         print_wastage_form_15 = request.POST.get('print_wastage_form_15')
#         printing_received_form_16 =request.POST.get('printing_received_form_16')
#         print_wastage_form_16 = request.POST.get('print_wastage_form_16')
#         printing_received_form_17 =request.POST.get('printing_received_form_17')
#         print_wastage_form_17 = request.POST.get('print_wastage_form_17')
#         printing_received_form_18 =request.POST.get('printing_received_form_18')
#         print_wastage_form_18 = request.POST.get('print_wastage_form_18')
#         printing_received_form_19 =request.POST.get('printing_received_form_19')
#         print_wastage_form_19 = request.POST.get('print_wastage_form_19')
#         printing_received_form_20 =request.POST.get('printing_received_form_20')
#         print_wastage_form_20 = request.POST.get('print_wastage_form_20')

#         printing_received_form_21 =request.POST.get('printing_received_form_21')
#         print_wastage_form_21 = request.POST.get('print_wastage_form_21')
#         printing_received_form_22 =request.POST.get('printing_received_form_22')
#         print_wastage_form_22 = request.POST.get('print_wastage_form_22')
#         printing_received_form_23 =request.POST.get('printing_received_form_23')
#         print_wastage_form_23 = request.POST.get('print_wastage_form_23')
#         printing_received_form_24 =request.POST.get('printing_received_form_24')
#         print_wastage_form_24 = request.POST.get('print_wastage_form_24')
#         printing_received_form_25 =request.POST.get('printing_received_form_25')
#         print_wastage_form_25 = request.POST.get('print_wastage_form_25')
#         printing_received_form_26 =request.POST.get('printing_received_form_26')
#         print_wastage_form_26 = request.POST.get('print_wastage_form_26')
#         printing_received_form_27 =request.POST.get('printing_received_form_27')
#         print_wastage_form_27 = request.POST.get('print_wastage_form_27')
#         printing_received_form_28 =request.POST.get('printing_received_form_28')
#         print_wastage_form_28 = request.POST.get('print_wastage_form_28')
#         printing_received_form_29 =request.POST.get('printing_received_form_29')
#         print_wastage_form_29 = request.POST.get('print_wastage_form_29')
#         printing_received_form_30 =request.POST.get('printing_received_form_30')
#         print_wastage_form_30 = request.POST.get('print_wastage_form_30')

#         printing_received_form_31 =request.POST.get('printing_received_form_31')
#         print_wastage_form_31 = request.POST.get('print_wastage_form_31')
#         printing_received_form_32 =request.POST.get('printing_received_form_32')
#         print_wastage_form_32 = request.POST.get('print_wastage_form_32')
#         printing_received_form_33 =request.POST.get('printing_received_form_33')
#         print_wastage_form_33 = request.POST.get('print_wastage_form_33')
#         printing_received_form_34 =request.POST.get('printing_received_form_34')
#         print_wastage_form_34 = request.POST.get('print_wastage_form_34')
#         printing_received_form_35 =request.POST.get('printing_received_form_35')
#         print_wastage_form_35 = request.POST.get('print_wastage_form_35')
#         printing_received_form_36 =request.POST.get('printing_received_form_36')
#         print_wastage_form_36 = request.POST.get('print_wastage_form_36')
#         printing_received_form_37 =request.POST.get('printing_received_form_37')
#         print_wastage_form_37 = request.POST.get('print_wastage_form_37')
#         printing_received_form_38 =request.POST.get('printing_received_form_38')
#         print_wastage_form_38 = request.POST.get('print_wastage_form_38')
#         printing_received_form_39 =request.POST.get('printing_received_form_39')
#         print_wastage_form_39 = request.POST.get('print_wastage_form_39')
#         printing_received_form_40 =request.POST.get('printing_received_form_40')
#         print_wastage_form_40 = request.POST.get('print_wastage_form_40')

#         printing_received_form_41 =request.POST.get('printing_received_form_41')
#         print_wastage_form_41 = request.POST.get('print_wastage_form_41')
#         printing_received_form_42 =request.POST.get('printing_received_form_42')
#         print_wastage_form_42 = request.POST.get('print_wastage_form_42')
#         printing_received_form_43 =request.POST.get('printing_received_form_43')
#         print_wastage_form_43 = request.POST.get('print_wastage_form_43')
#         printing_received_form_44 =request.POST.get('printing_received_form_44')
#         print_wastage_form_44 = request.POST.get('print_wastage_form_44')
#         printing_received_form_45 =request.POST.get('printing_received_form_45')
#         print_wastage_form_45 = request.POST.get('print_wastage_form_45')
#         printing_received_form_46 =request.POST.get('printing_received_form_46')
#         print_wastage_form_46 = request.POST.get('print_wastage_form_46')
#         printing_received_form_47 =request.POST.get('printing_received_form_47')
#         print_wastage_form_47 = request.POST.get('print_wastage_form_47')
#         printing_received_form_48 =request.POST.get('printing_received_form_48')
#         print_wastage_form_48 = request.POST.get('print_wastage_form_48')
#         printing_received_form_49 =request.POST.get('printing_received_form_49')
#         print_wastage_form_49 = request.POST.get('print_wastage_form_49')
#         printing_received_form_50=request.POST.get('printing_received_form_50')
#         print_wastage_form_50 = request.POST.get('print_wastage_form_50')

        

#         print_date = request.POST.get('print_date')
#         order = orders.objects.filter(order_id=id).get()
#         print('order',order)
#         order.printing_received_form=printing_received_form
#         order.print_wastage_form=print_wastage_form
#         order.printing_received_form_1=printing_received_form_1
#         order.print_wastage_form_1=print_wastage_form_1 
#         order.printing_received_form_2=printing_received_form_2
#         order.print_wastage_form_2=print_wastage_form_2 
#         order.printing_received_form_3=printing_received_form_3
#         order.print_wastage_form_3=print_wastage_form_3 
#         order.printing_received_form_4=printing_received_form_4
#         order.print_wastage_form_4=print_wastage_form_4 
#         order.printing_received_form_5=printing_received_form_5
#         order.print_wastage_form_5=print_wastage_form_5 
#         order.printing_received_form_6=printing_received_form_6
#         order.print_wastage_form_6=print_wastage_form_6 
#         order.printing_received_form_7=printing_received_form_7
#         order.print_wastage_form_7=print_wastage_form_7 
#         order.printing_received_form_8=printing_received_form_8
#         order.print_wastage_form_8=print_wastage_form_8 
#         order.printing_received_form_9=printing_received_form_9
#         order.print_wastage_form_9=print_wastage_form_9 
#         order.printing_received_form_10=printing_received_form_10
#         order.print_wastage_form_10=print_wastage_form_10  

#         order.printing_received_form_11=printing_received_form_11
#         order.print_wastage_form_11=print_wastage_form_11 
#         order.printing_received_form_12=printing_received_form_12
#         order.print_wastage_form_12=print_wastage_form_12 
#         order.printing_received_form_13=printing_received_form_13
#         order.print_wastage_form_13=print_wastage_form_13 
#         order.printing_received_form_14=printing_received_form_14
#         order.print_wastage_form_14=print_wastage_form_14 
#         order.printing_received_form_15=printing_received_form_15
#         order.print_wastage_form_15=print_wastage_form_15 
#         order.printing_received_form_16=printing_received_form_16
#         order.print_wastage_form_16=print_wastage_form_16 
#         order.printing_received_form_17=printing_received_form_17
#         order.print_wastage_form_17=print_wastage_form_17 
#         order.printing_received_form_18=printing_received_form_18
#         order.print_wastage_form_18=print_wastage_form_18 
#         order.printing_received_form_19=printing_received_form_19
#         order.print_wastage_form_19=print_wastage_form_19 
#         order.printing_received_form_20=printing_received_form_20
#         order.print_wastage_form_20=print_wastage_form_20 

#         order.printing_received_form_21=printing_received_form_21
#         order.print_wastage_form_21=print_wastage_form_21 
#         order.printing_received_form_22=printing_received_form_22
#         order.print_wastage_form_22=print_wastage_form_22 
#         order.printing_received_form_23=printing_received_form_23
#         order.print_wastage_form_23=print_wastage_form_23 
#         order.printing_received_form_24=printing_received_form_24
#         order.print_wastage_form_24=print_wastage_form_24 
#         order.printing_received_form_25=printing_received_form_25
#         order.print_wastage_form_25=print_wastage_form_25 
#         order.printing_received_form_26=printing_received_form_26
#         order.print_wastage_form_26=print_wastage_form_26 
#         order.printing_received_form_27=printing_received_form_27
#         order.print_wastage_form_27=print_wastage_form_27 
#         order.printing_received_form_28=printing_received_form_28
#         order.print_wastage_form_28=print_wastage_form_28 
#         order.printing_received_form_29=printing_received_form_29
#         order.print_wastage_form_29=print_wastage_form_29 
#         order.printing_received_form_30=printing_received_form_30
#         order.print_wastage_form_30=print_wastage_form_30 

#         order.printing_received_form_31=printing_received_form_31
#         order.print_wastage_form_31=print_wastage_form_31 
#         order.printing_received_form_32=printing_received_form_32
#         order.print_wastage_form_32=print_wastage_form_32 
#         order.printing_received_form_33=printing_received_form_33
#         order.print_wastage_form_33=print_wastage_form_33 
#         order.printing_received_form_34=printing_received_form_34
#         order.print_wastage_form_34=print_wastage_form_34 
#         order.printing_received_form_35=printing_received_form_35
#         order.print_wastage_form_35=print_wastage_form_35 
#         order.printing_received_form_36=printing_received_form_36
#         order.print_wastage_form_36=print_wastage_form_36 
#         order.printing_received_form_37=printing_received_form_37
#         order.print_wastage_form_37=print_wastage_form_37 
#         order.printing_received_form_38=printing_received_form_38
#         order.print_wastage_form_38=print_wastage_form_38 
#         order.printing_received_form_39=printing_received_form_39
#         order.print_wastage_form_39=print_wastage_form_39 
#         order.printing_received_form_40=printing_received_form_40
#         order.print_wastage_form_40=print_wastage_form_40 

#         order.printing_received_form_41=printing_received_form_41
#         order.print_wastage_form_41=print_wastage_form_41 
#         order.printing_received_form_42=printing_received_form_42
#         order.print_wastage_form_42=print_wastage_form_42 
#         order.printing_received_form_43=printing_received_form_43
#         order.print_wastage_form_43=print_wastage_form_43 
#         order.printing_received_form_44=printing_received_form_44
#         order.print_wastage_form_44=print_wastage_form_44 
#         order.printing_received_form_45=printing_received_form_45
#         order.print_wastage_form_45=print_wastage_form_45 
#         order.printing_received_form_46=printing_received_form_46
#         order.print_wastage_form_46=print_wastage_form_46 
#         order.printing_received_form_47=printing_received_form_47
#         order.print_wastage_form_47=print_wastage_form_47 
#         order.printing_received_form_48=printing_received_form_48
#         order.print_wastage_form_48=print_wastage_form_48 
#         order.printing_received_form_49=printing_received_form_49
#         order.print_wastage_form_49=print_wastage_form_49 
#         order.printing_received_form_50=printing_received_form_50
#         order.print_wastage_form_50=print_wastage_form_50 

        
#         order.print_date=datetime.datetime.now()
#         order.save()
    
#     data1 = orders.objects.all().order_by('-order_id')     
#     context={
#         'data1':data1,       
#     }
#     return render(request,'processing/printing.html',context)

# @login_required(login_url="")
# def edit_printing(request, order_id):
#     data1 = orders.objects.get(order_id=order_id)
#     print('gjhgjmgj',order_id)

#     if request.method == 'POST':
#         data1.printing_received_form = request.POST.get('printing_received_form')

#         data1.printing_received_form_1=request.POST.get('printing_received_form_1')
#         data1.printing_received_form_2=request.POST.get('printing_received_form_2')
#         data1.printing_received_form_3=request.POST.get('printing_received_form_3')
#         data1.printing_received_form_4=request.POST.get('printing_received_form_4')
#         data1.printing_received_form_5=request.POST.get('printing_received_form_5')
#         data1.printing_received_form_6=request.POST.get('printing_received_form_6')
#         data1.printing_received_form_7=request.POST.get('printing_received_form_7')
#         data1.printing_received_form_8=request.POST.get('printing_received_form_8')
#         data1.printing_received_form_9=request.POST.get('printing_received_form_9')
#         data1.printing_received_form_10=request.POST.get('printing_received_form_10')
        

#         data1.printing_received_form_11=request.POST.get('printing_received_form_11')
#         data1.printing_received_form_12=request.POST.get('printing_received_form_12')
#         data1.printing_received_form_13=request.POST.get('printing_received_form_13')
#         data1.printing_received_form_14=request.POST.get('printing_received_form_14')
#         data1.printing_received_form_15=request.POST.get('printing_received_form_15')
#         data1.printing_received_form_16=request.POST.get('printing_received_form_16')
#         data1.printing_received_form_17=request.POST.get('printing_received_form_17')
#         data1.printing_received_form_18=request.POST.get('printing_received_form_18')
#         data1.printing_received_form_19=request.POST.get('printing_received_form_19')
#         data1.printing_received_form_20=request.POST.get('printing_received_form_20')
        

#         data1.printing_received_form_21=request.POST.get('printing_received_form_21')
#         data1.printing_received_form_22=request.POST.get('printing_received_form_22')
#         data1.printing_received_form_23=request.POST.get('printing_received_form_23')
#         data1.printing_received_form_24=request.POST.get('printing_received_form_24')
#         data1.printing_received_form_25=request.POST.get('printing_received_form_25')
#         data1.printing_received_form_26=request.POST.get('printing_received_form_26')
#         data1.printing_received_form_27=request.POST.get('printing_received_form_27')
#         data1.printing_received_form_28=request.POST.get('printing_received_form_28')
#         data1.printing_received_form_29=request.POST.get('printing_received_form_29')
#         data1.printing_received_form_30=request.POST.get('printing_received_form_30')
        

#         data1.printing_received_form_31=request.POST.get('printing_received_form_31')
#         data1.printing_received_form_32=request.POST.get('printing_received_form_32')
#         data1.printing_received_form_33=request.POST.get('printing_received_form_33')
#         data1.printing_received_form_34=request.POST.get('printing_received_form_34')
#         data1.printing_received_form_35=request.POST.get('printing_received_form_35')
#         data1.printing_received_form_36=request.POST.get('printing_received_form_36')
#         data1.printing_received_form_37=request.POST.get('printing_received_form_37')
#         data1.printing_received_form_38=request.POST.get('printing_received_form_38')
#         data1.printing_received_form_39=request.POST.get('printing_received_form_39')
#         data1.printing_received_form_40=request.POST.get('printing_received_form_40')
        

#         data1.printing_received_form_41=request.POST.get('printing_received_form_41')
#         data1.printing_received_form_42=request.POST.get('printing_received_form_42')
#         data1.printing_received_form_43=request.POST.get('printing_received_form_43')
#         data1.printing_received_form_44=request.POST.get('printing_received_form_44')
#         data1.printing_received_form_45=request.POST.get('printing_received_form_45')
#         data1.printing_received_form_46=request.POST.get('printing_received_form_46')
#         data1.printing_received_form_47=request.POST.get('printing_received_form_47')
#         data1.printing_received_form_48=request.POST.get('printing_received_form_48')
#         data1.printing_received_form_49=request.POST.get('printing_received_form_49')
#         data1.printing_received_form_50=request.POST.get('printing_received_form_50')




#         data1.form1_page1=request.POST.get('form1_page1')
#         data1.form1_page2=request.POST.get('form1_page2')
#         data1.form1_page3=request.POST.get('form1_page3')
#         data1.form1_page4=request.POST.get('form1_page4')
#         data1.form1_page5=request.POST.get('form1_page5')
#         data1.form1_page6=request.POST.get('form1_page6')
#         data1.form1_page7=request.POST.get('form1_page7')
#         data1.form1_page8=request.POST.get('form1_page8')
#         data1.form1_page9=request.POST.get('form1_page9')
#         data1.form1_page10=request.POST.get('form1_page10')


#         data1.form2_page1=request.POST.get('form2_page1')
#         data1.form2_page2=request.POST.get('form2_page2')
#         data1.form2_page3=request.POST.get('form2_page3')
#         data1.form2_page4=request.POST.get('form2_page4')
#         data1.form2_page5=request.POST.get('form2_page5')
#         data1.form2_page6=request.POST.get('form2_page6')
#         data1.form2_page7=request.POST.get('form2_page7')
#         data1.form2_page8=request.POST.get('form2_page8')
#         data1.form2_page9=request.POST.get('form2_page9')
#         data1.form2_page10=request.POST.get('form2_page10')


#         data1.form3_page1=request.POST.get('form3_page1')
#         data1.form3_page2=request.POST.get('form3_page2')
#         data1.form3_page3=request.POST.get('form3_page3')
#         data1.form3_page4=request.POST.get('form3_page4')
#         data1.form3_page5=request.POST.get('form3_page5')
#         data1.form3_page6=request.POST.get('form3_page6')
#         data1.form3_page7=request.POST.get('form3_page7')
#         data1.form3_page8=request.POST.get('form3_page8')
#         data1.form3_page9=request.POST.get('form3_page9')
#         data1.form3_page10=request.POST.get('form3_page10')


#         data1.form4_page1=request.POST.get('form4_page1')
#         data1.form4_page2=request.POST.get('form4_page2')
#         data1.form4_page3=request.POST.get('form4_page3')
#         data1.form4_page4=request.POST.get('form4_page4')
#         data1.form4_page5=request.POST.get('form4_page5')
#         data1.form4_page6=request.POST.get('form4_page6')
#         data1.form4_page7=request.POST.get('form4_page7')
#         data1.form4_page8=request.POST.get('form4_page8')
#         data1.form4_page9=request.POST.get('form4_page9')
#         data1.form4_page10=request.POST.get('form4_page10')


#         data1.form5_page1=request.POST.get('form5_page1')
#         data1.form5_page2=request.POST.get('form5_page2')
#         data1.form5_page3=request.POST.get('form5_page3')
#         data1.form5_page4=request.POST.get('form5_page4')
#         data1.form5_page5=request.POST.get('form5_page5')
#         data1.form5_page6=request.POST.get('form5_page6')
#         data1.form5_page7=request.POST.get('form5_page7')
#         data1.form5_page8=request.POST.get('form5_page8')
#         data1.form5_page9=request.POST.get('form5_page9')
#         data1.form5_page10=request.POST.get('form5_page10')



#         data1.form6_page1=request.POST.get('form6_page1')
#         data1.form6_page2=request.POST.get('form6_page2')
#         data1.form6_page3=request.POST.get('form6_page3')
#         data1.form6_page4=request.POST.get('form6_page4')
#         data1.form6_page5=request.POST.get('form6_page5')
#         data1.form6_page6=request.POST.get('form6_page6')
#         data1.form6_page7=request.POST.get('form6_page7')
#         data1.form6_page8=request.POST.get('form6_page8')
#         data1.form6_page9=request.POST.get('form6_page9')
#         data1.form6_page10=request.POST.get('form6_page10')


#         data1.form7_page1=request.POST.get('form7_page1')
#         data1.form7_page2=request.POST.get('form7_page2')
#         data1.form7_page3=request.POST.get('form7_page3')
#         data1.form7_page4=request.POST.get('form7_page4')
#         data1.form7_page5=request.POST.get('form7_page5')
#         data1.form7_page6=request.POST.get('form7_page6')
#         data1.form7_page7=request.POST.get('form7_page7')
#         data1.form7_page8=request.POST.get('form7_page8')
#         data1.form7_page9=request.POST.get('form7_page9')
#         data1.form7_page10=request.POST.get('form7_page10')


#         data1.form8_page1=request.POST.get('form8_page1')
#         data1.form8_page2=request.POST.get('form8_page2')
#         data1.form8_page3=request.POST.get('form8_page3')
#         data1.form8_page4=request.POST.get('form8_page4')
#         data1.form8_page5=request.POST.get('form8_page5')
#         data1.form8_page6=request.POST.get('form8_page6')
#         data1.form8_page7=request.POST.get('form8_page7')
#         data1.form8_page8=request.POST.get('form8_page8')
#         data1.form8_page9=request.POST.get('form8_page9')
#         data1.form8_page10=request.POST.get('form8_page10')


#         data1.form9_page1=request.POST.get('form9_page1')
#         data1.form9_page2=request.POST.get('form9_page2')
#         data1.form9_page3=request.POST.get('form9_page3')
#         data1.form9_page4=request.POST.get('form9_page4')
#         data1.form9_page5=request.POST.get('form9_page5')
#         data1.form9_page6=request.POST.get('form9_page6')
#         data1.form9_page7=request.POST.get('form9_page7')
#         data1.form9_page8=request.POST.get('form9_page8')
#         data1.form9_page9=request.POST.get('form9_page9')
#         data1.form9_page10=request.POST.get('form9_page10')


#         data1.form10_page1=request.POST.get('form10_page1')
#         data1.form10_page2=request.POST.get('form10_page2')
#         data1.form10_page3=request.POST.get('form10_page3')
#         data1.form10_page4=request.POST.get('form10_page4')
#         data1.form10_page5=request.POST.get('form10_page5')
#         data1.form10_page6=request.POST.get('form10_page6')
#         data1.form10_page7=request.POST.get('form10_page7')
#         data1.form10_page8=request.POST.get('form10_page8')
#         data1.form10_page9=request.POST.get('form10_page9')
#         data1.form10_page10=request.POST.get('form10_page10')



#         data1.form11_page1=request.POST.get('form11_page1')
#         data1.form11_page2=request.POST.get('form11_page2')
#         data1.form11_page3=request.POST.get('form11_page3')
#         data1.form11_page4=request.POST.get('form11_page4')
#         data1.form11_page5=request.POST.get('form11_page5')
#         data1.form11_page6=request.POST.get('form11_page6')
#         data1.form11_page7=request.POST.get('form11_page7')
#         data1.form11_page8=request.POST.get('form11_page8')
#         data1.form11_page9=request.POST.get('form11_page9')
#         data1.form11_page10=request.POST.get('form11_page10')
        
        
        
#         data1.print_date = datetime.datetime.now()
        
#         if data1.printing_received_form_1:
#             data1.print_wastage_form_1 = float(data1.quantity_1) - float(data1.printing_received_form_1)
#         else:
#             data1.print_wastage_form_1 = 0

#         if data1.printing_received_form_2:
#             data1.print_wastage_form_2 = float(data1.quantity_2) - float(data1.printing_received_form_2)
#         else:
#             data1.print_wastage_form_2 = 0

#         if data1.printing_received_form_3:
#             data1.print_wastage_form_3 = float(data1.quantity_3) - float(data1.printing_received_form_3)
#         else:
#             data1.print_wastage_form_3 = 0

#         if data1.printing_received_form_4:
#             data1.print_wastage_form_4 = float(data1.quantity_4) - float(data1.printing_received_form_4)
#         else:
#             data1.print_wastage_form_4 = 0

#         if data1.printing_received_form_5:
#             data1.print_wastage_form_5 = float(data1.quantity_5) - float(data1.printing_received_form_5)
#         else:
#             data1.print_wastage_form_5 = 0

#         if data1.printing_received_form_6:
#             data1.print_wastage_form_6 = float(data1.quantity_6) - float(data1.printing_received_form_6)
#         else:
#             data1.print_wastage_form_6 = 0

#         if data1.printing_received_form_7:
#             data1.print_wastage_form_7 = float(data1.quantity_7) - float(data1.printing_received_form_7)
#         else:
#             data1.print_wastage_form_7 = 0

#         if data1.printing_received_form_8:
#             data1.print_wastage_form_8 = float(data1.quantity_8) - float(data1.printing_received_form_8)
#         else:
#             data1.print_wastage_form_8 = 0

#         if data1.printing_received_form_9:
#             data1.print_wastage_form_9 = float(data1.quantity_9) - float(data1.printing_received_form_9)
#         else:
#             data1.print_wastage_form_9 = 0

#         if data1.printing_received_form_10:
#             data1.print_wastage_form_10 = float(data1.quantity_10) - float(data1.printing_received_form_10)
#         else:
#             data1.print_wastage_form_10 = 0




#         if data1.printing_received_form_11:
#             data1.print_wastage_form_11 = float(data1.quantity_11) - float(data1.printing_received_form_11)
#         else:
#             data1.print_wastage_form_11 = 0

#         if data1.printing_received_form_12:
#             data1.print_wastage_form_12 = float(data1.quantity_12) - float(data1.printing_received_form_12)
#         else:
#             data1.print_wastage_form_12 = 0

#         if data1.printing_received_form_13:
#             data1.print_wastage_form_13 = float(data1.quantity_13) - float(data1.printing_received_form_13)
#         else:
#             data1.print_wastage_form_13 = 0

#         if data1.printing_received_form_14:
#             data1.print_wastage_form_14 = float(data1.quantity_14) - float(data1.printing_received_form_14)
#         else:
#             data1.print_wastage_form_14 = 0

#         if data1.printing_received_form_15:
#             data1.print_wastage_form_15 = float(data1.quantity_15) - float(data1.printing_received_form_15)
#         else:
#             data1.print_wastage_form_15 = 0

#         if data1.printing_received_form_16:
#             data1.print_wastage_form_16 = float(data1.quantity_16) - float(data1.printing_received_form_16)
#         else:
#             data1.print_wastage_form_16 = 0

#         if data1.printing_received_form_17:
#             data1.print_wastage_form_17 = float(data1.quantity_17) - float(data1.printing_received_form_17)
#         else:
#             data1.print_wastage_form_17 = 0

#         if data1.printing_received_form_18:
#             data1.print_wastage_form_18 = float(data1.quantity_18) - float(data1.printing_received_form_18)
#         else:
#             data1.print_wastage_form_18 = 0

#         if data1.printing_received_form_19:
#             data1.print_wastage_form_19 = float(data1.quantity_19) - float(data1.printing_received_form_19)
#         else:
#             data1.print_wastage_form_19 = 0

#         if data1.printing_received_form_20:
#             data1.print_wastage_form_20 = float(data1.quantity_20) - float(data1.printing_received_form_20)
#         else:
#             data1.print_wastage_form_20 = 0




#         if data1.printing_received_form_21:
#             data1.print_wastage_form_21 = float(data1.quantity_21) - float(data1.printing_received_form_21)
#         else:
#             data1.print_wastage_form_21 = 0

#         if data1.printing_received_form_22:
#             data1.print_wastage_form_22 = float(data1.quantity_22) - float(data1.printing_received_form_22)
#         else:
#             data1.print_wastage_form_22 = 0

#         if data1.printing_received_form_23:
#             data1.print_wastage_form_23 = float(data1.quantity_23) - float(data1.printing_received_form_23)
#         else:
#             data1.print_wastage_form_23 = 0

#         if data1.printing_received_form_24:
#             data1.print_wastage_form_24 = float(data1.quantity_24) - float(data1.printing_received_form_24)
#         else:
#             data1.print_wastage_form_24 = 0

#         if data1.printing_received_form_25:
#             data1.print_wastage_form_25 = float(data1.quantity_25) - float(data1.printing_received_form_25)
#         else:
#             data1.print_wastage_form_25 = 0

#         if data1.printing_received_form_26:
#             data1.print_wastage_form_26 = float(data1.quantity_26) - float(data1.printing_received_form_26)
#         else:
#             data1.print_wastage_form_26 = 0

#         if data1.printing_received_form_27:
#             data1.print_wastage_form_27 = float(data1.quantity_27) - float(data1.printing_received_form_27)
#         else:
#             data1.print_wastage_form_27 = 0

#         if data1.printing_received_form_28:
#             data1.print_wastage_form_28 = float(data1.quantity_28) - float(data1.printing_received_form_28)
#         else:
#             data1.print_wastage_form_28 = 0

#         if data1.printing_received_form_29:
#             data1.print_wastage_form_29 = float(data1.quantity_29) - float(data1.printing_received_form_29)
#         else:
#             data1.print_wastage_form_29 = 0

#         if data1.printing_received_form_30:
#             data1.print_wastage_form_30 = float(data1.quantity_30) - float(data1.printing_received_form_30)
#         else:
#             data1.print_wastage_form_30 = 0



#         if data1.printing_received_form_31:
#             data1.print_wastage_form_31 = float(data1.quantity_31) - float(data1.printing_received_form_31)
#         else:
#             data1.print_wastage_form_31 = 0

#         if data1.printing_received_form_32:
#             data1.print_wastage_form_32 = float(data1.quantity_32) - float(data1.printing_received_form_32)
#         else:
#             data1.print_wastage_form_32 = 0

#         if data1.printing_received_form_33:
#             data1.print_wastage_form_33 = float(data1.quantity_33) - float(data1.printing_received_form_33)
#         else:
#             data1.print_wastage_form_33 = 0

#         if data1.printing_received_form_34:
#             data1.print_wastage_form_34 = float(data1.quantity_34) - float(data1.printing_received_form_34)
#         else:
#             data1.print_wastage_form_34 = 0

#         if data1.printing_received_form_35:
#             data1.print_wastage_form_35 = float(data1.quantity_35) - float(data1.printing_received_form_35)
#         else:
#             data1.print_wastage_form_35 = 0

#         if data1.printing_received_form_36:
#             data1.print_wastage_form_36 = float(data1.quantity_36) - float(data1.printing_received_form_36)
#         else:
#             data1.print_wastage_form_36 = 0

#         if data1.printing_received_form_37:
#             data1.print_wastage_form_37 = float(data1.quantity_37) - float(data1.printing_received_form_37)
#         else:
#             data1.print_wastage_form_37 = 0

#         if data1.printing_received_form_38:
#             data1.print_wastage_form_38 = float(data1.quantity_38) - float(data1.printing_received_form_38)
#         else:
#             data1.print_wastage_form_38 = 0

#         if data1.printing_received_form_39:
#             data1.print_wastage_form_39 = float(data1.quantity_39) - float(data1.printing_received_form_39)
#         else:
#             data1.print_wastage_form_39 = 0

#         if data1.printing_received_form_40:
#             data1.print_wastage_form_40 = float(data1.quantity_40) - float(data1.printing_received_form_40)
#         else:
#             data1.print_wastage_form_40 = 0




#         if data1.printing_received_form_41:
#             data1.print_wastage_form_41 = float(data1.quantity_41) - float(data1.printing_received_form_41)
#         else:
#             data1.print_wastage_form_41 = 0

#         if data1.printing_received_form_42:
#             data1.print_wastage_form_42 = float(data1.quantity_42) - float(data1.printing_received_form_42)
#         else:
#             data1.print_wastage_form_42 = 0

#         if data1.printing_received_form_43:
#             data1.print_wastage_form_43 = float(data1.quantity_43) - float(data1.printing_received_form_43)
#         else:
#             data1.print_wastage_form_43 = 0

#         if data1.printing_received_form_44:
#             data1.print_wastage_form_44 = float(data1.quantity_44) - float(data1.printing_received_form_44)
#         else:
#             data1.print_wastage_form_44 = 0

#         if data1.printing_received_form_45:
#             data1.print_wastage_form_45 = float(data1.quantity_45) - float(data1.printing_received_form_45)
#         else:
#             data1.print_wastage_form_45 = 0

#         if data1.printing_received_form_46:
#             data1.print_wastage_form_46 = float(data1.quantity_46) - float(data1.printing_received_form_46)
#         else:
#             data1.print_wastage_form_46 = 0

#         if data1.printing_received_form_47:
#             data1.print_wastage_form_47 = float(data1.quantity_47) - float(data1.printing_received_form_47)
#         else:
#             data1.print_wastage_form_47 = 0

#         if data1.printing_received_form_48:
#             data1.print_wastage_form_48 = float(data1.quantity_48) - float(data1.printing_received_form_48)
#         else:
#             data1.print_wastage_form_48 = 0

#         if data1.printing_received_form_49:
#             data1.print_wastage_form_49 = float(data1.quantity_49) - float(data1.printing_received_form_49)
#         else:
#             data1.print_wastage_form_49 = 0

#         if data1.printing_received_form_50:
#             data1.print_wastage_form_50 = float(data1.quantity_50) - float(data1.printing_received_form_50)
#         else:
#             data1.print_wastage_form_50 = 0



#         temp_print=[]
#         if data1.printing_received_form_1:
#             temp_print.append(int(data1.printing_received_form_1))
#         if data1.printing_received_form_2:
#             temp_print.append(int(data1.printing_received_form_2))
#         if data1.printing_received_form_3:
#             temp_print.append(int(data1.printing_received_form_3))
#         if data1.printing_received_form_4:
#             temp_print.append(int(data1.printing_received_form_4))
#         if data1.printing_received_form_5:
#             temp_print.append(int(data1.printing_received_form_5))
#         if data1.printing_received_form_6:
#             temp_print.append(int(data1.printing_received_form_6))
#         if data1.printing_received_form_7:
#             temp_print.append(int(data1.printing_received_form_7))
#         if data1.printing_received_form_8:
#             temp_print.append(int(data1.printing_received_form_8))
#         if data1.printing_received_form_9:
#             temp_print.append(int(data1.printing_received_form_9))
#         if data1.printing_received_form_10:
#             temp_print.append(int(data1.printing_received_form_10))

#         if data1.printing_received_form_11:
#             temp_print.append(int(data1.printing_received_form_11))
#         if data1.printing_received_form_12:
#             temp_print.append(int(data1.printing_received_form_12))
#         if data1.printing_received_form_13:
#             temp_print.append(int(data1.printing_received_form_13))
#         if data1.printing_received_form_14:
#             temp_print.append(int(data1.printing_received_form_14))
#         if data1.printing_received_form_15:
#             temp_print.append(int(data1.printing_received_form_15))
#         if data1.printing_received_form_16:
#             temp_print.append(int(data1.printing_received_form_16))
#         if data1.printing_received_form_17:
#             temp_print.append(int(data1.printing_received_form_17))
#         if data1.printing_received_form_18:
#             temp_print.append(int(data1.printing_received_form_18))
#         if data1.printing_received_form_19:
#             temp_print.append(int(data1.printing_received_form_19))
#         if data1.printing_received_form_20:
#             temp_print.append(int(data1.printing_received_form_20))

#         if data1.printing_received_form_21:
#             temp_print.append(int(data1.printing_received_form_21))
#         if data1.printing_received_form_22:
#             temp_print.append(int(data1.printing_received_form_22))
#         if data1.printing_received_form_23:
#             temp_print.append(int(data1.printing_received_form_23))
#         if data1.printing_received_form_24:
#             temp_print.append(int(data1.printing_received_form_24))
#         if data1.printing_received_form_25:
#             temp_print.append(int(data1.printing_received_form_25))
#         if data1.printing_received_form_26:
#             temp_print.append(int(data1.printing_received_form_26))
#         if data1.printing_received_form_27:
#             temp_print.append(int(data1.printing_received_form_27))
#         if data1.printing_received_form_28:
#             temp_print.append(int(data1.printing_received_form_28))
#         if data1.printing_received_form_29:
#             temp_print.append(int(data1.printing_received_form_29))
#         if data1.printing_received_form_30:
#             temp_print.append(int(data1.printing_received_form_30))

#         if data1.printing_received_form_31:
#             temp_print.append(int(data1.printing_received_form_31))
#         if data1.printing_received_form_32:
#             temp_print.append(int(data1.printing_received_form_32))
#         if data1.printing_received_form_33:
#             temp_print.append(int(data1.printing_received_form_33))
#         if data1.printing_received_form_34:
#             temp_print.append(int(data1.printing_received_form_34))
#         if data1.printing_received_form_35:
#             temp_print.append(int(data1.printing_received_form_35))
#         if data1.printing_received_form_36:
#             temp_print.append(int(data1.printing_received_form_36))
#         if data1.printing_received_form_37:
#             temp_print.append(int(data1.printing_received_form_37))
#         if data1.printing_received_form_38:
#             temp_print.append(int(data1.printing_received_form_38))
#         if data1.printing_received_form_39:
#             temp_print.append(int(data1.printing_received_form_39))
#         if data1.printing_received_form_40:
#             temp_print.append(int(data1.printing_received_form_40))

#         if data1.printing_received_form_41:
#             temp_print.append(int(data1.printing_received_form_41))
#         if data1.printing_received_form_42:
#             temp_print.append(int(data1.printing_received_form_42))
#         if data1.printing_received_form_43:
#             temp_print.append(int(data1.printing_received_form_43))
#         if data1.printing_received_form_44:
#             temp_print.append(int(data1.printing_received_form_44))
#         if data1.printing_received_form_45:
#             temp_print.append(int(data1.printing_received_form_45))
#         if data1.printing_received_form_46:
#             temp_print.append(int(data1.printing_received_form_46))
#         if data1.printing_received_form_47:
#             temp_print.append(int(data1.printing_received_form_47))
#         if data1.printing_received_form_48:
#             temp_print.append(int(data1.printing_received_form_48))
#         if data1.printing_received_form_49:
#             temp_print.append(int(data1.printing_received_form_49))
#         if data1.printing_received_form_50:
#             temp_print.append(int(data1.printing_received_form_50))


#         temp_print=[i for i in temp_print]
#         print('temp_print',temp_print)
#         data1.printing_received_form=0
#         for i in temp_print:
#             data1.printing_received_form=data1.printing_received_form+i
#         print('data1.printing_received_form',data1.printing_received_form)
        
       

        
#         if data1.printing_received_form:
#             data1.print_wastage_form = float(data1.total_quantity) - float(data1.printing_received_form)
#         else:
#             data1.print_wastage_form = 0
        
#         data1.save()
#         messages.success(request, "Updated Successfully...!!")
#         return redirect('/printing-data/') 
       
#     context = {'data1':data1}
#     return render(request, 'processing/edit_printing.html', context)











# @login_required(login_url="")
# def cutting_form(request): 
#     if request.method =='POST':
#         id = request.POST.get('id')
#         total_cutting=request.POST.get('total_cutting')
#         balance_cutting = request.POST.get('balance_cutting')


#         cutting_received_1=request.POST.get('cutting_received_1')
#         balance_cutting_1=request.POST.get('balance_cutting_1')
#         cutting_received_2=request.POST.get('cutting_received_2')
#         balance_cutting_2=request.POST.get('balance_cutting_2')
#         cutting_received_3=request.POST.get('cutting_received_3')
#         balance_cutting_3=request.POST.get('balance_cutting_3')
#         cutting_received_4=request.POST.get('cutting_received_4')
#         balance_cutting_4=request.POST.get('balance_cutting_4')
#         cutting_received_5=request.POST.get('cutting_received_5')
#         balance_cutting_5=request.POST.get('balance_cutting_5')
#         cutting_received_6=request.POST.get('cutting_received_6')
#         balance_cutting_6=request.POST.get('balance_cutting_6')
#         cutting_received_7=request.POST.get('cutting_received_7')
#         balance_cutting_7=request.POST.get('balance_cutting_7')
#         cutting_received_8=request.POST.get('cutting_received_8')
#         balance_cutting_8=request.POST.get('balance_cutting_8')
#         cutting_received_9=request.POST.get('cutting_received_9')
#         balance_cutting_9=request.POST.get('balance_cutting_9')
#         cutting_received_10=request.POST.get('cutting_received_10')
#         balance_cutting_10=request.POST.get('balance_cutting_10')

#         cutting_received_11=request.POST.get('cutting_received_11')
#         balance_cutting_11=request.POST.get('balance_cutting_11')
#         cutting_received_12=request.POST.get('cutting_received_12')
#         balance_cutting_12=request.POST.get('balance_cutting_12')
#         cutting_received_13=request.POST.get('cutting_received_13')
#         balance_cutting_13=request.POST.get('balance_cutting_13')
#         cutting_received_14=request.POST.get('cutting_received_14')
#         balance_cutting_14=request.POST.get('balance_cutting_14')
#         cutting_received_15=request.POST.get('cutting_received_15')
#         balance_cutting_15=request.POST.get('balance_cutting_15')
#         cutting_received_16=request.POST.get('cutting_received_16')
#         balance_cutting_16=request.POST.get('balance_cutting_16')
#         cutting_received_17=request.POST.get('cutting_received_17')
#         balance_cutting_17=request.POST.get('balance_cutting_17')
#         cutting_received_18=request.POST.get('cutting_received_18')
#         balance_cutting_18=request.POST.get('balance_cutting_18')
#         cutting_received_19=request.POST.get('cutting_received_19')
#         balance_cutting_19=request.POST.get('balance_cutting_19')
#         cutting_received_20=request.POST.get('cutting_received_20')
#         balance_cutting_20=request.POST.get('balance_cutting_20')

#         cutting_received_21=request.POST.get('cutting_received_21')
#         balance_cutting_21=request.POST.get('balance_cutting_21')
#         cutting_received_22=request.POST.get('cutting_received_22')
#         balance_cutting_22=request.POST.get('balance_cutting_22')
#         cutting_received_23=request.POST.get('cutting_received_23')
#         balance_cutting_23=request.POST.get('balance_cutting_23')
#         cutting_received_24=request.POST.get('cutting_received_24')
#         balance_cutting_24=request.POST.get('balance_cutting_24')
#         cutting_received_25=request.POST.get('cutting_received_25')
#         balance_cutting_25=request.POST.get('balance_cutting_25')
#         cutting_received_26=request.POST.get('cutting_received_26')
#         balance_cutting_26=request.POST.get('balance_cutting_26')
#         cutting_received_27=request.POST.get('cutting_received_27')
#         balance_cutting_27=request.POST.get('balance_cutting_27')
#         cutting_received_28=request.POST.get('cutting_received_28')
#         balance_cutting_28=request.POST.get('balance_cutting_28')
#         cutting_received_29=request.POST.get('cutting_received_29')
#         balance_cutting_29=request.POST.get('balance_cutting_29')
#         cutting_received_30=request.POST.get('cutting_received_30')
#         balance_cutting_30=request.POST.get('balance_cutting_30')

#         cutting_received_31=request.POST.get('cutting_received_31')
#         balance_cutting_31=request.POST.get('balance_cutting_31')
#         cutting_received_32=request.POST.get('cutting_received_32')
#         balance_cutting_32=request.POST.get('balance_cutting_32')
#         cutting_received_33=request.POST.get('cutting_received_33')
#         balance_cutting_33=request.POST.get('balance_cutting_33')
#         cutting_received_34=request.POST.get('cutting_received_34')
#         balance_cutting_34=request.POST.get('balance_cutting_34')
#         cutting_received_35=request.POST.get('cutting_received_35')
#         balance_cutting_35=request.POST.get('balance_cutting_35')
#         cutting_received_36=request.POST.get('cutting_received_36')
#         balance_cutting_36=request.POST.get('balance_cutting_36')
#         cutting_received_37=request.POST.get('cutting_received_37')
#         balance_cutting_37=request.POST.get('balance_cutting_37')
#         cutting_received_38=request.POST.get('cutting_received_38')
#         balance_cutting_38=request.POST.get('balance_cutting_38')
#         cutting_received_39=request.POST.get('cutting_received_39')
#         balance_cutting_39=request.POST.get('balance_cutting_39')
#         cutting_received_40=request.POST.get('cutting_received_40')
#         balance_cutting_40=request.POST.get('balance_cutting_40')

#         cutting_received_41=request.POST.get('cutting_received_41')
#         balance_cutting_41=request.POST.get('balance_cutting_41')
#         cutting_received_42=request.POST.get('cutting_received_42')
#         balance_cutting_42=request.POST.get('balance_cutting_42')
#         cutting_received_43=request.POST.get('cutting_received_43')
#         balance_cutting_43=request.POST.get('balance_cutting_43')
#         cutting_received_44=request.POST.get('cutting_received_44')
#         balance_cutting_44=request.POST.get('balance_cutting_44')
#         cutting_received_45=request.POST.get('cutting_received_45')
#         balance_cutting_45=request.POST.get('balance_cutting_45')
#         cutting_received_46=request.POST.get('cutting_received_46')
#         balance_cutting_46=request.POST.get('balance_cutting_46')
#         cutting_received_47=request.POST.get('cutting_received_47')
#         balance_cutting_47=request.POST.get('balance_cutting_47')
#         cutting_received_48=request.POST.get('cutting_received_48')
#         balance_cutting_48=request.POST.get('balance_cutting_48')
#         cutting_received_49=request.POST.get('cutting_received_49')
#         balance_cutting_49=request.POST.get('balance_cutting_49')
#         cutting_received_50=request.POST.get('cutting_received_50')
#         balance_cutting_50=request.POST.get('balance_cutting_50')

#         cutting_date = request.POST.get('cutting_date')
#         order = orders.objects.filter(order_id=id).get()
#         print('order',order)
#         order.cutting_received_1=cutting_received_1
#         order.balance_cutting_1=balance_cutting_1
#         order.cutting_received_2=cutting_received_2
#         order.balance_cutting_2=balance_cutting_2
#         order.cutting_received_3=cutting_received_3
#         order.balance_cutting_3=balance_cutting_3
#         order.cutting_received_4=cutting_received_4
#         order.balance_cutting_4=balance_cutting_4
#         order.cutting_received_5=cutting_received_5
#         order.balance_cutting_5=balance_cutting_5
#         order.cutting_received_6=cutting_received_6
#         order.balance_cutting_6=balance_cutting_6
#         order.cutting_received_7=cutting_received_7
#         order.balance_cutting_7=balance_cutting_7
#         order.cutting_received_8=cutting_received_8
#         order.balance_cutting_8=balance_cutting_8
#         order.cutting_received_9=cutting_received_9
#         order.balance_cutting_9=balance_cutting_9
#         order.cutting_received_10=cutting_received_10
#         order.balance_cutting_10=balance_cutting_10

#         order.cutting_received_11=cutting_received_11
#         order.balance_cutting_11=balance_cutting_11
#         order.cutting_received_12=cutting_received_12
#         order.balance_cutting_12=balance_cutting_12
#         order.cutting_received_13=cutting_received_13
#         order.balance_cutting_13=balance_cutting_13
#         order.cutting_received_14=cutting_received_14
#         order.balance_cutting_14=balance_cutting_14
#         order.cutting_received_15=cutting_received_15
#         order.balance_cutting_15=balance_cutting_15
#         order.cutting_received_16=cutting_received_16
#         order.balance_cutting_16=balance_cutting_16
#         order.cutting_received_17=cutting_received_17
#         order.balance_cutting_17=balance_cutting_17
#         order.cutting_received_18=cutting_received_18
#         order.balance_cutting_18=balance_cutting_18
#         order.cutting_received_19=cutting_received_19
#         order.balance_cutting_19=balance_cutting_19
#         order.cutting_received_20=cutting_received_20
#         order.balance_cutting_20=balance_cutting_20

#         order.cutting_received_21=cutting_received_21
#         order.balance_cutting_21=balance_cutting_21
#         order.cutting_received_22=cutting_received_22
#         order.balance_cutting_22=balance_cutting_22
#         order.cutting_received_23=cutting_received_23
#         order.balance_cutting_23=balance_cutting_23
#         order.cutting_received_24=cutting_received_24
#         order.balance_cutting_24=balance_cutting_24
#         order.cutting_received_25=cutting_received_25
#         order.balance_cutting_25=balance_cutting_25
#         order.cutting_received_26=cutting_received_26
#         order.balance_cutting_26=balance_cutting_26
#         order.cutting_received_27=cutting_received_27
#         order.balance_cutting_27=balance_cutting_27
#         order.cutting_received_28=cutting_received_28
#         order.balance_cutting_28=balance_cutting_28
#         order.cutting_received_29=cutting_received_29
#         order.balance_cutting_29=balance_cutting_29
#         order.cutting_received_30=cutting_received_30
#         order.balance_cutting_30=balance_cutting_30

#         order.cutting_received_31=cutting_received_31
#         order.balance_cutting_31=balance_cutting_31
#         order.cutting_received_32=cutting_received_32
#         order.balance_cutting_32=balance_cutting_32
#         order.cutting_received_33=cutting_received_33
#         order.balance_cutting_33=balance_cutting_33
#         order.cutting_received_34=cutting_received_34
#         order.balance_cutting_34=balance_cutting_34
#         order.cutting_received_35=cutting_received_35
#         order.balance_cutting_35=balance_cutting_35
#         order.cutting_received_36=cutting_received_36
#         order.balance_cutting_36=balance_cutting_36
#         order.cutting_received_37=cutting_received_37
#         order.balance_cutting_37=balance_cutting_37
#         order.cutting_received_38=cutting_received_38
#         order.balance_cutting_38=balance_cutting_38
#         order.cutting_received_39=cutting_received_39
#         order.balance_cutting_39=balance_cutting_39
#         order.cutting_received_40=cutting_received_40
#         order.balance_cutting_40=balance_cutting_40

#         order.cutting_received_41=cutting_received_41
#         order.balance_cutting_41=balance_cutting_41
#         order.cutting_received_42=cutting_received_42
#         order.balance_cutting_42=balance_cutting_42
#         order.cutting_received_43=cutting_received_43
#         order.balance_cutting_43=balance_cutting_43
#         order.cutting_received_44=cutting_received_44
#         order.balance_cutting_44=balance_cutting_44
#         order.cutting_received_45=cutting_received_45
#         order.balance_cutting_45=balance_cutting_45
#         order.cutting_received_46=cutting_received_46
#         order.balance_cutting_46=balance_cutting_46
#         order.cutting_received_47=cutting_received_47
#         order.balance_cutting_47=balance_cutting_47
#         order.cutting_received_48=cutting_received_48
#         order.balance_cutting_48=balance_cutting_48
#         order.cutting_received_49=cutting_received_49
#         order.balance_cutting_49=balance_cutting_49
#         order.cutting_received_50=cutting_received_50
#         order.balance_cutting_50=balance_cutting_50

        


#         order.total_cutting=total_cutting
#         order.balance_cutting=balance_cutting
#         order.cutting_date=datetime.datetime.now()
#         order.save()
    
#     data1 = orders.objects.all().order_by('-order_id')    
#     context={
#         'data1':data1,       
#     }
#     return render(request,'processing/cutting.html',context)



# @login_required(login_url="")
# def edit_cutting(request, order_id):
#     data1 = orders.objects.get(order_id=order_id)
#     print('gjhgjmgj',order_id)

#     if request.method == 'POST':
#         data1.total_cutting = request.POST.get('total_cutting')

#         data1.cutting_received_1=request.POST.get('cutting_received_1')
#         data1.cutting_received_2=request.POST.get('cutting_received_2')
#         data1.cutting_received_3=request.POST.get('cutting_received_3')
#         data1.cutting_received_4=request.POST.get('cutting_received_4')
#         data1.cutting_received_5=request.POST.get('cutting_received_5')
#         data1.cutting_received_6=request.POST.get('cutting_received_6')
#         data1.cutting_received_7=request.POST.get('cutting_received_7')
#         data1.cutting_received_8=request.POST.get('cutting_received_8')
#         data1.cutting_received_9=request.POST.get('cutting_received_9')
#         data1.cutting_received_10=request.POST.get('cutting_received_10')

#         data1.cutting_received_11=request.POST.get('cutting_received_11')
#         data1.cutting_received_12=request.POST.get('cutting_received_12')
#         data1.cutting_received_13=request.POST.get('cutting_received_13')
#         data1.cutting_received_14=request.POST.get('cutting_received_14')
#         data1.cutting_received_15=request.POST.get('cutting_received_15')
#         data1.cutting_received_16=request.POST.get('cutting_received_16')
#         data1.cutting_received_17=request.POST.get('cutting_received_17')
#         data1.cutting_received_18=request.POST.get('cutting_received_18')
#         data1.cutting_received_19=request.POST.get('cutting_received_19')
#         data1.cutting_received_20=request.POST.get('cutting_received_20')

#         data1.cutting_received_21=request.POST.get('cutting_received_21')
#         data1.cutting_received_22=request.POST.get('cutting_received_22')
#         data1.cutting_received_23=request.POST.get('cutting_received_23')
#         data1.cutting_received_24=request.POST.get('cutting_received_24')
#         data1.cutting_received_25=request.POST.get('cutting_received_25')
#         data1.cutting_received_26=request.POST.get('cutting_received_26')
#         data1.cutting_received_27=request.POST.get('cutting_received_27')
#         data1.cutting_received_28=request.POST.get('cutting_received_28')
#         data1.cutting_received_29=request.POST.get('cutting_received_29')
#         data1.cutting_received_30=request.POST.get('cutting_received_30')

#         data1.cutting_received_31=request.POST.get('cutting_received_31')
#         data1.cutting_received_32=request.POST.get('cutting_received_32')
#         data1.cutting_received_33=request.POST.get('cutting_received_33')
#         data1.cutting_received_34=request.POST.get('cutting_received_34')
#         data1.cutting_received_35=request.POST.get('cutting_received_35')
#         data1.cutting_received_36=request.POST.get('cutting_received_36')
#         data1.cutting_received_37=request.POST.get('cutting_received_37')
#         data1.cutting_received_38=request.POST.get('cutting_received_38')
#         data1.cutting_received_39=request.POST.get('cutting_received_39')
#         data1.cutting_received_40=request.POST.get('cutting_received_40')

#         data1.cutting_received_41=request.POST.get('cutting_received_41')
#         data1.cutting_received_42=request.POST.get('cutting_received_42')
#         data1.cutting_received_43=request.POST.get('cutting_received_43')
#         data1.cutting_received_44=request.POST.get('cutting_received_44')
#         data1.cutting_received_45=request.POST.get('cutting_received_45')
#         data1.cutting_received_46=request.POST.get('cutting_received_46')
#         data1.cutting_received_47=request.POST.get('cutting_received_47')
#         data1.cutting_received_48=request.POST.get('cutting_received_48')
#         data1.cutting_received_49=request.POST.get('cutting_received_49')
#         data1.cutting_received_50=request.POST.get('cutting_received_50')
    
#         data1.cutting_date = datetime.datetime.now()
        
#         if data1.cutting_received_1:
#             data1.balance_cutting_1 = float(data1.quantity_1) - float(data1.cutting_received_1)
#         else:
#             data1.cutting_received_1 = 0
        
#         if data1.cutting_received_2:
#             data1.balance_cutting_2 = float(data1.quantity_2) - float(data1.cutting_received_2)
#         else:
#             data1.cutting_received_2 = 0

#         if data1.cutting_received_3:
#             data1.balance_cutting_3 = float(data1.quantity_3) - float(data1.cutting_received_3)
#         else:
#             data1.cutting_received_3 = 0

#         if data1.cutting_received_4:
#             data1.balance_cutting_4 = float(data1.quantity_4) - float(data1.cutting_received_4)
#         else:
#             data1.cutting_received_4 = 0

#         if data1.cutting_received_5:
#             data1.balance_cutting_5 = float(data1.quantity_5) - float(data1.cutting_received_5)
#         else:
#             data1.cutting_received_5 = 0

#         if data1.cutting_received_6:
#             data1.balance_cutting_6 = float(data1.quantity_6) - float(data1.cutting_received_6)
#         else:
#             data1.cutting_received_6 = 0

#         if data1.cutting_received_7:
#             data1.balance_cutting_7 = float(data1.quantity_7) - float(data1.cutting_received_7)
#         else:
#             data1.cutting_received_7 = 0

#         if data1.cutting_received_8:
#             data1.balance_cutting_8 = float(data1.quantity_8) - float(data1.cutting_received_8)
#         else:
#             data1.cutting_received_8 = 0

#         if data1.cutting_received_9:
#             data1.balance_cutting_9 = float(data1.quantity_9) - float(data1.cutting_received_9)
#         else:
#             data1.cutting_received_9 = 0

#         if data1.cutting_received_10:
#             data1.balance_cutting_10 = float(data1.quantity_10) - float(data1.cutting_received_10)
#         else:
#             data1.cutting_received_10 = 0


#         if data1.cutting_received_11:
#             data1.balance_cutting_11 = float(data1.quantity_11) - float(data1.cutting_received_11)
#         else:
#             data1.cutting_received_11 = 0
        
#         if data1.cutting_received_12:
#             data1.balance_cutting_12 = float(data1.quantity_12) - float(data1.cutting_received_12)
#         else:
#             data1.cutting_received_12 = 0

#         if data1.cutting_received_13:
#             data1.balance_cutting_13 = float(data1.quantity_13) - float(data1.cutting_received_13)
#         else:
#             data1.cutting_received_13 = 0

#         if data1.cutting_received_14:
#             data1.balance_cutting_14 = float(data1.quantity_14) - float(data1.cutting_received_14)
#         else:
#             data1.cutting_received_14 = 0

#         if data1.cutting_received_15:
#             data1.balance_cutting_15 = float(data1.quantity_15) - float(data1.cutting_received_15)
#         else:
#             data1.cutting_received_15 = 0

#         if data1.cutting_received_16:
#             data1.balance_cutting_16 = float(data1.quantity_16) - float(data1.cutting_received_16)
#         else:
#             data1.cutting_received_16 = 0

#         if data1.cutting_received_17:
#             data1.balance_cutting_17 = float(data1.quantity_17) - float(data1.cutting_received_17)
#         else:
#             data1.cutting_received_17 = 0

#         if data1.cutting_received_18:
#             data1.balance_cutting_18 = float(data1.quantity_18) - float(data1.cutting_received_18)
#         else:
#             data1.cutting_received_18 = 0

#         if data1.cutting_received_19:
#             data1.balance_cutting_19 = float(data1.quantity_19) - float(data1.cutting_received_19)
#         else:
#             data1.cutting_received_19 = 0

#         if data1.cutting_received_20:
#             data1.balance_cutting_20 = float(data1.quantity_20) - float(data1.cutting_received_20)
#         else:
#             data1.cutting_received_20 = 0


#         if data1.cutting_received_21:
#             data1.balance_cutting_21 = float(data1.quantity_21) - float(data1.cutting_received_21)
#         else:
#             data1.cutting_received_21 = 0
        
#         if data1.cutting_received_22:
#             data1.balance_cutting_22 = float(data1.quantity_22) - float(data1.cutting_received_22)
#         else:
#             data1.cutting_received_22 = 0

#         if data1.cutting_received_23:
#             data1.balance_cutting_23 = float(data1.quantity_23) - float(data1.cutting_received_23)
#         else:
#             data1.cutting_received_23 = 0

#         if data1.cutting_received_24:
#             data1.balance_cutting_24 = float(data1.quantity_24) - float(data1.cutting_received_24)
#         else:
#             data1.cutting_received_24 = 0

#         if data1.cutting_received_25:
#             data1.balance_cutting_25 = float(data1.quantity_25) - float(data1.cutting_received_25)
#         else:
#             data1.cutting_received_25 = 0

#         if data1.cutting_received_26:
#             data1.balance_cutting_26 = float(data1.quantity_26) - float(data1.cutting_received_26)
#         else:
#             data1.cutting_received_26 = 0

#         if data1.cutting_received_27:
#             data1.balance_cutting_27 = float(data1.quantity_27) - float(data1.cutting_received_27)
#         else:
#             data1.cutting_received_27 = 0

#         if data1.cutting_received_28:
#             data1.balance_cutting_28 = float(data1.quantity_28) - float(data1.cutting_received_28)
#         else:
#             data1.cutting_received_28 = 0

#         if data1.cutting_received_29:
#             data1.balance_cutting_29 = float(data1.quantity_29) - float(data1.cutting_received_29)
#         else:
#             data1.cutting_received_29 = 0

#         if data1.cutting_received_30:
#             data1.balance_cutting_30 = float(data1.quantity_30) - float(data1.cutting_received_30)
#         else:
#             data1.cutting_received_30 = 0


#         if data1.cutting_received_31:
#             data1.balance_cutting_31 = float(data1.quantity_31) - float(data1.cutting_received_31)
#         else:
#             data1.cutting_received_31 = 0
        
#         if data1.cutting_received_32:
#             data1.balance_cutting_32 = float(data1.quantity_32) - float(data1.cutting_received_32)
#         else:
#             data1.cutting_received_32 = 0

#         if data1.cutting_received_33:
#             data1.balance_cutting_33 = float(data1.quantity_33) - float(data1.cutting_received_33)
#         else:
#             data1.cutting_received_33 = 0

#         if data1.cutting_received_34:
#             data1.balance_cutting_34 = float(data1.quantity_34) - float(data1.cutting_received_34)
#         else:
#             data1.cutting_received_34 = 0

#         if data1.cutting_received_35:
#             data1.balance_cutting_35 = float(data1.quantity_35) - float(data1.cutting_received_35)
#         else:
#             data1.cutting_received_35 = 0

#         if data1.cutting_received_36:
#             data1.balance_cutting_36 = float(data1.quantity_36) - float(data1.cutting_received_36)
#         else:
#             data1.cutting_received_36 = 0

#         if data1.cutting_received_37:
#             data1.balance_cutting_37 = float(data1.quantity_37) - float(data1.cutting_received_37)
#         else:
#             data1.cutting_received_37 = 0

#         if data1.cutting_received_38:
#             data1.balance_cutting_38 = float(data1.quantity_38) - float(data1.cutting_received_38)
#         else:
#             data1.cutting_received_38 = 0

#         if data1.cutting_received_39:
#             data1.balance_cutting_39 = float(data1.quantity_39) - float(data1.cutting_received_39)
#         else:
#             data1.cutting_received_39 = 0

#         if data1.cutting_received_40:
#             data1.balance_cutting_40 = float(data1.quantity_40) - float(data1.cutting_received_40)
#         else:
#             data1.cutting_received_40 = 0


#         if data1.cutting_received_41:
#             data1.balance_cutting_41 = float(data1.quantity_41) - float(data1.cutting_received_41)
#         else:
#             data1.cutting_received_41 = 0
        
#         if data1.cutting_received_42:
#             data1.balance_cutting_42 = float(data1.quantity_42) - float(data1.cutting_received_42)
#         else:
#             data1.cutting_received_42 = 0

#         if data1.cutting_received_43:
#             data1.balance_cutting_43 = float(data1.quantity_43) - float(data1.cutting_received_43)
#         else:
#             data1.cutting_received_43 = 0

#         if data1.cutting_received_44:
#             data1.balance_cutting_44 = float(data1.quantity_44) - float(data1.cutting_received_44)
#         else:
#             data1.cutting_received_44 = 0

#         if data1.cutting_received_45:
#             data1.balance_cutting_45 = float(data1.quantity_45) - float(data1.cutting_received_45)
#         else:
#             data1.cutting_received_45 = 0

#         if data1.cutting_received_46:
#             data1.balance_cutting_46 = float(data1.quantity_46) - float(data1.cutting_received_46)
#         else:
#             data1.cutting_received_46 = 0

#         if data1.cutting_received_47:
#             data1.balance_cutting_47 = float(data1.quantity_47) - float(data1.cutting_received_47)
#         else:
#             data1.cutting_received_47 = 0

#         if data1.cutting_received_48:
#             data1.balance_cutting_48 = float(data1.quantity_48) - float(data1.cutting_received_48)
#         else:
#             data1.cutting_received_48 = 0

#         if data1.cutting_received_49:
#             data1.balance_cutting_49 = float(data1.quantity_49) - float(data1.cutting_received_49)
#         else:
#             data1.cutting_received_49 = 0

#         if data1.cutting_received_50:
#             data1.balance_cutting_50 = float(data1.quantity_50) - float(data1.cutting_received_50)
#         else:
#             data1.cutting_received_50 = 0

        

#         temp_cut=[]
#         if data1.cutting_received_1:
#             temp_cut.append(int(data1.cutting_received_1))
#         if data1.cutting_received_2:
#             temp_cut.append(int(data1.cutting_received_2))
#         if data1.cutting_received_3:
#             temp_cut.append(int(data1.cutting_received_3))
#         if data1.cutting_received_4:
#             temp_cut.append(int(data1.cutting_received_4))
#         if data1.cutting_received_5:
#             temp_cut.append(int(data1.cutting_received_5))
#         if data1.cutting_received_6:
#             temp_cut.append(int(data1.cutting_received_6))
#         if data1.cutting_received_7:
#             temp_cut.append(int(data1.cutting_received_7))
#         if data1.cutting_received_8:
#             temp_cut.append(int(data1.cutting_received_8))
#         if data1.cutting_received_9:
#             temp_cut.append(int(data1.cutting_received_9))
#         if data1.cutting_received_10:
#             temp_cut.append(int(data1.cutting_received_10))

#         if data1.cutting_received_11:
#             temp_cut.append(int(data1.cutting_received_11))
#         if data1.cutting_received_12:
#             temp_cut.append(int(data1.cutting_received_12))
#         if data1.cutting_received_13:
#             temp_cut.append(int(data1.cutting_received_13))
#         if data1.cutting_received_14:
#             temp_cut.append(int(data1.cutting_received_14))
#         if data1.cutting_received_15:
#             temp_cut.append(int(data1.cutting_received_15))
#         if data1.cutting_received_16:
#             temp_cut.append(int(data1.cutting_received_16))
#         if data1.cutting_received_17:
#             temp_cut.append(int(data1.cutting_received_17))
#         if data1.cutting_received_18:
#             temp_cut.append(int(data1.cutting_received_18))
#         if data1.cutting_received_19:
#             temp_cut.append(int(data1.cutting_received_19))
#         if data1.cutting_received_20:
#             temp_cut.append(int(data1.cutting_received_20))

#         if data1.cutting_received_21:
#             temp_cut.append(int(data1.cutting_received_21))
#         if data1.cutting_received_22:
#             temp_cut.append(int(data1.cutting_received_22))
#         if data1.cutting_received_23:
#             temp_cut.append(int(data1.cutting_received_23))
#         if data1.cutting_received_24:
#             temp_cut.append(int(data1.cutting_received_24))
#         if data1.cutting_received_25:
#             temp_cut.append(int(data1.cutting_received_25))
#         if data1.cutting_received_26:
#             temp_cut.append(int(data1.cutting_received_26))
#         if data1.cutting_received_27:
#             temp_cut.append(int(data1.cutting_received_27))
#         if data1.cutting_received_28:
#             temp_cut.append(int(data1.cutting_received_28))
#         if data1.cutting_received_29:
#             temp_cut.append(int(data1.cutting_received_29))
#         if data1.cutting_received_30:
#             temp_cut.append(int(data1.cutting_received_30))

#         if data1.cutting_received_31:
#             temp_cut.append(int(data1.cutting_received_31))
#         if data1.cutting_received_32:
#             temp_cut.append(int(data1.cutting_received_32))
#         if data1.cutting_received_33:
#             temp_cut.append(int(data1.cutting_received_33))
#         if data1.cutting_received_34:
#             temp_cut.append(int(data1.cutting_received_34))
#         if data1.cutting_received_35:
#             temp_cut.append(int(data1.cutting_received_35))
#         if data1.cutting_received_36:
#             temp_cut.append(int(data1.cutting_received_36))
#         if data1.cutting_received_37:
#             temp_cut.append(int(data1.cutting_received_37))
#         if data1.cutting_received_38:
#             temp_cut.append(int(data1.cutting_received_38))
#         if data1.cutting_received_39:
#             temp_cut.append(int(data1.cutting_received_39))
#         if data1.cutting_received_40:
#             temp_cut.append(int(data1.cutting_received_40))

#         if data1.cutting_received_41:
#             temp_cut.append(int(data1.cutting_received_41))
#         if data1.cutting_received_42:
#             temp_cut.append(int(data1.cutting_received_42))
#         if data1.cutting_received_43:
#             temp_cut.append(int(data1.cutting_received_43))
#         if data1.cutting_received_44:
#             temp_cut.append(int(data1.cutting_received_44))
#         if data1.cutting_received_45:
#             temp_cut.append(int(data1.cutting_received_45))
#         if data1.cutting_received_46:
#             temp_cut.append(int(data1.cutting_received_46))
#         if data1.cutting_received_47:
#             temp_cut.append(int(data1.cutting_received_47))
#         if data1.cutting_received_48:
#             temp_cut.append(int(data1.cutting_received_48))
#         if data1.cutting_received_49:
#             temp_cut.append(int(data1.cutting_received_49))
#         if data1.cutting_received_50:
#             temp_cut.append(int(data1.cutting_received_50))

        
#         temp_cut=[i for i in temp_cut]
#         data1.total_cutting=0
#         for i in temp_cut:
#             data1.total_cutting=data1.total_cutting+i
        

#         if data1.total_cutting:
#             data1.balance_cutting = float(data1.total_quantity) - float(data1.total_cutting)
#         else:
#             data1.balance_cutting = 0
        
#         data1.save()
#         messages.success(request, "Updated Successfully...!!")
#         return redirect('/cutting-data/')
       
#     context = {'data1':data1}
#     return render(request, 'processing/edit_cutting.html', context)






 




# @login_required(login_url="")
# def binding_data(request):
#     if request.method =='POST':
#         id = request.POST.get('id')
#         total_binding=request.POST.get('total_binding')
#         balance_binding = request.POST.get('balance_binding')

#         binding_received_1=request.POST.get('binding_received_1')
#         balance_binding_1=request.POST.get('balance_binding_1')
#         binding_received_2=request.POST.get('binding_received_2')
#         balance_binding_2=request.POST.get('balance_binding_2')
#         binding_received_3=request.POST.get('binding_received_3')
#         balance_binding_3=request.POST.get('balance_binding_3')
#         binding_received_4=request.POST.get('binding_received_4')
#         balance_binding_4=request.POST.get('balance_binding_4')
#         binding_received_5=request.POST.get('binding_received_5')
#         balance_binding_5=request.POST.get('balance_binding_5')
#         binding_received_6=request.POST.get('binding_received_6')
#         balance_binding_6=request.POST.get('balance_binding_6')
#         binding_received_7=request.POST.get('binding_received_7')
#         balance_binding_7=request.POST.get('balance_binding_7')
#         binding_received_8=request.POST.get('binding_received_8')
#         balance_binding_8=request.POST.get('balance_binding_8')
#         binding_received_9=request.POST.get('binding_received_9')
#         balance_binding_9=request.POST.get('balance_binding_9')
#         binding_received_10=request.POST.get('binding_received_10')
#         balance_binding_10=request.POST.get('balance_binding_10')

#         binding_received_11=request.POST.get('binding_received_11')
#         balance_binding_11=request.POST.get('balance_binding_11')
#         binding_received_12=request.POST.get('binding_received_12')
#         balance_binding_12=request.POST.get('balance_binding_12')
#         binding_received_13=request.POST.get('binding_received_13')
#         balance_binding_13=request.POST.get('balance_binding_13')
#         binding_received_14=request.POST.get('binding_received_14')
#         balance_binding_14=request.POST.get('balance_binding_14')
#         binding_received_15=request.POST.get('binding_received_15')
#         balance_binding_15=request.POST.get('balance_binding_15')
#         binding_received_16=request.POST.get('binding_received_16')
#         balance_binding_16=request.POST.get('balance_binding_16')
#         binding_received_17=request.POST.get('binding_received_17')
#         balance_binding_17=request.POST.get('balance_binding_17')
#         binding_received_18=request.POST.get('binding_received_18')
#         balance_binding_18=request.POST.get('balance_binding_18')
#         binding_received_19=request.POST.get('binding_received_19')
#         balance_binding_19=request.POST.get('balance_binding_19')
#         binding_received_20=request.POST.get('binding_received_20')
#         balance_binding_20=request.POST.get('balance_binding_20')

#         binding_received_21=request.POST.get('binding_received_21')
#         balance_binding_21=request.POST.get('balance_binding_21')
#         binding_received_22=request.POST.get('binding_received_22')
#         balance_binding_22=request.POST.get('balance_binding_22')
#         binding_received_23=request.POST.get('binding_received_23')
#         balance_binding_23=request.POST.get('balance_binding_23')
#         binding_received_24=request.POST.get('binding_received_24')
#         balance_binding_24=request.POST.get('balance_binding_24')
#         binding_received_25=request.POST.get('binding_received_25')
#         balance_binding_25=request.POST.get('balance_binding_25')
#         binding_received_26=request.POST.get('binding_received_26')
#         balance_binding_26=request.POST.get('balance_binding_26')
#         binding_received_27=request.POST.get('binding_received_27')
#         balance_binding_27=request.POST.get('balance_binding_27')
#         binding_received_28=request.POST.get('binding_received_28')
#         balance_binding_28=request.POST.get('balance_binding_28')
#         binding_received_29=request.POST.get('binding_received_29')
#         balance_binding_29=request.POST.get('balance_binding_29')
#         binding_received_30=request.POST.get('binding_received_30')
#         balance_binding_30=request.POST.get('balance_binding_30')

#         binding_received_31=request.POST.get('binding_received_31')
#         balance_binding_31=request.POST.get('balance_binding_31')
#         binding_received_32=request.POST.get('binding_received_32')
#         balance_binding_32=request.POST.get('balance_binding_32')
#         binding_received_33=request.POST.get('binding_received_33')
#         balance_binding_33=request.POST.get('balance_binding_33')
#         binding_received_34=request.POST.get('binding_received_34')
#         balance_binding_34=request.POST.get('balance_binding_34')
#         binding_received_35=request.POST.get('binding_received_35')
#         balance_binding_35=request.POST.get('balance_binding_35')
#         binding_received_36=request.POST.get('binding_received_36')
#         balance_binding_36=request.POST.get('balance_binding_36')
#         binding_received_37=request.POST.get('binding_received_37')
#         balance_binding_37=request.POST.get('balance_binding_37')
#         binding_received_38=request.POST.get('binding_received_38')
#         balance_binding_38=request.POST.get('balance_binding_38')
#         binding_received_39=request.POST.get('binding_received_39')
#         balance_binding_39=request.POST.get('balance_binding_39')
#         binding_received_40=request.POST.get('binding_received_40')
#         balance_binding_40=request.POST.get('balance_binding_40')

#         binding_received_41=request.POST.get('binding_received_41')
#         balance_binding_41=request.POST.get('balance_binding_41')
#         binding_received_42=request.POST.get('binding_received_42')
#         balance_binding_42=request.POST.get('balance_binding_42')
#         binding_received_43=request.POST.get('binding_received_43')
#         balance_binding_43=request.POST.get('balance_binding_43')
#         binding_received_44=request.POST.get('binding_received_44')
#         balance_binding_44=request.POST.get('balance_binding_44')
#         binding_received_45=request.POST.get('binding_received_45')
#         balance_binding_45=request.POST.get('balance_binding_45')
#         binding_received_46=request.POST.get('binding_received_46')
#         balance_binding_46=request.POST.get('balance_binding_46')
#         binding_received_47=request.POST.get('binding_received_47')
#         balance_binding_47=request.POST.get('balance_binding_47')
#         binding_received_48=request.POST.get('binding_received_48')
#         balance_binding_48=request.POST.get('balance_binding_48')
#         binding_received_49=request.POST.get('binding_received_49')
#         balance_binding_49=request.POST.get('balance_binding_49')
#         binding_received_50=request.POST.get('binding_received_50')
#         balance_binding_50=request.POST.get('balance_binding_50')
#         binding_date = request.POST.get('print_date')

#         order = orders.objects.filter(order_id=id).get()
#         print('order',order)
#         order.binding_received_1=binding_received_1
#         order.balance_binding_1=balance_binding_1
#         order.binding_received_2=binding_received_2
#         order.balance_binding_2=balance_binding_2
#         order.binding_received_3=binding_received_3
#         order.balance_binding_3=balance_binding_3
#         order.binding_received_4=binding_received_4
#         order.balance_binding_4=balance_binding_4
#         order.binding_received_5=binding_received_5
#         order.balance_binding_5=balance_binding_5
#         order.binding_received_6=binding_received_6
#         order.balance_binding_6=balance_binding_6
#         order.binding_received_7=binding_received_7
#         order.balance_binding_7=balance_binding_7
#         order.binding_received_8=binding_received_8
#         order.balance_binding_8=balance_binding_8
#         order.binding_received_9=binding_received_9
#         order.balance_binding_9=balance_binding_9
#         order.binding_received_10=binding_received_10
#         order.balance_binding_10=balance_binding_10

#         order.binding_received_11=binding_received_11
#         order.balance_binding_11=balance_binding_11
#         order.binding_received_12=binding_received_12
#         order.balance_binding_12=balance_binding_12
#         order.binding_received_13=binding_received_13
#         order.balance_binding_13=balance_binding_13
#         order.binding_received_14=binding_received_14
#         order.balance_binding_14=balance_binding_14
#         order.binding_received_15=binding_received_15
#         order.balance_binding_15=balance_binding_15
#         order.binding_received_16=binding_received_16
#         order.balance_binding_16=balance_binding_16
#         order.binding_received_17=binding_received_17
#         order.balance_binding_17=balance_binding_17
#         order.binding_received_18=binding_received_18
#         order.balance_binding_18=balance_binding_18
#         order.binding_received_19=binding_received_19
#         order.balance_binding_19=balance_binding_19
#         order.binding_received_20=binding_received_20
#         order.balance_binding_20=balance_binding_20

#         order.binding_received_21=binding_received_21
#         order.balance_binding_21=balance_binding_21
#         order.binding_received_22=binding_received_22
#         order.balance_binding_22=balance_binding_22
#         order.binding_received_23=binding_received_23
#         order.balance_binding_23=balance_binding_23
#         order.binding_received_24=binding_received_24
#         order.balance_binding_24=balance_binding_24
#         order.binding_received_25=binding_received_25
#         order.balance_binding_25=balance_binding_25
#         order.binding_received_26=binding_received_26
#         order.balance_binding_26=balance_binding_26
#         order.binding_received_27=binding_received_27
#         order.balance_binding_27=balance_binding_27
#         order.binding_received_28=binding_received_28
#         order.balance_binding_28=balance_binding_28
#         order.binding_received_29=binding_received_29
#         order.balance_binding_29=balance_binding_29
#         order.binding_received_30=binding_received_30
#         order.balance_binding_30=balance_binding_30

#         order.binding_received_31=binding_received_31
#         order.balance_binding_31=balance_binding_31
#         order.binding_received_32=binding_received_32
#         order.balance_binding_32=balance_binding_32
#         order.binding_received_33=binding_received_33
#         order.balance_binding_33=balance_binding_33
#         order.binding_received_34=binding_received_34
#         order.balance_binding_34=balance_binding_34
#         order.binding_received_35=binding_received_35
#         order.balance_binding_35=balance_binding_35
#         order.binding_received_36=binding_received_36
#         order.balance_binding_36=balance_binding_36
#         order.binding_received_37=binding_received_37
#         order.balance_binding_37=balance_binding_37
#         order.binding_received_38=binding_received_38
#         order.balance_binding_38=balance_binding_38
#         order.binding_received_39=binding_received_39
#         order.balance_binding_39=balance_binding_39
#         order.binding_received_40=binding_received_40
#         order.balance_binding_40=balance_binding_40

#         order.binding_received_41=binding_received_41
#         order.balance_binding_41=balance_binding_41
#         order.binding_received_42=binding_received_42
#         order.balance_binding_42=balance_binding_42
#         order.binding_received_43=binding_received_43
#         order.balance_binding_43=balance_binding_43
#         order.binding_received_44=binding_received_44
#         order.balance_binding_44=balance_binding_44
#         order.binding_received_45=binding_received_45
#         order.balance_binding_45=balance_binding_45
#         order.binding_received_46=binding_received_46
#         order.balance_binding_46=balance_binding_46
#         order.binding_received_47=binding_received_47
#         order.balance_binding_47=balance_binding_47
#         order.binding_received_48=binding_received_48
#         order.balance_binding_48=balance_binding_48
#         order.binding_received_49=binding_received_49
#         order.balance_binding_49=balance_binding_49
#         order.binding_received_50=binding_received_50
#         order.balance_binding_50=balance_binding_50

#         order.total_binding=total_binding
#         order.balance_binding=balance_binding 
#         order.binding_date=datetime.datetime.now()
#         order.save()

#     data1 = orders.objects.all().order_by('-order_id')    
#     context={
#         'data1':data1,       
#     }
#     return render(request,'processing/bindings.html',context) 




# @login_required(login_url="")
# def edit_binding(request,order_id):
#     data2 = orders.objects.get(order_id=order_id)
#     print('gjhgjmgj',order_id)

#     if request.method == 'POST':
#         id = request.POST.get('id')
#         data2.total_binding=request.POST.get('total_binding')
#         data2.balance_binding = request.POST.get('balance_binding')

#         data2.binding_received_1=request.POST.get('binding_received_1')
#         data2.binding_received_2=request.POST.get('binding_received_2')
#         data2.binding_received_3=request.POST.get('binding_received_3')
#         data2.binding_received_4=request.POST.get('binding_received_4')
#         data2.binding_received_5=request.POST.get('binding_received_5')
#         data2.binding_received_6=request.POST.get('binding_received_6')
#         data2.binding_received_7=request.POST.get('binding_received_7')
#         data2.binding_received_8=request.POST.get('binding_received_8')
#         data2.binding_received_9=request.POST.get('binding_received_9')
#         data2.binding_received_10=request.POST.get('binding_received_10')
    

#         data2.binding_received_11=request.POST.get('binding_received_11')
#         data2.binding_received_12=request.POST.get('binding_received_12')
#         data2.binding_received_13=request.POST.get('binding_received_13')
#         data2.binding_received_14=request.POST.get('binding_received_14')
#         data2.binding_received_15=request.POST.get('binding_received_15')
#         data2.binding_received_16=request.POST.get('binding_received_16')
#         data2.binding_received_17=request.POST.get('binding_received_17')
#         data2.binding_received_18=request.POST.get('binding_received_18')
#         data2.binding_received_19=request.POST.get('binding_received_19')
#         data2.binding_received_20=request.POST.get('binding_received_20')
        

#         data2.binding_received_21=request.POST.get('binding_received_21')
#         data2.binding_received_22=request.POST.get('binding_received_22')
#         data2.binding_received_23=request.POST.get('binding_received_23')
#         data2.binding_received_24=request.POST.get('binding_received_24')
#         data2.binding_received_25=request.POST.get('binding_received_25')
#         data2.binding_received_26=request.POST.get('binding_received_26')
#         data2.binding_received_27=request.POST.get('binding_received_27')
#         data2.binding_received_28=request.POST.get('binding_received_28')
#         data2.binding_received_29=request.POST.get('binding_received_29')
#         data2.binding_received_30=request.POST.get('binding_received_30')
        

#         data2.binding_received_31=request.POST.get('binding_received_31')
#         data2.binding_received_32=request.POST.get('binding_received_32')
#         data2.binding_received_33=request.POST.get('binding_received_33')
#         data2.binding_received_34=request.POST.get('binding_received_34')
#         data2.binding_received_35=request.POST.get('binding_received_35')
#         data2.binding_received_36=request.POST.get('binding_received_36')
#         data2.binding_received_37=request.POST.get('binding_received_37')
#         data2.binding_received_38=request.POST.get('binding_received_38')
#         data2.binding_received_39=request.POST.get('binding_received_39')
#         data2.binding_received_40=request.POST.get('binding_received_40')
        

#         data2.binding_received_41=request.POST.get('binding_received_41')
#         data2.binding_received_42=request.POST.get('binding_received_42')
#         data2.binding_received_43=request.POST.get('binding_received_43')
#         data2.binding_received_44=request.POST.get('binding_received_44')
#         data2.binding_received_45=request.POST.get('binding_received_45')
#         data2.binding_received_46=request.POST.get('binding_received_46')
#         data2.binding_received_47=request.POST.get('binding_received_47')
#         data2.binding_received_48=request.POST.get('binding_received_48')
#         data2.binding_received_49=request.POST.get('binding_received_49')
#         data2.binding_received_40=request.POST.get('binding_received_50')
        

        
#         data2.binding_date = datetime.datetime.now()

#         if data2.binding_received_1:
#             data2.balance_binding_1 = float(data2.quantity_1) - float(data2.binding_received_1)
#         else:
#             data2.balance_binding_1 = 0
        
#         if data2.binding_received_2:
#             data2.balance_binding_2 = float(data2.quantity_2) - float(data2.binding_received_2)
#         else:
#             data2.balance_binding_2 = 0
        
#         if data2.binding_received_3:
#             data2.balance_binding_3 = float(data2.quantity_3) - float(data2.binding_received_3)
#         else:
#             data2.balance_binding_3 = 0
        
#         if data2.binding_received_4:
#             data2.balance_binding_4 = float(data2.quantity_4) - float(data2.binding_received_4)
#         else:
#             data2.balance_binding_4 = 0
        
#         if data2.binding_received_5:
#             data2.balance_binding_5 = float(data2.quantity_5) - float(data2.binding_received_5)
#         else:
#             data2.balance_binding_5 = 0
        
#         if data2.binding_received_6:
#             data2.balance_binding_6 = float(data2.quantity_6) - float(data2.binding_received_6)
#         else:
#             data2.balance_binding_6 = 0
        
#         if data2.binding_received_7:
#             data2.balance_binding_7 = float(data2.quantity_7) - float(data2.binding_received_7)
#         else:
#             data2.balance_binding_7 = 0
        
#         if data2.binding_received_8:
#             data2.balance_binding_8 = float(data2.quantity_8) - float(data2.binding_received_8)
#         else:
#             data2.balance_binding_8 = 0
        
#         if data2.binding_received_9:
#             data2.balance_binding_9 = float(data2.quantity_9) - float(data2.binding_received_9)
#         else:
#             data2.balance_binding_9 = 0
        
#         if data2.binding_received_10:
#             data2.balance_binding_10 = float(data2.quantity_10) - float(data2.binding_received_10)
#         else:
#             data2.balance_binding_10 = 0


        
#         if data2.binding_received_11:
#             data2.balance_binding_11 = float(data2.quantity_11) - float(data2.binding_received_11)
#         else:
#             data2.balance_binding_11 = 0
        
#         if data2.binding_received_12:
#             data2.balance_binding_12 = float(data2.quantity_12) - float(data2.binding_received_12)
#         else:
#             data2.balance_binding_12 = 0
        
#         if data2.binding_received_13:
#             data2.balance_binding_13 = float(data2.quantity_13) - float(data2.binding_received_13)
#         else:
#             data2.balance_binding_13 = 0
        
#         if data2.binding_received_14:
#             data2.balance_binding_14 = float(data2.quantity_14) - float(data2.binding_received_14)
#         else:
#             data2.balance_binding_14 = 0
        
#         if data2.binding_received_15:
#             data2.balance_binding_15 = float(data2.quantity_15) - float(data2.binding_received_15)
#         else:
#             data2.balance_binding_15 = 0
        
#         if data2.binding_received_16:
#             data2.balance_binding_16 = float(data2.quantity_16) - float(data2.binding_received_16)
#         else:
#             data2.balance_binding_16 = 0
        
#         if data2.binding_received_17:
#             data2.balance_binding_17 = float(data2.quantity_17) - float(data2.binding_received_17)
#         else:
#             data2.balance_binding_17 = 0
        
#         if data2.binding_received_18:
#             data2.balance_binding_18 = float(data2.quantity_18) - float(data2.binding_received_18)
#         else:
#             data2.balance_binding_18 = 0
        
#         if data2.binding_received_19:
#             data2.balance_binding_19 = float(data2.quantity_19) - float(data2.binding_received_19)
#         else:
#             data2.balance_binding_19 = 0
        
        
#         if data2.binding_received_20:
#             data2.balance_binding_20 = float(data2.quantity_20) - float(data2.binding_received_20)
#         else:
#             data2.balance_binding_20 = 0

#         if data2.binding_received_21:
#             data2.balance_binding_21 = float(data2.quantity_21) - float(data2.binding_received_21)
#         else:
#             data2.balance_binding_21 = 0
        
#         if data2.binding_received_22:
#             data2.balance_binding_22 = float(data2.quantity_22) - float(data2.binding_received_22)
#         else:
#             data2.balance_binding_22 = 0
        
#         if data2.binding_received_23:
#             data2.balance_binding_23 = float(data2.quantity_23) - float(data2.binding_received_23)
#         else:
#             data2.balance_binding_23 = 0
        
#         if data2.binding_received_24:
#             data2.balance_binding_24 = float(data2.quantity_24) - float(data2.binding_received_24)
#         else:
#             data2.balance_binding_24 = 0
        
#         if data2.binding_received_25:
#             data2.balance_binding_25 = float(data2.quantity_25) - float(data2.binding_received_25)
#         else:
#             data2.balance_binding_25 = 0
        
#         if data2.binding_received_26:
#             data2.balance_binding_26 = float(data2.quantity_26) - float(data2.binding_received_26)
#         else:
#             data2.balance_binding_26 = 0
        
#         if data2.binding_received_27:
#             data2.balance_binding_27 = float(data2.quantity_27) - float(data2.binding_received_27)
#         else:
#             data2.balance_binding_27 = 0
        
#         if data2.binding_received_28:
#             data2.balance_binding_28 = float(data2.quantity_28) - float(data2.binding_received_28)
#         else:
#             data2.balance_binding_28 = 0
        
#         if data2.binding_received_29:
#             data2.balance_binding_29 = float(data2.quantity_29) - float(data2.binding_received_29)
#         else:
#             data2.balance_binding_29 = 0
        
#         if data2.binding_received_30:
#             data2.balance_binding_30 = float(data2.quantity_30) - float(data2.binding_received_30)
#         else:
#             data2.balance_binding_30 = 0

#         if data2.binding_received_31:
#             data2.balance_binding_31 = float(data2.quantity_31) - float(data2.binding_received_31)
#         else:
#             data2.balance_binding_31 = 0
        
#         if data2.binding_received_32:
#             data2.balance_binding_32 = float(data2.quantity_32) - float(data2.binding_received_32)
#         else:
#             data2.balance_binding_32 = 0
        
#         if data2.binding_received_33:
#             data2.balance_binding_33 = float(data2.quantity_33) - float(data2.binding_received_33)
#         else:
#             data2.balance_binding_33 = 0
        
#         if data2.binding_received_34:
#             data2.balance_binding_34 = float(data2.quantity_34) - float(data2.binding_received_34)
#         else:
#             data2.balance_binding_34 = 0
        
#         if data2.binding_received_35:
#             data2.balance_binding_35 = float(data2.quantity_35) - float(data2.binding_received_35)
#         else:
#             data2.balance_binding_35 = 0
        
#         if data2.binding_received_36:
#             data2.balance_binding_36 = float(data2.quantity_36) - float(data2.binding_received_36)
#         else:
#             data2.balance_binding_36 = 0
        
#         if data2.binding_received_37:
#             data2.balance_binding_37 = float(data2.quantity_37) - float(data2.binding_received_37)
#         else:
#             data2.balance_binding_37 = 0
        
#         if data2.binding_received_38:
#             data2.balance_binding_38 = float(data2.quantity_38) - float(data2.binding_received_38)
#         else:
#             data2.balance_binding_38 = 0
        
#         if data2.binding_received_39:
#             data2.balance_binding_39 = float(data2.quantity_39) - float(data2.binding_received_39)
#         else:
#             data2.balance_binding_39 = 0
        
#         if data2.binding_received_40:
#             data2.balance_binding_40 = float(data2.quantity_40) - float(data2.binding_received_40)
#         else:
#             data2.balance_binding_40 = 0

#         if data2.binding_received_41:
#             data2.balance_binding_41 = float(data2.quantity_41) - float(data2.binding_received_41)
#         else:
#             data2.balance_binding_41 = 0
        
#         if data2.binding_received_42:
#             data2.balance_binding_42 = float(data2.quantity_42) - float(data2.binding_received_42)
#         else:
#             data2.balance_binding_42 = 0
        
#         if data2.binding_received_43:
#             data2.balance_binding_43 = float(data2.quantity_43) - float(data2.binding_received_43)
#         else:
#             data2.balance_binding_43 = 0
        
#         if data2.binding_received_44:
#             data2.balance_binding_44 = float(data2.quantity_44) - float(data2.binding_received_44)
#         else:
#             data2.balance_binding_44 = 0
        
#         if data2.binding_received_45:
#             data2.balance_binding_45 = float(data2.quantity_45) - float(data2.binding_received_45)
#         else:
#             data2.balance_binding_45 = 0
        
#         if data2.binding_received_46:
#             data2.balance_binding_46 = float(data2.quantity_46) - float(data2.binding_received_46)
#         else:
#             data2.balance_binding_46 = 0
        
#         if data2.binding_received_47:
#             data2.balance_binding_47 = float(data2.quantity_47) - float(data2.binding_received_47)
#         else:
#             data2.balance_binding_47 = 0
        
#         if data2.binding_received_48:
#             data2.balance_binding_48 = float(data2.quantity_48) - float(data2.binding_received_48)
#         else:
#             data2.balance_binding_48 = 0
        
#         if data2.binding_received_49:
#             data2.balance_binding_49 = float(data2.quantity_49) - float(data2.binding_received_49)
#         else:
#             data2.balance_binding_49 = 0
        
#         if data2.binding_received_50:
#             data2.balance_binding_50 = float(data2.quantity_50) - float(data2.binding_received_50)
#         else:
#             data2.balance_binding_50 = 0


        
        
#         temp_bind=[]
#         if data2.binding_received_1:
#             temp_bind.append(int(data2.binding_received_1))
#         if data2.binding_received_2:
#             temp_bind.append(int(data2.binding_received_2))
#         if data2.binding_received_3:
#             temp_bind.append(int(data2.binding_received_3))
#         if data2.binding_received_4:
#             temp_bind.append(int(data2.binding_received_4))
#         if data2.binding_received_5:
#             temp_bind.append(int(data2.binding_received_5))
#         if data2.binding_received_6:
#             temp_bind.append(int(data2.binding_received_6))
#         if data2.binding_received_7:
#             temp_bind.append(int(data2.binding_received_7))
#         if data2.binding_received_8:
#             temp_bind.append(int(data2.binding_received_8))
#         if data2.binding_received_9:
#             temp_bind.append(int(data2.binding_received_9))
#         if data2.binding_received_10:
#             temp_bind.append(int(data2.binding_received_10))

#         if data2.binding_received_11:
#             temp_bind.append(int(data2.binding_received_11))
#         if data2.binding_received_12:
#             temp_bind.append(int(data2.binding_received_12))
#         if data2.binding_received_13:
#             temp_bind.append(int(data2.binding_received_13))
#         if data2.binding_received_14:
#             temp_bind.append(int(data2.binding_received_14))
#         if data2.binding_received_15:
#             temp_bind.append(int(data2.binding_received_15))
#         if data2.binding_received_16:
#             temp_bind.append(int(data2.binding_received_16))
#         if data2.binding_received_17:
#             temp_bind.append(int(data2.binding_received_17))
#         if data2.binding_received_18:
#             temp_bind.append(int(data2.binding_received_18))
#         if data2.binding_received_19:
#             temp_bind.append(int(data2.binding_received_19))
#         if data2.binding_received_20:
#             temp_bind.append(int(data2.binding_received_20))

#         if data2.binding_received_21:
#             temp_bind.append(int(data2.binding_received_21))
#         if data2.binding_received_22:
#             temp_bind.append(int(data2.binding_received_22))
#         if data2.binding_received_23:
#             temp_bind.append(int(data2.binding_received_23))
#         if data2.binding_received_24:
#             temp_bind.append(int(data2.binding_received_24))
#         if data2.binding_received_25:
#             temp_bind.append(int(data2.binding_received_25))
#         if data2.binding_received_26:
#             temp_bind.append(int(data2.binding_received_26))
#         if data2.binding_received_27:
#             temp_bind.append(int(data2.binding_received_27))
#         if data2.binding_received_28:
#             temp_bind.append(int(data2.binding_received_28))
#         if data2.binding_received_29:
#             temp_bind.append(int(data2.binding_received_29))
#         if data2.binding_received_30:
#             temp_bind.append(int(data2.binding_received_30))

#         if data2.binding_received_31:
#             temp_bind.append(int(data2.binding_received_31))
#         if data2.binding_received_32:
#             temp_bind.append(int(data2.binding_received_32))
#         if data2.binding_received_33:
#             temp_bind.append(int(data2.binding_received_33))
#         if data2.binding_received_34:
#             temp_bind.append(int(data2.binding_received_34))
#         if data2.binding_received_35:
#             temp_bind.append(int(data2.binding_received_35))
#         if data2.binding_received_36:
#             temp_bind.append(int(data2.binding_received_36))
#         if data2.binding_received_37:
#             temp_bind.append(int(data2.binding_received_37))
#         if data2.binding_received_38:
#             temp_bind.append(int(data2.binding_received_38))
#         if data2.binding_received_39:
#             temp_bind.append(int(data2.binding_received_39))
#         if data2.binding_received_40:
#             temp_bind.append(int(data2.binding_received_40))

#         if data2.binding_received_41:
#             temp_bind.append(int(data2.binding_received_41))
#         if data2.binding_received_42:
#             temp_bind.append(int(data2.binding_received_42))
#         if data2.binding_received_43:
#             temp_bind.append(int(data2.binding_received_43))
#         if data2.binding_received_44:
#             temp_bind.append(int(data2.binding_received_44))
#         if data2.binding_received_45:
#             temp_bind.append(int(data2.binding_received_45))
#         if data2.binding_received_46:
#             temp_bind.append(int(data2.binding_received_46))
#         if data2.binding_received_47:
#             temp_bind.append(int(data2.binding_received_47))
#         if data2.binding_received_48:
#             temp_bind.append(int(data2.binding_received_48))
#         if data2.binding_received_49:
#             temp_bind.append(int(data2.binding_received_49))
#         if data2.binding_received_50:
#             temp_bind.append(int(data2.binding_received_50))
        
#         temp_bind=[i for i in temp_bind]
#         data2.total_binding=0
#         for i in temp_bind:
#             data2.total_binding=data2.total_binding+i
        
#         if data2.total_binding:
#             data2.balance_binding = float(data2.total_quantity) - float(data2.total_binding)
#         else:
#             data2.balance_binding = 0
        
#         data2.save()
#         messages.success(request, "Updated Successfully...!!")
#         return redirect('/bindings-data/') 
    
       
#     context = {
#         'data2':data2,
#     }
#     return render(request, 'processing/edit-bindings.html', context)








# @login_required(login_url="")
# def gathering_info(request):
#     if request.method =='POST':
#         id = request.POST.get('id')
        
#         item1_page1 = request.POST.get('item1_page1')
#         item1_page2 = request.POST.get('item1_page2')
#         item1_page3 = request.POST.get('item1_page3')
#         item1_page4 = request.POST.get('item1_page4')
#         item1_page5 = request.POST.get('item1_page5')
#         item1_page6 = request.POST.get('item1_page6')
#         item1_page7 = request.POST.get('item1_page7')
#         item1_page8 = request.POST.get('item1_page8')
#         item1_page9 = request.POST.get('item1_page9')
#         item1_page10 = request.POST.get('item1_page10')

#         item2_page1 = request.POST.get('item2_page1')
#         item2_page2 = request.POST.get('item2_page2')
#         item2_page3 = request.POST.get('item2_page3')
#         item2_page4 = request.POST.get('item2_page4')
#         item2_page5 = request.POST.get('item2_page5')
#         item2_page6 = request.POST.get('item2_page6')
#         item2_page7 = request.POST.get('item2_page7')
#         item2_page8 = request.POST.get('item2_page8')
#         item2_page9 = request.POST.get('item2_page9')
#         item2_page10 = request.POST.get('item2_page10')

#         item3_page1 = request.POST.get('item3_page1')
#         item3_page2 = request.POST.get('item3_page2')
#         item3_page3 = request.POST.get('item3_page3')
#         item3_page4 = request.POST.get('item3_page4')
#         item3_page5 = request.POST.get('item3_page5')
#         item3_page6 = request.POST.get('item3_page6')
#         item3_page7 = request.POST.get('item3_page7')
#         item3_page8 = request.POST.get('item3_page8')
#         item3_page9 = request.POST.get('item3_page9')
#         item3_page10 = request.POST.get('item3_page10')

#         item4_page1 = request.POST.get('item4_page1')
#         item4_page2 = request.POST.get('item4_page2')
#         item4_page3 = request.POST.get('item4_page3')
#         item4_page4 = request.POST.get('item4_page4')
#         item4_page5 = request.POST.get('item4_page5')
#         item4_page6 = request.POST.get('item4_page6')
#         item4_page7 = request.POST.get('item4_page7')
#         item4_page8 = request.POST.get('item4_page8')
#         item4_page9 = request.POST.get('item4_page9')
#         item4_page10 = request.POST.get('item4_page10')

#         item5_page1 = request.POST.get('item5_page1')
#         item5_page2 = request.POST.get('item5_page2')
#         item5_page3 = request.POST.get('item5_page3')
#         item5_page4 = request.POST.get('item5_page4')
#         item5_page5 = request.POST.get('item5_page5')
#         item5_page6 = request.POST.get('item5_page6')
#         item5_page7 = request.POST.get('item5_page7')
#         item5_page8 = request.POST.get('item5_page8')
#         item5_page9 = request.POST.get('item5_page9')
#         item5_page10 = request.POST.get('item5_page10')

#         item6_page1 = request.POST.get('item6_page1')
#         item6_page2 = request.POST.get('item6_page2')
#         item6_page3 = request.POST.get('item6_page3')
#         item6_page4 = request.POST.get('item6_page4')
#         item6_page5 = request.POST.get('item6_page5')
#         item6_page6 = request.POST.get('item6_page6')
#         item6_page7 = request.POST.get('item6_page7')
#         item6_page8 = request.POST.get('item6_page8')
#         item6_page9 = request.POST.get('item6_page9')
#         item6_page10 = request.POST.get('item6_page10')

#         item7_page1 = request.POST.get('item7_page1')
#         item7_page2 = request.POST.get('item7_page2')
#         item7_page3 = request.POST.get('item7_page3')
#         item7_page4 = request.POST.get('item7_page4')
#         item7_page5 = request.POST.get('item7_page5')
#         item7_page6 = request.POST.get('item7_page6')
#         item7_page7 = request.POST.get('item7_page7')
#         item7_page8 = request.POST.get('item7_page8')
#         item7_page9 = request.POST.get('item7_page9')
#         item7_page10 = request.POST.get('item7_page10')

#         item8_page1 = request.POST.get('item8_page1')
#         item8_page2 = request.POST.get('item8_page2')
#         item8_page3 = request.POST.get('item8_page3')
#         item8_page4 = request.POST.get('item8_page4')
#         item8_page5 = request.POST.get('item8_page5')
#         item8_page6 = request.POST.get('item8_page6')
#         item8_page7 = request.POST.get('item8_page7')
#         item8_page8 = request.POST.get('item8_page8')
#         item8_page9 = request.POST.get('item8_page9')
#         item8_page10 = request.POST.get('item8_page10')

#         item9_page1 = request.POST.get('item9_page1')
#         item9_page2 = request.POST.get('item9_page2')
#         item9_page3 = request.POST.get('item9_page3')
#         item9_page4 = request.POST.get('item9_page4')
#         item9_page5 = request.POST.get('item9_page5')
#         item9_page6 = request.POST.get('item9_page6')
#         item9_page7 = request.POST.get('item9_page7')
#         item9_page8 = request.POST.get('item9_page8')
#         item9_page9 = request.POST.get('item9_page9')
#         item9_page10 = request.POST.get('item9_page10')

#         item10_page1 = request.POST.get('item10_page1')
#         item10_page2 = request.POST.get('item10_page2')
#         item10_page3 = request.POST.get('item10_page3')
#         item10_page4 = request.POST.get('item10_page4')
#         item10_page5 = request.POST.get('item10_page5')
#         item10_page6 = request.POST.get('item10_page6')
#         item10_page7 = request.POST.get('item10_page7')
#         item10_page8 = request.POST.get('item10_page8')
#         item10_page9 = request.POST.get('item10_page9')
#         item10_page10 = request.POST.get('item10_page10')
        
#         item11_page1 = request.POST.get('item11_page1')
#         item11_page2 = request.POST.get('item11_page2')
#         item11_page3 = request.POST.get('item11_page3')
#         item11_page4 = request.POST.get('item11_page4')
#         item11_page5 = request.POST.get('item11_page5')
#         item11_page6 = request.POST.get('item11_page6')
#         item11_page7 = request.POST.get('item11_page7')
#         item11_page8 = request.POST.get('item11_page8')
#         item11_page9 = request.POST.get('item11_page9')
#         item11_page10 = request.POST.get('item11_page10')

#         item12_page1 = request.POST.get('item12_page1')
#         item12_page2 = request.POST.get('item12_page2')
#         item12_page3 = request.POST.get('item12_page3')
#         item12_page4 = request.POST.get('item12_page4')
#         item12_page5 = request.POST.get('item12_page5')
#         item12_page6 = request.POST.get('item12_page6')
#         item12_page7 = request.POST.get('item12_page7')
#         item12_page8 = request.POST.get('item12_page8')
#         item12_page9 = request.POST.get('item12_page9')
#         item12_page10 = request.POST.get('item12_page10')

#         item13_page1 = request.POST.get('item13_page1')
#         item13_page2 = request.POST.get('item13_page2')
#         item13_page3 = request.POST.get('item13_page3')
#         item13_page4 = request.POST.get('item13_page4')
#         item13_page5 = request.POST.get('item13_page5')
#         item13_page6 = request.POST.get('item13_page6')
#         item13_page7 = request.POST.get('item13_page7')
#         item13_page8 = request.POST.get('item13_page8')
#         item13_page9 = request.POST.get('item13_page9')
#         item13_page10 = request.POST.get('item13_page10')

#         item14_page1 = request.POST.get('item14_page1')
#         item14_page2 = request.POST.get('item14_page2')
#         item14_page3 = request.POST.get('item14_page3')
#         item14_page4 = request.POST.get('item14_page4')
#         item14_page5 = request.POST.get('item14_page5')
#         item14_page6 = request.POST.get('item14_page6')
#         item14_page7 = request.POST.get('item14_page7')
#         item14_page8 = request.POST.get('item14_page8')
#         item14_page9 = request.POST.get('item14_page9')
#         item14_page10 = request.POST.get('item14_page10')

#         item15_page1 = request.POST.get('item15_page1')
#         item15_page2 = request.POST.get('item15_page2')
#         item15_page3 = request.POST.get('item15_page3')
#         item15_page4 = request.POST.get('item15_page4')
#         item15_page5 = request.POST.get('item15_page5')
#         item15_page6 = request.POST.get('item15_page6')
#         item15_page7 = request.POST.get('item15_page7')
#         item15_page8 = request.POST.get('item15_page8')
#         item15_page9 = request.POST.get('item15_page9')
#         item15_page10 = request.POST.get('item15_page10')

#         item16_page1 = request.POST.get('item16_page1')
#         item16_page2 = request.POST.get('item16_page2')
#         item16_page3 = request.POST.get('item16_page3')
#         item16_page4 = request.POST.get('item16_page4')
#         item16_page5 = request.POST.get('item16_page5')
#         item16_page6 = request.POST.get('item16_page6')
#         item16_page7 = request.POST.get('item16_page7')
#         item16_page8 = request.POST.get('item16_page8')
#         item16_page9 = request.POST.get('item16_page9')
#         item16_page10 = request.POST.get('item16_page10')

#         item17_page1 = request.POST.get('item17_page1')
#         item17_page2 = request.POST.get('item17_page2')
#         item17_page3 = request.POST.get('item17_page3')
#         item17_page4 = request.POST.get('item17_page4')
#         item17_page5 = request.POST.get('item17_page5')
#         item17_page6 = request.POST.get('item17_page6')
#         item17_page7 = request.POST.get('item17_page7')
#         item17_page8 = request.POST.get('item17_page8')
#         item17_page9 = request.POST.get('item17_page9')
#         item17_page10 = request.POST.get('item17_page10')

#         item18_page1 = request.POST.get('item18_page1')
#         item18_page2 = request.POST.get('item18_page2')
#         item18_page3 = request.POST.get('item18_page3')
#         item18_page4 = request.POST.get('item18_page4')
#         item18_page5 = request.POST.get('item18_page5')
#         item18_page6 = request.POST.get('item18_page6')
#         item18_page7 = request.POST.get('item18_page7')
#         item18_page8 = request.POST.get('item18_page8')
#         item18_page9 = request.POST.get('item18_page9')
#         item18_page10 = request.POST.get('item18_page10')

#         item19_page1 = request.POST.get('item19_page1')
#         item19_page2 = request.POST.get('item19_page2')
#         item19_page3 = request.POST.get('item19_page3')
#         item19_page4 = request.POST.get('item19_page4')
#         item19_page5 = request.POST.get('item19_page5')
#         item19_page6 = request.POST.get('item19_page6')
#         item19_page7 = request.POST.get('item19_page7')
#         item19_page8 = request.POST.get('item19_page8')
#         item19_page9 = request.POST.get('item19_page9')
#         item19_page10 = request.POST.get('item19_page10')

#         item20_page1 = request.POST.get('item20_page1')
#         item20_page2 = request.POST.get('item20_page2')
#         item20_page3 = request.POST.get('item20_page3')
#         item20_page4 = request.POST.get('item20_page4')
#         item20_page5 = request.POST.get('item20_page5')
#         item20_page6 = request.POST.get('item20_page6')
#         item20_page7 = request.POST.get('item20_page7')
#         item20_page8 = request.POST.get('item20_page8')
#         item20_page9 = request.POST.get('item20_page9')
#         item20_page10 = request.POST.get('item20_page10')

#         item21_page1 = request.POST.get('item21_page1')
#         item21_page2 = request.POST.get('item21_page2')
#         item21_page3 = request.POST.get('item21_page3')
#         item21_page4 = request.POST.get('item21_page4')
#         item21_page5 = request.POST.get('item21_page5')
#         item21_page6 = request.POST.get('item21_page6')
#         item21_page7 = request.POST.get('item21_page7')
#         item21_page8 = request.POST.get('item21_page8')
#         item21_page9 = request.POST.get('item21_page9')
#         item21_page10 = request.POST.get('item21_page10')

#         item22_page1 = request.POST.get('item22_page1')
#         item22_page2 = request.POST.get('item22_page2')
#         item22_page3 = request.POST.get('item22_page3')
#         item22_page4 = request.POST.get('item22_page4')
#         item22_page5 = request.POST.get('item22_page5')
#         item22_page6 = request.POST.get('item22_page6')
#         item22_page7 = request.POST.get('item22_page7')
#         item22_page8 = request.POST.get('item22_page8')
#         item22_page9 = request.POST.get('item22_page9')
#         item22_page10 = request.POST.get('item22_page10')

#         item23_page1 = request.POST.get('item23_page1')
#         item23_page2 = request.POST.get('item23_page2')
#         item23_page3 = request.POST.get('item23_page3')
#         item23_page4 = request.POST.get('item23_page4')
#         item23_page5 = request.POST.get('item23_page5')
#         item23_page6 = request.POST.get('item23_page6')
#         item23_page7 = request.POST.get('item23_page7')
#         item23_page8 = request.POST.get('item23_page8')
#         item23_page9 = request.POST.get('item23_page9')
#         item23_page10 = request.POST.get('item23_page10')

#         item24_page1 = request.POST.get('item24_page1')
#         item24_page2 = request.POST.get('item24_page2')
#         item24_page3 = request.POST.get('item24_page3')
#         item24_page4 = request.POST.get('item24_page4')
#         item24_page5 = request.POST.get('item24_page5')
#         item24_page6 = request.POST.get('item24_page6')
#         item24_page7 = request.POST.get('item24_page7')
#         item24_page8 = request.POST.get('item24_page8')
#         item24_page9 = request.POST.get('item24_page9')
#         item24_page10 = request.POST.get('item24_page10')

#         item25_page1 = request.POST.get('item25_page1')
#         item25_page2 = request.POST.get('item25_page2')
#         item25_page3 = request.POST.get('item25_page3')
#         item25_page4 = request.POST.get('item25_page4')
#         item25_page5 = request.POST.get('item25_page5')
#         item25_page6 = request.POST.get('item25_page6')
#         item25_page7 = request.POST.get('item25_page7')
#         item25_page8 = request.POST.get('item25_page8')
#         item25_page9 = request.POST.get('item25_page9')
#         item25_page10 = request.POST.get('item25_page10')

#         item26_page1 = request.POST.get('item26_page1')
#         item26_page2 = request.POST.get('item26_page2')
#         item26_page3 = request.POST.get('item26_page3')
#         item26_page4 = request.POST.get('item26_page4')
#         item26_page5 = request.POST.get('item26_page5')
#         item26_page6 = request.POST.get('item26_page6')
#         item26_page7 = request.POST.get('item26_page7')
#         item26_page8 = request.POST.get('item26_page8')
#         item26_page9 = request.POST.get('item26_page9')
#         item26_page10 = request.POST.get('item26_page10')

#         item27_page1 = request.POST.get('item27_page1')
#         item27_page2 = request.POST.get('item27_page2')
#         item27_page3 = request.POST.get('item27_page3')
#         item27_page4 = request.POST.get('item27_page4')
#         item27_page5 = request.POST.get('item27_page5')
#         item27_page6 = request.POST.get('item27_page6')
#         item27_page7 = request.POST.get('item27_page7')
#         item27_page8 = request.POST.get('item27_page8')
#         item27_page9 = request.POST.get('item27_page9')
#         item27_page10 = request.POST.get('item27_page10')

#         item28_page1 = request.POST.get('item28_page1')
#         item28_page2 = request.POST.get('item28_page2')
#         item28_page3 = request.POST.get('item28_page3')
#         item28_page4 = request.POST.get('item28_page4')
#         item28_page5 = request.POST.get('item28_page5')
#         item28_page6 = request.POST.get('item28_page6')
#         item28_page7 = request.POST.get('item28_page7')
#         item28_page8 = request.POST.get('item28_page8')
#         item28_page9 = request.POST.get('item28_page9')
#         item28_page10 = request.POST.get('item28_page10')

#         item29_page1 = request.POST.get('item29_page1')
#         item29_page2 = request.POST.get('item29_page2')
#         item29_page3 = request.POST.get('item29_page3')
#         item29_page4 = request.POST.get('item29_page4')
#         item29_page5 = request.POST.get('item29_page5')
#         item29_page6 = request.POST.get('item29_page6')
#         item29_page7 = request.POST.get('item29_page7')
#         item29_page8 = request.POST.get('item29_page8')
#         item29_page8 = request.POST.get('item29_page8')
#         item29_page8 = request.POST.get('item29_page8')
#         item29_page9 = request.POST.get('item29_page9')
#         item29_page10 = request.POST.get('item29_page10')

#         item30_page1 = request.POST.get('item30_page1')
#         item30_page2 = request.POST.get('item30_page2')
#         item30_page3 = request.POST.get('item30_page3')
#         item30_page4 = request.POST.get('item30_page4')
#         item30_page5 = request.POST.get('item30_page5')
#         item30_page6 = request.POST.get('item30_page6')
#         item30_page7 = request.POST.get('item30_page7')
#         item30_page8 = request.POST.get('item30_page8')
#         item30_page9 = request.POST.get('item30_page9')
#         item30_page10 = request.POST.get('item30_page10')

#         item31_page1 = request.POST.get('item31_page1')
#         item31_page2 = request.POST.get('item31_page2')
#         item31_page3 = request.POST.get('item31_page3')
#         item31_page4 = request.POST.get('item31_page4')
#         item31_page5 = request.POST.get('item31_page5')
#         item31_page6 = request.POST.get('item31_page6')
#         item31_page7 = request.POST.get('item31_page7')
#         item31_page8 = request.POST.get('item31_page8')
#         item31_page9 = request.POST.get('item31_page9')
#         item31_page10 = request.POST.get('item31_page10')

#         item32_page1 = request.POST.get('item32_page1')
#         item32_page2 = request.POST.get('item32_page2')
#         item32_page3 = request.POST.get('item32_page3')
#         item32_page4 = request.POST.get('item32_page4')
#         item32_page5 = request.POST.get('item32_page5')
#         item32_page6 = request.POST.get('item32_page6')
#         item32_page7 = request.POST.get('item32_page7')
#         item32_page8 = request.POST.get('item32_page8')
#         item32_page9 = request.POST.get('item32_page9')
#         item32_page10 = request.POST.get('item32_page10')

#         item33_page1 = request.POST.get('item33_page1')
#         item33_page2 = request.POST.get('item33_page2')
#         item33_page3 = request.POST.get('item33_page3')
#         item33_page4 = request.POST.get('item33_page4')
#         item33_page5 = request.POST.get('item33_page5')
#         item33_page6 = request.POST.get('item33_page6')
#         item33_page7 = request.POST.get('item33_page7')
#         item33_page8 = request.POST.get('item33_page8')
#         item33_page9 = request.POST.get('item33_page9')
#         item33_page10 = request.POST.get('item33_page10')

#         item34_page1 = request.POST.get('item34_page1')
#         item34_page2 = request.POST.get('item34_page2')
#         item34_page3 = request.POST.get('item34_page3')
#         item34_page4 = request.POST.get('item34_page4')
#         item34_page5 = request.POST.get('item34_page5')
#         item34_page6 = request.POST.get('item34_page6')
#         item34_page7 = request.POST.get('item34_page7')
#         item34_page8 = request.POST.get('item34_page8')
#         item34_page9 = request.POST.get('item34_page9')
#         item34_page10 = request.POST.get('item34_page10')

#         item35_page1 = request.POST.get('item35_page1')
#         item35_page2 = request.POST.get('item35_page2')
#         item35_page3 = request.POST.get('item35_page3')
#         item35_page4 = request.POST.get('item35_page4')
#         item35_page5 = request.POST.get('item35_page5')
#         item35_page6 = request.POST.get('item35_page6')
#         item35_page7 = request.POST.get('item35_page7')
#         item35_page8 = request.POST.get('item35_page8')
#         item35_page9 = request.POST.get('item35_page9')
#         item35_page10 = request.POST.get('item35_page10')

#         item36_page1 = request.POST.get('item36_page1')
#         item36_page2 = request.POST.get('item36_page2')
#         item36_page3 = request.POST.get('item36_page3')
#         item36_page4 = request.POST.get('item36_page4')
#         item36_page5 = request.POST.get('item36_page5')
#         item36_page6 = request.POST.get('item36_page6')
#         item36_page7 = request.POST.get('item36_page7')
#         item36_page8 = request.POST.get('item36_page8')
#         item36_page9 = request.POST.get('item36_page9')
#         item36_page10 = request.POST.get('item36_page10')

#         item37_page1 = request.POST.get('item37_page1')
#         item37_page2 = request.POST.get('item37_page2')
#         item37_page3 = request.POST.get('item37_page3')
#         item37_page4 = request.POST.get('item37_page4')
#         item37_page5 = request.POST.get('item37_page5')
#         item37_page6 = request.POST.get('item37_page6')
#         item37_page7 = request.POST.get('item37_page7')
#         item37_page8 = request.POST.get('item37_page8')
#         item37_page9 = request.POST.get('item37_page9')
#         item37_page10 = request.POST.get('item37_page10')

#         item38_page1 = request.POST.get('item38_page1')
#         item38_page2 = request.POST.get('item38_page2')
#         item38_page3 = request.POST.get('item38_page3')
#         item38_page4 = request.POST.get('item38_page4')
#         item38_page5 = request.POST.get('item38_page5')
#         item38_page6 = request.POST.get('item38_page6')
#         item38_page7 = request.POST.get('item38_page7')
#         item38_page8 = request.POST.get('item38_page8')
#         item38_page9 = request.POST.get('item38_page9')
#         item38_page10 = request.POST.get('item38_page10')

#         item39_page1 = request.POST.get('item39_page1')
#         item39_page2 = request.POST.get('item39_page2')
#         item39_page3 = request.POST.get('item39_page3')
#         item39_page4 = request.POST.get('item39_page4')
#         item39_page5 = request.POST.get('item39_page5')
#         item39_page6 = request.POST.get('item39_page6')
#         item39_page7 = request.POST.get('item39_page7')
#         item39_page8 = request.POST.get('item39_page8')
#         item39_page9 = request.POST.get('item39_page9')
#         item39_page10 = request.POST.get('item39_page10')

#         item40_page1 = request.POST.get('item40_page1')
#         item40_page2 = request.POST.get('item40_page2')
#         item40_page3 = request.POST.get('item40_page3')
#         item40_page4 = request.POST.get('item40_page4')
#         item40_page5 = request.POST.get('item40_page5')
#         item40_page6 = request.POST.get('item40_page6')
#         item40_page7 = request.POST.get('item40_page7')
#         item40_page8 = request.POST.get('item40_page8')
#         item40_page9 = request.POST.get('item40_page9')
#         item40_page10 = request.POST.get('item40_page10')

#         item41_page1 = request.POST.get('item41_page1')
#         item41_page2 = request.POST.get('item41_page2')
#         item41_page3 = request.POST.get('item41_page3')
#         item41_page4 = request.POST.get('item41_page4')
#         item41_page5 = request.POST.get('item41_page5')
#         item41_page6 = request.POST.get('item41_page6')
#         item41_page7 = request.POST.get('item41_page7')
#         item41_page8 = request.POST.get('item41_page8')
#         item41_page9 = request.POST.get('item41_page9')
#         item41_page10 = request.POST.get('item41_page10')

#         item42_page1 = request.POST.get('item42_page1')
#         item42_page2 = request.POST.get('item42_page2')
#         item42_page3 = request.POST.get('item42_page3')
#         item42_page4 = request.POST.get('item42_page4')
#         item42_page5 = request.POST.get('item42_page5')
#         item42_page6 = request.POST.get('item42_page6')
#         item42_page7 = request.POST.get('item42_page7')
#         item42_page8 = request.POST.get('item42_page8')
#         item42_page9 = request.POST.get('item42_page9')
#         item42_page10 = request.POST.get('item42_page10')

#         item43_page1 = request.POST.get('item43_page1')
#         item43_page2 = request.POST.get('item43_page2')
#         item43_page3 = request.POST.get('item43_page3')
#         item43_page4 = request.POST.get('item43_page4')
#         item43_page5 = request.POST.get('item43_page5')
#         item43_page6 = request.POST.get('item43_page6')
#         item43_page7 = request.POST.get('item43_page7')
#         item43_page8 = request.POST.get('item43_page8')
#         item43_page9 = request.POST.get('item43_page9')
#         item43_page10 = request.POST.get('item43_page10')

#         item44_page1 = request.POST.get('item44_page1')
#         item44_page2 = request.POST.get('item44_page2')
#         item44_page3 = request.POST.get('item44_page3')
#         item44_page4 = request.POST.get('item44_page4')
#         item44_page5 = request.POST.get('item44_page5')
#         item44_page6 = request.POST.get('item44_page6')
#         item44_page7 = request.POST.get('item44_page7')
#         item44_page8 = request.POST.get('item44_page8')
#         item44_page9 = request.POST.get('item44_page9')
#         item44_page10 = request.POST.get('item44_page10')

#         item45_page1 = request.POST.get('item45_page1')
#         item45_page2 = request.POST.get('item45_page2')
#         item45_page3 = request.POST.get('item45_page3')
#         item45_page4 = request.POST.get('item45_page4')
#         item45_page5 = request.POST.get('item45_page5')
#         item45_page6 = request.POST.get('item45_page6')
#         item45_page7 = request.POST.get('item45_page7')
#         item45_page8 = request.POST.get('item45_page8')
#         item45_page9 = request.POST.get('item45_page9')
#         item45_page10 = request.POST.get('item45_page10')

#         item46_page1 = request.POST.get('item46_page1')
#         item46_page2 = request.POST.get('item46_page2')
#         item46_page3 = request.POST.get('item46_page3')
#         item46_page4 = request.POST.get('item46_page4')
#         item46_page5 = request.POST.get('item46_page5')
#         item46_page6 = request.POST.get('item46_page6')
#         item46_page7 = request.POST.get('item46_page7')
#         item46_page8 = request.POST.get('item46_page8')
#         item46_page9 = request.POST.get('item46_page9')
#         item46_page10 = request.POST.get('item46_page10')

#         item47_page1 = request.POST.get('item47_page1')
#         item47_page2 = request.POST.get('item47_page2')
#         item47_page3 = request.POST.get('item47_page3')
#         item47_page4 = request.POST.get('item47_page4')
#         item47_page5 = request.POST.get('item47_page5')
#         item47_page6 = request.POST.get('item47_page6')
#         item47_page7 = request.POST.get('item47_page7')
#         item47_page8 = request.POST.get('item47_page8')
#         item47_page9 = request.POST.get('item47_page9')
#         item47_page10 = request.POST.get('item47_page10')

#         item48_page1 = request.POST.get('item48_page1')
#         item48_page2 = request.POST.get('item48_page2')
#         item48_page3 = request.POST.get('item48_page3')
#         item48_page4 = request.POST.get('item48_page4')
#         item48_page5 = request.POST.get('item48_page5')
#         item48_page6 = request.POST.get('item48_page6')
#         item48_page7 = request.POST.get('item48_page7')
#         item48_page8 = request.POST.get('item48_page8')
#         item48_page9 = request.POST.get('item48_page9')
#         item48_page10 = request.POST.get('item48_page10')

#         item49_page1 = request.POST.get('item49_page1')
#         item49_page2 = request.POST.get('item49_page2')
#         item49_page3 = request.POST.get('item49_page3')
#         item49_page3 = request.POST.get('item49_page3')
#         item49_page3 = request.POST.get('item49_page3')
#         item49_page4 = request.POST.get('item49_page4')
#         item49_page5 = request.POST.get('item49_page5')
#         item49_page6 = request.POST.get('item49_page6')
#         item49_page7 = request.POST.get('item49_page7')
#         item49_page8 = request.POST.get('item49_page8')
#         item49_page9 = request.POST.get('item49_page9')
#         item49_page10 = request.POST.get('item49_page10')

#         item50_page1 = request.POST.get('item50_page1')
#         item50_page2 = request.POST.get('item50_page2')
#         item50_page3 = request.POST.get('item50_page3')
#         item50_page4 = request.POST.get('item50_page4')
#         item50_page5 = request.POST.get('item50_page5')
#         item50_page6 = request.POST.get('item50_page6')
#         item50_page7 = request.POST.get('item50_page7')
#         item50_page8 = request.POST.get('item50_page8')
#         item50_page9 = request.POST.get('item50_page9')
#         item50_page10 = request.POST.get('item50_page10')

        
#         total_gathering=request.POST.get('printing_received_form')
#         wastage_form = request.POST.get('print_wastage_form')
#         gathering_date = request.POST.get('print_date')
#         order = orders.objects.filter(order_id=id).get()
#         print('order',order)
        
#         order.item1_page1=item1_page1
#         order.item1_page2=item1_page2
#         order.item1_page3=item1_page3
#         order.item1_page4=item1_page4
#         order.item1_page5=item1_page5
#         order.item1_page6=item1_page6
#         order.item1_page7=item1_page7
#         order.item1_page8=item1_page8
#         order.item1_page9=item1_page9
#         order.item1_page10=item1_page10

#         order.item2_page1=item2_page1
#         order.item2_page2=item2_page2
#         order.item2_page3=item2_page3
#         order.item2_page4=item2_page4
#         order.item2_page5=item2_page5
#         order.item2_page6=item2_page6
#         order.item2_page7=item2_page7
#         order.item2_page8=item2_page8
#         order.item2_page9=item2_page9
#         order.item2_page10=item2_page10

#         order.item3_page1=item3_page1
#         order.item3_page2=item3_page2
#         order.item3_page3=item3_page3
#         order.item3_page4=item3_page4
#         order.item3_page5=item3_page5
#         order.item3_page6=item3_page6
#         order.item3_page7=item3_page7
#         order.item3_page8=item3_page8
#         order.item3_page9=item3_page9
#         order.item3_page10=item3_page10

#         order.item4_page1=item4_page1
#         order.item4_page2=item4_page2
#         order.item4_page3=item4_page3
#         order.item4_page4=item4_page4
#         order.item4_page5=item4_page5
#         order.item4_page6=item4_page6
#         order.item4_page7=item4_page7
#         order.item4_page8=item4_page8
#         order.item4_page9=item4_page9
#         order.item4_page10=item4_page10

#         order.item5_page1=item5_page1
#         order.item5_page2=item5_page2
#         order.item5_page3=item5_page3
#         order.item5_page4=item5_page4
#         order.item5_page5=item5_page5
#         order.item5_page6=item5_page6
#         order.item5_page7=item5_page7
#         order.item5_page8=item5_page8
#         order.item5_page9=item5_page9
#         order.item5_page10=item5_page10

#         order.item6_page1=item6_page1
#         order.item6_page2=item6_page2
#         order.item6_page3=item6_page3
#         order.item6_page4=item6_page4
#         order.item6_page5=item6_page5
#         order.item6_page6=item6_page6
#         order.item6_page7=item6_page7
#         order.item6_page8=item6_page8
#         order.item6_page9=item6_page9
#         order.item6_page10=item6_page10

#         order.item7_page1=item7_page1
#         order.item7_page2=item7_page2
#         order.item7_page3=item7_page3
#         order.item7_page4=item7_page4
#         order.item7_page5=item7_page5
#         order.item7_page6=item7_page6
#         order.item7_page7=item7_page7
#         order.item7_page8=item7_page8
#         order.item7_page9=item7_page9
#         order.item7_page10=item7_page10

#         order.item8_page1=item8_page1
#         order.item8_page2=item8_page2
#         order.item8_page3=item8_page3
#         order.item8_page4=item8_page4
#         order.item8_page5=item8_page5
#         order.item8_page6=item8_page6
#         order.item8_page7=item8_page7
#         order.item8_page8=item8_page8
#         order.item8_page9=item8_page9
#         order.item8_page10=item8_page10

#         order.item9_page1=item9_page1
#         order.item9_page2=item9_page2
#         order.item9_page3=item9_page3
#         order.item9_page4=item9_page4
#         order.item9_page5=item9_page5
#         order.item9_page6=item9_page6
#         order.item9_page7=item9_page7
#         order.item9_page8=item9_page8
#         order.item9_page9=item9_page9
#         order.item9_page10=item9_page10

#         order.item10_page1=item10_page1
#         order.item10_page2=item10_page2
#         order.item10_page3=item10_page3
#         order.item10_page4=item10_page4
#         order.item10_page5=item10_page5
#         order.item10_page6=item10_page6
#         order.item10_page7=item10_page7
#         order.item10_page8=item10_page8
#         order.item10_page9=item10_page9
#         order.item10_page10=item10_page10

#         order.item11_page1=item11_page1
#         order.item11_page2=item11_page2
#         order.item11_page3=item11_page3
#         order.item11_page4=item11_page4
#         order.item11_page5=item11_page5
#         order.item11_page6=item11_page6
#         order.item11_page7=item11_page7
#         order.item11_page8=item11_page8
#         order.item11_page9=item11_page9
#         order.item11_page10=item11_page10

#         order.item12_page1=item12_page1
#         order.item12_page2=item12_page2
#         order.item12_page3=item12_page3
#         order.item12_page4=item12_page4
#         order.item12_page5=item12_page5
#         order.item12_page6=item12_page6
#         order.item12_page7=item12_page7
#         order.item12_page8=item12_page8
#         order.item12_page9=item12_page9
#         order.item12_page10=item12_page10

#         order.item13_page1=item13_page1
#         order.item13_page2=item13_page2
#         order.item13_page3=item13_page3
#         order.item13_page4=item13_page4
#         order.item13_page5=item13_page5
#         order.item13_page6=item13_page6
#         order.item13_page7=item13_page7
#         order.item13_page8=item13_page8
#         order.item13_page9=item13_page9
#         order.item13_page10=item13_page10

#         order.item14_page1=item14_page1
#         order.item14_page2=item14_page2
#         order.item14_page3=item14_page3
#         order.item14_page4=item14_page4
#         order.item14_page5=item14_page5
#         order.item14_page6=item14_page6
#         order.item14_page7=item14_page7
#         order.item14_page8=item14_page8
#         order.item14_page9=item14_page9
#         order.item14_page10=item14_page10

#         order.item15_page1=item15_page1
#         order.item15_page2=item15_page2
#         order.item15_page3=item15_page3
#         order.item15_page4=item15_page4
#         order.item15_page5=item15_page5
#         order.item15_page6=item15_page6
#         order.item15_page7=item15_page7
#         order.item15_page8=item15_page8
#         order.item15_page9=item15_page9
#         order.item15_page10=item15_page10

#         order.item16_page1=item16_page1
#         order.item16_page2=item16_page2
#         order.item16_page3=item16_page3
#         order.item16_page4=item16_page4
#         order.item16_page5=item16_page5
#         order.item16_page6=item16_page6
#         order.item16_page7=item16_page7
#         order.item16_page8=item16_page8
#         order.item16_page9=item16_page9
#         order.item16_page10=item16_page10

#         order.item17_page1=item17_page1
#         order.item17_page2=item17_page2
#         order.item17_page3=item17_page3
#         order.item17_page4=item17_page4
#         order.item17_page5=item17_page5
#         order.item17_page6=item17_page6
#         order.item17_page7=item17_page7
#         order.item17_page8=item17_page8
#         order.item17_page9=item17_page9
#         order.item17_page10=item17_page10

#         order.item18_page1=item18_page1
#         order.item18_page2=item18_page2
#         order.item18_page3=item18_page3
#         order.item18_page4=item18_page4
#         order.item18_page5=item18_page5
#         order.item18_page6=item18_page6
#         order.item18_page7=item18_page7
#         order.item18_page8=item18_page8
#         order.item18_page9=item18_page9
#         order.item18_page10=item18_page10

#         order.item19_page1=item19_page1
#         order.item19_page2=item19_page2
#         order.item19_page3=item19_page3
#         order.item19_page4=item19_page4
#         order.item19_page5=item19_page5
#         order.item19_page6=item19_page6
#         order.item19_page7=item19_page7
#         order.item19_page8=item19_page8
#         order.item19_page9=item19_page9
#         order.item19_page10=item19_page10

#         order.item20_page1=item20_page1
#         order.item20_page2=item20_page2
#         order.item20_page3=item20_page3
#         order.item20_page4=item20_page4
#         order.item20_page5=item20_page5
#         order.item20_page6=item20_page6
#         order.item20_page7=item20_page7
#         order.item20_page8=item20_page8
#         order.item20_page9=item20_page9
#         order.item20_page10=item20_page10


#         order.item21_page1=item21_page1
#         order.item21_page2=item21_page2
#         order.item21_page3=item21_page3
#         order.item21_page4=item21_page4
#         order.item21_page5=item21_page5
#         order.item21_page6=item21_page6
#         order.item21_page7=item21_page7
#         order.item21_page8=item21_page8
#         order.item21_page9=item21_page9
#         order.item21_page10=item21_page10

#         order.item22_page1=item22_page1
#         order.item22_page2=item22_page2
#         order.item22_page3=item22_page3
#         order.item22_page4=item22_page4
#         order.item22_page5=item22_page5
#         order.item22_page6=item22_page6
#         order.item22_page7=item22_page7
#         order.item22_page8=item22_page8
#         order.item22_page9=item22_page9
#         order.item22_page10=item22_page10

#         order.item23_page1=item23_page1
#         order.item23_page2=item23_page2
#         order.item23_page3=item23_page3
#         order.item23_page4=item23_page4
#         order.item23_page5=item23_page5
#         order.item23_page6=item23_page6
#         order.item23_page7=item23_page7
#         order.item23_page8=item23_page8
#         order.item23_page9=item23_page9
#         order.item23_page10=item23_page10

#         order.item24_page1=item24_page1
#         order.item24_page2=item24_page2
#         order.item24_page3=item24_page3
#         order.item24_page4=item24_page4
#         order.item24_page5=item24_page5
#         order.item24_page6=item24_page6
#         order.item24_page7=item24_page7
#         order.item24_page8=item24_page8
#         order.item24_page9=item24_page9
#         order.item24_page10=item24_page10

#         order.item25_page1=item25_page1
#         order.item25_page2=item25_page2
#         order.item25_page3=item25_page3
#         order.item25_page4=item25_page4
#         order.item25_page5=item25_page5
#         order.item25_page6=item25_page6
#         order.item25_page7=item25_page7
#         order.item25_page8=item25_page8
#         order.item25_page9=item25_page9
#         order.item25_page10=item25_page10

#         order.item26_page1=item26_page1
#         order.item26_page2=item26_page2
#         order.item26_page3=item26_page3
#         order.item26_page4=item26_page4
#         order.item26_page5=item26_page5
#         order.item26_page6=item26_page6
#         order.item26_page7=item26_page7
#         order.item26_page8=item26_page8
#         order.item26_page9=item26_page9
#         order.item26_page10=item26_page10

#         order.item27_page1=item27_page1
#         order.item27_page2=item27_page2
#         order.item27_page3=item27_page3
#         order.item27_page4=item27_page4
#         order.item27_page5=item27_page5
#         order.item27_page6=item27_page6
#         order.item27_page7=item27_page7
#         order.item27_page8=item27_page8
#         order.item27_page9=item27_page9
#         order.item27_page10=item27_page10

#         order.item28_page1=item28_page1
#         order.item28_page2=item28_page2
#         order.item28_page3=item28_page3
#         order.item28_page4=item28_page4
#         order.item28_page5=item28_page5
#         order.item28_page6=item28_page6
#         order.item28_page7=item28_page7
#         order.item28_page8=item28_page8
#         order.item28_page9=item28_page9
#         order.item28_page10=item28_page10

#         order.item29_page1=item29_page1
#         order.item29_page2=item29_page2
#         order.item29_page3=item29_page3
#         order.item29_page4=item29_page4
#         order.item29_page5=item29_page5
#         order.item29_page6=item29_page6
#         order.item29_page7=item29_page7
#         order.item29_page8=item29_page8
#         order.item29_page9=item29_page9
#         order.item29_page10=item29_page10

#         order.item30_page1=item30_page1
#         order.item30_page2=item30_page2
#         order.item30_page3=item30_page3
#         order.item30_page4=item30_page4
#         order.item30_page5=item30_page5
#         order.item30_page6=item30_page6
#         order.item30_page7=item30_page7
#         order.item30_page8=item30_page8
#         order.item30_page9=item30_page9
#         order.item30_page10=item30_page10


#         order.item31_page1=item31_page1
#         order.item31_page2=item31_page2
#         order.item31_page3=item31_page3
#         order.item31_page4=item31_page4
#         order.item31_page5=item31_page5
#         order.item31_page6=item31_page6
#         order.item31_page7=item31_page7
#         order.item31_page8=item31_page8
#         order.item31_page9=item31_page9
#         order.item31_page10=item31_page10

#         order.item32_page1=item32_page1
#         order.item32_page2=item32_page2
#         order.item32_page3=item32_page3
#         order.item32_page4=item32_page4
#         order.item32_page5=item32_page5
#         order.item32_page6=item32_page6
#         order.item32_page7=item32_page7
#         order.item32_page8=item32_page8
#         order.item32_page9=item32_page9
#         order.item32_page10=item32_page10

#         order.item33_page1=item33_page1
#         order.item33_page2=item33_page2
#         order.item33_page3=item33_page3
#         order.item33_page4=item33_page4
#         order.item33_page5=item33_page5
#         order.item33_page6=item33_page6
#         order.item33_page7=item33_page7
#         order.item33_page8=item33_page8
#         order.item33_page9=item33_page9
#         order.item33_page10=item33_page10

#         order.item34_page1=item34_page1
#         order.item34_page2=item34_page2
#         order.item34_page3=item34_page3
#         order.item34_page4=item34_page4
#         order.item34_page5=item34_page5
#         order.item34_page6=item34_page6
#         order.item34_page7=item34_page7
#         order.item34_page8=item34_page8
#         order.item34_page9=item34_page9
#         order.item34_page10=item34_page10

#         order.item35_page1=item35_page1
#         order.item35_page2=item35_page2
#         order.item35_page3=item35_page3
#         order.item35_page4=item35_page4
#         order.item35_page5=item35_page5
#         order.item35_page6=item35_page6
#         order.item35_page7=item35_page7
#         order.item35_page8=item35_page8
#         order.item35_page9=item35_page9
#         order.item35_page10=item35_page10

#         order.item36_page1=item36_page1
#         order.item36_page2=item36_page2
#         order.item36_page3=item36_page3
#         order.item36_page4=item36_page4
#         order.item36_page5=item36_page5
#         order.item36_page6=item36_page6
#         order.item36_page7=item36_page7
#         order.item36_page8=item36_page8
#         order.item36_page9=item36_page9
#         order.item36_page10=item36_page10

#         order.item37_page1=item37_page1
#         order.item37_page2=item37_page2
#         order.item37_page3=item37_page3
#         order.item37_page4=item37_page4
#         order.item37_page5=item37_page5
#         order.item37_page6=item37_page6
#         order.item37_page7=item37_page7
#         order.item37_page8=item37_page8
#         order.item37_page9=item37_page9
#         order.item37_page10=item37_page10

#         order.item38_page1=item38_page1
#         order.item38_page2=item38_page2
#         order.item38_page3=item38_page3
#         order.item38_page4=item38_page4
#         order.item38_page5=item38_page5
#         order.item38_page6=item38_page6
#         order.item38_page7=item38_page7
#         order.item38_page8=item38_page8
#         order.item38_page9=item38_page9
#         order.item38_page10=item38_page10

#         order.item39_page1=item39_page1
#         order.item39_page2=item39_page2
#         order.item39_page3=item39_page3
#         order.item39_page4=item39_page4
#         order.item39_page5=item39_page5
#         order.item39_page6=item39_page6
#         order.item39_page7=item39_page7
#         order.item39_page8=item39_page8
#         order.item39_page9=item39_page9
#         order.item39_page10=item39_page10

#         order.item40_page1=item40_page1
#         order.item40_page2=item40_page2
#         order.item40_page3=item40_page3
#         order.item40_page4=item40_page4
#         order.item40_page5=item40_page5
#         order.item40_page6=item40_page6
#         order.item40_page7=item40_page7
#         order.item40_page8=item40_page8
#         order.item40_page9=item40_page9
#         order.item40_page10=item40_page10


#         order.item41_page1=item41_page1
#         order.item41_page2=item41_page2
#         order.item41_page3=item41_page3
#         order.item41_page4=item41_page4
#         order.item41_page5=item41_page5
#         order.item41_page6=item41_page6
#         order.item41_page7=item41_page7
#         order.item41_page8=item41_page8
#         order.item41_page9=item41_page9
#         order.item41_page10=item41_page10

#         order.item42_page1=item42_page1
#         order.item42_page2=item42_page2
#         order.item42_page3=item42_page3
#         order.item42_page4=item42_page4
#         order.item42_page5=item42_page5
#         order.item42_page6=item42_page6
#         order.item42_page7=item42_page7
#         order.item42_page8=item42_page8
#         order.item42_page9=item42_page9
#         order.item42_page10=item42_page10

#         order.item43_page1=item43_page1
#         order.item43_page2=item43_page2
#         order.item43_page3=item43_page3
#         order.item43_page4=item43_page4
#         order.item43_page5=item43_page5
#         order.item43_page6=item43_page6
#         order.item43_page7=item43_page7
#         order.item43_page8=item43_page8
#         order.item43_page9=item43_page9
#         order.item43_page10=item43_page10

#         order.item44_page1=item44_page1
#         order.item44_page2=item44_page2
#         order.item44_page3=item44_page3
#         order.item44_page4=item44_page4
#         order.item44_page5=item44_page5
#         order.item44_page6=item44_page6
#         order.item44_page7=item44_page7
#         order.item44_page8=item44_page8
#         order.item44_page9=item44_page9
#         order.item44_page10=item44_page10

#         order.item45_page1=item45_page1
#         order.item45_page2=item45_page2
#         order.item45_page3=item45_page3
#         order.item45_page4=item45_page4
#         order.item45_page5=item45_page5
#         order.item45_page6=item45_page6
#         order.item45_page7=item45_page7
#         order.item45_page8=item45_page8
#         order.item45_page9=item45_page9
#         order.item45_page10=item45_page10

#         order.item46_page1=item46_page1
#         order.item46_page2=item46_page2
#         order.item46_page3=item46_page3
#         order.item46_page4=item46_page4
#         order.item46_page5=item46_page5
#         order.item46_page6=item46_page6
#         order.item46_page7=item46_page7
#         order.item46_page8=item46_page8
#         order.item46_page9=item46_page9
#         order.item46_page10=item46_page10

#         order.item47_page1=item47_page1
#         order.item47_page2=item47_page2
#         order.item47_page3=item47_page3
#         order.item47_page4=item47_page4
#         order.item47_page5=item47_page5
#         order.item47_page6=item47_page6
#         order.item47_page7=item47_page7
#         order.item47_page8=item47_page8
#         order.item47_page9=item47_page9
#         order.item47_page10=item47_page10

#         order.item48_page1=item48_page1
#         order.item48_page2=item48_page2
#         order.item48_page3=item48_page3
#         order.item48_page4=item48_page4
#         order.item48_page5=item48_page5
#         order.item48_page6=item48_page6
#         order.item48_page7=item48_page7
#         order.item48_page8=item48_page8
#         order.item48_page9=item48_page9
#         order.item48_page10=item48_page10

#         order.item49_page1=item49_page1
#         order.item49_page2=item49_page2
#         order.item49_page3=item49_page3
#         order.item49_page4=item49_page4
#         order.item49_page5=item49_page5
#         order.item49_page6=item49_page6
#         order.item49_page7=item49_page7
#         order.item49_page8=item49_page8
#         order.item49_page9=item49_page9
#         order.item49_page10=item49_page10

#         order.item50_page1=item50_page1
#         order.item50_page2=item50_page2
#         order.item50_page3=item50_page3
#         order.item50_page4=item50_page4
#         order.item50_page5=item50_page5
#         order.item50_page6=item50_page6
#         order.item50_page7=item50_page7
#         order.item50_page8=item50_page8
#         order.item50_page9=item50_page9
#         order.item50_page10=item50_page10
        
        

        
#         order.total_gathering=total_gathering 
#         order.wastage_form=wastage_form 
#         order.gathering_date=datetime.datetime.now()
#         order.save()

#     data1 = orders.objects.all().order_by('-order_id')    
#     context={
#         'data1':data1,       
#     }
#     return render(request,'processing/gathering-info.html',context) 








# @login_required(login_url="")
# def view_gathering_info(request,order_id):
#     gathering = orders.objects.get(order_id=order_id)
#     print('gjhgjmgj',order_id)

#     if request.method == 'POST':
#         id = request.POST.get('id')

#         gathering.item1_page1 = request.POST.get('item1_page1')
#         gathering.item1_page2 = request.POST.get('item1_page2')
#         gathering.item1_page3 = request.POST.get('item1_page3')
#         gathering.item1_page4 = request.POST.get('item1_page4')
#         gathering.item1_page5 = request.POST.get('item1_page5')
#         gathering.item1_page6 = request.POST.get('item1_page6')
#         gathering.item1_page7 = request.POST.get('item1_page7')
#         gathering.item1_page8 = request.POST.get('item1_page8')
#         gathering.item1_page9 = request.POST.get('item1_page9')
#         gathering.item1_page10 = request.POST.get('item1_page10')

#         gathering.item2_page1 = request.POST.get('item2_page1')
#         gathering.item2_page2 = request.POST.get('item2_page2')
#         gathering.item2_page3 = request.POST.get('item2_page3')
#         gathering.item2_page4 = request.POST.get('item2_page4')
#         gathering.item2_page5 = request.POST.get('item2_page5')
#         gathering.item2_page6 = request.POST.get('item2_page6')
#         gathering.item2_page7 = request.POST.get('item2_page7')
#         gathering.item2_page8 = request.POST.get('item2_page8')
#         gathering.item2_page9 = request.POST.get('item2_page9')
#         gathering.item2_page10 = request.POST.get('item2_page10')

#         gathering.item3_page1 = request.POST.get('item3_page1')
#         gathering.item3_page2 = request.POST.get('item3_page2')
#         gathering.item3_page3 = request.POST.get('item3_page3')
#         gathering.item3_page4 = request.POST.get('item3_page4')
#         gathering.item3_page5 = request.POST.get('item3_page5')
#         gathering.item3_page6 = request.POST.get('item3_page6')
#         gathering.item3_page7 = request.POST.get('item3_page7')
#         gathering.item3_page8 = request.POST.get('item3_page8')
#         gathering.item3_page9 = request.POST.get('item3_page9')
#         gathering.item3_page10 = request.POST.get('item3_page10')

#         gathering.item4_page1 = request.POST.get('item4_page1')
#         gathering.item4_page2 = request.POST.get('item4_page2')
#         gathering.item4_page3 = request.POST.get('item4_page3')
#         gathering.item4_page4 = request.POST.get('item4_page4')
#         gathering.item4_page5 = request.POST.get('item4_page5')
#         gathering.item4_page6 = request.POST.get('item4_page6')
#         gathering.item4_page7 = request.POST.get('item4_page7')
#         gathering.item4_page8 = request.POST.get('item4_page8')
#         gathering.item4_page9 = request.POST.get('item4_page9')
#         gathering.item4_page10 = request.POST.get('item4_page10')

#         gathering.item5_page1 = request.POST.get('item5_page1')
#         gathering.item5_page2 = request.POST.get('item5_page2')
#         gathering.item5_page3 = request.POST.get('item5_page3')
#         gathering.item5_page4 = request.POST.get('item5_page4')
#         gathering.item5_page5 = request.POST.get('item5_page5')
#         gathering.item5_page6 = request.POST.get('item5_page6')
#         gathering.item5_page7 = request.POST.get('item5_page7')
#         gathering.item5_page8 = request.POST.get('item5_page8')
#         gathering.item5_page9 = request.POST.get('item5_page9')
#         gathering.item5_page10 = request.POST.get('item5_page10')

#         gathering.item6_page1 = request.POST.get('item6_page1')
#         gathering.item6_page2 = request.POST.get('item6_page2')
#         gathering.item6_page3 = request.POST.get('item6_page3')
#         gathering.item6_page4 = request.POST.get('item6_page4')
#         gathering.item6_page5 = request.POST.get('item6_page5')
#         gathering.item6_page6 = request.POST.get('item6_page6')
#         gathering.item6_page7 = request.POST.get('item6_page7')
#         gathering.item6_page8 = request.POST.get('item6_page8')
#         gathering.item6_page9 = request.POST.get('item6_page9')
#         gathering.item6_page10 = request.POST.get('item6_page10')

#         gathering.item7_page1 = request.POST.get('item7_page1')
#         gathering.item7_page2 = request.POST.get('item7_page2')
#         gathering.item7_page3 = request.POST.get('item7_page3')
#         gathering.item7_page4 = request.POST.get('item7_page4')
#         gathering.item7_page5 = request.POST.get('item7_page5')
#         gathering.item7_page6 = request.POST.get('item7_page6')
#         gathering.item7_page7 = request.POST.get('item7_page7')
#         gathering.item7_page8 = request.POST.get('item7_page8')
#         gathering.item7_page9 = request.POST.get('item7_page9')
#         gathering.item7_page10 = request.POST.get('item7_page10')

#         gathering.item8_page1 = request.POST.get('item8_page1')
#         gathering.item8_page2 = request.POST.get('item8_page2')
#         gathering.item8_page3 = request.POST.get('item8_page3')
#         gathering.item8_page4 = request.POST.get('item8_page4')
#         gathering.item8_page5 = request.POST.get('item8_page5')
#         gathering.item8_page6 = request.POST.get('item8_page6')
#         gathering.item8_page7 = request.POST.get('item8_page7')
#         gathering.item8_page8 = request.POST.get('item8_page8')
#         gathering.item8_page9 = request.POST.get('item8_page9')
#         gathering.item8_page10 = request.POST.get('item8_page10')

#         gathering.item9_page1 = request.POST.get('item9_page1')
#         gathering.item9_page2 = request.POST.get('item9_page2')
#         gathering.item9_page3 = request.POST.get('item9_page3')
#         gathering.item9_page4 = request.POST.get('item9_page4')
#         gathering.item9_page5 = request.POST.get('item9_page5')
#         gathering.item9_page6 = request.POST.get('item9_page6')
#         gathering.item9_page7 = request.POST.get('item9_page7')
#         gathering.item9_page8 = request.POST.get('item9_page8')
#         gathering.item9_page9 = request.POST.get('item9_page9')
#         gathering.item9_page10 = request.POST.get('item9_page10')

#         gathering.item10_page1 = request.POST.get('item10_page1')
#         gathering.item10_page2 = request.POST.get('item10_page2')
#         gathering.item10_page3 = request.POST.get('item10_page3')
#         gathering.item10_page4 = request.POST.get('item10_page4')
#         gathering.item10_page5 = request.POST.get('item10_page5')
#         gathering.item10_page6 = request.POST.get('item10_page6')
#         gathering.item10_page7 = request.POST.get('item10_page7')
#         gathering.item10_page8 = request.POST.get('item10_page8')
#         gathering.item10_page9 = request.POST.get('item10_page9')
#         gathering.item10_page10 = request.POST.get('item10_page10')
        
#         gathering.item11_page1 = request.POST.get('item11_page1')
#         gathering.item11_page2 = request.POST.get('item11_page2')
#         gathering.item11_page3 = request.POST.get('item11_page3')
#         gathering.item11_page4 = request.POST.get('item11_page4')
#         gathering.item11_page5 = request.POST.get('item11_page5')
#         gathering.item11_page6 = request.POST.get('item11_page6')
#         gathering.item11_page7 = request.POST.get('item11_page7')
#         gathering.item11_page8 = request.POST.get('item11_page8')
#         gathering.item11_page9 = request.POST.get('item11_page9')
#         gathering.item11_page10 = request.POST.get('item11_page10')

#         gathering.item12_page1 = request.POST.get('item12_page1')
#         gathering.item12_page2 = request.POST.get('item12_page2')
#         gathering.item12_page3 = request.POST.get('item12_page3')
#         gathering.item12_page4 = request.POST.get('item12_page4')
#         gathering.item12_page5 = request.POST.get('item12_page5')
#         gathering.item12_page6 = request.POST.get('item12_page6')
#         gathering.item12_page7 = request.POST.get('item12_page7')
#         gathering.item12_page8 = request.POST.get('item12_page8')
#         gathering.item12_page9 = request.POST.get('item12_page9')
#         gathering.item12_page10 = request.POST.get('item12_page10')

#         gathering.item13_page1 = request.POST.get('item13_page1')
#         gathering.item13_page2 = request.POST.get('item13_page2')
#         gathering.item13_page3 = request.POST.get('item13_page3')
#         gathering.item13_page4 = request.POST.get('item13_page4')
#         gathering.item13_page5 = request.POST.get('item13_page5')
#         gathering.item13_page6 = request.POST.get('item13_page6')
#         gathering.item13_page7 = request.POST.get('item13_page7')
#         gathering.item13_page8 = request.POST.get('item13_page8')
#         gathering.item13_page9 = request.POST.get('item13_page9')
#         gathering.item13_page10 = request.POST.get('item13_page10')

#         gathering.item14_page1 = request.POST.get('item14_page1')
#         gathering.item14_page2 = request.POST.get('item14_page2')
#         gathering.item14_page3 = request.POST.get('item14_page3')
#         gathering.item14_page4 = request.POST.get('item14_page4')
#         gathering.item14_page5 = request.POST.get('item14_page5')
#         gathering.item14_page6 = request.POST.get('item14_page6')
#         gathering.item14_page7 = request.POST.get('item14_page7')
#         gathering.item14_page8 = request.POST.get('item14_page8')
#         gathering.item14_page9 = request.POST.get('item14_page9')
#         gathering.item14_page10 = request.POST.get('item14_page10')

#         gathering.item15_page1 = request.POST.get('item15_page1')
#         gathering.item15_page2 = request.POST.get('item15_page2')
#         gathering.item15_page3 = request.POST.get('item15_page3')
#         gathering.item15_page4 = request.POST.get('item15_page4')
#         gathering.item15_page5 = request.POST.get('item15_page5')
#         gathering.item15_page6 = request.POST.get('item15_page6')
#         gathering.item15_page7 = request.POST.get('item15_page7')
#         gathering.item15_page8 = request.POST.get('item15_page8')
#         gathering.item15_page9 = request.POST.get('item15_page9')
#         gathering.item15_page10 = request.POST.get('item15_page10')

#         gathering.item16_page1 = request.POST.get('item16_page1')
#         gathering.item16_page2 = request.POST.get('item16_page2')
#         gathering.item16_page3 = request.POST.get('item16_page3')
#         gathering.item16_page4 = request.POST.get('item16_page4')
#         gathering.item16_page5 = request.POST.get('item16_page5')
#         gathering.item16_page6 = request.POST.get('item16_page6')
#         gathering.item16_page7 = request.POST.get('item16_page7')
#         gathering.item16_page8 = request.POST.get('item16_page8')
#         gathering.item16_page9 = request.POST.get('item16_page9')
#         gathering.item16_page10 = request.POST.get('item16_page10')

#         gathering.item17_page1 = request.POST.get('item17_page1')
#         gathering.item17_page2 = request.POST.get('item17_page2')
#         gathering.item17_page3 = request.POST.get('item17_page3')
#         gathering.item17_page4 = request.POST.get('item17_page4')
#         gathering.item17_page5 = request.POST.get('item17_page5')
#         gathering.item17_page6 = request.POST.get('item17_page6')
#         gathering.item17_page7 = request.POST.get('item17_page7')
#         gathering.item17_page8 = request.POST.get('item17_page8')
#         gathering.item17_page9 = request.POST.get('item17_page9')
#         gathering.item17_page10 = request.POST.get('item17_page10')

#         gathering.item18_page1 = request.POST.get('item18_page1')
#         gathering.item18_page2 = request.POST.get('item18_page2')
#         gathering.item18_page3 = request.POST.get('item18_page3')
#         gathering.item18_page4 = request.POST.get('item18_page4')
#         gathering.item18_page5 = request.POST.get('item18_page5')
#         gathering.item18_page6 = request.POST.get('item18_page6')
#         gathering.item18_page7 = request.POST.get('item18_page7')
#         gathering.item18_page8 = request.POST.get('item18_page8')
#         gathering.item18_page9 = request.POST.get('item18_page9')
#         gathering.item18_page10 = request.POST.get('item18_page10')

#         gathering.item19_page1 = request.POST.get('item19_page1')
#         gathering.item19_page2 = request.POST.get('item19_page2')
#         gathering.item19_page3 = request.POST.get('item19_page3')
#         gathering.item19_page4 = request.POST.get('item19_page4')
#         gathering.item19_page5 = request.POST.get('item19_page5')
#         gathering.item19_page6 = request.POST.get('item19_page6')
#         gathering.item19_page7 = request.POST.get('item19_page7')
#         gathering.item19_page8 = request.POST.get('item19_page8')
#         gathering.item19_page9 = request.POST.get('item19_page9')
#         gathering.item19_page10 = request.POST.get('item19_page10')

#         gathering.item20_page1 = request.POST.get('item20_page1')
#         gathering.item20_page2 = request.POST.get('item20_page2')
#         gathering.item20_page3 = request.POST.get('item20_page3')
#         gathering.item20_page4 = request.POST.get('item20_page4')
#         gathering.item20_page5 = request.POST.get('item20_page5')
#         gathering.item20_page6 = request.POST.get('item20_page6')
#         gathering.item20_page7 = request.POST.get('item20_page7')
#         gathering.item20_page8 = request.POST.get('item20_page8')
#         gathering.item20_page9 = request.POST.get('item20_page9')
#         gathering.item20_page10 = request.POST.get('item20_page10')

#         gathering.item21_page1 = request.POST.get('item21_page1')
#         gathering.item21_page2 = request.POST.get('item21_page2')
#         gathering.item21_page3 = request.POST.get('item21_page3')
#         gathering.item21_page4 = request.POST.get('item21_page4')
#         gathering.item21_page5 = request.POST.get('item21_page5')
#         gathering.item21_page6 = request.POST.get('item21_page6')
#         gathering.item21_page7 = request.POST.get('item21_page7')
#         gathering.item21_page8 = request.POST.get('item21_page8')
#         gathering.item21_page9 = request.POST.get('item21_page9')
#         gathering.item21_page10 = request.POST.get('item21_page10')

#         gathering.item22_page1 = request.POST.get('item22_page1')
#         gathering.item22_page2 = request.POST.get('item22_page2')
#         gathering.item22_page3 = request.POST.get('item22_page3')
#         gathering.item22_page4 = request.POST.get('item22_page4')
#         gathering.item22_page5 = request.POST.get('item22_page5')
#         gathering.item22_page6 = request.POST.get('item22_page6')
#         gathering.item22_page7 = request.POST.get('item22_page7')
#         gathering.item22_page8 = request.POST.get('item22_page8')
#         gathering.item22_page9 = request.POST.get('item22_page9')
#         gathering.item22_page10 = request.POST.get('item22_page10')

#         gathering.item23_page1 = request.POST.get('item23_page1')
#         gathering.item23_page2 = request.POST.get('item23_page2')
#         gathering.item23_page3 = request.POST.get('item23_page3')
#         gathering.item23_page4 = request.POST.get('item23_page4')
#         gathering.item23_page5 = request.POST.get('item23_page5')
#         gathering.item23_page6 = request.POST.get('item23_page6')
#         gathering.item23_page7 = request.POST.get('item23_page7')
#         gathering.item23_page8 = request.POST.get('item23_page8')
#         gathering.item23_page9 = request.POST.get('item23_page9')
#         gathering.item23_page10 = request.POST.get('item23_page10')

#         gathering.item24_page1 = request.POST.get('item24_page1')
#         gathering.item24_page2 = request.POST.get('item24_page2')
#         gathering.item24_page3 = request.POST.get('item24_page3')
#         gathering.item24_page4 = request.POST.get('item24_page4')
#         gathering.item24_page5 = request.POST.get('item24_page5')
#         gathering.item24_page6 = request.POST.get('item24_page6')
#         gathering.item24_page7 = request.POST.get('item24_page7')
#         gathering.item24_page8 = request.POST.get('item24_page8')
#         gathering.item24_page9 = request.POST.get('item24_page9')
#         gathering.item24_page10 = request.POST.get('item24_page10')

#         gathering.item25_page1 = request.POST.get('item25_page1')
#         gathering.item25_page2 = request.POST.get('item25_page2')
#         gathering.item25_page3 = request.POST.get('item25_page3')
#         gathering.item25_page4 = request.POST.get('item25_page4')
#         gathering.item25_page5 = request.POST.get('item25_page5')
#         gathering.item25_page6 = request.POST.get('item25_page6')
#         gathering.item25_page7 = request.POST.get('item25_page7')
#         gathering.item25_page8 = request.POST.get('item25_page8')
#         gathering.item25_page9 = request.POST.get('item25_page9')
#         gathering.item25_page10 = request.POST.get('item25_page10')

#         gathering.item26_page1 = request.POST.get('item26_page1')
#         gathering.item26_page2 = request.POST.get('item26_page2')
#         gathering.item26_page3 = request.POST.get('item26_page3')
#         gathering.item26_page4 = request.POST.get('item26_page4')
#         gathering.item26_page5 = request.POST.get('item26_page5')
#         gathering.item26_page6 = request.POST.get('item26_page6')
#         gathering.item26_page7 = request.POST.get('item26_page7')
#         gathering.item26_page8 = request.POST.get('item26_page8')
#         gathering.item26_page9 = request.POST.get('item26_page9')
#         gathering.item26_page10 = request.POST.get('item26_page10')

#         gathering.item27_page1 = request.POST.get('item27_page1')
#         gathering.item27_page2 = request.POST.get('item27_page2')
#         gathering.item27_page3 = request.POST.get('item27_page3')
#         gathering.item27_page4 = request.POST.get('item27_page4')
#         gathering.item27_page5 = request.POST.get('item27_page5')
#         gathering.item27_page6 = request.POST.get('item27_page6')
#         gathering.item27_page7 = request.POST.get('item27_page7')
#         gathering.item27_page8 = request.POST.get('item27_page8')
#         gathering.item27_page9 = request.POST.get('item27_page9')
#         gathering.item27_page10 = request.POST.get('item27_page10')

#         gathering.item28_page1 = request.POST.get('item28_page1')
#         gathering.item28_page2 = request.POST.get('item28_page2')
#         gathering.item28_page3 = request.POST.get('item28_page3')
#         gathering.item28_page4 = request.POST.get('item28_page4')
#         gathering.item28_page5 = request.POST.get('item28_page5')
#         gathering.item28_page6 = request.POST.get('item28_page6')
#         gathering.item28_page7 = request.POST.get('item28_page7')
#         gathering.item28_page8 = request.POST.get('item28_page8')
#         gathering.item28_page9 = request.POST.get('item28_page9')
#         gathering.item28_page10 = request.POST.get('item28_page10')

#         gathering.item29_page1 = request.POST.get('item29_page1')
#         gathering.item29_page2 = request.POST.get('item29_page2')
#         gathering.item29_page3 = request.POST.get('item29_page3')
#         gathering.item29_page4 = request.POST.get('item29_page4')
#         gathering.item29_page5 = request.POST.get('item29_page5')
#         gathering.item29_page6 = request.POST.get('item29_page6')
#         gathering.item29_page7 = request.POST.get('item29_page7')
#         gathering.item29_page8 = request.POST.get('item29_page8')
#         gathering.item29_page8 = request.POST.get('item29_page8')
#         gathering.item29_page8 = request.POST.get('item29_page8')
#         gathering.item29_page9 = request.POST.get('item29_page9')
#         gathering.item29_page10 = request.POST.get('item29_page10')

#         gathering.item30_page1 = request.POST.get('item30_page1')
#         gathering.item30_page2 = request.POST.get('item30_page2')
#         gathering.item30_page3 = request.POST.get('item30_page3')
#         gathering.item30_page4 = request.POST.get('item30_page4')
#         gathering.item30_page5 = request.POST.get('item30_page5')
#         gathering.item30_page6 = request.POST.get('item30_page6')
#         gathering.item30_page7 = request.POST.get('item30_page7')
#         gathering.item30_page8 = request.POST.get('item30_page8')
#         gathering.item30_page9 = request.POST.get('item30_page9')
#         gathering.item30_page10 = request.POST.get('item30_page10')

#         gathering.item31_page1 = request.POST.get('item31_page1')
#         gathering.item31_page2 = request.POST.get('item31_page2')
#         gathering.item31_page3 = request.POST.get('item31_page3')
#         gathering.item31_page4 = request.POST.get('item31_page4')
#         gathering.item31_page5 = request.POST.get('item31_page5')
#         gathering.item31_page6 = request.POST.get('item31_page6')
#         gathering.item31_page7 = request.POST.get('item31_page7')
#         gathering.item31_page8 = request.POST.get('item31_page8')
#         gathering.item31_page9 = request.POST.get('item31_page9')
#         gathering.item31_page10 = request.POST.get('item31_page10')

#         gathering.item32_page1 = request.POST.get('item32_page1')
#         gathering.item32_page2 = request.POST.get('item32_page2')
#         gathering.item32_page3 = request.POST.get('item32_page3')
#         gathering.item32_page4 = request.POST.get('item32_page4')
#         gathering.item32_page5 = request.POST.get('item32_page5')
#         gathering.item32_page6 = request.POST.get('item32_page6')
#         gathering.item32_page7 = request.POST.get('item32_page7')
#         gathering.item32_page8 = request.POST.get('item32_page8')
#         gathering.item32_page9 = request.POST.get('item32_page9')
#         gathering.item32_page10 = request.POST.get('item32_page10')

#         gathering.item33_page1 = request.POST.get('item33_page1')
#         gathering.item33_page2 = request.POST.get('item33_page2')
#         gathering.item33_page3 = request.POST.get('item33_page3')
#         gathering.item33_page4 = request.POST.get('item33_page4')
#         gathering.item33_page5 = request.POST.get('item33_page5')
#         gathering.item33_page6 = request.POST.get('item33_page6')
#         gathering.item33_page7 = request.POST.get('item33_page7')
#         gathering.item33_page8 = request.POST.get('item33_page8')
#         gathering.item33_page9 = request.POST.get('item33_page9')
#         gathering.item33_page10 = request.POST.get('item33_page10')

#         gathering.item34_page1 = request.POST.get('item34_page1')
#         gathering.item34_page2 = request.POST.get('item34_page2')
#         gathering.item34_page3 = request.POST.get('item34_page3')
#         gathering.item34_page4 = request.POST.get('item34_page4')
#         gathering.item34_page5 = request.POST.get('item34_page5')
#         gathering.item34_page6 = request.POST.get('item34_page6')
#         gathering.item34_page7 = request.POST.get('item34_page7')
#         gathering.item34_page8 = request.POST.get('item34_page8')
#         gathering.item34_page9 = request.POST.get('item34_page9')
#         gathering.item34_page10 = request.POST.get('item34_page10')

#         gathering.item35_page1 = request.POST.get('item35_page1')
#         gathering.item35_page2 = request.POST.get('item35_page2')
#         gathering.item35_page3 = request.POST.get('item35_page3')
#         gathering.item35_page4 = request.POST.get('item35_page4')
#         gathering.item35_page5 = request.POST.get('item35_page5')
#         gathering.item35_page6 = request.POST.get('item35_page6')
#         gathering.item35_page7 = request.POST.get('item35_page7')
#         gathering.item35_page8 = request.POST.get('item35_page8')
#         gathering.item35_page9 = request.POST.get('item35_page9')
#         gathering.item35_page10 = request.POST.get('item35_page10')

#         gathering.item36_page1 = request.POST.get('item36_page1')
#         gathering.item36_page2 = request.POST.get('item36_page2')
#         gathering.item36_page3 = request.POST.get('item36_page3')
#         gathering.item36_page4 = request.POST.get('item36_page4')
#         gathering.item36_page5 = request.POST.get('item36_page5')
#         gathering.item36_page6 = request.POST.get('item36_page6')
#         gathering.item36_page7 = request.POST.get('item36_page7')
#         gathering.item36_page8 = request.POST.get('item36_page8')
#         gathering.item36_page9 = request.POST.get('item36_page9')
#         gathering.item36_page10 = request.POST.get('item36_page10')

#         gathering.item37_page1 = request.POST.get('item37_page1')
#         gathering.item37_page2 = request.POST.get('item37_page2')
#         gathering.item37_page3 = request.POST.get('item37_page3')
#         gathering.item37_page4 = request.POST.get('item37_page4')
#         gathering.item37_page5 = request.POST.get('item37_page5')
#         gathering.item37_page6 = request.POST.get('item37_page6')
#         gathering.item37_page7 = request.POST.get('item37_page7')
#         gathering.item37_page8 = request.POST.get('item37_page8')
#         gathering.item37_page9 = request.POST.get('item37_page9')
#         gathering.item37_page10 = request.POST.get('item37_page10')

#         gathering.item38_page1 = request.POST.get('item38_page1')
#         gathering.item38_page2 = request.POST.get('item38_page2')
#         gathering.item38_page3 = request.POST.get('item38_page3')
#         gathering.item38_page4 = request.POST.get('item38_page4')
#         gathering.item38_page5 = request.POST.get('item38_page5')
#         gathering.item38_page6 = request.POST.get('item38_page6')
#         gathering.item38_page7 = request.POST.get('item38_page7')
#         gathering.item38_page8 = request.POST.get('item38_page8')
#         gathering.item38_page9 = request.POST.get('item38_page9')
#         gathering.item38_page10 = request.POST.get('item38_page10')

#         gathering.item39_page1 = request.POST.get('item39_page1')
#         gathering.item39_page2 = request.POST.get('item39_page2')
#         gathering.item39_page3 = request.POST.get('item39_page3')
#         gathering.item39_page4 = request.POST.get('item39_page4')
#         gathering.item39_page5 = request.POST.get('item39_page5')
#         gathering.item39_page6 = request.POST.get('item39_page6')
#         gathering.item39_page7 = request.POST.get('item39_page7')
#         gathering.item39_page8 = request.POST.get('item39_page8')
#         gathering.item39_page9 = request.POST.get('item39_page9')
#         gathering.item39_page10 = request.POST.get('item39_page10')

#         gathering.item40_page1 = request.POST.get('item40_page1')
#         gathering.item40_page2 = request.POST.get('item40_page2')
#         gathering.item40_page3 = request.POST.get('item40_page3')
#         gathering.item40_page4 = request.POST.get('item40_page4')
#         gathering.item40_page5 = request.POST.get('item40_page5')
#         gathering.item40_page6 = request.POST.get('item40_page6')
#         gathering.item40_page7 = request.POST.get('item40_page7')
#         gathering.item40_page8 = request.POST.get('item40_page8')
#         gathering.item40_page9 = request.POST.get('item40_page9')
#         gathering.item40_page10 = request.POST.get('item40_page10')

#         gathering.item41_page1 = request.POST.get('item41_page1')
#         gathering.item41_page2 = request.POST.get('item41_page2')
#         gathering.item41_page3 = request.POST.get('item41_page3')
#         gathering.item41_page4 = request.POST.get('item41_page4')
#         gathering.item41_page5 = request.POST.get('item41_page5')
#         gathering.item41_page6 = request.POST.get('item41_page6')
#         gathering.item41_page7 = request.POST.get('item41_page7')
#         gathering.item41_page8 = request.POST.get('item41_page8')
#         gathering.item41_page9 = request.POST.get('item41_page9')
#         gathering.item41_page10 = request.POST.get('item41_page10')

#         gathering.item42_page1 = request.POST.get('item42_page1')
#         gathering.item42_page2 = request.POST.get('item42_page2')
#         gathering.item42_page3 = request.POST.get('item42_page3')
#         gathering.item42_page4 = request.POST.get('item42_page4')
#         gathering.item42_page5 = request.POST.get('item42_page5')
#         gathering.item42_page6 = request.POST.get('item42_page6')
#         gathering.item42_page7 = request.POST.get('item42_page7')
#         gathering.item42_page8 = request.POST.get('item42_page8')
#         gathering.item42_page9 = request.POST.get('item42_page9')
#         gathering.item42_page10 = request.POST.get('item42_page10')

#         gathering.item43_page1 = request.POST.get('item43_page1')
#         gathering.item43_page2 = request.POST.get('item43_page2')
#         gathering.item43_page3 = request.POST.get('item43_page3')
#         gathering.item43_page4 = request.POST.get('item43_page4')
#         gathering.item43_page5 = request.POST.get('item43_page5')
#         gathering.item43_page6 = request.POST.get('item43_page6')
#         gathering.item43_page7 = request.POST.get('item43_page7')
#         gathering.item43_page8 = request.POST.get('item43_page8')
#         gathering.item43_page9 = request.POST.get('item43_page9')
#         gathering.item43_page10 = request.POST.get('item43_page10')

#         gathering.item44_page1 = request.POST.get('item44_page1')
#         gathering.item44_page2 = request.POST.get('item44_page2')
#         gathering.item44_page3 = request.POST.get('item44_page3')
#         gathering.item44_page4 = request.POST.get('item44_page4')
#         gathering.item44_page5 = request.POST.get('item44_page5')
#         gathering.item44_page6 = request.POST.get('item44_page6')
#         gathering.item44_page7 = request.POST.get('item44_page7')
#         gathering.item44_page8 = request.POST.get('item44_page8')
#         gathering.item44_page9 = request.POST.get('item44_page9')
#         gathering.item44_page10 = request.POST.get('item44_page10')

#         gathering.item45_page1 = request.POST.get('item45_page1')
#         gathering.item45_page2 = request.POST.get('item45_page2')
#         gathering.item45_page3 = request.POST.get('item45_page3')
#         gathering.item45_page4 = request.POST.get('item45_page4')
#         gathering.item45_page5 = request.POST.get('item45_page5')
#         gathering.item45_page6 = request.POST.get('item45_page6')
#         gathering.item45_page7 = request.POST.get('item45_page7')
#         gathering.item45_page8 = request.POST.get('item45_page8')
#         gathering.item45_page9 = request.POST.get('item45_page9')
#         gathering.item45_page10 = request.POST.get('item45_page10')

#         gathering.item46_page1 = request.POST.get('item46_page1')
#         gathering.item46_page2 = request.POST.get('item46_page2')
#         gathering.item46_page3 = request.POST.get('item46_page3')
#         gathering.item46_page4 = request.POST.get('item46_page4')
#         gathering.item46_page5 = request.POST.get('item46_page5')
#         gathering.item46_page6 = request.POST.get('item46_page6')
#         gathering.item46_page7 = request.POST.get('item46_page7')
#         gathering.item46_page8 = request.POST.get('item46_page8')
#         gathering.item46_page9 = request.POST.get('item46_page9')
#         gathering.item46_page10 = request.POST.get('item46_page10')

#         gathering.item47_page1 = request.POST.get('item47_page1')
#         gathering.item47_page2 = request.POST.get('item47_page2')
#         gathering.item47_page3 = request.POST.get('item47_page3')
#         gathering.item47_page4 = request.POST.get('item47_page4')
#         gathering.item47_page5 = request.POST.get('item47_page5')
#         gathering.item47_page6 = request.POST.get('item47_page6')
#         gathering.item47_page7 = request.POST.get('item47_page7')
#         gathering.item47_page8 = request.POST.get('item47_page8')
#         gathering.item47_page9 = request.POST.get('item47_page9')
#         gathering.item47_page10 = request.POST.get('item47_page10')

#         gathering.item48_page1 = request.POST.get('item48_page1')
#         gathering.item48_page2 = request.POST.get('item48_page2')
#         gathering.item48_page3 = request.POST.get('item48_page3')
#         gathering.item48_page4 = request.POST.get('item48_page4')
#         gathering.item48_page5 = request.POST.get('item48_page5')
#         gathering.item48_page6 = request.POST.get('item48_page6')
#         gathering.item48_page7 = request.POST.get('item48_page7')
#         gathering.item48_page8 = request.POST.get('item48_page8')
#         gathering.item48_page9 = request.POST.get('item48_page9')
#         gathering.item48_page10 = request.POST.get('item48_page10')

#         gathering.item49_page1 = request.POST.get('item49_page1')
#         gathering.item49_page2 = request.POST.get('item49_page2')
#         gathering.item49_page3 = request.POST.get('item49_page3')
#         gathering.item49_page3 = request.POST.get('item49_page3')
#         gathering.item49_page3 = request.POST.get('item49_page3')
#         gathering.item49_page4 = request.POST.get('item49_page4')
#         gathering.item49_page5 = request.POST.get('item49_page5')
#         gathering.item49_page6 = request.POST.get('item49_page6')
#         gathering.item49_page7 = request.POST.get('item49_page7')
#         gathering.item49_page8 = request.POST.get('item49_page8')
#         gathering.item49_page9 = request.POST.get('item49_page9')
#         gathering.item49_page10 = request.POST.get('item49_page10')

#         gathering.item50_page1 = request.POST.get('item50_page1')
#         gathering.item50_page2 = request.POST.get('item50_page2')
#         gathering.item50_page3 = request.POST.get('item50_page3')
#         gathering.item50_page4 = request.POST.get('item50_page4')
#         gathering.item50_page5 = request.POST.get('item50_page5')
#         gathering.item50_page6 = request.POST.get('item50_page6')
#         gathering.item50_page7 = request.POST.get('item50_page7')
#         gathering.item50_page8 = request.POST.get('item50_page8')
#         gathering.item50_page9 = request.POST.get('item50_page9')
#         gathering.item50_page10 = request.POST.get('item50_page10')

#         gathering.total_gathering=request.POST.get('printing_received_form')
#         gathering.wastage_form = request.POST.get('print_wastage_form')
#         gathering.gathering_date = request.POST.get('print_date')
#         gathering.gathering_date = datetime.datetime.now()
#         temp_page1=[]
#         if gathering.item1_page1:
#             temp_page1.append(gathering.item1_page1)
#         if gathering.item1_page2:
#             temp_page1.append(gathering.item1_page2)
#         if gathering.item1_page3:
#             temp_page1.append(gathering.item1_page3)
#         if gathering.item1_page4:
#             temp_page1.append(gathering.item1_page4)
#         if gathering.item1_page5:
#             temp_page1.append(gathering.item1_page5)
#         if gathering.item1_page6:
#             temp_page1.append(gathering.item1_page6)
#         if gathering.item1_page7:
#             temp_page1.append(gathering.item1_page7)
#         if gathering.item1_page8:
#             temp_page1.append(gathering.item1_page8)
#         if gathering.item1_page9:
#             temp_page1.append(gathering.item1_page9)
#         if gathering.item1_page10:
#             temp_page1.append(gathering.item1_page10)
        
#         temp_page1=[int(i) for i in temp_page1] 
#         temp_page1.sort(reverse=False)
    
#         if temp_page1:
#             gathering.total_gathering_1=temp_page1[0]
#             gathering.wastage_form_1 = float(gathering.quantity_1) - float(gathering.total_gathering_1)
#         else:
#             gathering.item1_page1=0
#             gathering.item1_page2=0
#             gathering.item1_page3=0
#             gathering.item1_page4=0
#             gathering.item1_page5=0
#             gathering.item1_page6=0
#             gathering.item1_page7=0
#             gathering.item1_page8=0
#             gathering.item1_page9=0
#             gathering.item1_page10=0

    


#         temp_page2=[]
#         if gathering.item2_page1:
#             temp_page2.append(gathering.item2_page1)
#         if gathering.item2_page2:
#             temp_page2.append(gathering.item2_page2)
#         if gathering.item2_page3:
#             temp_page2.append(gathering.item2_page3)
#         if gathering.item2_page4:
#             temp_page2.append(gathering.item2_page4)
#         if gathering.item2_page5:
#             temp_page2.append(gathering.item2_page5)
#         if gathering.item2_page6:
#             temp_page2.append(gathering.item2_page6)
#         if gathering.item2_page7:
#             temp_page2.append(gathering.item2_page7)
#         if gathering.item2_page8:
#             temp_page2.append(gathering.item2_page8)
#         if gathering.item2_page9:
#             temp_page2.append(gathering.item2_page9)
#         if gathering.item2_page10:
#             temp_page2.append(gathering.item2_page10)
#         temp_page2=[int(i) for i in temp_page2]
#         temp_page2.sort(reverse=False)
        
    
        
#         if temp_page2:
#             gathering.total_gathering_2=temp_page2[0]
#             gathering.wastage_form_2 = float(gathering.quantity_2) - float(gathering.total_gathering_2)
#         else:
#             gathering.item2_page1=0
#             gathering.item2_page2=0
#             gathering.item2_page3=0
#             gathering.item2_page4=0
#             gathering.item2_page5=0
#             gathering.item2_page6=0
#             gathering.item2_page7=0
#             gathering.item2_page8=0
#             gathering.item2_page9=0
#             gathering.item2_page10=0


#         temp_page3=[]
#         if gathering.item3_page1:
#             temp_page3.append(gathering.item3_page1)
#         if gathering.item3_page2:
#             temp_page3.append(gathering.item3_page2)
#         if gathering.item3_page3:
#             temp_page3.append(gathering.item3_page3)
#         if gathering.item3_page4:
#             temp_page3.append(gathering.item3_page4)
#         if gathering.item3_page5:
#             temp_page3.append(gathering.item3_page5)
#         if gathering.item3_page6:
#             temp_page3.append(gathering.item3_page6)
#         if gathering.item3_page7:
#             temp_page3.append(gathering.item3_page7)
#         if gathering.item3_page8:
#             temp_page3.append(gathering.item3_page8)
#         if gathering.item3_page9:
#             temp_page3.append(gathering.item3_page9)
#         if gathering.item3_page10:
#             temp_page3.append(gathering.item3_page10)
#         temp_page3=[int(i) for i in temp_page3]
#         temp_page3.sort(reverse=False)
        
        
        
#         if temp_page3:
#             gathering.total_gathering_3=temp_page3[0]
#             gathering.wastage_form_3 = float(gathering.quantity_3) - float(gathering.total_gathering_3)
#         else:
#             gathering.item3_page1=0
#             gathering.item3_page2=0
#             gathering.item3_page3=0
#             gathering.item3_page4=0
#             gathering.item3_page5=0
#             gathering.item3_page6=0
#             gathering.item3_page7=0
#             gathering.item3_page8=0
#             gathering.item3_page9=0
#             gathering.item3_page10=0


#         temp_page4=[]
#         if gathering.item4_page1:
#             temp_page4.append(gathering.item4_page1)
#         if gathering.item4_page2:
#             temp_page4.append(gathering.item4_page2)
#         if gathering.item4_page3:
#             temp_page4.append(gathering.item4_page3)
#         if gathering.item4_page4:
#             temp_page4.append(gathering.item4_page4)
#         if gathering.item4_page5:
#             temp_page4.append(gathering.item4_page5)
#         if gathering.item4_page6:
#             temp_page4.append(gathering.item4_page6)
#         if gathering.item4_page7:
#             temp_page4.append(gathering.item4_page7)
#         if gathering.item4_page8:
#             temp_page4.append(gathering.item4_page8)
#         if gathering.item4_page9:
#             temp_page4.append(gathering.item4_page9)
#         if gathering.item4_page10:
#             temp_page4.append(gathering.item4_page10)
#         temp_page4=[int(i) for i in temp_page4]
#         temp_page4.sort(reverse=False)
    
    
        
#         if temp_page4:
#             gathering.total_gathering_4=temp_page4[0]
#             gathering.wastage_form_4 = float(gathering.quantity_4) - float(gathering.total_gathering_4)
#         else:
#             gathering.item4_page1=0
#             gathering.item4_page2=0
#             gathering.item4_page3=0
#             gathering.item4_page4=0
#             gathering.item4_page5=0
#             gathering.item4_page6=0
#             gathering.item4_page7=0
#             gathering.item4_page8=0
#             gathering.item4_page9=0
#             gathering.item4_page10=0



#         temp_page5=[]
#         if gathering.item5_page1:
#             temp_page5.append(gathering.item5_page1)
#         if gathering.item5_page2:
#             temp_page5.append(gathering.item5_page2)
#         if gathering.item5_page3:
#             temp_page5.append(gathering.item5_page3)
#         if gathering.item5_page4:
#             temp_page5.append(gathering.item5_page4)
#         if gathering.item5_page5:
#             temp_page5.append(gathering.item5_page5)
#         if gathering.item5_page6:
#             temp_page5.append(gathering.item5_page6)
#         if gathering.item5_page7:
#             temp_page5.append(gathering.item5_page7)
#         if gathering.item5_page8:
#             temp_page5.append(gathering.item5_page8)
#         if gathering.item5_page9:
#             temp_page5.append(gathering.item5_page9)
#         if gathering.item5_page10:
#             temp_page5.append(gathering.item5_page10)
#         temp_page5=[int(i) for i in temp_page5]
#         temp_page5.sort(reverse=False)
    

        
#         if temp_page5:
#             gathering.total_gathering_5=temp_page5[0]
#             gathering.wastage_form_5 = float(gathering.quantity_5) - float(gathering.total_gathering_5)
#         else:
#             gathering.item5_page1=0
#             gathering.item5_page2=0
#             gathering.item5_page3=0
#             gathering.item5_page4=0
#             gathering.item5_page5=0
#             gathering.item5_page6=0
#             gathering.item5_page7=0
#             gathering.item5_page8=0
#             gathering.item5_page9=0
#             gathering.item5_page10=0



#         temp_page6=[]
#         if gathering.item6_page1:
#             temp_page6.append(gathering.item6_page1)
#         if gathering.item6_page2:
#             temp_page6.append(gathering.item6_page2)
#         if gathering.item6_page3:
#             temp_page6.append(gathering.item6_page3)
#         if gathering.item6_page4:
#             temp_page6.append(gathering.item6_page4)
#         if gathering.item6_page5:
#             temp_page6.append(gathering.item6_page5)
#         if gathering.item6_page6:
#             temp_page6.append(gathering.item6_page6)
#         if gathering.item6_page7:
#             temp_page6.append(gathering.item6_page7)
#         if gathering.item6_page8:
#             temp_page6.append(gathering.item6_page8)
#         if gathering.item6_page9:
#             temp_page6.append(gathering.item6_page9)
#         if gathering.item6_page10:
#             temp_page6.append(gathering.item6_page10)
#         temp_page6=[int(i) for i in temp_page6]
#         temp_page6.sort(reverse=False)
    
        
        
#         if temp_page6:
#             gathering.total_gathering_6=temp_page6[0]
#             gathering.wastage_form_6 = float(gathering.quantity_6) - float(gathering.total_gathering_6)
#         else:
#             gathering.item6_page1=0
#             gathering.item6_page2=0
#             gathering.item6_page3=0
#             gathering.item6_page4=0
#             gathering.item6_page5=0
#             gathering.item6_page6=0
#             gathering.item6_page7=0
#             gathering.item6_page8=0
#             gathering.item6_page9=0
#             gathering.item6_page10=0


#         temp_page7=[]
#         if gathering.item7_page1:
#             temp_page7.append(gathering.item7_page1)
#         if gathering.item7_page2:
#             temp_page7.append(gathering.item7_page2)
#         if gathering.item7_page3:
#             temp_page7.append(gathering.item7_page3)
#         if gathering.item7_page4:
#             temp_page7.append(gathering.item7_page4)
#         if gathering.item7_page5:
#             temp_page7.append(gathering.item7_page5)
#         if gathering.item7_page6:
#             temp_page7.append(gathering.item7_page6)
#         if gathering.item7_page7:
#             temp_page7.append(gathering.item7_page7)
#         if gathering.item7_page8:
#             temp_page7.append(gathering.item7_page8)
#         if gathering.item7_page9:
#             temp_page7.append(gathering.item7_page9)
#         if gathering.item7_page10:
#             temp_page7.append(gathering.item7_page10)
#         temp_page7=[int(i) for i in temp_page7]
#         temp_page7.sort(reverse=False)
        
        
#         if temp_page7:
#             gathering.total_gathering_7=temp_page7[0]
#             gathering.wastage_form_7 = float(gathering.quantity_7) - float(gathering.total_gathering_7)
#         else:
#             gathering.item7_page1=0
#             gathering.item7_page2=0
#             gathering.item7_page3=0
#             gathering.item7_page4=0
#             gathering.item7_page5=0
#             gathering.item7_page6=0
#             gathering.item7_page7=0
#             gathering.item7_page8=0
#             gathering.item7_page9=0
#             gathering.item7_page10=0



#         temp_page8=[]
#         if gathering.item8_page1:
#             temp_page8.append(gathering.item8_page1)
#         if gathering.item8_page2:
#             temp_page8.append(gathering.item8_page2)
#         if gathering.item8_page3:
#             temp_page8.append(gathering.item8_page3)
#         if gathering.item8_page4:
#             temp_page8.append(gathering.item8_page4)
#         if gathering.item8_page5:
#             temp_page8.append(gathering.item8_page5)
#         if gathering.item8_page6:
#             temp_page8.append(gathering.item8_page6)
#         if gathering.item8_page7:
#             temp_page8.append(gathering.item8_page7)
#         if gathering.item8_page8:
#             temp_page8.append(gathering.item8_page8)
#         if gathering.item8_page9:
#             temp_page8.append(gathering.item8_page9)
#         if gathering.item8_page10:
#             temp_page8.append(gathering.item8_page10)
#         temp_page8=[int(i) for i in temp_page8]
#         temp_page8.sort(reverse=False)
        
        
#         if temp_page8:
#             gathering.total_gathering_8=temp_page8[0]
#             gathering.wastage_form_8 = float(gathering.quantity_8) - float(gathering.total_gathering_8)
#         else:
#             gathering.item8_page1=0
#             gathering.item8_page2=0
#             gathering.item8_page3=0
#             gathering.item8_page4=0
#             gathering.item8_page5=0
#             gathering.item8_page6=0
#             gathering.item8_page7=0
#             gathering.item8_page8=0
#             gathering.item8_page9=0
#             gathering.item8_page10=0



#         temp_page9=[]
#         if gathering.item9_page1:
#             temp_page9.append(gathering.item9_page1)
#         if gathering.item9_page2:
#             temp_page9.append(gathering.item9_page2)
#         if gathering.item9_page3:
#             temp_page9.append(gathering.item9_page3)
#         if gathering.item9_page4:
#             temp_page9.append(gathering.item9_page4)
#         if gathering.item9_page5:
#             temp_page9.append(gathering.item9_page5)
#         if gathering.item9_page6:
#             temp_page9.append(gathering.item9_page6)
#         if gathering.item9_page7:
#             temp_page9.append(gathering.item9_page7)
#         if gathering.item9_page8:
#             temp_page9.append(gathering.item9_page8)
#         if gathering.item9_page9:
#             temp_page9.append(gathering.item9_page9)
#         if gathering.item9_page10:
#             temp_page9.append(gathering.item9_page10)
#         temp_page9=[int(i) for i in temp_page9]
#         temp_page9.sort(reverse=False)
    
    
        
#         if temp_page9:
#             gathering.total_gathering_9=temp_page9[0]
#             gathering.wastage_form_9 = float(gathering.quantity_9) - float(gathering.total_gathering_9)
#         else:
#             gathering.item9_page1=0
#             gathering.item9_page2=0
#             gathering.item9_page3=0
#             gathering.item9_page4=0
#             gathering.item9_page5=0
#             gathering.item9_page6=0
#             gathering.item9_page7=0
#             gathering.item9_page8=0
#             gathering.item9_page9=0
#             gathering.item9_page10=0




#         temp_page10=[]
#         if gathering.item10_page1:
#             temp_page10.append(gathering.item10_page1)
#         if gathering.item10_page2:
#             temp_page10.append(gathering.item10_page2)
#         if gathering.item10_page3:
#             temp_page10.append(gathering.item10_page3)
#         if gathering.item10_page4:
#             temp_page10.append(gathering.item10_page4)
#         if gathering.item10_page5:
#             temp_page10.append(gathering.item10_page5)
#         if gathering.item10_page6:
#             temp_page10.append(gathering.item10_page6)
#         if gathering.item10_page7:
#             temp_page10.append(gathering.item10_page7)
#         if gathering.item10_page8:
#             temp_page10.append(gathering.item10_page8)
#         if gathering.item10_page9:
#             temp_page10.append(gathering.item10_page9)
#         if gathering.item10_page10:
#             temp_page10.append(gathering.item10_page10)
#         temp_page10=[int(i) for i in temp_page10]
#         temp_page10.sort(reverse=False)
    
    
        
#         if temp_page10:
#             gathering.total_gathering_10=temp_page10[0]
#             gathering.wastage_form_10 = float(gathering.quantity_10) - float(gathering.total_gathering_10)
#         else:
#             gathering.item10_page1=0
#             gathering.item10_page2=0
#             gathering.item10_page3=0
#             gathering.item10_page4=0
#             gathering.item10_page5=0
#             gathering.item10_page6=0
#             gathering.item10_page7=0
#             gathering.item10_page8=0
#             gathering.item10_page9=0
#             gathering.item10_page10=0



#         temp_page11=[]
#         if gathering.item11_page1:
#             temp_page11.append(gathering.item11_page1)
#         if gathering.item11_page2:
#             temp_page11.append(gathering.item11_page2)
#         if gathering.item11_page3:
#             temp_page11.append(gathering.item11_page3)
#         if gathering.item11_page4:
#             temp_page11.append(gathering.item11_page4)
#         if gathering.item11_page5:
#             temp_page11.append(gathering.item11_page5)
#         if gathering.item11_page6:
#             temp_page11.append(gathering.item11_page6)
#         if gathering.item11_page7:
#             temp_page11.append(gathering.item11_page7)
#         if gathering.item11_page8:
#             temp_page11.append(gathering.item11_page8)
#         if gathering.item11_page9:
#             temp_page11.append(gathering.item11_page9)
#         if gathering.item11_page10:
#             temp_page11.append(gathering.item11_page10)
#         temp_page11=[int(i) for i in temp_page11]
#         temp_page11.sort(reverse=False)

#         if temp_page11:
#             gathering.total_gathering_11=temp_page11[0]
#             gathering.wastage_form_11 = float(gathering.quantity_11) - float(gathering.total_gathering_11)
#         else:
#             gathering.item11_page1=0
#             gathering.item11_page2=0
#             gathering.item11_page3=0
#             gathering.item11_page4=0
#             gathering.item11_page5=0
#             gathering.item11_page6=0
#             gathering.item11_page7=0
#             gathering.item11_page8=0
#             gathering.item11_page9=0
#             gathering.item11_page10=0



#         temp_page12=[]
#         if gathering.item12_page1:
#             temp_page12.append(gathering.item12_page1)
#         if gathering.item12_page2:
#             temp_page12.append(gathering.item12_page2)
#         if gathering.item12_page3:
#             temp_page12.append(gathering.item12_page3)
#         if gathering.item12_page4:
#             temp_page12.append(gathering.item12_page4)
#         if gathering.item12_page5:
#             temp_page12.append(gathering.item12_page5)
#         if gathering.item12_page6:
#             temp_page12.append(gathering.item12_page6)
#         if gathering.item12_page7:
#             temp_page12.append(gathering.item12_page7)
#         if gathering.item12_page8:
#             temp_page12.append(gathering.item12_page8)
#         if gathering.item12_page9:
#             temp_page12.append(gathering.item12_page9)
#         if gathering.item12_page10:
#             temp_page12.append(gathering.item12_page10)
        
#         temp_page12=[int(i) for i in temp_page12] 
#         temp_page12.sort(reverse=False)

#         if temp_page12:
#             gathering.total_gathering_12=temp_page1[0]
#             gathering.wastage_form_12 = float(gathering.quantity_12) - float(gathering.total_gathering_12)
#         else:
#             gathering.item12_page1=0
#             gathering.item12_page2=0
#             gathering.item12_page3=0
#             gathering.item12_page4=0
#             gathering.item12_page5=0
#             gathering.item12_page6=0
#             gathering.item12_page7=0
#             gathering.item12_page8=0
#             gathering.item12_page9=0
#             gathering.item12_page10=0

    


#         temp_page13=[]
#         if gathering.item13_page1:
#             temp_page13.append(gathering.item13_page1)
#         if gathering.item13_page2:
#             temp_page13.append(gathering.item13_page2)
#         if gathering.item13_page3:
#             temp_page13.append(gathering.item13_page3)
#         if gathering.item13_page4:
#             temp_page13.append(gathering.item13_page4)
#         if gathering.item13_page5:
#             temp_page13.append(gathering.item13_page5)
#         if gathering.item13_page6:
#             temp_page13.append(gathering.item13_page6)
#         if gathering.item13_page7:
#             temp_page13.append(gathering.item13_page7)
#         if gathering.item13_page8:
#             temp_page13.append(gathering.item13_page8)
#         if gathering.item13_page9:
#             temp_page13.append(gathering.item13_page9)
#         if gathering.item13_page10:
#             temp_page13.append(gathering.item13_page10)
#         temp_page13=[int(i) for i in temp_page13]
#         temp_page13.sort(reverse=False)
        
    
        
#         if temp_page13:
#             gathering.total_gathering_13=temp_page13[0]
#             gathering.wastage_form_13 = float(gathering.quantity_13) - float(gathering.total_gathering_13)
#         else:
#             gathering.item13_page1=0
#             gathering.item13_page2=0
#             gathering.item13_page3=0
#             gathering.item13_page4=0
#             gathering.item13_page5=0
#             gathering.item13_page6=0
#             gathering.item13_page7=0
#             gathering.item13_page8=0
#             gathering.item13_page9=0
#             gathering.item13_page10=0


#         temp_page14=[]
#         if gathering.item14_page1:
#             temp_page14.append(gathering.item14_page1)
#         if gathering.item14_page2:
#             temp_page14.append(gathering.item14_page2)
#         if gathering.item14_page3:
#             temp_page14.append(gathering.item14_page3)
#         if gathering.item14_page4:
#             temp_page14.append(gathering.item14_page4)
#         if gathering.item14_page5:
#             temp_page14.append(gathering.item14_page5)
#         if gathering.item14_page6:
#             temp_page14.append(gathering.item14_page6)
#         if gathering.item14_page7:
#             temp_page14.append(gathering.item14_page7)
#         if gathering.item14_page8:
#             temp_page14.append(gathering.item14_page8)
#         if gathering.item14_page9:
#             temp_page14.append(gathering.item14_page9)
#         if gathering.item14_page10:
#             temp_page14.append(gathering.item14_page10)
#         temp_page14=[int(i) for i in temp_page14]
#         temp_page14.sort(reverse=False)
        
        
        
#         if temp_page14:
#             gathering.total_gathering_14=temp_page14[0]
#             gathering.wastage_form_14 = float(gathering.quantity_14) - float(gathering.total_gathering_14)
#         else:
#             gathering.item14_page1=0
#             gathering.item14_page2=0
#             gathering.item14_page3=0
#             gathering.item14_page4=0
#             gathering.item14_page5=0
#             gathering.item14_page6=0
#             gathering.item14_page7=0
#             gathering.item14_page8=0
#             gathering.item14_page9=0
#             gathering.item14_page10=0


#         temp_page15=[]
#         if gathering.item15_page1:
#             temp_page15.append(gathering.item15_page1)
#         if gathering.item15_page2:
#             temp_page15.append(gathering.item15_page2)
#         if gathering.item15_page3:
#             temp_page15.append(gathering.item15_page3)
#         if gathering.item15_page4:
#             temp_page15.append(gathering.item15_page4)
#         if gathering.item15_page5:
#             temp_page15.append(gathering.item15_page5)
#         if gathering.item15_page6:
#             temp_page15.append(gathering.item15_page6)
#         if gathering.item15_page7:
#             temp_page15.append(gathering.item15_page7)
#         if gathering.item15_page8:
#             temp_page15.append(gathering.item15_page8)
#         if gathering.item15_page9:
#             temp_page15.append(gathering.item15_page9)
#         if gathering.item15_page10:
#             temp_page15.append(gathering.item15_page10)
#         temp_page15=[int(i) for i in temp_page15]
#         temp_page15.sort(reverse=False)
    
    
        
#         if temp_page15:
#             gathering.total_gathering_15=temp_page15[0]
#             gathering.wastage_form_15 = float(gathering.quantity_15) - float(gathering.total_gathering_15)
#         else:
#             gathering.item15_page1=0
#             gathering.item15_page2=0
#             gathering.item15_page3=0
#             gathering.item15_page4=0
#             gathering.item15_page5=0
#             gathering.item15_page6=0
#             gathering.item15_page7=0
#             gathering.item15_page8=0
#             gathering.item15_page9=0
#             gathering.item15_page10=0




        

#         temp_page16=[]
#         if gathering.item16_page1:
#             temp_page16.append(gathering.item16_page1)
#         if gathering.item16_page2:
#             temp_page16.append(gathering.item16_page2)
#         if gathering.item16_page3:
#             temp_page16.append(gathering.item16_page3)
#         if gathering.item16_page4:
#             temp_page16.append(gathering.item16_page4)
#         if gathering.item16_page5:
#             temp_page16.append(gathering.item16_page5)
#         if gathering.item16_page6:
#             temp_page16.append(gathering.item16_page6)
#         if gathering.item16_page7:
#             temp_page16.append(gathering.item16_page7)
#         if gathering.item16_page8:
#             temp_page16.append(gathering.item16_page8)
#         if gathering.item16_page9:
#             temp_page16.append(gathering.item16_page9)
#         if gathering.item16_page10:
#             temp_page16.append(gathering.item16_page10)
#         temp_page16=[int(i) for i in temp_page16]
#         temp_page16.sort(reverse=False)
    
        
        
#         if temp_page16:
#             gathering.total_gathering_16=temp_page16[0]
#             gathering.wastage_form_16 = float(gathering.quantity_16) - float(gathering.total_gathering_16)
#         else:
#             gathering.item16_page1=0
#             gathering.item16_page2=0
#             gathering.item16_page3=0
#             gathering.item16_page4=0
#             gathering.item16_page5=0
#             gathering.item16_page6=0
#             gathering.item16_page7=0
#             gathering.item16_page8=0
#             gathering.item16_page9=0
#             gathering.item16_page10=0


#         temp_page17=[]
#         if gathering.item17_page1:
#             temp_page17.append(gathering.item17_page1)
#         if gathering.item17_page2:
#             temp_page17.append(gathering.item17_page2)
#         if gathering.item17_page3:
#             temp_page17.append(gathering.item17_page3)
#         if gathering.item7_page4:
#             temp_page17.append(gathering.item17_page4)
#         if gathering.item17_page5:
#             temp_page17.append(gathering.item17_page5)
#         if gathering.item17_page6:
#             temp_page17.append(gathering.item17_page6)
#         if gathering.item17_page7:
#             temp_page17.append(gathering.item17_page7)
#         if gathering.item17_page8:
#             temp_page17.append(gathering.item17_page8)
#         if gathering.item17_page9:
#             temp_page17.append(gathering.item17_page9)
#         if gathering.item17_page10:
#             temp_page17.append(gathering.item17_page10)
#         temp_page17=[int(i) for i in temp_page17]
#         temp_page17.sort(reverse=False)
        
        
#         if temp_page17:
#             gathering.total_gathering_17=temp_page17[0]
#             gathering.wastage_form_17 = float(gathering.quantity_17) - float(gathering.total_gathering_17)
#         else:
#             gathering.item17_page1=0
#             gathering.item17_page2=0
#             gathering.item17_page3=0
#             gathering.item17_page4=0
#             gathering.item17_page5=0
#             gathering.item17_page6=0
#             gathering.item17_page7=0
#             gathering.item17_page8=0
#             gathering.item17_page9=0
#             gathering.item17_page10=0



#         temp_page18=[]
#         if gathering.item18_page1:
#             temp_page18.append(gathering.item18_page1)
#         if gathering.item18_page2:
#             temp_page18.append(gathering.item18_page2)
#         if gathering.item18_page3:
#             temp_page18.append(gathering.item18_page3)
#         if gathering.item18_page4:
#             temp_page18.append(gathering.item18_page4)
#         if gathering.item18_page5:
#             temp_page18.append(gathering.item18_page5)
#         if gathering.item18_page6:
#             temp_page18.append(gathering.item18_page6)
#         if gathering.item18_page7:
#             temp_page18.append(gathering.item18_page7)
#         if gathering.item18_page8:
#             temp_page18.append(gathering.item18_page8)
#         if gathering.item18_page9:
#             temp_page18.append(gathering.item18_page9)
#         if gathering.item18_page10:
#             temp_page18.append(gathering.item18_page10)
#         temp_page18=[int(i) for i in temp_page18]
#         temp_page18.sort(reverse=False)
        
        
#         if temp_page18:
#             gathering.total_gathering_18=temp_page18[0]
#             gathering.wastage_form_18 = float(gathering.quantity_18) - float(gathering.total_gathering_18)
#         else:
#             gathering.item18_page1=0
#             gathering.item18_page2=0
#             gathering.item18_page3=0
#             gathering.item18_page4=0
#             gathering.item18_page5=0
#             gathering.item18_page6=0
#             gathering.item18_page7=0
#             gathering.item18_page8=0
#             gathering.item18_page9=0
#             gathering.item18_page10=0



#         temp_page19=[]
#         if gathering.item19_page1:
#             temp_page19.append(gathering.item19_page1)
#         if gathering.item19_page2:
#             temp_page19.append(gathering.item19_page2)
#         if gathering.item19_page3:
#             temp_page19.append(gathering.item19_page3)
#         if gathering.item19_page4:
#             temp_page19.append(gathering.item19_page4)
#         if gathering.item19_page5:
#             temp_page19.append(gathering.item19_page5)
#         if gathering.item19_page6:
#             temp_page19.append(gathering.item19_page6)
#         if gathering.item19_page7:
#             temp_page19.append(gathering.item19_page7)
#         if gathering.item19_page8:
#             temp_page19.append(gathering.item19_page8)
#         if gathering.item19_page9:
#             temp_page19.append(gathering.item19_page9)
#         if gathering.item19_page10:
#             temp_page19.append(gathering.item19_page10)
#         temp_page19=[int(i) for i in temp_page19]
#         temp_page19.sort(reverse=False)
    
    
        
#         if temp_page19:
#             gathering.total_gathering_19=temp_page19[0]
#             gathering.wastage_form_19 = float(gathering.quantity_19) - float(gathering.total_gathering_19)
#         else:
#             gathering.item19_page1=0
#             gathering.item19_page2=0
#             gathering.item19_page3=0
#             gathering.item19_page4=0
#             gathering.item19_page5=0
#             gathering.item19_page6=0
#             gathering.item19_page7=0
#             gathering.item19_page8=0
#             gathering.item19_page9=0
#             gathering.item19_page10=0




#         temp_page20=[]
#         if gathering.item20_page1:
#             temp_page20.append(gathering.item20_page1)
#         if gathering.item20_page2:
#             temp_page20.append(gathering.item20_page2)
#         if gathering.item20_page3:
#             temp_page20.append(gathering.item20_page3)
#         if gathering.item20_page4:
#             temp_page20.append(gathering.item20_page4)
#         if gathering.item20_page5:
#             temp_page20.append(gathering.item20_page5)
#         if gathering.item20_page6:
#             temp_page20.append(gathering.item20_page6)
#         if gathering.item20_page7:
#             temp_page20.append(gathering.item20_page7)
#         if gathering.item20_page8:
#             temp_page20.append(gathering.item20_page8)
#         if gathering.item20_page9:
#             temp_page20.append(gathering.item20_page9)
#         if gathering.item20_page10:
#             temp_page20.append(gathering.item20_page10)
#         temp_page20=[int(i) for i in temp_page20]
#         temp_page20.sort(reverse=False)
    
    
        
#         if temp_page20:
#             gathering.total_gathering_20=temp_page20[0]
#             gathering.wastage_form_20 = float(gathering.quantity_20) - float(gathering.total_gathering_20)
#         else:
#             gathering.item20_page1=0
#             gathering.item20_page2=0
#             gathering.item20_page3=0
#             gathering.item20_page4=0
#             gathering.item20_page5=0
#             gathering.item20_page6=0
#             gathering.item20_page7=0
#             gathering.item20_page8=0
#             gathering.item20_page9=0
#             gathering.item20_page10=0
    
    
        
#         temp_page21=[]
#         if gathering.item21_page1:
#             temp_page21.append(gathering.item21_page1)
#         if gathering.item21_page2:
#             temp_page21.append(gathering.item21_page2)
#         if gathering.item21_page3:
#             temp_page21.append(gathering.item21_page3)
#         if gathering.item21_page4:
#             temp_page21.append(gathering.item21_page4)
#         if gathering.item21_page5:
#             temp_page21.append(gathering.item21_page5)
#         if gathering.item21_page6:
#             temp_page21.append(gathering.item21_page6)
#         if gathering.item21_page7:
#             temp_page21.append(gathering.item21_page7)
#         if gathering.item21_page8:
#             temp_page21.append(gathering.item21_page8)
#         if gathering.item21_page9:
#             temp_page21.append(gathering.item21_page9)
#         if gathering.item21_page10:
#             temp_page21.append(gathering.item21_page10)
#         temp_page21=[int(i) for i in temp_page21]
#         temp_page21.sort(reverse=False)
        
    
        
#         if temp_page21:
#             gathering.total_gathering_21=temp_page21[0]
#             gathering.wastage_form_21 = float(gathering.quantity_21) - float(gathering.total_gathering_21)
#         else:
#             gathering.item21_page1=0
#             gathering.item21_page2=0
#             gathering.item21_page3=0
#             gathering.item21_page4=0
#             gathering.item21_page5=0
#             gathering.item21_page6=0
#             gathering.item21_page7=0
#             gathering.item21_page8=0
#             gathering.item21_page9=0
#             gathering.item21_page10=0
        
            

#         # temp_page21=[]
#         # if gathering.item21_page1:
#         #     temp_page21.append(gathering.item21_page1)
#         # if gathering.item21_page2:
#         #     temp_page21.append(gathering.item21_page2)
#         # if gathering.item21_page3:
#         #     temp_page21.append(gathering.item21_page3)
#         # if gathering.item21_page4:
#         #     temp_page21.append(gathering.item21_page4)
#         # if gathering.item21_page5:
#         #     temp_page21.append(gathering.item21_page5)
#         # if gathering.item21_page6:
#         #     temp_page21.append(gathering.item21_page6)
#         # if gathering.item21_page7:
#         #     temp_page21.append(gathering.item21_page7)
#         # if gathering.item21_page8:
#         #     temp_page21.append(gathering.item21_page8)
#         # if gathering.item21_page9:
#         #     temp_page21.append(gathering.item21_page9)
#         # if gathering.item21_page10:
#         #     temp_page21.append(gathering.item21_page10)
#         # temp_page21=[int(i) for i in temp_page21]
#         # temp_page21.sort(reverse=False)
        
    
        
#         # if temp_page21:
#         #     gathering.total_gathering_21=temp_page21[0]
#         #     gathering.wastage_form_21 = float(gathering.quantity_21) - float(gathering.total_gathering_21)
#         # else:
#         #     gathering.item21_page1=0
#         #     gathering.item21_page2=0
#         #     gathering.item21_page3=0
#         #     gathering.item21_page4=0
#         #     gathering.item21_page5=0


#         temp_page22=[]
#         if gathering.item22_page1:
#             temp_page22.append(gathering.item22_page1)
#         if gathering.item22_page2:
#             temp_page22.append(gathering.item22_page2)
#         if gathering.item22_page3:
#             temp_page22.append(gathering.item22_page3)
#         if gathering.item22_page4:
#             temp_page22.append(gathering.item22_page4)
#         if gathering.item22_page5:
#             temp_page22.append(gathering.item22_page5)
#         if gathering.item22_page6:
#             temp_page22.append(gathering.item22_page6)
#         if gathering.item22_page7:
#             temp_page22.append(gathering.item22_page7)
#         if gathering.item22_page8:
#             temp_page22.append(gathering.item22_page8)
#         if gathering.item22_page9:
#             temp_page22.append(gathering.item22_page9)
#         if gathering.item22_page10:
#             temp_page22.append(gathering.item22_page10)
#         temp_page22=[int(i) for i in temp_page22]
#         temp_page22.sort(reverse=False)
        
    
        
#         if temp_page22:
#             gathering.total_gathering_22=temp_page22[0]
#             gathering.wastage_form_22 = float(gathering.quantity_22) - float(gathering.total_gathering_22)
#         else:
#             gathering.item22_page1=0
#             gathering.item22_page2=0
#             gathering.item22_page3=0
#             gathering.item22_page4=0
#             gathering.item22_page5=0
#             gathering.item22_page6=0
#             gathering.item22_page7=0
#             gathering.item22_page8=0
#             gathering.item22_page9=0
#             gathering.item22_page10=0



#         temp_page23=[]
#         if gathering.item23_page1:
#             temp_page23.append(gathering.item23_page1)
#         if gathering.item23_page2:
#             temp_page23.append(gathering.item23_page2)
#         if gathering.item23_page3:
#             temp_page23.append(gathering.item23_page3)
#         if gathering.item23_page4:
#             temp_page23.append(gathering.item23_page4)
#         if gathering.item23_page5:
#             temp_page23.append(gathering.item23_page5)
#         if gathering.item23_page6:
#             temp_page23.append(gathering.item23_page6)
#         if gathering.item23_page7:
#             temp_page23.append(gathering.item23_page7)
#         if gathering.item23_page8:
#             temp_page23.append(gathering.item23_page8)
#         if gathering.item23_page9:
#             temp_page23.append(gathering.item23_page9)
#         if gathering.item23_page10:
#             temp_page23.append(gathering.item23_page10)
#         temp_page23=[int(i) for i in temp_page23]
#         temp_page23.sort(reverse=False)
        
    
        
#         if temp_page23:
#             gathering.total_gathering_23=temp_page23[0]
#             gathering.wastage_form_23 = float(gathering.quantity_23) - float(gathering.total_gathering_23)
#         else:
#             gathering.item23_page1=0
#             gathering.item23_page2=0
#             gathering.item23_page3=0
#             gathering.item23_page4=0
#             gathering.item23_page5=0
#             gathering.item23_page6=0
#             gathering.item23_page7=0
#             gathering.item23_page8=0
#             gathering.item23_page9=0
#             gathering.item23_page10=0


#         temp_page24=[]
#         if gathering.item24_page1:
#             temp_page24.append(gathering.item24_page1)
#         if gathering.item24_page2:
#             temp_page24.append(gathering.item24_page2)
#         if gathering.item24_page3:
#             temp_page24.append(gathering.item24_page3)
#         if gathering.item24_page4:
#             temp_page24.append(gathering.item24_page4)
#         if gathering.item24_page5:
#             temp_page24.append(gathering.item24_page5)
#         if gathering.item24_page6:
#             temp_page24.append(gathering.item24_page6)
#         if gathering.item24_page7:
#             temp_page24.append(gathering.item24_page7)
#         if gathering.item24_page8:
#             temp_page24.append(gathering.item24_page8)
#         if gathering.item24_page9:
#             temp_page24.append(gathering.item24_page9)
#         if gathering.item24_page10:
#             temp_page24.append(gathering.item24_page10)
#         temp_page24=[int(i) for i in temp_page24]
#         temp_page24.sort(reverse=False)
        
    
        
#         if temp_page24:
#             gathering.total_gathering_24=temp_page24[0]
#             gathering.wastage_form_24 = float(gathering.quantity_24) - float(gathering.total_gathering_24)
#         else:
#             gathering.item24_page1=0
#             gathering.item24_page2=0
#             gathering.item24_page3=0
#             gathering.item24_page4=0
#             gathering.item24_page5=0
#             gathering.item24_page6=0
#             gathering.item24_page7=0
#             gathering.item24_page8=0
#             gathering.item24_page9=0
#             gathering.item24_page10=0


#         temp_page25=[]
#         if gathering.item25_page1:
#             temp_page25.append(gathering.item25_page1)
#         if gathering.item25_page2:
#             temp_page25.append(gathering.item25_page2)
#         if gathering.item25_page3:
#             temp_page25.append(gathering.item25_page3)
#         if gathering.item25_page4:
#             temp_page25.append(gathering.item25_page4)
#         if gathering.item25_page5:
#             temp_page25.append(gathering.item25_page5)
#         if gathering.item25_page6:
#             temp_page25.append(gathering.item25_page6)
#         if gathering.item25_page7:
#             temp_page25.append(gathering.item25_page7)
#         if gathering.item25_page8:
#             temp_page25.append(gathering.item25_page8)
#         if gathering.item25_page9:
#             temp_page25.append(gathering.item25_page9)
#         if gathering.item25_page10:
#             temp_page25.append(gathering.item25_page10)
#         temp_page25=[int(i) for i in temp_page25]
#         temp_page25.sort(reverse=False)
        
    
        
#         if temp_page25:
#             gathering.total_gathering_25=temp_page25[0]
#             gathering.wastage_form_25 = float(gathering.quantity_25) - float(gathering.total_gathering_25)
#         else:
#             gathering.item25_page1=0
#             gathering.item25_page2=0
#             gathering.item25_page3=0
#             gathering.item25_page4=0
#             gathering.item25_page5=0
#             gathering.item25_page6=0
#             gathering.item25_page7=0
#             gathering.item25_page8=0
#             gathering.item25_page9=0
#             gathering.item25_page10=0


#         temp_page26=[]
#         if gathering.item26_page1:
#             temp_page26.append(gathering.item26_page1)
#         if gathering.item26_page2:
#             temp_page26.append(gathering.item26_page2)
#         if gathering.item26_page3:
#             temp_page26.append(gathering.item26_page3)
#         if gathering.item26_page4:
#             temp_page26.append(gathering.item26_page4)
#         if gathering.item26_page5:
#             temp_page26.append(gathering.item26_page5)
#         if gathering.item26_page6:
#             temp_page26.append(gathering.item26_page6)
#         if gathering.item26_page7:
#             temp_page26.append(gathering.item26_page7)
#         if gathering.item26_page8:
#             temp_page26.append(gathering.item26_page8)
#         if gathering.item26_page9:
#             temp_page26.append(gathering.item26_page9)
#         if gathering.item26_page10:
#             temp_page26.append(gathering.item26_page10)
#         temp_page26=[int(i) for i in temp_page26]
#         temp_page26.sort(reverse=False)
        
    
        
#         if temp_page26:
#             gathering.total_gathering_26=temp_page26[0]
#             gathering.wastage_form_26 = float(gathering.quantity_26) - float(gathering.total_gathering_26)
#         else:
#             gathering.item26_page1=0
#             gathering.item26_page2=0
#             gathering.item26_page3=0
#             gathering.item26_page4=0
#             gathering.item26_page5=0
#             gathering.item26_page6=0
#             gathering.item26_page7=0
#             gathering.item26_page8=0
#             gathering.item26_page9=0
#             gathering.item26_page10=0



#         temp_page27=[]
#         if gathering.item27_page1:
#             temp_page27.append(gathering.item27_page1)
#         if gathering.item27_page2:
#             temp_page27.append(gathering.item27_page2)
#         if gathering.item27_page3:
#             temp_page27.append(gathering.item27_page3)
#         if gathering.item27_page4:
#             temp_page27.append(gathering.item27_page4)
#         if gathering.item27_page5:
#             temp_page27.append(gathering.item27_page5)
#         if gathering.item27_page6:
#             temp_page27.append(gathering.item27_page6)
#         if gathering.item27_page7:
#             temp_page27.append(gathering.item27_page7)
#         if gathering.item27_page8:
#             temp_page27.append(gathering.item27_page8)
#         if gathering.item27_page9:
#             temp_page27.append(gathering.item27_page9)
#         if gathering.item27_page10:
#             temp_page27.append(gathering.item27_page10)
#         temp_page27=[int(i) for i in temp_page27]
#         temp_page27.sort(reverse=False)
        
    
        
#         if temp_page27:
#             gathering.total_gathering_27=temp_page27[0]
#             gathering.wastage_form_27 = float(gathering.quantity_27) - float(gathering.total_gathering_27)
#         else:
#             gathering.item27_page1=0
#             gathering.item27_page2=0
#             gathering.item27_page3=0
#             gathering.item27_page4=0
#             gathering.item27_page5=0
#             gathering.item27_page6=0
#             gathering.item27_page7=0
#             gathering.item27_page8=0
#             gathering.item27_page9=0
#             gathering.item27_page10=0



#         temp_page28=[]
#         if gathering.item28_page1:
#             temp_page28.append(gathering.item28_page1)
#         if gathering.item28_page2:
#             temp_page28.append(gathering.item28_page2)
#         if gathering.item28_page3:
#             temp_page28.append(gathering.item28_page3)
#         if gathering.item28_page4:
#             temp_page28.append(gathering.item28_page4)
#         if gathering.item28_page5:
#             temp_page28.append(gathering.item28_page5)
#         if gathering.item28_page6:
#             temp_page28.append(gathering.item28_page6)
#         if gathering.item28_page7:
#             temp_page28.append(gathering.item28_page7)
#         if gathering.item28_page8:
#             temp_page28.append(gathering.item28_page8)
#         if gathering.item28_page9:
#             temp_page28.append(gathering.item28_page9)
#         if gathering.item28_page10:
#             temp_page28.append(gathering.item28_page10)
#         temp_page28=[int(i) for i in temp_page28]
#         temp_page28.sort(reverse=False)
        
    
        
#         if temp_page28:
#             gathering.total_gathering_28=temp_page28[0]
#             gathering.wastage_form_28 = float(gathering.quantity_28) - float(gathering.total_gathering_28)
#         else:
#             gathering.item28_page1=0
#             gathering.item28_page2=0
#             gathering.item28_page3=0
#             gathering.item28_page4=0
#             gathering.item28_page5=0
#             gathering.item28_page6=0
#             gathering.item28_page7=0
#             gathering.item28_page8=0
#             gathering.item28_page9=0
#             gathering.item28_page10=0


#         temp_page29=[]
#         if gathering.item29_page1:
#             temp_page29.append(gathering.item29_page1)
#         if gathering.item29_page2:
#             temp_page29.append(gathering.item29_page2)
#         if gathering.item29_page3:
#             temp_page29.append(gathering.item29_page3)
#         if gathering.item29_page4:
#             temp_page29.append(gathering.item29_page4)
#         if gathering.item29_page5:
#             temp_page29.append(gathering.item29_page5)
#         if gathering.item29_page6:
#             temp_page29.append(gathering.item29_page6)
#         if gathering.item29_page7:
#             temp_page29.append(gathering.item29_page7)
#         if gathering.item29_page8:
#             temp_page29.append(gathering.item29_page8)
#         if gathering.item29_page9:
#             temp_page29.append(gathering.item29_page9)
#         if gathering.item29_page10:
#             temp_page29.append(gathering.item29_page10)
#         temp_page29=[int(i) for i in temp_page29]
#         temp_page29.sort(reverse=False)
        
    
        
#         if temp_page29:
#             gathering.total_gathering_29=temp_page29[0]
#             gathering.wastage_form_29 = float(gathering.quantity_29) - float(gathering.total_gathering_29)
#         else:
#             gathering.item29_page1=0
#             gathering.item29_page2=0
#             gathering.item29_page3=0
#             gathering.item29_page4=0
#             gathering.item29_page5=0
#             gathering.item29_page6=0
#             gathering.item29_page7=0
#             gathering.item29_page8=0
#             gathering.item29_page9=0
#             gathering.item29_page10=0



#         temp_page30=[]
#         if gathering.item30_page1:
#             temp_page30.append(gathering.item30_page1)
#         if gathering.item30_page2:
#             temp_page30.append(gathering.item30_page2)
#         if gathering.item30_page3:
#             temp_page30.append(gathering.item30_page3)
#         if gathering.item30_page4:
#             temp_page30.append(gathering.item30_page4)
#         if gathering.item30_page5:
#             temp_page30.append(gathering.item30_page5)
#         if gathering.item30_page6:
#             temp_page30.append(gathering.item30_page6)
#         if gathering.item30_page7:
#             temp_page30.append(gathering.item30_page7)
#         if gathering.item30_page8:
#             temp_page30.append(gathering.item30_page8)
#         if gathering.item30_page9:
#             temp_page30.append(gathering.item30_page9)
#         if gathering.item30_page10:
#             temp_page30.append(gathering.item30_page10)
#         temp_page30=[int(i) for i in temp_page30]
#         temp_page30.sort(reverse=False)
        
        
        
#         if temp_page30:
#             gathering.total_gathering_30=temp_page30[0]
#             gathering.wastage_form_30 = float(gathering.quantity_30) - float(gathering.total_gathering_30)
#         else:
#             gathering.item30_page1=0
#             gathering.item30_page2=0
#             gathering.item30_page3=0
#             gathering.item30_page4=0
#             gathering.item30_page5=0
#             gathering.item30_page6=0
#             gathering.item30_page7=0
#             gathering.item30_page8=0
#             gathering.item30_page9=0
#             gathering.item30_page10=0



#         temp_page31=[]
#         if gathering.item31_page1:
#             temp_page31.append(gathering.item31_page1)
#         if gathering.item31_page2:
#             temp_page31.append(gathering.item31_page2)
#         if gathering.item31_page3:
#             temp_page31.append(gathering.item31_page3)
#         if gathering.item31_page4:
#             temp_page31.append(gathering.item31_page4)
#         if gathering.item31_page5:
#             temp_page31.append(gathering.item31_page5)
#         if gathering.item31_page6:
#             temp_page31.append(gathering.item31_page6)
#         if gathering.item31_page7:
#             temp_page31.append(gathering.item31_page7)
#         if gathering.item31_page8:
#             temp_page31.append(gathering.item31_page8)
#         if gathering.item31_page9:
#             temp_page31.append(gathering.item31_page9)
#         if gathering.item31_page10:
#             temp_page31.append(gathering.item31_page10)
#         temp_page31=[int(i) for i in temp_page31]
#         temp_page31.sort(reverse=False)
        
        
        
#         if temp_page31:
#             gathering.total_gathering_31=temp_page31[0]
#             gathering.wastage_form_31 = float(gathering.quantity_31) - float(gathering.total_gathering_31)
#         else:
#             gathering.item31_page1=0
#             gathering.item31_page2=0
#             gathering.item31_page3=0
#             gathering.item31_page4=0
#             gathering.item31_page5=0
#             gathering.item31_page6=0
#             gathering.item31_page7=0
#             gathering.item31_page8=0
#             gathering.item31_page9=0
#             gathering.item31_page10=0


#         temp_page32=[]
#         if gathering.item3_page1:
#             temp_page32.append(gathering.item32_page1)
#         if gathering.item3_page2:
#             temp_page32.append(gathering.item32_page2)
#         if gathering.item3_page3:
#             temp_page32.append(gathering.item32_page3)
#         if gathering.item3_page4:
#             temp_page32.append(gathering.item32_page4)
#         if gathering.item3_page5:
#             temp_page32.append(gathering.item32_page5)
#         if gathering.item3_page6:
#             temp_page32.append(gathering.item32_page6)
#         if gathering.item3_page7:
#             temp_page32.append(gathering.item32_page7)
#         if gathering.item3_page8:
#             temp_page32.append(gathering.item32_page8)
#         if gathering.item3_page9:
#             temp_page32.append(gathering.item32_page9)
#         if gathering.item3_page10:
#             temp_page32.append(gathering.item32_page10)
#         temp_page32=[int(i) for i in temp_page32]
#         temp_page32.sort(reverse=False)
        
        
        
#         if temp_page32:
#             gathering.total_gathering_32=temp_page32[0]
#             gathering.wastage_form_32 = float(gathering.quantity_32) - float(gathering.total_gathering_32)
#         else:
#             gathering.item32_page1=0
#             gathering.item32_page2=0
#             gathering.item32_page3=0
#             gathering.item32_page4=0
#             gathering.item32_page5=0
#             gathering.item32_page6=0
#             gathering.item32_page7=0
#             gathering.item32_page8=0
#             gathering.item32_page9=0
#             gathering.item32_page10=0



#         temp_page33=[]
#         if gathering.item33_page1:
#             temp_page33.append(gathering.item33_page1)
#         if gathering.item33_page2:
#             temp_page33.append(gathering.item33_page2)
#         if gathering.item33_page3:
#             temp_page33.append(gathering.item33_page3)
#         if gathering.item33_page4:
#             temp_page33.append(gathering.item33_page4)
#         if gathering.item33_page5:
#             temp_page33.append(gathering.item33_page5)
#         if gathering.item33_page6:
#             temp_page33.append(gathering.item33_page6)
#         if gathering.item33_page7:
#             temp_page33.append(gathering.item33_page7)
#         if gathering.item33_page8:
#             temp_page33.append(gathering.item33_page8)
#         if gathering.item33_page9:
#             temp_page33.append(gathering.item33_page9)
#         if gathering.item33_page10:
#             temp_page33.append(gathering.item33_page10)
#         temp_page33=[int(i) for i in temp_page33]
#         temp_page33.sort(reverse=False)
        
        
        
#         if temp_page33:
#             gathering.total_gathering_33=temp_page33[0]
#             gathering.wastage_form_33 = float(gathering.quantity_33) - float(gathering.total_gathering_33)
#         else:
#             gathering.item33_page1=0
#             gathering.item33_page2=0
#             gathering.item33_page3=0
#             gathering.item33_page4=0
#             gathering.item33_page5=0
#             gathering.item33_page6=0
#             gathering.item33_page7=0
#             gathering.item33_page8=0
#             gathering.item33_page9=0
#             gathering.item33_page10=0


#         temp_page34=[]
#         if gathering.item34_page1:
#             temp_page34.append(gathering.item34_page1)
#         if gathering.item34_page2:
#             temp_page34.append(gathering.item34_page2)
#         if gathering.item34_page3:
#             temp_page34.append(gathering.item34_page3)
#         if gathering.item34_page4:
#             temp_page34.append(gathering.item34_page4)
#         if gathering.item34_page5:
#             temp_page34.append(gathering.item34_page5)
#         if gathering.item34_page6:
#             temp_page34.append(gathering.item34_page6)
#         if gathering.item34_page7:
#             temp_page34.append(gathering.item34_page7)
#         if gathering.item34_page8:
#             temp_page34.append(gathering.item34_page8)
#         if gathering.item34_page9:
#             temp_page34.append(gathering.item34_page9)
#         if gathering.item34_page10:
#             temp_page34.append(gathering.item34_page10)
#         temp_page34=[int(i) for i in temp_page34]
#         temp_page34.sort(reverse=False)
        
        
        
#         if temp_page34:
#             gathering.total_gathering_34=temp_page34[0]
#             gathering.wastage_form_34 = float(gathering.quantity_34) - float(gathering.total_gathering_34)
#         else:
#             gathering.item34_page1=0
#             gathering.item34_page2=0
#             gathering.item34_page3=0
#             gathering.item34_page4=0
#             gathering.item34_page5=0
#             gathering.item34_page6=0
#             gathering.item34_page7=0
#             gathering.item34_page8=0
#             gathering.item34_page9=0
#             gathering.item34_page10=0



#         temp_page35=[]
#         if gathering.item35_page1:
#             temp_page35.append(gathering.item35_page1)
#         if gathering.item35_page2:
#             temp_page35.append(gathering.item35_page2)
#         if gathering.item35_page3:
#             temp_page35.append(gathering.item35_page3)
#         if gathering.item35_page4:
#             temp_page35.append(gathering.item35_page4)
#         if gathering.item35_page5:
#             temp_page35.append(gathering.item35_page5)
#         if gathering.item35_page6:
#             temp_page35.append(gathering.item35_page6)
#         if gathering.item35_page7:
#             temp_page35.append(gathering.item35_page7)
#         if gathering.item35_page8:
#             temp_page35.append(gathering.item35_page8)
#         if gathering.item35_page9:
#             temp_page35.append(gathering.item35_page9)
#         if gathering.item35_page10:
#             temp_page35.append(gathering.item35_page10)
#         temp_page35=[int(i) for i in temp_page35]
#         temp_page35.sort(reverse=False)
        
        
        
#         if temp_page35:
#             gathering.total_gathering_35=temp_page35[0]
#             gathering.wastage_form_35 = float(gathering.quantity_35) - float(gathering.total_gathering_35)
#         else:
#             gathering.item35_page1=0
#             gathering.item35_page2=0
#             gathering.item35_page3=0
#             gathering.item35_page4=0
#             gathering.item35_page5=0
#             gathering.item35_page6=0
#             gathering.item35_page7=0
#             gathering.item35_page8=0
#             gathering.item35_page9=0
#             gathering.item35_page10=0



#         temp_page36=[]
#         if gathering.item36_page1:
#             temp_page36.append(gathering.item36_page1)
#         if gathering.item36_page2:
#             temp_page36.append(gathering.item36_page2)
#         if gathering.item36_page3:
#             temp_page36.append(gathering.item36_page3)
#         if gathering.item36_page4:
#             temp_page36.append(gathering.item36_page4)
#         if gathering.item36_page5:
#             temp_page36.append(gathering.item36_page5)
#         if gathering.item36_page6:
#             temp_page36.append(gathering.item36_page6)
#         if gathering.item36_page7:
#             temp_page36.append(gathering.item36_page7)
#         if gathering.item36_page8:
#             temp_page36.append(gathering.item36_page8)
#         if gathering.item36_page9:
#             temp_page36.append(gathering.item36_page9)
#         if gathering.item36_page10:
#             temp_page36.append(gathering.item36_page10)
#         temp_page36=[int(i) for i in temp_page36]
#         temp_page36.sort(reverse=False)
        
        
        
#         if temp_page36:
#             gathering.total_gathering_36=temp_page36[0]
#             gathering.wastage_form_36 = float(gathering.quantity_36) - float(gathering.total_gathering_36)
#         else:
#             gathering.item36_page1=0
#             gathering.item36_page2=0
#             gathering.item36_page3=0
#             gathering.item36_page4=0
#             gathering.item36_page5=0
#             gathering.item36_page6=0
#             gathering.item36_page7=0
#             gathering.item36_page8=0
#             gathering.item36_page9=0
#             gathering.item36_page10=0



#         temp_page37=[]
#         if gathering.item37_page1:
#             temp_page37.append(gathering.item37_page1)
#         if gathering.item37_page2:
#             temp_page37.append(gathering.item37_page2)
#         if gathering.item37_page3:
#             temp_page37.append(gathering.item37_page3)
#         if gathering.item37_page4:
#             temp_page37.append(gathering.item37_page4)
#         if gathering.item37_page5:
#             temp_page37.append(gathering.item37_page5)
#         if gathering.item37_page6:
#             temp_page37.append(gathering.item37_page6)
#         if gathering.item37_page7:
#             temp_page37.append(gathering.item37_page7)
#         if gathering.item37_page8:
#             temp_page37.append(gathering.item37_page8)
#         if gathering.item37_page9:
#             temp_page37.append(gathering.item37_page9)
#         if gathering.item37_page10:
#             temp_page37.append(gathering.item37_page10)
#         temp_page37=[int(i) for i in temp_page37]
#         temp_page37.sort(reverse=False)
        
        
        
#         if temp_page37:
#             gathering.total_gathering_37=temp_page37[0]
#             gathering.wastage_form_37 = float(gathering.quantity_37) - float(gathering.total_gathering_37)
#         else:
#             gathering.item37_page1=0
#             gathering.item37_page2=0
#             gathering.item37_page3=0
#             gathering.item37_page4=0
#             gathering.item37_page5=0
#             gathering.item37_page6=0
#             gathering.item37_page7=0
#             gathering.item37_page8=0
#             gathering.item37_page9=0
#             gathering.item37_page10=0



#         temp_page38=[]
#         if gathering.item38_page1:
#             temp_page38.append(gathering.item38_page1)
#         if gathering.item38_page2:
#             temp_page38.append(gathering.item38_page2)
#         if gathering.item38_page3:
#             temp_page38.append(gathering.item38_page3)
#         if gathering.item38_page4:
#             temp_page38.append(gathering.item38_page4)
#         if gathering.item38_page5:
#             temp_page38.append(gathering.item38_page5)
#         if gathering.item38_page6:
#             temp_page38.append(gathering.item38_page6)
#         if gathering.item38_page7:
#             temp_page38.append(gathering.item38_page7)
#         if gathering.item38_page8:
#             temp_page38.append(gathering.item38_page8)
#         if gathering.item38_page9:
#             temp_page38.append(gathering.item38_page9)
#         if gathering.item38_page10:
#             temp_page38.append(gathering.item38_page10)
#         temp_page38=[int(i) for i in temp_page38]
#         temp_page38.sort(reverse=False)
        
        
        
#         if temp_page38:
#             gathering.total_gathering_38=temp_page38[0]
#             gathering.wastage_form_38 = float(gathering.quantity_38) - float(gathering.total_gathering_38)
#         else:
#             gathering.item38_page1=0
#             gathering.item38_page2=0
#             gathering.item38_page3=0
#             gathering.item38_page4=0
#             gathering.item38_page5=0
#             gathering.item38_page6=0
#             gathering.item38_page7=0
#             gathering.item38_page8=0
#             gathering.item38_page9=0
#             gathering.item38_page10=0



#         temp_page39=[]
#         if gathering.item39_page1:
#             temp_page39.append(gathering.item39_page1)
#         if gathering.item39_page2:
#             temp_page39.append(gathering.item39_page2)
#         if gathering.item39_page3:
#             temp_page39.append(gathering.item39_page3)
#         if gathering.item39_page4:
#             temp_page39.append(gathering.item39_page4)
#         if gathering.item39_page5:
#             temp_page39.append(gathering.item39_page5)
#         if gathering.item39_page6:
#             temp_page39.append(gathering.item39_page6)
#         if gathering.item39_page7:
#             temp_page39.append(gathering.item39_page7)
#         if gathering.item39_page8:
#             temp_page39.append(gathering.item39_page8)
#         if gathering.item39_page9:
#             temp_page39.append(gathering.item39_page9)
#         if gathering.item39_page10:
#             temp_page39.append(gathering.item39_page10)
#         temp_page39=[int(i) for i in temp_page39]
#         temp_page39.sort(reverse=False)
        
        
        
#         if temp_page39:
#             gathering.total_gathering_39=temp_page39[0]
#             gathering.wastage_form_39 = float(gathering.quantity_39) - float(gathering.total_gathering_39)
#         else:
#             gathering.item39_page1=0
#             gathering.item39_page2=0
#             gathering.item39_page3=0
#             gathering.item39_page4=0
#             gathering.item39_page5=0
#             gathering.item39_page6=0
#             gathering.item39_page7=0
#             gathering.item39_page8=0
#             gathering.item39_page9=0
#             gathering.item39_page10=0



#         temp_page40=[]
#         if gathering.item40_page1:
#             temp_page40.append(gathering.item40_page1)
#         if gathering.item40_page2:
#             temp_page40.append(gathering.item40_page2)
#         if gathering.item40_page3:
#             temp_page40.append(gathering.item40_page3)
#         if gathering.item40_page4:
#             temp_page40.append(gathering.item40_page4)
#         if gathering.item40_page5:
#             temp_page40.append(gathering.item40_page5)
#         if gathering.item40_page6:
#             temp_page40.append(gathering.item40_page6)
#         if gathering.item40_page7:
#             temp_page40.append(gathering.item40_page7)
#         if gathering.item40_page8:
#             temp_page40.append(gathering.item40_page8)
#         if gathering.item40_page9:
#             temp_page40.append(gathering.item40_page9)
#         if gathering.item40_page10:
#             temp_page40.append(gathering.item40_page10)
#         temp_page40=[int(i) for i in temp_page40]
#         temp_page40.sort(reverse=False)
        
        
        
#         if temp_page40:
#             gathering.total_gathering_40=temp_page40[0]
#             gathering.wastage_form_40 = float(gathering.quantity_40) - float(gathering.total_gathering_40)
#         else:
#             gathering.item40_page1=0
#             gathering.item40_page2=0
#             gathering.item40_page3=0
#             gathering.item40_page4=0
#             gathering.item40_page5=0
#             gathering.item40_page6=0
#             gathering.item40_page7=0
#             gathering.item40_page8=0
#             gathering.item40_page9=0
#             gathering.item40_page10=0


#         temp_page41=[]
#         if gathering.item41_page1:
#             temp_page41.append(gathering.item41_page1)
#         if gathering.item41_page2:
#             temp_page41.append(gathering.item41_page2)
#         if gathering.item41_page3:
#             temp_page41.append(gathering.item41_page3)
#         if gathering.item41_page4:
#             temp_page41.append(gathering.item41_page4)
#         if gathering.item41_page5:
#             temp_page41.append(gathering.item41_page5)
#         if gathering.item41_page6:
#             temp_page41.append(gathering.item41_page6)
#         if gathering.item41_page7:
#             temp_page41.append(gathering.item41_page7)
#         if gathering.item41_page8:
#             temp_page41.append(gathering.item41_page8)
#         if gathering.item41_page9:
#             temp_page41.append(gathering.item41_page9)
#         if gathering.item41_page10:
#             temp_page41.append(gathering.item41_page10)
#         temp_page41=[int(i) for i in temp_page41]
#         temp_page41.sort(reverse=False)
    
    
        
#         if temp_page41:
#             gathering.total_gathering_41=temp_page41[0]
#             gathering.wastage_form_41 = float(gathering.quantity_41) - float(gathering.total_gathering_41)
#         else:
#             gathering.item41_page1=0
#             gathering.item41_page2=0
#             gathering.item41_page3=0
#             gathering.item41_page4=0
#             gathering.item41_page5=0
#             gathering.item41_page6=0
#             gathering.item41_page7=0
#             gathering.item41_page8=0
#             gathering.item41_page9=0
#             gathering.item41_page10=0



#         temp_page42=[]
#         if gathering.item42_page1:
#             temp_page42.append(gathering.item42_page1)
#         if gathering.item42_page2:
#             temp_page42.append(gathering.item42_page2)
#         if gathering.item42_page3:
#             temp_page42.append(gathering.item42_page3)
#         if gathering.item42_page4:
#             temp_page42.append(gathering.item42_page4)
#         if gathering.item42_page5:
#             temp_page42.append(gathering.item42_page5)
#         if gathering.item42_page6:
#             temp_page42.append(gathering.item42_page6)
#         if gathering.item42_page7:
#             temp_page42.append(gathering.item42_page7)
#         if gathering.item42_page8:
#             temp_page42.append(gathering.item42_page8)
#         if gathering.item42_page9:
#             temp_page42.append(gathering.item42_page9)
#         if gathering.item42_page10:
#             temp_page42.append(gathering.item42_page10)
#         temp_page42=[int(i) for i in temp_page42]
#         temp_page42.sort(reverse=False)
    
    
        
#         if temp_page42:
#             gathering.total_gathering_42=temp_page42[0]
#             gathering.wastage_form_42 = float(gathering.quantity_42) - float(gathering.total_gathering_42)
#         else:
#             gathering.item42_page1=0
#             gathering.item42_page2=0
#             gathering.item42_page3=0
#             gathering.item42_page4=0
#             gathering.item42_page5=0
#             gathering.item42_page6=0
#             gathering.item42_page7=0
#             gathering.item42_page8=0
#             gathering.item42_page9=0
#             gathering.item42_page10=0



#         temp_page43=[]
#         if gathering.item43_page1:
#             temp_page43.append(gathering.item43_page1)
#         if gathering.item43_page2:
#             temp_page43.append(gathering.item43_page2)
#         if gathering.item43_page3:
#             temp_page43.append(gathering.item43_page3)
#         if gathering.item43_page4:
#             temp_page43.append(gathering.item43_page4)
#         if gathering.item43_page5:
#             temp_page43.append(gathering.item43_page5)
#         if gathering.item43_page6:
#             temp_page43.append(gathering.item43_page6)
#         if gathering.item43_page7:
#             temp_page43.append(gathering.item43_page7)
#         if gathering.item43_page8:
#             temp_page43.append(gathering.item43_page8)
#         if gathering.item43_page9:
#             temp_page43.append(gathering.item43_page9)
#         if gathering.item43_page10:
#             temp_page43.append(gathering.item43_page10)
#         temp_page43=[int(i) for i in temp_page43]
#         temp_page43.sort(reverse=False)
    
    
        
#         if temp_page43:
#             gathering.total_gathering_43=temp_page43[0]
#             gathering.wastage_form_43 = float(gathering.quantity_43) - float(gathering.total_gathering_43)
#         else:
#             gathering.item43_page1=0
#             gathering.item43_page2=0
#             gathering.item43_page3=0
#             gathering.item43_page4=0
#             gathering.item43_page5=0
#             gathering.item43_page6=0
#             gathering.item43_page7=0
#             gathering.item43_page8=0
#             gathering.item43_page9=0
#             gathering.item43_page10=0



#         temp_page44=[]
#         if gathering.item44_page1:
#             temp_page44.append(gathering.item44_page1)
#         if gathering.item44_page2:
#             temp_page44.append(gathering.item44_page2)
#         if gathering.item44_page3:
#             temp_page44.append(gathering.item44_page3)
#         if gathering.item44_page4:
#             temp_page44.append(gathering.item44_page4)
#         if gathering.item44_page5:
#             temp_page44.append(gathering.item44_page5)
#         if gathering.item44_page6:
#             temp_page44.append(gathering.item44_page6)
#         if gathering.item44_page7:
#             temp_page44.append(gathering.item44_page7)
#         if gathering.item44_page8:
#             temp_page44.append(gathering.item44_page8)
#         if gathering.item44_page9:
#             temp_page44.append(gathering.item44_page9)
#         if gathering.item44_page10:
#             temp_page44.append(gathering.item44_page10)
#         temp_page44=[int(i) for i in temp_page44]
#         temp_page44.sort(reverse=False)
    
    
        
#         if temp_page44:
#             gathering.total_gathering_44=temp_page44[0]
#             gathering.wastage_form_44 = float(gathering.quantity_44) - float(gathering.total_gathering_44)
#         else:
#             gathering.item44_page1=0
#             gathering.item44_page2=0
#             gathering.item44_page3=0
#             gathering.item44_page4=0
#             gathering.item44_page5=0
#             gathering.item44_page6=0
#             gathering.item44_page7=0
#             gathering.item44_page8=0
#             gathering.item44_page9=0
#             gathering.item44_page10=0



#         temp_page45=[]
#         if gathering.item45_page1:
#             temp_page45.append(gathering.item45_page1)
#         if gathering.item45_page2:
#             temp_page45.append(gathering.item45_page2)
#         if gathering.item45_page3:
#             temp_page45.append(gathering.item45_page3)
#         if gathering.item45_page4:
#             temp_page45.append(gathering.item45_page4)
#         if gathering.item45_page5:
#             temp_page45.append(gathering.item45_page5)
#         if gathering.item45_page6:
#             temp_page45.append(gathering.item45_page6)
#         if gathering.item45_page7:
#             temp_page45.append(gathering.item45_page7)
#         if gathering.item45_page8:
#             temp_page45.append(gathering.item45_page8)
#         if gathering.item45_page9:
#             temp_page45.append(gathering.item45_page9)
#         if gathering.item45_page10:
#             temp_page45.append(gathering.item45_page10)
#         temp_page45=[int(i) for i in temp_page45]
#         temp_page45.sort(reverse=False)
    
    
        
#         if temp_page45:
#             gathering.total_gathering_45=temp_page45[0]
#             gathering.wastage_form_45 = float(gathering.quantity_45) - float(gathering.total_gathering_45)
#         else:
#             gathering.item45_page1=0
#             gathering.item45_page2=0
#             gathering.item45_page3=0
#             gathering.item45_page4=0
#             gathering.item45_page5=0
#             gathering.item45_page6=0
#             gathering.item45_page7=0
#             gathering.item45_page8=0
#             gathering.item45_page9=0
#             gathering.item45_page10=0



#         temp_page46=[]
#         if gathering.item46_page1:
#             temp_page46.append(gathering.item46_page1)
#         if gathering.item46_page2:
#             temp_page46.append(gathering.item46_page2)
#         if gathering.item46_page3:
#             temp_page46.append(gathering.item46_page3)
#         if gathering.item46_page4:
#             temp_page46.append(gathering.item46_page4)
#         if gathering.item46_page5:
#             temp_page46.append(gathering.item46_page5)
#         if gathering.item46_page6:
#             temp_page46.append(gathering.item46_page6)
#         if gathering.item46_page7:
#             temp_page46.append(gathering.item46_page7)
#         if gathering.item46_page8:
#             temp_page46.append(gathering.item46_page8)
#         if gathering.item46_page9:
#             temp_page46.append(gathering.item46_page9)
#         if gathering.item46_page10:
#             temp_page46.append(gathering.item46_page10)
#         temp_page46=[int(i) for i in temp_page46]
#         temp_page46.sort(reverse=False)
    
    
        
#         if temp_page46:
#             gathering.total_gathering_46=temp_page46[0]
#             gathering.wastage_form_46 = float(gathering.quantity_46) - float(gathering.total_gathering_46)
#         else:
#             gathering.item46_page1=0
#             gathering.item46_page2=0
#             gathering.item46_page3=0
#             gathering.item46_page4=0
#             gathering.item46_page5=0
#             gathering.item46_page6=0
#             gathering.item46_page7=0
#             gathering.item46_page8=0
#             gathering.item46_page9=0
#             gathering.item46_page10=0


#         temp_page47=[]
#         if gathering.item47_page1:
#             temp_page47.append(gathering.item47_page1)
#         if gathering.item47_page2:
#             temp_page47.append(gathering.item47_page2)
#         if gathering.item47_page3:
#             temp_page47.append(gathering.item47_page3)
#         if gathering.item47_page4:
#             temp_page47.append(gathering.item47_page4)
#         if gathering.item47_page5:
#             temp_page47.append(gathering.item47_page5)
#         if gathering.item47_page6:
#             temp_page47.append(gathering.item47_page6)
#         if gathering.item47_page7:
#             temp_page47.append(gathering.item47_page7)
#         if gathering.item47_page8:
#             temp_page47.append(gathering.item47_page8)
#         if gathering.item47_page9:
#             temp_page47.append(gathering.item47_page9)
#         if gathering.item47_page10:
#             temp_page47.append(gathering.item47_page10)
#         temp_page47=[int(i) for i in temp_page47]
#         temp_page47.sort(reverse=False)
    
    
        
#         if temp_page47:
#             gathering.total_gathering_47=temp_page47[0]
#             gathering.wastage_form_47 = float(gathering.quantity_47) - float(gathering.total_gathering_47)
#         else:
#             gathering.item47_page1=0
#             gathering.item47_page2=0
#             gathering.item47_page3=0
#             gathering.item47_page4=0
#             gathering.item47_page5=0
#             gathering.item47_page6=0
#             gathering.item47_page7=0
#             gathering.item47_page8=0
#             gathering.item47_page9=0
#             gathering.item47_page10=0


#         temp_page48=[]
#         if gathering.item48_page1:
#             temp_page48.append(gathering.item48_page1)
#         if gathering.item48_page2:
#             temp_page48.append(gathering.item48_page2)
#         if gathering.item48_page3:
#             temp_page48.append(gathering.item48_page3)
#         if gathering.item48_page4:
#             temp_page48.append(gathering.item48_page4)
#         if gathering.item48_page5:
#             temp_page48.append(gathering.item48_page5)
#         if gathering.item48_page6:
#             temp_page48.append(gathering.item48_page6)
#         if gathering.item48_page7:
#             temp_page48.append(gathering.item48_page7)
#         if gathering.item48_page8:
#             temp_page48.append(gathering.item48_page8)
#         if gathering.item48_page9:
#             temp_page48.append(gathering.item48_page9)
#         if gathering.item48_page10:
#             temp_page48.append(gathering.item48_page10)
#         temp_page48=[int(i) for i in temp_page48]
#         temp_page48.sort(reverse=False)
    
    
        
#         if temp_page48:
#             gathering.total_gathering_48=temp_page48[0]
#             gathering.wastage_form_48 = float(gathering.quantity_48) - float(gathering.total_gathering_48)
#         else:
#             gathering.item48_page1=0
#             gathering.item48_page2=0
#             gathering.item48_page3=0
#             gathering.item48_page4=0
#             gathering.item48_page5=0
#             gathering.item48_page6=0
#             gathering.item48_page7=0
#             gathering.item48_page8=0
#             gathering.item48_page9=0
#             gathering.item48_page10=0

        
            
#         temp_page49=[]
#         if gathering.item49_page1:
#             temp_page49.append(gathering.item49_page1)
#         if gathering.item49_page2:
#             temp_page49.append(gathering.item49_page2)
#         if gathering.item49_page3:
#             temp_page49.append(gathering.item49_page3)
#         if gathering.item49_page4:
#             temp_page49.append(gathering.item49_page4)
#         if gathering.item49_page5:
#             temp_page49.append(gathering.item49_page5)
#         if gathering.item49_page6:
#             temp_page49.append(gathering.item49_page6)
#         if gathering.item49_page7:
#             temp_page49.append(gathering.item49_page7)
#         if gathering.item49_page8:
#             temp_page49.append(gathering.item49_page8)
#         if gathering.item49_page9:
#             temp_page49.append(gathering.item49_page9)
#         if gathering.item49_page10:
#             temp_page49.append(gathering.item49_page10)
#         temp_page49=[int(i) for i in temp_page49]
#         temp_page49.sort(reverse=False)
    
    
        
#         if temp_page49:
#             gathering.total_gathering_49=temp_page49[0]
#             gathering.wastage_form_49 = float(gathering.quantity_49) - float(gathering.total_gathering_49)
#         else:
#             gathering.item49_page1=0
#             gathering.item49_page2=0
#             gathering.item49_page3=0
#             gathering.item49_page4=0
#             gathering.item49_page5=0
#             gathering.item49_page6=0
#             gathering.item49_page7=0
#             gathering.item49_page8=0
#             gathering.item49_page9=0
#             gathering.item49_page10=0



#         temp_page50=[]
#         if gathering.item50_page1:
#             temp_page50.append(gathering.item50_page1)
#         if gathering.item50_page2:
#             temp_page50.append(gathering.item50_page2)
#         if gathering.item50_page3:
#             temp_page50.append(gathering.item50_page3)
#         if gathering.item50_page4:
#             temp_page50.append(gathering.item50_page4)
#         if gathering.item50_page5:
#             temp_page50.append(gathering.item50_page5)
#         if gathering.item50_page6:
#             temp_page50.append(gathering.item50_page6)
#         if gathering.item50_page7:
#             temp_page50.append(gathering.item50_page7)
#         if gathering.item50_page8:
#             temp_page50.append(gathering.item50_page8)
#         if gathering.item50_page9:
#             temp_page50.append(gathering.item50_page9)
#         if gathering.item50_page10:
#             temp_page50.append(gathering.item50_page10)
#         temp_page50=[int(i) for i in temp_page50]
#         temp_page50.sort(reverse=False)
    
    
        
#         if temp_page50:
#             gathering.total_gathering_50=temp_page50[0]
#             gathering.wastage_form_50 = float(gathering.quantity_50) - float(gathering.total_gathering_50)
#         else:
#             gathering.item50_page1=0
#             gathering.item50_page2=0
#             gathering.item50_page3=0
#             gathering.item50_page4=0
#             gathering.item50_page5=0
#             gathering.item50_page6=0
#             gathering.item50_page7=0
#             gathering.item50_page8=0
#             gathering.item50_page9=0
#             gathering.item50_page10=0




        
        
        
#         temp_gather=[]
#         if gathering.total_gathering_1:
#             temp_gather.append(int(gathering.total_gathering_1))
#         if gathering.total_gathering_2:
#             temp_gather.append(int(gathering.total_gathering_2))
#         if gathering.total_gathering_3:
#             temp_gather.append(int(gathering.total_gathering_3))
#         if gathering.total_gathering_4:
#             temp_gather.append(int(gathering.total_gathering_4))
#         if gathering.total_gathering_5:
#             temp_gather.append(int(gathering.total_gathering_5))
#         if gathering.total_gathering_6:
#             temp_gather.append(int(gathering.total_gathering_6))
#         if gathering.total_gathering_7:
#             temp_gather.append(int(gathering.total_gathering_7))
#         if gathering.total_gathering_8:
#             temp_gather.append(int(gathering.total_gathering_8))
#         if gathering.total_gathering_9:
#             temp_gather.append(int(gathering.total_gathering_9))
#         if gathering.total_gathering_10:
#             temp_gather.append(int(gathering.total_gathering_10))
        
#         if gathering.total_gathering_11:
#             temp_gather.append(int(gathering.total_gathering_11))
#         if gathering.total_gathering_12:
#             temp_gather.append(int(gathering.total_gathering_12))
#         if gathering.total_gathering_13:
#             temp_gather.append(int(gathering.total_gathering_13))
#         if gathering.total_gathering_14:
#             temp_gather.append(int(gathering.total_gathering_14))
#         if gathering.total_gathering_15:
#             temp_gather.append(int(gathering.total_gathering_15))
#         if gathering.total_gathering_16:
#             temp_gather.append(int(gathering.total_gathering_16))
#         if gathering.total_gathering_17:
#             temp_gather.append(int(gathering.total_gathering_17))
#         if gathering.total_gathering_18:
#             temp_gather.append(int(gathering.total_gathering_18))
#         if gathering.total_gathering_19:
#             temp_gather.append(int(gathering.total_gathering_19))
#         if gathering.total_gathering_20:
#             temp_gather.append(int(gathering.total_gathering_20))
        
#         if gathering.total_gathering_21:
#             temp_gather.append(int(gathering.total_gathering_21))
#         if gathering.total_gathering_22:
#             temp_gather.append(int(gathering.total_gathering_22))
#         if gathering.total_gathering_23:
#             temp_gather.append(int(gathering.total_gathering_23))
#         if gathering.total_gathering_24:
#             temp_gather.append(int(gathering.total_gathering_24))
#         if gathering.total_gathering_25:
#             temp_gather.append(int(gathering.total_gathering_25))
#         if gathering.total_gathering_26:
#             temp_gather.append(int(gathering.total_gathering_26))
#         if gathering.total_gathering_27:
#             temp_gather.append(int(gathering.total_gathering_27))
#         if gathering.total_gathering_28:
#             temp_gather.append(int(gathering.total_gathering_28))
#         if gathering.total_gathering_29:
#             temp_gather.append(int(gathering.total_gathering_29))
#         if gathering.total_gathering_30:
#             temp_gather.append(int(gathering.total_gathering_30))

#         if gathering.total_gathering_31:
#             temp_gather.append(int(gathering.total_gathering_31))
#         if gathering.total_gathering_32:
#             temp_gather.append(int(gathering.total_gathering_32))
#         if gathering.total_gathering_33:
#             temp_gather.append(int(gathering.total_gathering_33))
#         if gathering.total_gathering_34:
#             temp_gather.append(int(gathering.total_gathering_34))
#         if gathering.total_gathering_35:
#             temp_gather.append(int(gathering.total_gathering_35))
#         if gathering.total_gathering_36:
#             temp_gather.append(int(gathering.total_gathering_36))
#         if gathering.total_gathering_37:
#             temp_gather.append(int(gathering.total_gathering_37))
#         if gathering.total_gathering_38:
#             temp_gather.append(int(gathering.total_gathering_38))
#         if gathering.total_gathering_39:
#             temp_gather.append(int(gathering.total_gathering_39))
#         if gathering.total_gathering_40:
#             temp_gather.append(int(gathering.total_gathering_40))

#         if gathering.total_gathering_41:
#             temp_gather.append(int(gathering.total_gathering_41))
#         if gathering.total_gathering_42:
#             temp_gather.append(int(gathering.total_gathering_42))
#         if gathering.total_gathering_43:
#             temp_gather.append(int(gathering.total_gathering_43))
#         if gathering.total_gathering_44:
#             temp_gather.append(int(gathering.total_gathering_44))
#         if gathering.total_gathering_45:
#             temp_gather.append(int(gathering.total_gathering_45))
#         if gathering.total_gathering_46:
#             temp_gather.append(int(gathering.total_gathering_46))
#         if gathering.total_gathering_47:
#             temp_gather.append(int(gathering.total_gathering_47))
#         if gathering.total_gathering_48:
#             temp_gather.append(int(gathering.total_gathering_48))
#         if gathering.total_gathering_49:
#             temp_gather.append(int(gathering.total_gathering_49))
#         if gathering.total_gathering_50:
#             temp_gather.append(int(gathering.total_gathering_50))

#         temp_gather=[i for i in temp_gather]
#         gathering.total_gathering=0
#         for i in temp_gather:
#             gathering.total_gathering=gathering.total_gathering+float(i)
#         if gathering.total_gathering:
#             gathering.wastage_form = float(gathering.total_quantity) - float(gathering.total_gathering)
#             gathering.total_gathering= float(gathering.total_quantity)-gathering.wastage_form
        
#         gathering.save()
        
#         messages.success(request, "Updated Successfully...!!")
#         return redirect('/gathering-info/') 
    
       
#     context = {
#         'gathering':gathering,
#     }
#     return render(request, 'processing/view-gathering.html', context)




















# new view 


from django.shortcuts import render
from multiprocessing import context
from os import system
from django.shortcuts import render, redirect
import datetime
from processing.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from brand_app.models import mediums
from django.http import JsonResponse
from django.contrib.auth.models import User
from order_app.models import orders
# Create your views here.


@login_required(login_url="")
def printing_data(request):
    if request.method =='POST':
        id = request.POST.get('id')
        printing_received_form=request.POST.get('printing_received_form')
        print_wastage_form = request.POST.get('print_wastage_form')

        printing_received_form_1 =request.POST.get('printing_received_form_1')
        print_wastage_form_1 = request.POST.get('print_wastage_form_1')
        printing_received_form_2 =request.POST.get('printing_received_form_2')
        print_wastage_form_2 = request.POST.get('print_wastage_form_2')
        printing_received_form_3 =request.POST.get('printing_received_form_3')
        print_wastage_form_3 = request.POST.get('print_wastage_form_3')
        printing_received_form_4 =request.POST.get('printing_received_form_4')
        print_wastage_form_4 = request.POST.get('print_wastage_form_4')
        printing_received_form_5 =request.POST.get('printing_received_form_5')
        print_wastage_form_5 = request.POST.get('print_wastage_form_5')
        printing_received_form_6 =request.POST.get('printing_received_form_6')
        print_wastage_form_6 = request.POST.get('print_wastage_form_6')
        printing_received_form_7 =request.POST.get('printing_received_form_7')
        print_wastage_form_7 = request.POST.get('print_wastage_form_7')
        printing_received_form_8 =request.POST.get('printing_received_form_8')
        print_wastage_form_8 = request.POST.get('print_wastage_form_8')
        printing_received_form_9 =request.POST.get('printing_received_form_9')
        print_wastage_form_9 = request.POST.get('print_wastage_form_9')
        printing_received_form_10 =request.POST.get('printing_received_form_10')
        print_wastage_form_10 = request.POST.get('print_wastage_form_10')
        
        printing_received_form_11 =request.POST.get('printing_received_form_11')
        print_wastage_form_11 = request.POST.get('print_wastage_form_11')
        printing_received_form_12 =request.POST.get('printing_received_form_12')
        print_wastage_form_12 = request.POST.get('print_wastage_form_12')
        printing_received_form_13 =request.POST.get('printing_received_form_13')
        print_wastage_form_13 = request.POST.get('print_wastage_form_13')
        printing_received_form_14 =request.POST.get('printing_received_form_14')
        print_wastage_form_14 = request.POST.get('print_wastage_form_14')
        printing_received_form_15 =request.POST.get('printing_received_form_15')
        print_wastage_form_15 = request.POST.get('print_wastage_form_15')
        printing_received_form_16 =request.POST.get('printing_received_form_16')
        print_wastage_form_16 = request.POST.get('print_wastage_form_16')
        printing_received_form_17 =request.POST.get('printing_received_form_17')
        print_wastage_form_17 = request.POST.get('print_wastage_form_17')
        printing_received_form_18 =request.POST.get('printing_received_form_18')
        print_wastage_form_18 = request.POST.get('print_wastage_form_18')
        printing_received_form_19 =request.POST.get('printing_received_form_19')
        print_wastage_form_19 = request.POST.get('print_wastage_form_19')
        printing_received_form_20 =request.POST.get('printing_received_form_20')
        print_wastage_form_20 = request.POST.get('print_wastage_form_20')

        printing_received_form_21 =request.POST.get('printing_received_form_21')
        print_wastage_form_21 = request.POST.get('print_wastage_form_21')
        printing_received_form_22 =request.POST.get('printing_received_form_22')
        print_wastage_form_22 = request.POST.get('print_wastage_form_22')
        printing_received_form_23 =request.POST.get('printing_received_form_23')
        print_wastage_form_23 = request.POST.get('print_wastage_form_23')
        printing_received_form_24 =request.POST.get('printing_received_form_24')
        print_wastage_form_24 = request.POST.get('print_wastage_form_24')
        printing_received_form_25 =request.POST.get('printing_received_form_25')
        print_wastage_form_25 = request.POST.get('print_wastage_form_25')
        printing_received_form_26 =request.POST.get('printing_received_form_26')
        print_wastage_form_26 = request.POST.get('print_wastage_form_26')
        printing_received_form_27 =request.POST.get('printing_received_form_27')
        print_wastage_form_27 = request.POST.get('print_wastage_form_27')
        printing_received_form_28 =request.POST.get('printing_received_form_28')
        print_wastage_form_28 = request.POST.get('print_wastage_form_28')
        printing_received_form_29 =request.POST.get('printing_received_form_29')
        print_wastage_form_29 = request.POST.get('print_wastage_form_29')
        printing_received_form_30 =request.POST.get('printing_received_form_30')
        print_wastage_form_30 = request.POST.get('print_wastage_form_30')

        printing_received_form_31 =request.POST.get('printing_received_form_31')
        print_wastage_form_31 = request.POST.get('print_wastage_form_31')
        printing_received_form_32 =request.POST.get('printing_received_form_32')
        print_wastage_form_32 = request.POST.get('print_wastage_form_32')
        printing_received_form_33 =request.POST.get('printing_received_form_33')
        print_wastage_form_33 = request.POST.get('print_wastage_form_33')
        printing_received_form_34 =request.POST.get('printing_received_form_34')
        print_wastage_form_34 = request.POST.get('print_wastage_form_34')
        printing_received_form_35 =request.POST.get('printing_received_form_35')
        print_wastage_form_35 = request.POST.get('print_wastage_form_35')
        printing_received_form_36 =request.POST.get('printing_received_form_36')
        print_wastage_form_36 = request.POST.get('print_wastage_form_36')
        printing_received_form_37 =request.POST.get('printing_received_form_37')
        print_wastage_form_37 = request.POST.get('print_wastage_form_37')
        printing_received_form_38 =request.POST.get('printing_received_form_38')
        print_wastage_form_38 = request.POST.get('print_wastage_form_38')
        printing_received_form_39 =request.POST.get('printing_received_form_39')
        print_wastage_form_39 = request.POST.get('print_wastage_form_39')
        printing_received_form_40 =request.POST.get('printing_received_form_40')
        print_wastage_form_40 = request.POST.get('print_wastage_form_40')

        printing_received_form_41 =request.POST.get('printing_received_form_41')
        print_wastage_form_41 = request.POST.get('print_wastage_form_41')
        printing_received_form_42 =request.POST.get('printing_received_form_42')
        print_wastage_form_42 = request.POST.get('print_wastage_form_42')
        printing_received_form_43 =request.POST.get('printing_received_form_43')
        print_wastage_form_43 = request.POST.get('print_wastage_form_43')
        printing_received_form_44 =request.POST.get('printing_received_form_44')
        print_wastage_form_44 = request.POST.get('print_wastage_form_44')
        printing_received_form_45 =request.POST.get('printing_received_form_45')
        print_wastage_form_45 = request.POST.get('print_wastage_form_45')
        printing_received_form_46 =request.POST.get('printing_received_form_46')
        print_wastage_form_46 = request.POST.get('print_wastage_form_46')
        printing_received_form_47 =request.POST.get('printing_received_form_47')
        print_wastage_form_47 = request.POST.get('print_wastage_form_47')
        printing_received_form_48 =request.POST.get('printing_received_form_48')
        print_wastage_form_48 = request.POST.get('print_wastage_form_48')
        printing_received_form_49 =request.POST.get('printing_received_form_49')
        print_wastage_form_49 = request.POST.get('print_wastage_form_49')
        printing_received_form_50=request.POST.get('printing_received_form_50')
        print_wastage_form_50 = request.POST.get('print_wastage_form_50')

        

        print_date = request.POST.get('print_date')
        order = orders.objects.filter(order_id=id).get()
        print('order',order)
        order.printing_received_form=printing_received_form
        order.print_wastage_form=print_wastage_form
        order.printing_received_form_1=printing_received_form_1
        order.print_wastage_form_1=print_wastage_form_1 
        order.printing_received_form_2=printing_received_form_2
        order.print_wastage_form_2=print_wastage_form_2 
        order.printing_received_form_3=printing_received_form_3
        order.print_wastage_form_3=print_wastage_form_3 
        order.printing_received_form_4=printing_received_form_4
        order.print_wastage_form_4=print_wastage_form_4 
        order.printing_received_form_5=printing_received_form_5
        order.print_wastage_form_5=print_wastage_form_5 
        order.printing_received_form_6=printing_received_form_6
        order.print_wastage_form_6=print_wastage_form_6 
        order.printing_received_form_7=printing_received_form_7
        order.print_wastage_form_7=print_wastage_form_7 
        order.printing_received_form_8=printing_received_form_8
        order.print_wastage_form_8=print_wastage_form_8 
        order.printing_received_form_9=printing_received_form_9
        order.print_wastage_form_9=print_wastage_form_9 
        order.printing_received_form_10=printing_received_form_10
        order.print_wastage_form_10=print_wastage_form_10  

        order.printing_received_form_11=printing_received_form_11
        order.print_wastage_form_11=print_wastage_form_11 
        order.printing_received_form_12=printing_received_form_12
        order.print_wastage_form_12=print_wastage_form_12 
        order.printing_received_form_13=printing_received_form_13
        order.print_wastage_form_13=print_wastage_form_13 
        order.printing_received_form_14=printing_received_form_14
        order.print_wastage_form_14=print_wastage_form_14 
        order.printing_received_form_15=printing_received_form_15
        order.print_wastage_form_15=print_wastage_form_15 
        order.printing_received_form_16=printing_received_form_16
        order.print_wastage_form_16=print_wastage_form_16 
        order.printing_received_form_17=printing_received_form_17
        order.print_wastage_form_17=print_wastage_form_17 
        order.printing_received_form_18=printing_received_form_18
        order.print_wastage_form_18=print_wastage_form_18 
        order.printing_received_form_19=printing_received_form_19
        order.print_wastage_form_19=print_wastage_form_19 
        order.printing_received_form_20=printing_received_form_20
        order.print_wastage_form_20=print_wastage_form_20 

        order.printing_received_form_21=printing_received_form_21
        order.print_wastage_form_21=print_wastage_form_21 
        order.printing_received_form_22=printing_received_form_22
        order.print_wastage_form_22=print_wastage_form_22 
        order.printing_received_form_23=printing_received_form_23
        order.print_wastage_form_23=print_wastage_form_23 
        order.printing_received_form_24=printing_received_form_24
        order.print_wastage_form_24=print_wastage_form_24 
        order.printing_received_form_25=printing_received_form_25
        order.print_wastage_form_25=print_wastage_form_25 
        order.printing_received_form_26=printing_received_form_26
        order.print_wastage_form_26=print_wastage_form_26 
        order.printing_received_form_27=printing_received_form_27
        order.print_wastage_form_27=print_wastage_form_27 
        order.printing_received_form_28=printing_received_form_28
        order.print_wastage_form_28=print_wastage_form_28 
        order.printing_received_form_29=printing_received_form_29
        order.print_wastage_form_29=print_wastage_form_29 
        order.printing_received_form_30=printing_received_form_30
        order.print_wastage_form_30=print_wastage_form_30 

        order.printing_received_form_31=printing_received_form_31
        order.print_wastage_form_31=print_wastage_form_31 
        order.printing_received_form_32=printing_received_form_32
        order.print_wastage_form_32=print_wastage_form_32 
        order.printing_received_form_33=printing_received_form_33
        order.print_wastage_form_33=print_wastage_form_33 
        order.printing_received_form_34=printing_received_form_34
        order.print_wastage_form_34=print_wastage_form_34 
        order.printing_received_form_35=printing_received_form_35  
        order.print_wastage_form_35=print_wastage_form_35 
        order.printing_received_form_36=printing_received_form_36
        order.print_wastage_form_36=print_wastage_form_36 
        order.printing_received_form_37=printing_received_form_37
        order.print_wastage_form_37=print_wastage_form_37 
        order.printing_received_form_38=printing_received_form_38
        order.print_wastage_form_38=print_wastage_form_38 
        order.printing_received_form_39=printing_received_form_39
        order.print_wastage_form_39=print_wastage_form_39 
        order.printing_received_form_40=printing_received_form_40
        order.print_wastage_form_40=print_wastage_form_40 

        order.printing_received_form_41=printing_received_form_41
        order.print_wastage_form_41=print_wastage_form_41 
        order.printing_received_form_42=printing_received_form_42
        order.print_wastage_form_42=print_wastage_form_42 
        order.printing_received_form_43=printing_received_form_43
        order.print_wastage_form_43=print_wastage_form_43 
        order.printing_received_form_44=printing_received_form_44
        order.print_wastage_form_44=print_wastage_form_44 
        order.printing_received_form_45=printing_received_form_45
        order.print_wastage_form_45=print_wastage_form_45 
        order.printing_received_form_46=printing_received_form_46
        order.print_wastage_form_46=print_wastage_form_46 
        order.printing_received_form_47=printing_received_form_47
        order.print_wastage_form_47=print_wastage_form_47 
        order.printing_received_form_48=printing_received_form_48
        order.print_wastage_form_48=print_wastage_form_48 
        order.printing_received_form_49=printing_received_form_49
        order.print_wastage_form_49=print_wastage_form_49 
        order.printing_received_form_50=printing_received_form_50
        order.print_wastage_form_50=print_wastage_form_50 

        
        order.print_date=datetime.datetime.now()
        order.save()
    
    data1 = orders.objects.all().order_by('-order_id') 
    # for i in data1:

    #     data2 = orders.objects.get(order_id = i.order_id)  
    #     print('dataa',data2.print_approved)
    context={
        'data1':data1,    
        # 'data2':data2,   
    }
    return render(request,'processing/printing.html',context)



from django.db.models import Q
@login_required(login_url="")
def view_printing(request, order_id):
    data1 = orders.objects.get(order_id=order_id)
    print('gjhgjmgj',order_id)

    if request.method == 'POST':
        data1.printing_received_form = request.POST.get('printing_received_form')

        data1.printing_received_form_1=request.POST.get('printing_received_form_1')
        data1.printing_received_form_2=request.POST.get('printing_received_form_2')
        data1.printing_received_form_3=request.POST.get('printing_received_form_3')
        data1.printing_received_form_4=request.POST.get('printing_received_form_4')
        data1.printing_received_form_5=request.POST.get('printing_received_form_5')
        data1.printing_received_form_6=request.POST.get('printing_received_form_6')
        data1.printing_received_form_7=request.POST.get('printing_received_form_7')
        data1.printing_received_form_8=request.POST.get('printing_received_form_8')
        data1.printing_received_form_9=request.POST.get('printing_received_form_9')
        data1.printing_received_form_10=request.POST.get('printing_received_form_10')
        

        data1.printing_received_form_11=request.POST.get('printing_received_form_11')
        data1.printing_received_form_12=request.POST.get('printing_received_form_12')
        data1.printing_received_form_13=request.POST.get('printing_received_form_13')
        data1.printing_received_form_14=request.POST.get('printing_received_form_14')
        data1.printing_received_form_15=request.POST.get('printing_received_form_15')
        data1.printing_received_form_16=request.POST.get('printing_received_form_16')
        data1.printing_received_form_17=request.POST.get('printing_received_form_17')
        data1.printing_received_form_18=request.POST.get('printing_received_form_18')
        data1.printing_received_form_19=request.POST.get('printing_received_form_19')
        data1.printing_received_form_20=request.POST.get('printing_received_form_20')
        

        data1.printing_received_form_21=request.POST.get('printing_received_form_21')
        data1.printing_received_form_22=request.POST.get('printing_received_form_22')
        data1.printing_received_form_23=request.POST.get('printing_received_form_23')
        data1.printing_received_form_24=request.POST.get('printing_received_form_24')
        data1.printing_received_form_25=request.POST.get('printing_received_form_25')
        data1.printing_received_form_26=request.POST.get('printing_received_form_26')
        data1.printing_received_form_27=request.POST.get('printing_received_form_27')
        data1.printing_received_form_28=request.POST.get('printing_received_form_28')
        data1.printing_received_form_29=request.POST.get('printing_received_form_29')
        data1.printing_received_form_30=request.POST.get('printing_received_form_30')
        

        data1.printing_received_form_31=request.POST.get('printing_received_form_31')
        data1.printing_received_form_32=request.POST.get('printing_received_form_32')
        data1.printing_received_form_33=request.POST.get('printing_received_form_33')
        data1.printing_received_form_34=request.POST.get('printing_received_form_34')
        data1.printing_received_form_35=request.POST.get('printing_received_form_35')
        data1.printing_received_form_36=request.POST.get('printing_received_form_36')
        data1.printing_received_form_37=request.POST.get('printing_received_form_37')
        data1.printing_received_form_38=request.POST.get('printing_received_form_38')
        data1.printing_received_form_39=request.POST.get('printing_received_form_39')
        data1.printing_received_form_40=request.POST.get('printing_received_form_40')
        

        data1.printing_received_form_41=request.POST.get('printing_received_form_41')
        data1.printing_received_form_42=request.POST.get('printing_received_form_42')
        data1.printing_received_form_43=request.POST.get('printing_received_form_43')
        data1.printing_received_form_44=request.POST.get('printing_received_form_44')
        data1.printing_received_form_45=request.POST.get('printing_received_form_45')
        data1.printing_received_form_46=request.POST.get('printing_received_form_46')
        data1.printing_received_form_47=request.POST.get('printing_received_form_47')
        data1.printing_received_form_48=request.POST.get('printing_received_form_48')
        data1.printing_received_form_49=request.POST.get('printing_received_form_49')
        data1.printing_received_form_50=request.POST.get('printing_received_form_50')



        data1.printing_received_form_51 = request.POST.get('printing_received_form_51')
        data1.printing_received_form_52 = request.POST.get('printing_received_form_52')
        data1.printing_received_form_53 = request.POST.get('printing_received_form_53')
        data1.printing_received_form_54 = request.POST.get('printing_received_form_54')
        data1.printing_received_form_55 = request.POST.get('printing_received_form_55')
        data1.printing_received_form_56 = request.POST.get('printing_received_form_56')
        data1.printing_received_form_57 = request.POST.get('printing_received_form_57')
        data1.printing_received_form_58 = request.POST.get('printing_received_form_58')
        data1.printing_received_form_59 = request.POST.get('printing_received_form_59')
        data1.printing_received_form_60 = request.POST.get('printing_received_form_60')
        
        
        data1.print_date = datetime.datetime.now()
        
        if data1.printing_received_form_1:
            data1.print_wastage_form_1 = float(data1.pform_1) - float(data1.printing_received_form_1)
        else:
            data1.print_wastage_form_1 = 0

        if data1.printing_received_form_2:
            data1.print_wastage_form_2 = float(data1.pform_1) - float(data1.printing_received_form_2)
        else:
            data1.print_wastage_form_2 = 0

        if data1.printing_received_form_3:
            data1.print_wastage_form_3 = float(data1.pform_1) - float(data1.printing_received_form_3)
        else:
            data1.print_wastage_form_3 = 0

        if data1.printing_received_form_4:
            data1.print_wastage_form_4 = float(data1.pform_1) - float(data1.printing_received_form_4)
        else:
            data1.print_wastage_form_4 = 0

        if data1.printing_received_form_5:
            data1.print_wastage_form_5 = float(data1.pform_1) - float(data1.printing_received_form_5)
        else:
            data1.print_wastage_form_5 = 0

        if data1.printing_received_form_6:
            data1.print_wastage_form_6 = float(data1.pform_1) - float(data1.printing_received_form_6)
        else:
            data1.print_wastage_form_6 = 0

        if data1.printing_received_form_7:
            data1.print_wastage_form_7 = float(data1.pform_1) - float(data1.printing_received_form_7)
        else:
            data1.print_wastage_form_7 = 0

        if data1.printing_received_form_8:
            data1.print_wastage_form_8 = float(data1.pform_1) - float(data1.printing_received_form_8)
        else:
            data1.print_wastage_form_8 = 0

        if data1.printing_received_form_9:
            data1.print_wastage_form_9 = float(data1.pform_1) - float(data1.printing_received_form_9)
        else:
            data1.print_wastage_form_9 = 0

        if data1.printing_received_form_10:
            data1.print_wastage_form_10 = float(data1.pform_1) - float(data1.printing_received_form_10)
        else:
            data1.print_wastage_form_10 = 0  




        if data1.printing_received_form_11:
            data1.print_wastage_form_11 = float(data1.pform_2) - float(data1.printing_received_form_11)
        else:
            data1.print_wastage_form_11 = 0

        if data1.printing_received_form_12:
            data1.print_wastage_form_12 = float(data1.pform_2) - float(data1.printing_received_form_12)
        else:
            data1.print_wastage_form_12 = 0

        if data1.printing_received_form_13:
            data1.print_wastage_form_13 = float(data1.pform_2) - float(data1.printing_received_form_13)
        else:
            data1.print_wastage_form_13 = 0

        if data1.printing_received_form_14:
            data1.print_wastage_form_14 = float(data1.pform_2) - float(data1.printing_received_form_14)
        else:
            data1.print_wastage_form_14 = 0

        if data1.printing_received_form_15:
            data1.print_wastage_form_15 = float(data1.pform_2) - float(data1.printing_received_form_15)
        else:
            data1.print_wastage_form_15 = 0

        if data1.printing_received_form_16:
            data1.print_wastage_form_16 = float(data1.pform_2) - float(data1.printing_received_form_16)
        else:
            data1.print_wastage_form_16 = 0

        if data1.printing_received_form_17:
            data1.print_wastage_form_17 = float(data1.pform_2) - float(data1.printing_received_form_17)
        else:
            data1.print_wastage_form_17 = 0

        if data1.printing_received_form_18:
            data1.print_wastage_form_18 = float(data1.pform_2) - float(data1.printing_received_form_18)
        else:
            data1.print_wastage_form_18 = 0

        if data1.printing_received_form_19:
            data1.print_wastage_form_19 = float(data1.pform_2) - float(data1.printing_received_form_19)
        else:
            data1.print_wastage_form_19 = 0

        if data1.printing_received_form_20:
            data1.print_wastage_form_20 = float(data1.pform_2) - float(data1.printing_received_form_20)
        else:
            data1.print_wastage_form_20 = 0




        if data1.printing_received_form_21:
            data1.print_wastage_form_21 = float(data1.pform_3) - float(data1.printing_received_form_21)
        else:
            data1.print_wastage_form_21 = 0

        if data1.printing_received_form_22:
            data1.print_wastage_form_22 = float(data1.pform_3) - float(data1.printing_received_form_22)
        else:
            data1.print_wastage_form_22 = 0

        if data1.printing_received_form_23:
            data1.print_wastage_form_23 = float(data1.pform_3) - float(data1.printing_received_form_23)
        else:
            data1.print_wastage_form_23 = 0

        if data1.printing_received_form_24:
            data1.print_wastage_form_24 = float(data1.pform_3) - float(data1.printing_received_form_24)
        else:
            data1.print_wastage_form_24 = 0

        if data1.printing_received_form_25:
            data1.print_wastage_form_25 = float(data1.pform_3) - float(data1.printing_received_form_25)
        else:
            data1.print_wastage_form_25 = 0

        if data1.printing_received_form_26:
            data1.print_wastage_form_26 = float(data1.pform_3) - float(data1.printing_received_form_26)
        else:
            data1.print_wastage_form_26 = 0

        if data1.printing_received_form_27:
            data1.print_wastage_form_27 = float(data1.pform_3) - float(data1.printing_received_form_27)
        else:
            data1.print_wastage_form_27 = 0

        if data1.printing_received_form_28:
            data1.print_wastage_form_28 = float(data1.pform_3) - float(data1.printing_received_form_28)
        else:
            data1.print_wastage_form_28 = 0

        if data1.printing_received_form_29:
            data1.print_wastage_form_29 = float(data1.pform_3) - float(data1.printing_received_form_29)
        else:
            data1.print_wastage_form_29 = 0

        if data1.printing_received_form_30:
            data1.print_wastage_form_30 = float(data1.pform_3) - float(data1.printing_received_form_30)
        else:
            data1.print_wastage_form_30 = 0



        if data1.printing_received_form_31:
            data1.print_wastage_form_31 = float(data1.pform_4) - float(data1.printing_received_form_31)
        else:
            data1.print_wastage_form_31 = 0

        if data1.printing_received_form_32:
            data1.print_wastage_form_32 = float(data1.pform_4) - float(data1.printing_received_form_32)
        else:
            data1.print_wastage_form_32 = 0

        if data1.printing_received_form_33:
            data1.print_wastage_form_33 = float(data1.pform_4) - float(data1.printing_received_form_33)
        else:
            data1.print_wastage_form_33 = 0

        if data1.printing_received_form_34:
            data1.print_wastage_form_34 = float(data1.pform_4) - float(data1.printing_received_form_34)
        else:
            data1.print_wastage_form_34 = 0

        if data1.printing_received_form_35:
            data1.print_wastage_form_35 = float(data1.pform_4) - float(data1.printing_received_form_35)
        else:
            data1.print_wastage_form_35 = 0

        if data1.printing_received_form_36:
            data1.print_wastage_form_36 = float(data1.pform_4) - float(data1.printing_received_form_36)
        else:
            data1.print_wastage_form_36 = 0

        if data1.printing_received_form_37:
            data1.print_wastage_form_37 = float(data1.pform_4) - float(data1.printing_received_form_37)
        else:
            data1.print_wastage_form_37 = 0

        if data1.printing_received_form_38:
            data1.print_wastage_form_38 = float(data1.pform_4) - float(data1.printing_received_form_38)
        else:
            data1.print_wastage_form_38 = 0

        if data1.printing_received_form_39:
            data1.print_wastage_form_39 = float(data1.pform_4) - float(data1.printing_received_form_39)
        else:
            data1.print_wastage_form_39 = 0

        if data1.printing_received_form_40:
            data1.print_wastage_form_40 = float(data1.pform_4) - float(data1.printing_received_form_40)
        else:
            data1.print_wastage_form_40 = 0




        if data1.printing_received_form_41:
            data1.print_wastage_form_41 = float(data1.pform_5) - float(data1.printing_received_form_41)
        else:
            data1.print_wastage_form_41 = 0

        if data1.printing_received_form_42:
            data1.print_wastage_form_42 = float(data1.pform_5) - float(data1.printing_received_form_42)
        else:
            data1.print_wastage_form_42 = 0

        if data1.printing_received_form_43:
            data1.print_wastage_form_43 = float(data1.pform_5) - float(data1.printing_received_form_43)
        else:
            data1.print_wastage_form_43 = 0

        if data1.printing_received_form_44:
            data1.print_wastage_form_44 = float(data1.pform_5) - float(data1.printing_received_form_44)
        else:
            data1.print_wastage_form_44 = 0

        if data1.printing_received_form_45:
            data1.print_wastage_form_45 = float(data1.pform_5) - float(data1.printing_received_form_45)
        else:
            data1.print_wastage_form_45 = 0

        if data1.printing_received_form_46:
            data1.print_wastage_form_46 = float(data1.pform_5) - float(data1.printing_received_form_46)
        else:
            data1.print_wastage_form_46 = 0

        if data1.printing_received_form_47:
            data1.print_wastage_form_47 = float(data1.pform_5) - float(data1.printing_received_form_47)
        else:
            data1.print_wastage_form_47 = 0

        if data1.printing_received_form_48:
            data1.print_wastage_form_48 = float(data1.pform_5) - float(data1.printing_received_form_48)
        else:
            data1.print_wastage_form_48 = 0

        if data1.printing_received_form_49:
            data1.print_wastage_form_49 = float(data1.pform_5) - float(data1.printing_received_form_49)
        else:
            data1.print_wastage_form_49 = 0

        if data1.printing_received_form_50:
            data1.print_wastage_form_50 = float(data1.pform_5) - float(data1.printing_received_form_50)
        else:
            data1.print_wastage_form_50 = 0





        if data1.printing_received_form_51:
            data1.print_wastage_form_51 = float(data1.pform_6) - float(data1.printing_received_form_51)
        else:
            data1.print_wastage_form_51 = 0

        if data1.printing_received_form_52:
            data1.print_wastage_form_52 = float(data1.pform_6) - float(data1.printing_received_form_52)
        else:
            data1.print_wastage_form_52 = 0

        if data1.printing_received_form_53:
            data1.print_wastage_form_53 = float(data1.pform_6) - float(data1.printing_received_form_53)
        else:
            data1.print_wastage_form_53 = 0

        if data1.printing_received_form_54:
            data1.print_wastage_form_54 = float(data1.pform_6) - float(data1.printing_received_form_54)
        else:
            data1.print_wastage_form_54 = 0

        if data1.printing_received_form_55:
            data1.print_wastage_form_55 = float(data1.pform_6) - float(data1.printing_received_form_55)
        else:
            data1.print_wastage_form_55 = 0

        if data1.printing_received_form_56:
            data1.print_wastage_form_56 = float(data1.pform_6) - float(data1.printing_received_form_56)
        else:
            data1.print_wastage_form_56 = 0

        if data1.printing_received_form_57:
            data1.print_wastage_form_57 = float(data1.pform_6) - float(data1.printing_received_form_57)
        else:
            data1.print_wastage_form_57 = 0

        if data1.printing_received_form_58:
            data1.print_wastage_form_58 = float(data1.pform_6) - float(data1.printing_received_form_58)
        else:
            data1.print_wastage_form_58 = 0

        if data1.printing_received_form_59:
            data1.print_wastage_form_59 = float(data1.pform_6) - float(data1.printing_received_form_59)
        else:
            data1.print_wastage_form_59 = 0

        if data1.printing_received_form_60:
            data1.print_wastage_form_60 = float(data1.pform_6) - float(data1.printing_received_form_60)
        else:
            data1.print_wastage_form_60 = 0




        temp_print=[]
        if data1.printing_received_form_1:
            temp_print.append(float(data1.printing_received_form_1))
        if data1.printing_received_form_2:
            temp_print.append(float(data1.printing_received_form_2))
        if data1.printing_received_form_3:
            temp_print.append(float(data1.printing_received_form_3))
        if data1.printing_received_form_4:
            temp_print.append(float(data1.printing_received_form_4))
        if data1.printing_received_form_5:
            temp_print.append(float(data1.printing_received_form_5))
        if data1.printing_received_form_6:
            temp_print.append(float(data1.printing_received_form_6))
        if data1.printing_received_form_7:
            temp_print.append(float(data1.printing_received_form_7))
        if data1.printing_received_form_8:
            temp_print.append(float(data1.printing_received_form_8))
        if data1.printing_received_form_9:
            temp_print.append(float(data1.printing_received_form_9))
        if data1.printing_received_form_10:
            temp_print.append(float(data1.printing_received_form_10))

        if data1.printing_received_form_11:
            temp_print.append(float(data1.printing_received_form_11))
        if data1.printing_received_form_12:
            temp_print.append(float(data1.printing_received_form_12))
        if data1.printing_received_form_13:
            temp_print.append(float(data1.printing_received_form_13))
        if data1.printing_received_form_14:
            temp_print.append(float(data1.printing_received_form_14))
        if data1.printing_received_form_15:
            temp_print.append(float(data1.printing_received_form_15))
        if data1.printing_received_form_16:
            temp_print.append(float(data1.printing_received_form_16))
        if data1.printing_received_form_17:
            temp_print.append(float(data1.printing_received_form_17))
        if data1.printing_received_form_18:   
            temp_print.append(float(data1.printing_received_form_18))
        if data1.printing_received_form_19:
            temp_print.append(float(data1.printing_received_form_19))
        if data1.printing_received_form_20:
            temp_print.append(float(data1.printing_received_form_20))

        if data1.printing_received_form_21:
            temp_print.append(float(data1.printing_received_form_21))
        if data1.printing_received_form_22:
            temp_print.append(float(data1.printing_received_form_22))
        if data1.printing_received_form_23:
            temp_print.append(float(data1.printing_received_form_23))
        if data1.printing_received_form_24:
            temp_print.append(float(data1.printing_received_form_24))
        if data1.printing_received_form_25:
            temp_print.append(float(data1.printing_received_form_25))
        if data1.printing_received_form_26:
            temp_print.append(float(data1.printing_received_form_26))
        if data1.printing_received_form_27:
            temp_print.append(float(data1.printing_received_form_27))
        if data1.printing_received_form_28:
            temp_print.append(float(data1.printing_received_form_28))
        if data1.printing_received_form_29:
            temp_print.append(float(data1.printing_received_form_29))
        if data1.printing_received_form_30:
            temp_print.append(float(data1.printing_received_form_30))

        if data1.printing_received_form_31:
            temp_print.append(float(data1.printing_received_form_31))
        if data1.printing_received_form_32:
            temp_print.append(float(data1.printing_received_form_32))
        if data1.printing_received_form_33:
            temp_print.append(float(data1.printing_received_form_33))
        if data1.printing_received_form_34:
            temp_print.append(float(data1.printing_received_form_34))
        if data1.printing_received_form_35:
            temp_print.append(float(data1.printing_received_form_35))
        if data1.printing_received_form_36:
            temp_print.append(float(data1.printing_received_form_36))
        if data1.printing_received_form_37:
            temp_print.append(float(data1.printing_received_form_37))
        if data1.printing_received_form_38:
            temp_print.append(float(data1.printing_received_form_38))
        if data1.printing_received_form_39:
            temp_print.append(float(data1.printing_received_form_39))
        if data1.printing_received_form_40:
            temp_print.append(float(data1.printing_received_form_40))


        if data1.printing_received_form_41:
            temp_print.append(float(data1.printing_received_form_41))
        if data1.printing_received_form_42:
            temp_print.append(float(data1.printing_received_form_42))
        if data1.printing_received_form_43:
            temp_print.append(float(data1.printing_received_form_43))
        if data1.printing_received_form_44:
            temp_print.append(float(data1.printing_received_form_44))
        if data1.printing_received_form_45:
            temp_print.append(float(data1.printing_received_form_45))
        if data1.printing_received_form_46:
            temp_print.append(float(data1.printing_received_form_46))
        if data1.printing_received_form_47:
            temp_print.append(float(data1.printing_received_form_47))
        if data1.printing_received_form_48:
            temp_print.append(float(data1.printing_received_form_48))
        if data1.printing_received_form_49:
            temp_print.append(float(data1.printing_received_form_49))
        if data1.printing_received_form_50:
            temp_print.append(float(data1.printing_received_form_50))



        if data1.printing_received_form_51:
            temp_print.append(float(data1.printing_received_form_51))
        if data1.printing_received_form_52:
            temp_print.append(float(data1.printing_received_form_52))
        if data1.printing_received_form_53:
            temp_print.append(float(data1.printing_received_form_53))
        if data1.printing_received_form_54:
            temp_print.append(float(data1.printing_received_form_54))
        if data1.printing_received_form_55:
            temp_print.append(float(data1.printing_received_form_55))
        if data1.printing_received_form_56:
            temp_print.append(float(data1.printing_received_form_56))
        if data1.printing_received_form_57:
            temp_print.append(float(data1.printing_received_form_57))
        if data1.printing_received_form_58:
            temp_print.append(float(data1.printing_received_form_58))
        if data1.printing_received_form_59:
            temp_print.append(float(data1.printing_received_form_59))
        if data1.printing_received_form_60:
            temp_print.append(float(data1.printing_received_form_60))



        temp_print=[i for i in temp_print]
        print('temp_print',temp_print)
        data1.printing_received_form=0
        for i in temp_print:
            data1.printing_received_form=data1.printing_received_form+i
        print('data1.printing_received_form',data1.printing_received_form)
        
       

        
        if data1.printing_received_form:
            sum_wastage_form=0
            for i in range (1,51):
                sum_wastage_form += float(getattr(data1,f"print_wastage_form_{i}",0))
                data1.print_wastage_form = sum_wastage_form
        else:
            data1.print_wastage_form = 0
        
        data1.save()
        messages.success(request, "Updated Successfully...!!")
        if request.method == 'POST':
            if request.POST.get("print_approval") == "approval_button":
                orders.objects.filter(Q(order_id=order_id) & Q(print_approved=False)).update(print_approved=True)
            else:
                pass    

        return redirect('/printing-data/')
       
    context = {'data1':data1}
    return render(request, 'processing/view_printing.html', context)








from django.db.models import Q
@login_required(login_url="")
def edit_printing(request, order_id):
    data1 = orders.objects.get(order_id=order_id)
    print('gjhgjmgj',order_id)

    if request.method == 'POST':
        data1.printing_received_form = request.POST.get('printing_received_form')

        data1.printing_received_form_1=request.POST.get('printing_received_form_1')
        data1.printing_received_form_2=request.POST.get('printing_received_form_2')
        data1.printing_received_form_3=request.POST.get('printing_received_form_3')
        data1.printing_received_form_4=request.POST.get('printing_received_form_4')
        data1.printing_received_form_5=request.POST.get('printing_received_form_5')
        data1.printing_received_form_6=request.POST.get('printing_received_form_6')
        data1.printing_received_form_7=request.POST.get('printing_received_form_7')
        data1.printing_received_form_8=request.POST.get('printing_received_form_8')
        data1.printing_received_form_9=request.POST.get('printing_received_form_9')
        data1.printing_received_form_10=request.POST.get('printing_received_form_10')
        

        data1.printing_received_form_11=request.POST.get('printing_received_form_11')
        data1.printing_received_form_12=request.POST.get('printing_received_form_12')
        data1.printing_received_form_13=request.POST.get('printing_received_form_13')
        data1.printing_received_form_14=request.POST.get('printing_received_form_14')
        data1.printing_received_form_15=request.POST.get('printing_received_form_15')
        data1.printing_received_form_16=request.POST.get('printing_received_form_16')
        data1.printing_received_form_17=request.POST.get('printing_received_form_17')
        data1.printing_received_form_18=request.POST.get('printing_received_form_18')
        data1.printing_received_form_19=request.POST.get('printing_received_form_19')
        data1.printing_received_form_20=request.POST.get('printing_received_form_20')
        

        data1.printing_received_form_21=request.POST.get('printing_received_form_21')
        data1.printing_received_form_22=request.POST.get('printing_received_form_22')
        data1.printing_received_form_23=request.POST.get('printing_received_form_23')
        data1.printing_received_form_24=request.POST.get('printing_received_form_24')
        data1.printing_received_form_25=request.POST.get('printing_received_form_25')
        data1.printing_received_form_26=request.POST.get('printing_received_form_26')
        data1.printing_received_form_27=request.POST.get('printing_received_form_27')
        data1.printing_received_form_28=request.POST.get('printing_received_form_28')
        data1.printing_received_form_29=request.POST.get('printing_received_form_29')
        data1.printing_received_form_30=request.POST.get('printing_received_form_30')
        

        data1.printing_received_form_31=request.POST.get('printing_received_form_31')
        data1.printing_received_form_32=request.POST.get('printing_received_form_32')
        data1.printing_received_form_33=request.POST.get('printing_received_form_33')
        data1.printing_received_form_34=request.POST.get('printing_received_form_34')
        data1.printing_received_form_35=request.POST.get('printing_received_form_35')
        data1.printing_received_form_36=request.POST.get('printing_received_form_36')
        data1.printing_received_form_37=request.POST.get('printing_received_form_37')
        data1.printing_received_form_38=request.POST.get('printing_received_form_38')
        data1.printing_received_form_39=request.POST.get('printing_received_form_39')
        data1.printing_received_form_40=request.POST.get('printing_received_form_40')
        

        data1.printing_received_form_41=request.POST.get('printing_received_form_41')
        data1.printing_received_form_42=request.POST.get('printing_received_form_42')
        data1.printing_received_form_43=request.POST.get('printing_received_form_43')
        data1.printing_received_form_44=request.POST.get('printing_received_form_44')
        data1.printing_received_form_45=request.POST.get('printing_received_form_45')
        data1.printing_received_form_46=request.POST.get('printing_received_form_46')
        data1.printing_received_form_47=request.POST.get('printing_received_form_47')
        data1.printing_received_form_48=request.POST.get('printing_received_form_48')
        data1.printing_received_form_49=request.POST.get('printing_received_form_49')
        data1.printing_received_form_50=request.POST.get('printing_received_form_50')



        data1.printing_received_form_51 = request.POST.get('printing_received_form_51')
        data1.printing_received_form_52 = request.POST.get('printing_received_form_52')
        data1.printing_received_form_53 = request.POST.get('printing_received_form_53')
        data1.printing_received_form_54 = request.POST.get('printing_received_form_54')
        data1.printing_received_form_55 = request.POST.get('printing_received_form_55')
        data1.printing_received_form_56 = request.POST.get('printing_received_form_56')
        data1.printing_received_form_57 = request.POST.get('printing_received_form_57')
        data1.printing_received_form_58 = request.POST.get('printing_received_form_58')
        data1.printing_received_form_59 = request.POST.get('printing_received_form_59')
        data1.printing_received_form_60 = request.POST.get('printing_received_form_60')
        
        
        data1.print_date = datetime.datetime.now()
        
        if data1.printing_received_form_1:
            data1.print_wastage_form_1 = float(data1.pform_1) - float(data1.printing_received_form_1)
        else:
            data1.print_wastage_form_1 = 0

        if data1.printing_received_form_2:
            data1.print_wastage_form_2 = float(data1.pform_1) - float(data1.printing_received_form_2)
        else:
            data1.print_wastage_form_2 = 0

        if data1.printing_received_form_3:
            data1.print_wastage_form_3 = float(data1.pform_1) - float(data1.printing_received_form_3)
        else:
            data1.print_wastage_form_3 = 0

        if data1.printing_received_form_4:
            data1.print_wastage_form_4 = float(data1.pform_1) - float(data1.printing_received_form_4)
        else:
            data1.print_wastage_form_4 = 0

        if data1.printing_received_form_5:
            data1.print_wastage_form_5 = float(data1.pform_1) - float(data1.printing_received_form_5)
        else:
            data1.print_wastage_form_5 = 0

        if data1.printing_received_form_6:
            data1.print_wastage_form_6 = float(data1.pform_1) - float(data1.printing_received_form_6)
        else:
            data1.print_wastage_form_6 = 0

        if data1.printing_received_form_7:
            data1.print_wastage_form_7 = float(data1.pform_1) - float(data1.printing_received_form_7)
        else:
            data1.print_wastage_form_7 = 0

        if data1.printing_received_form_8:
            data1.print_wastage_form_8 = float(data1.pform_1) - float(data1.printing_received_form_8)
        else:
            data1.print_wastage_form_8 = 0

        if data1.printing_received_form_9:
            data1.print_wastage_form_9 = float(data1.pform_1) - float(data1.printing_received_form_9)
        else:
            data1.print_wastage_form_9 = 0

        if data1.printing_received_form_10:
            data1.print_wastage_form_10 = float(data1.pform_1) - float(data1.printing_received_form_10)
        else:
            data1.print_wastage_form_10 = 0  




        if data1.printing_received_form_11:
            data1.print_wastage_form_11 = float(data1.pform_2) - float(data1.printing_received_form_11)
        else:
            data1.print_wastage_form_11 = 0

        if data1.printing_received_form_12:
            data1.print_wastage_form_12 = float(data1.pform_2) - float(data1.printing_received_form_12)
        else:
            data1.print_wastage_form_12 = 0

        if data1.printing_received_form_13:
            data1.print_wastage_form_13 = float(data1.pform_2) - float(data1.printing_received_form_13)
        else:
            data1.print_wastage_form_13 = 0

        if data1.printing_received_form_14:
            data1.print_wastage_form_14 = float(data1.pform_2) - float(data1.printing_received_form_14)
        else:
            data1.print_wastage_form_14 = 0

        if data1.printing_received_form_15:
            data1.print_wastage_form_15 = float(data1.pform_2) - float(data1.printing_received_form_15)
        else:
            data1.print_wastage_form_15 = 0

        if data1.printing_received_form_16:
            data1.print_wastage_form_16 = float(data1.pform_2) - float(data1.printing_received_form_16)
        else:
            data1.print_wastage_form_16 = 0

        if data1.printing_received_form_17:
            data1.print_wastage_form_17 = float(data1.pform_2) - float(data1.printing_received_form_17)
        else:
            data1.print_wastage_form_17 = 0

        if data1.printing_received_form_18:
            data1.print_wastage_form_18 = float(data1.pform_2) - float(data1.printing_received_form_18)
        else:
            data1.print_wastage_form_18 = 0

        if data1.printing_received_form_19:
            data1.print_wastage_form_19 = float(data1.pform_2) - float(data1.printing_received_form_19)
        else:
            data1.print_wastage_form_19 = 0

        if data1.printing_received_form_20:
            data1.print_wastage_form_20 = float(data1.pform_2) - float(data1.printing_received_form_20)
        else:
            data1.print_wastage_form_20 = 0




        if data1.printing_received_form_21:
            data1.print_wastage_form_21 = float(data1.pform_3) - float(data1.printing_received_form_21)
        else:
            data1.print_wastage_form_21 = 0

        if data1.printing_received_form_22:
            data1.print_wastage_form_22 = float(data1.pform_3) - float(data1.printing_received_form_22)
        else:
            data1.print_wastage_form_22 = 0

        if data1.printing_received_form_23:
            data1.print_wastage_form_23 = float(data1.pform_3) - float(data1.printing_received_form_23)
        else:
            data1.print_wastage_form_23 = 0

        if data1.printing_received_form_24:
            data1.print_wastage_form_24 = float(data1.pform_3) - float(data1.printing_received_form_24)
        else:
            data1.print_wastage_form_24 = 0

        if data1.printing_received_form_25:
            data1.print_wastage_form_25 = float(data1.pform_3) - float(data1.printing_received_form_25)
        else:
            data1.print_wastage_form_25 = 0

        if data1.printing_received_form_26:
            data1.print_wastage_form_26 = float(data1.pform_3) - float(data1.printing_received_form_26)
        else:
            data1.print_wastage_form_26 = 0

        if data1.printing_received_form_27:
            data1.print_wastage_form_27 = float(data1.pform_3) - float(data1.printing_received_form_27)
        else:
            data1.print_wastage_form_27 = 0

        if data1.printing_received_form_28:
            data1.print_wastage_form_28 = float(data1.pform_3) - float(data1.printing_received_form_28)
        else:
            data1.print_wastage_form_28 = 0

        if data1.printing_received_form_29:
            data1.print_wastage_form_29 = float(data1.pform_3) - float(data1.printing_received_form_29)
        else:
            data1.print_wastage_form_29 = 0

        if data1.printing_received_form_30:
            data1.print_wastage_form_30 = float(data1.pform_3) - float(data1.printing_received_form_30)
        else:
            data1.print_wastage_form_30 = 0



        if data1.printing_received_form_31:
            data1.print_wastage_form_31 = float(data1.pform_4) - float(data1.printing_received_form_31)
        else:
            data1.print_wastage_form_31 = 0

        if data1.printing_received_form_32:
            data1.print_wastage_form_32 = float(data1.pform_4) - float(data1.printing_received_form_32)
        else:
            data1.print_wastage_form_32 = 0

        if data1.printing_received_form_33:
            data1.print_wastage_form_33 = float(data1.pform_4) - float(data1.printing_received_form_33)
        else:
            data1.print_wastage_form_33 = 0

        if data1.printing_received_form_34:
            data1.print_wastage_form_34 = float(data1.pform_4) - float(data1.printing_received_form_34)
        else:
            data1.print_wastage_form_34 = 0

        if data1.printing_received_form_35:
            data1.print_wastage_form_35 = float(data1.pform_4) - float(data1.printing_received_form_35)
        else:
            data1.print_wastage_form_35 = 0

        if data1.printing_received_form_36:
            data1.print_wastage_form_36 = float(data1.pform_4) - float(data1.printing_received_form_36)
        else:
            data1.print_wastage_form_36 = 0

        if data1.printing_received_form_37:
            data1.print_wastage_form_37 = float(data1.pform_4) - float(data1.printing_received_form_37)
        else:
            data1.print_wastage_form_37 = 0

        if data1.printing_received_form_38:
            data1.print_wastage_form_38 = float(data1.pform_4) - float(data1.printing_received_form_38)
        else:
            data1.print_wastage_form_38 = 0

        if data1.printing_received_form_39:
            data1.print_wastage_form_39 = float(data1.pform_4) - float(data1.printing_received_form_39)
        else:
            data1.print_wastage_form_39 = 0

        if data1.printing_received_form_40:
            data1.print_wastage_form_40 = float(data1.pform_4) - float(data1.printing_received_form_40)
        else:
            data1.print_wastage_form_40 = 0




        if data1.printing_received_form_41:
            data1.print_wastage_form_41 = float(data1.pform_5) - float(data1.printing_received_form_41)
        else:
            data1.print_wastage_form_41 = 0

        if data1.printing_received_form_42:
            data1.print_wastage_form_42 = float(data1.pform_5) - float(data1.printing_received_form_42)
        else:
            data1.print_wastage_form_42 = 0

        if data1.printing_received_form_43:
            data1.print_wastage_form_43 = float(data1.pform_5) - float(data1.printing_received_form_43)
        else:
            data1.print_wastage_form_43 = 0

        if data1.printing_received_form_44:
            data1.print_wastage_form_44 = float(data1.pform_5) - float(data1.printing_received_form_44)
        else:
            data1.print_wastage_form_44 = 0

        if data1.printing_received_form_45:
            data1.print_wastage_form_45 = float(data1.pform_5) - float(data1.printing_received_form_45)
        else:
            data1.print_wastage_form_45 = 0

        if data1.printing_received_form_46:
            data1.print_wastage_form_46 = float(data1.pform_5) - float(data1.printing_received_form_46)
        else:
            data1.print_wastage_form_46 = 0

        if data1.printing_received_form_47:
            data1.print_wastage_form_47 = float(data1.pform_5) - float(data1.printing_received_form_47)
        else:
            data1.print_wastage_form_47 = 0

        if data1.printing_received_form_48:
            data1.print_wastage_form_48 = float(data1.pform_5) - float(data1.printing_received_form_48)
        else:
            data1.print_wastage_form_48 = 0

        if data1.printing_received_form_49:
            data1.print_wastage_form_49 = float(data1.pform_5) - float(data1.printing_received_form_49)
        else:
            data1.print_wastage_form_49 = 0

        if data1.printing_received_form_50:
            data1.print_wastage_form_50 = float(data1.pform_5) - float(data1.printing_received_form_50)
        else:
            data1.print_wastage_form_50 = 0





        if data1.printing_received_form_51:
            data1.print_wastage_form_51 = float(data1.pform_6) - float(data1.printing_received_form_51)
        else:
            data1.print_wastage_form_51 = 0

        if data1.printing_received_form_52:
            data1.print_wastage_form_52 = float(data1.pform_6) - float(data1.printing_received_form_52)
        else:
            data1.print_wastage_form_52 = 0

        if data1.printing_received_form_53:
            data1.print_wastage_form_53 = float(data1.pform_6) - float(data1.printing_received_form_53)
        else:
            data1.print_wastage_form_53 = 0

        if data1.printing_received_form_54:
            data1.print_wastage_form_54 = float(data1.pform_6) - float(data1.printing_received_form_54)
        else:
            data1.print_wastage_form_54 = 0

        if data1.printing_received_form_55:
            data1.print_wastage_form_55 = float(data1.pform_6) - float(data1.printing_received_form_55)
        else:
            data1.print_wastage_form_55 = 0

        if data1.printing_received_form_56:
            data1.print_wastage_form_56 = float(data1.pform_6) - float(data1.printing_received_form_56)
        else:
            data1.print_wastage_form_56 = 0

        if data1.printing_received_form_57:
            data1.print_wastage_form_57 = float(data1.pform_6) - float(data1.printing_received_form_57)
        else:
            data1.print_wastage_form_57 = 0

        if data1.printing_received_form_58:
            data1.print_wastage_form_58 = float(data1.pform_6) - float(data1.printing_received_form_58)
        else:
            data1.print_wastage_form_58 = 0

        if data1.printing_received_form_59:
            data1.print_wastage_form_59 = float(data1.pform_6) - float(data1.printing_received_form_59)
        else:
            data1.print_wastage_form_59 = 0

        if data1.printing_received_form_60:
            data1.print_wastage_form_60 = float(data1.pform_6) - float(data1.printing_received_form_60)
        else:
            data1.print_wastage_form_60 = 0




        temp_print=[]
        if data1.printing_received_form_1:
            temp_print.append(float(data1.printing_received_form_1))
        if data1.printing_received_form_2:
            temp_print.append(float(data1.printing_received_form_2))
        if data1.printing_received_form_3:
            temp_print.append(float(data1.printing_received_form_3))
        if data1.printing_received_form_4:
            temp_print.append(float(data1.printing_received_form_4))
        if data1.printing_received_form_5:
            temp_print.append(float(data1.printing_received_form_5))
        if data1.printing_received_form_6:
            temp_print.append(float(data1.printing_received_form_6))
        if data1.printing_received_form_7:
            temp_print.append(float(data1.printing_received_form_7))
        if data1.printing_received_form_8:
            temp_print.append(float(data1.printing_received_form_8))
        if data1.printing_received_form_9:
            temp_print.append(float(data1.printing_received_form_9))
        if data1.printing_received_form_10:
            temp_print.append(float(data1.printing_received_form_10))

        if data1.printing_received_form_11:
            temp_print.append(float(data1.printing_received_form_11))
        if data1.printing_received_form_12:
            temp_print.append(float(data1.printing_received_form_12))
        if data1.printing_received_form_13:
            temp_print.append(float(data1.printing_received_form_13))
        if data1.printing_received_form_14:
            temp_print.append(float(data1.printing_received_form_14))
        if data1.printing_received_form_15:
            temp_print.append(float(data1.printing_received_form_15))
        if data1.printing_received_form_16:
            temp_print.append(float(data1.printing_received_form_16))
        if data1.printing_received_form_17:
            temp_print.append(float(data1.printing_received_form_17))
        if data1.printing_received_form_18:   
            temp_print.append(float(data1.printing_received_form_18))
        if data1.printing_received_form_19:
            temp_print.append(float(data1.printing_received_form_19))
        if data1.printing_received_form_20:
            temp_print.append(float(data1.printing_received_form_20))

        if data1.printing_received_form_21:
            temp_print.append(float(data1.printing_received_form_21))
        if data1.printing_received_form_22:
            temp_print.append(float(data1.printing_received_form_22))
        if data1.printing_received_form_23:
            temp_print.append(float(data1.printing_received_form_23))
        if data1.printing_received_form_24:
            temp_print.append(float(data1.printing_received_form_24))
        if data1.printing_received_form_25:
            temp_print.append(float(data1.printing_received_form_25))
        if data1.printing_received_form_26:
            temp_print.append(float(data1.printing_received_form_26))
        if data1.printing_received_form_27:
            temp_print.append(float(data1.printing_received_form_27))
        if data1.printing_received_form_28:
            temp_print.append(float(data1.printing_received_form_28))
        if data1.printing_received_form_29:
            temp_print.append(float(data1.printing_received_form_29))
        if data1.printing_received_form_30:
            temp_print.append(float(data1.printing_received_form_30))

        if data1.printing_received_form_31:
            temp_print.append(float(data1.printing_received_form_31))
        if data1.printing_received_form_32:
            temp_print.append(float(data1.printing_received_form_32))
        if data1.printing_received_form_33:
            temp_print.append(float(data1.printing_received_form_33))
        if data1.printing_received_form_34:
            temp_print.append(float(data1.printing_received_form_34))
        if data1.printing_received_form_35:
            temp_print.append(float(data1.printing_received_form_35))
        if data1.printing_received_form_36:
            temp_print.append(float(data1.printing_received_form_36))
        if data1.printing_received_form_37:
            temp_print.append(float(data1.printing_received_form_37))
        if data1.printing_received_form_38:
            temp_print.append(float(data1.printing_received_form_38))
        if data1.printing_received_form_39:
            temp_print.append(float(data1.printing_received_form_39))
        if data1.printing_received_form_40:
            temp_print.append(float(data1.printing_received_form_40))


        if data1.printing_received_form_41:
            temp_print.append(float(data1.printing_received_form_41))
        if data1.printing_received_form_42:
            temp_print.append(float(data1.printing_received_form_42))
        if data1.printing_received_form_43:
            temp_print.append(float(data1.printing_received_form_43))
        if data1.printing_received_form_44:
            temp_print.append(float(data1.printing_received_form_44))
        if data1.printing_received_form_45:
            temp_print.append(float(data1.printing_received_form_45))
        if data1.printing_received_form_46:
            temp_print.append(float(data1.printing_received_form_46))
        if data1.printing_received_form_47:
            temp_print.append(float(data1.printing_received_form_47))
        if data1.printing_received_form_48:
            temp_print.append(float(data1.printing_received_form_48))
        if data1.printing_received_form_49:
            temp_print.append(float(data1.printing_received_form_49))
        if data1.printing_received_form_50:
            temp_print.append(float(data1.printing_received_form_50))



        if data1.printing_received_form_51:
            temp_print.append(float(data1.printing_received_form_51))
        if data1.printing_received_form_52:
            temp_print.append(float(data1.printing_received_form_52))
        if data1.printing_received_form_53:
            temp_print.append(float(data1.printing_received_form_53))
        if data1.printing_received_form_54:
            temp_print.append(float(data1.printing_received_form_54))
        if data1.printing_received_form_55:
            temp_print.append(float(data1.printing_received_form_55))
        if data1.printing_received_form_56:
            temp_print.append(float(data1.printing_received_form_56))
        if data1.printing_received_form_57:
            temp_print.append(float(data1.printing_received_form_57))
        if data1.printing_received_form_58:
            temp_print.append(float(data1.printing_received_form_58))
        if data1.printing_received_form_59:
            temp_print.append(float(data1.printing_received_form_59))
        if data1.printing_received_form_60:
            temp_print.append(float(data1.printing_received_form_60))



        temp_print=[i for i in temp_print]
        print('temp_print',temp_print)
        data1.printing_received_form=0
        for i in temp_print:
            data1.printing_received_form=data1.printing_received_form+i
        print('data1.printing_received_form',data1.printing_received_form)
        
       

        
        if data1.printing_received_form:
            sum_wastage_form=0
            for i in range (1,51):
                sum_wastage_form += float(getattr(data1,f"print_wastage_form_{i}",0))
                data1.print_wastage_form = sum_wastage_form
        else:
            data1.print_wastage_form = 0
        
        data1.save()
        messages.success(request, "Updated Successfully...!!")
        if request.method == 'POST':
            if request.POST.get("print_approval") == "approval_button":
                orders.objects.filter(Q(order_id=order_id) & Q(print_approved=False)).update(print_approved=True)
                return redirect('/printing-data/')
            else:
                pass    

        # return redirect('/printing-data/')
       
    context = {'data1':data1}
    return render(request, 'processing/edit_printing.html', context)











@login_required(login_url="")
def cutting_form(request): 
    if request.method =='POST':
        id = request.POST.get('id')
        total_cutting=request.POST.get('total_cutting')
        balance_cutting = request.POST.get('balance_cutting')


        cutting_received_1=request.POST.get('cutting_received_1')
        balance_cutting_1=request.POST.get('balance_cutting_1')
        cutting_received_2=request.POST.get('cutting_received_2')
        balance_cutting_2=request.POST.get('balance_cutting_2')
        cutting_received_3=request.POST.get('cutting_received_3')
        balance_cutting_3=request.POST.get('balance_cutting_3')
        cutting_received_4=request.POST.get('cutting_received_4')
        balance_cutting_4=request.POST.get('balance_cutting_4')
        cutting_received_5=request.POST.get('cutting_received_5')
        balance_cutting_5=request.POST.get('balance_cutting_5')
        cutting_received_6=request.POST.get('cutting_received_6')
        balance_cutting_6=request.POST.get('balance_cutting_6')
        cutting_received_7=request.POST.get('cutting_received_7')
        balance_cutting_7=request.POST.get('balance_cutting_7')
        cutting_received_8=request.POST.get('cutting_received_8')
        balance_cutting_8=request.POST.get('balance_cutting_8')
        cutting_received_9=request.POST.get('cutting_received_9')
        balance_cutting_9=request.POST.get('balance_cutting_9')
        cutting_received_10=request.POST.get('cutting_received_10')
        balance_cutting_10=request.POST.get('balance_cutting_10')

        cutting_received_11=request.POST.get('cutting_received_11')
        balance_cutting_11=request.POST.get('balance_cutting_11')
        cutting_received_12=request.POST.get('cutting_received_12')
        balance_cutting_12=request.POST.get('balance_cutting_12')
        cutting_received_13=request.POST.get('cutting_received_13')
        balance_cutting_13=request.POST.get('balance_cutting_13')
        cutting_received_14=request.POST.get('cutting_received_14')
        balance_cutting_14=request.POST.get('balance_cutting_14')
        cutting_received_15=request.POST.get('cutting_received_15')
        balance_cutting_15=request.POST.get('balance_cutting_15')
        cutting_received_16=request.POST.get('cutting_received_16')
        balance_cutting_16=request.POST.get('balance_cutting_16')
        cutting_received_17=request.POST.get('cutting_received_17')
        balance_cutting_17=request.POST.get('balance_cutting_17')
        cutting_received_18=request.POST.get('cutting_received_18')
        balance_cutting_18=request.POST.get('balance_cutting_18')
        cutting_received_19=request.POST.get('cutting_received_19')
        balance_cutting_19=request.POST.get('balance_cutting_19')
        cutting_received_20=request.POST.get('cutting_received_20')
        balance_cutting_20=request.POST.get('balance_cutting_20')

        cutting_received_21=request.POST.get('cutting_received_21')
        balance_cutting_21=request.POST.get('balance_cutting_21')
        cutting_received_22=request.POST.get('cutting_received_22')
        balance_cutting_22=request.POST.get('balance_cutting_22')
        cutting_received_23=request.POST.get('cutting_received_23')
        balance_cutting_23=request.POST.get('balance_cutting_23')
        cutting_received_24=request.POST.get('cutting_received_24')
        balance_cutting_24=request.POST.get('balance_cutting_24')
        cutting_received_25=request.POST.get('cutting_received_25')
        balance_cutting_25=request.POST.get('balance_cutting_25')
        cutting_received_26=request.POST.get('cutting_received_26')
        balance_cutting_26=request.POST.get('balance_cutting_26')
        cutting_received_27=request.POST.get('cutting_received_27')
        balance_cutting_27=request.POST.get('balance_cutting_27')
        cutting_received_28=request.POST.get('cutting_received_28')
        balance_cutting_28=request.POST.get('balance_cutting_28')
        cutting_received_29=request.POST.get('cutting_received_29')
        balance_cutting_29=request.POST.get('balance_cutting_29')
        cutting_received_30=request.POST.get('cutting_received_30')
        balance_cutting_30=request.POST.get('balance_cutting_30')

        cutting_received_31=request.POST.get('cutting_received_31')
        balance_cutting_31=request.POST.get('balance_cutting_31')
        cutting_received_32=request.POST.get('cutting_received_32')
        balance_cutting_32=request.POST.get('balance_cutting_32')
        cutting_received_33=request.POST.get('cutting_received_33')
        balance_cutting_33=request.POST.get('balance_cutting_33')
        cutting_received_34=request.POST.get('cutting_received_34')
        balance_cutting_34=request.POST.get('balance_cutting_34')
        cutting_received_35=request.POST.get('cutting_received_35')
        balance_cutting_35=request.POST.get('balance_cutting_35')
        cutting_received_36=request.POST.get('cutting_received_36')
        balance_cutting_36=request.POST.get('balance_cutting_36')
        cutting_received_37=request.POST.get('cutting_received_37')
        balance_cutting_37=request.POST.get('balance_cutting_37')
        cutting_received_38=request.POST.get('cutting_received_38')
        balance_cutting_38=request.POST.get('balance_cutting_38')
        cutting_received_39=request.POST.get('cutting_received_39')
        balance_cutting_39=request.POST.get('balance_cutting_39')
        cutting_received_40=request.POST.get('cutting_received_40')
        balance_cutting_40=request.POST.get('balance_cutting_40')

        cutting_received_41=request.POST.get('cutting_received_41')
        balance_cutting_41=request.POST.get('balance_cutting_41')
        cutting_received_42=request.POST.get('cutting_received_42')
        balance_cutting_42=request.POST.get('balance_cutting_42')
        cutting_received_43=request.POST.get('cutting_received_43')
        balance_cutting_43=request.POST.get('balance_cutting_43')
        cutting_received_44=request.POST.get('cutting_received_44')
        balance_cutting_44=request.POST.get('balance_cutting_44')
        cutting_received_45=request.POST.get('cutting_received_45')
        balance_cutting_45=request.POST.get('balance_cutting_45')
        cutting_received_46=request.POST.get('cutting_received_46')
        balance_cutting_46=request.POST.get('balance_cutting_46')
        cutting_received_47=request.POST.get('cutting_received_47')
        balance_cutting_47=request.POST.get('balance_cutting_47')
        cutting_received_48=request.POST.get('cutting_received_48')
        balance_cutting_48=request.POST.get('balance_cutting_48')
        cutting_received_49=request.POST.get('cutting_received_49')
        balance_cutting_49=request.POST.get('balance_cutting_49')
        cutting_received_50=request.POST.get('cutting_received_50')
        balance_cutting_50=request.POST.get('balance_cutting_50')

        cutting_date = request.POST.get('cutting_date')
        order = orders.objects.filter(order_id=id).get()
        print('order',order)
        order.cutting_received_1=cutting_received_1
        order.balance_cutting_1=balance_cutting_1
        order.cutting_received_2=cutting_received_2
        order.balance_cutting_2=balance_cutting_2
        order.cutting_received_3=cutting_received_3
        order.balance_cutting_3=balance_cutting_3
        order.cutting_received_4=cutting_received_4
        order.balance_cutting_4=balance_cutting_4
        order.cutting_received_5=cutting_received_5
        order.balance_cutting_5=balance_cutting_5
        order.cutting_received_6=cutting_received_6
        order.balance_cutting_6=balance_cutting_6
        order.cutting_received_7=cutting_received_7
        order.balance_cutting_7=balance_cutting_7
        order.cutting_received_8=cutting_received_8
        order.balance_cutting_8=balance_cutting_8
        order.cutting_received_9=cutting_received_9
        order.balance_cutting_9=balance_cutting_9
        order.cutting_received_10=cutting_received_10
        order.balance_cutting_10=balance_cutting_10

        order.cutting_received_11=cutting_received_11
        order.balance_cutting_11=balance_cutting_11
        order.cutting_received_12=cutting_received_12
        order.balance_cutting_12=balance_cutting_12
        order.cutting_received_13=cutting_received_13
        order.balance_cutting_13=balance_cutting_13
        order.cutting_received_14=cutting_received_14
        order.balance_cutting_14=balance_cutting_14
        order.cutting_received_15=cutting_received_15
        order.balance_cutting_15=balance_cutting_15
        order.cutting_received_16=cutting_received_16
        order.balance_cutting_16=balance_cutting_16
        order.cutting_received_17=cutting_received_17
        order.balance_cutting_17=balance_cutting_17
        order.cutting_received_18=cutting_received_18
        order.balance_cutting_18=balance_cutting_18
        order.cutting_received_19=cutting_received_19
        order.balance_cutting_19=balance_cutting_19
        order.cutting_received_20=cutting_received_20
        order.balance_cutting_20=balance_cutting_20

        order.cutting_received_21=cutting_received_21
        order.balance_cutting_21=balance_cutting_21
        order.cutting_received_22=cutting_received_22
        order.balance_cutting_22=balance_cutting_22
        order.cutting_received_23=cutting_received_23
        order.balance_cutting_23=balance_cutting_23
        order.cutting_received_24=cutting_received_24
        order.balance_cutting_24=balance_cutting_24
        order.cutting_received_25=cutting_received_25
        order.balance_cutting_25=balance_cutting_25
        order.cutting_received_26=cutting_received_26
        order.balance_cutting_26=balance_cutting_26
        order.cutting_received_27=cutting_received_27
        order.balance_cutting_27=balance_cutting_27
        order.cutting_received_28=cutting_received_28
        order.balance_cutting_28=balance_cutting_28
        order.cutting_received_29=cutting_received_29
        order.balance_cutting_29=balance_cutting_29
        order.cutting_received_30=cutting_received_30
        order.balance_cutting_30=balance_cutting_30

        order.cutting_received_31=cutting_received_31
        order.balance_cutting_31=balance_cutting_31
        order.cutting_received_32=cutting_received_32
        order.balance_cutting_32=balance_cutting_32
        order.cutting_received_33=cutting_received_33
        order.balance_cutting_33=balance_cutting_33
        order.cutting_received_34=cutting_received_34
        order.balance_cutting_34=balance_cutting_34
        order.cutting_received_35=cutting_received_35
        order.balance_cutting_35=balance_cutting_35
        order.cutting_received_36=cutting_received_36
        order.balance_cutting_36=balance_cutting_36
        order.cutting_received_37=cutting_received_37
        order.balance_cutting_37=balance_cutting_37
        order.cutting_received_38=cutting_received_38
        order.balance_cutting_38=balance_cutting_38
        order.cutting_received_39=cutting_received_39
        order.balance_cutting_39=balance_cutting_39
        order.cutting_received_40=cutting_received_40
        order.balance_cutting_40=balance_cutting_40

        order.cutting_received_41=cutting_received_41
        order.balance_cutting_41=balance_cutting_41
        order.cutting_received_42=cutting_received_42
        order.balance_cutting_42=balance_cutting_42
        order.cutting_received_43=cutting_received_43
        order.balance_cutting_43=balance_cutting_43
        order.cutting_received_44=cutting_received_44
        order.balance_cutting_44=balance_cutting_44
        order.cutting_received_45=cutting_received_45
        order.balance_cutting_45=balance_cutting_45
        order.cutting_received_46=cutting_received_46
        order.balance_cutting_46=balance_cutting_46
        order.cutting_received_47=cutting_received_47
        order.balance_cutting_47=balance_cutting_47
        order.cutting_received_48=cutting_received_48
        order.balance_cutting_48=balance_cutting_48
        order.cutting_received_49=cutting_received_49
        order.balance_cutting_49=balance_cutting_49
        order.cutting_received_50=cutting_received_50
        order.balance_cutting_50=balance_cutting_50

        


        order.total_cutting=total_cutting
        order.balance_cutting=balance_cutting
        order.cutting_date=datetime.datetime.now()
        order.save()
    
    data1 = orders.objects.all().order_by('-order_id')    
    context={
        'data1':data1,       
    }
    return render(request,'processing/cutting.html',context)



@login_required(login_url="")
def edit_cutting(request, order_id):
    data1 = orders.objects.get(order_id=order_id)
    print('gjhgjmgj',order_id)

    if request.method == 'POST':
        data1.total_cutting = request.POST.get('total_cutting')

        data1.cutting_received_1=request.POST.get('cutting_received_1')
        data1.cutting_received_2=request.POST.get('cutting_received_2')
        data1.cutting_received_3=request.POST.get('cutting_received_3')
        data1.cutting_received_4=request.POST.get('cutting_received_4')
        data1.cutting_received_5=request.POST.get('cutting_received_5')
        data1.cutting_received_6=request.POST.get('cutting_received_6')
        data1.cutting_received_7=request.POST.get('cutting_received_7')
        data1.cutting_received_8=request.POST.get('cutting_received_8')
        data1.cutting_received_9=request.POST.get('cutting_received_9')
        data1.cutting_received_10=request.POST.get('cutting_received_10')

        data1.cutting_received_11=request.POST.get('cutting_received_11')
        data1.cutting_received_12=request.POST.get('cutting_received_12')
        data1.cutting_received_13=request.POST.get('cutting_received_13')
        data1.cutting_received_14=request.POST.get('cutting_received_14')
        data1.cutting_received_15=request.POST.get('cutting_received_15')
        data1.cutting_received_16=request.POST.get('cutting_received_16')
        data1.cutting_received_17=request.POST.get('cutting_received_17')
        data1.cutting_received_18=request.POST.get('cutting_received_18')
        data1.cutting_received_19=request.POST.get('cutting_received_19')
        data1.cutting_received_20=request.POST.get('cutting_received_20')

        data1.cutting_received_21=request.POST.get('cutting_received_21')
        data1.cutting_received_22=request.POST.get('cutting_received_22')
        data1.cutting_received_23=request.POST.get('cutting_received_23')
        data1.cutting_received_24=request.POST.get('cutting_received_24')
        data1.cutting_received_25=request.POST.get('cutting_received_25')
        data1.cutting_received_26=request.POST.get('cutting_received_26')
        data1.cutting_received_27=request.POST.get('cutting_received_27')
        data1.cutting_received_28=request.POST.get('cutting_received_28')
        data1.cutting_received_29=request.POST.get('cutting_received_29')
        data1.cutting_received_30=request.POST.get('cutting_received_30')

        data1.cutting_received_31=request.POST.get('cutting_received_31')
        data1.cutting_received_32=request.POST.get('cutting_received_32')
        data1.cutting_received_33=request.POST.get('cutting_received_33')
        data1.cutting_received_34=request.POST.get('cutting_received_34')
        data1.cutting_received_35=request.POST.get('cutting_received_35')
        data1.cutting_received_36=request.POST.get('cutting_received_36')
        data1.cutting_received_37=request.POST.get('cutting_received_37')
        data1.cutting_received_38=request.POST.get('cutting_received_38')
        data1.cutting_received_39=request.POST.get('cutting_received_39')
        data1.cutting_received_40=request.POST.get('cutting_received_40')

        data1.cutting_received_41=request.POST.get('cutting_received_41')
        data1.cutting_received_42=request.POST.get('cutting_received_42')
        data1.cutting_received_43=request.POST.get('cutting_received_43')
        data1.cutting_received_44=request.POST.get('cutting_received_44')
        data1.cutting_received_45=request.POST.get('cutting_received_45')
        data1.cutting_received_46=request.POST.get('cutting_received_46')
        data1.cutting_received_47=request.POST.get('cutting_received_47')
        data1.cutting_received_48=request.POST.get('cutting_received_48')
        data1.cutting_received_49=request.POST.get('cutting_received_49')
        data1.cutting_received_50=request.POST.get('cutting_received_50')
    
        data1.cutting_date = datetime.datetime.now()
        
        if data1.cutting_received_1:
            data1.balance_cutting_1 = float(data1.quantity_1) - float(data1.cutting_received_1)
        else:
            data1.cutting_received_1 = 0
        
        if data1.cutting_received_2:
            data1.balance_cutting_2 = float(data1.quantity_2) - float(data1.cutting_received_2)
        else:
            data1.cutting_received_2 = 0

        if data1.cutting_received_3:
            data1.balance_cutting_3 = float(data1.quantity_3) - float(data1.cutting_received_3)
        else:
            data1.cutting_received_3 = 0

        if data1.cutting_received_4:
            data1.balance_cutting_4 = float(data1.quantity_4) - float(data1.cutting_received_4)
        else:
            data1.cutting_received_4 = 0

        if data1.cutting_received_5:
            data1.balance_cutting_5 = float(data1.quantity_5) - float(data1.cutting_received_5)
        else:
            data1.cutting_received_5 = 0

        if data1.cutting_received_6:
            data1.balance_cutting_6 = float(data1.quantity_6) - float(data1.cutting_received_6)
        else:
            data1.cutting_received_6 = 0

        if data1.cutting_received_7:
            data1.balance_cutting_7 = float(data1.quantity_7) - float(data1.cutting_received_7)
        else:
            data1.cutting_received_7 = 0

        if data1.cutting_received_8:
            data1.balance_cutting_8 = float(data1.quantity_8) - float(data1.cutting_received_8)
        else:
            data1.cutting_received_8 = 0

        if data1.cutting_received_9:
            data1.balance_cutting_9 = float(data1.quantity_9) - float(data1.cutting_received_9)
        else:
            data1.cutting_received_9 = 0

        if data1.cutting_received_10:
            data1.balance_cutting_10 = float(data1.quantity_10) - float(data1.cutting_received_10)
        else:
            data1.cutting_received_10 = 0


        if data1.cutting_received_11:
            data1.balance_cutting_11 = float(data1.quantity_11) - float(data1.cutting_received_11)
        else:
            data1.cutting_received_11 = 0
        
        if data1.cutting_received_12:
            data1.balance_cutting_12 = float(data1.quantity_12) - float(data1.cutting_received_12)
        else:
            data1.cutting_received_12 = 0

        if data1.cutting_received_13:
            data1.balance_cutting_13 = float(data1.quantity_13) - float(data1.cutting_received_13)
        else:
            data1.cutting_received_13 = 0

        if data1.cutting_received_14:
            data1.balance_cutting_14 = float(data1.quantity_14) - float(data1.cutting_received_14)
        else:
            data1.cutting_received_14 = 0

        if data1.cutting_received_15:
            data1.balance_cutting_15 = float(data1.quantity_15) - float(data1.cutting_received_15)
        else:
            data1.cutting_received_15 = 0

        if data1.cutting_received_16:
            data1.balance_cutting_16 = float(data1.quantity_16) - float(data1.cutting_received_16)
        else:
            data1.cutting_received_16 = 0

        if data1.cutting_received_17:
            data1.balance_cutting_17 = float(data1.quantity_17) - float(data1.cutting_received_17)
        else:
            data1.cutting_received_17 = 0

        if data1.cutting_received_18:
            data1.balance_cutting_18 = float(data1.quantity_18) - float(data1.cutting_received_18)
        else:
            data1.cutting_received_18 = 0

        if data1.cutting_received_19:
            data1.balance_cutting_19 = float(data1.quantity_19) - float(data1.cutting_received_19)
        else:
            data1.cutting_received_19 = 0

        if data1.cutting_received_20:
            data1.balance_cutting_20 = float(data1.quantity_20) - float(data1.cutting_received_20)
        else:
            data1.cutting_received_20 = 0


        if data1.cutting_received_21:
            data1.balance_cutting_21 = float(data1.quantity_21) - float(data1.cutting_received_21)
        else:
            data1.cutting_received_21 = 0
        
        if data1.cutting_received_22:
            data1.balance_cutting_22 = float(data1.quantity_22) - float(data1.cutting_received_22)
        else:
            data1.cutting_received_22 = 0

        if data1.cutting_received_23:
            data1.balance_cutting_23 = float(data1.quantity_23) - float(data1.cutting_received_23)
        else:
            data1.cutting_received_23 = 0

        if data1.cutting_received_24:
            data1.balance_cutting_24 = float(data1.quantity_24) - float(data1.cutting_received_24)
        else:
            data1.cutting_received_24 = 0

        if data1.cutting_received_25:
            data1.balance_cutting_25 = float(data1.quantity_25) - float(data1.cutting_received_25)
        else:
            data1.cutting_received_25 = 0

        if data1.cutting_received_26:
            data1.balance_cutting_26 = float(data1.quantity_26) - float(data1.cutting_received_26)
        else:
            data1.cutting_received_26 = 0

        if data1.cutting_received_27:
            data1.balance_cutting_27 = float(data1.quantity_27) - float(data1.cutting_received_27)
        else:
            data1.cutting_received_27 = 0

        if data1.cutting_received_28:
            data1.balance_cutting_28 = float(data1.quantity_28) - float(data1.cutting_received_28)
        else:
            data1.cutting_received_28 = 0

        if data1.cutting_received_29:
            data1.balance_cutting_29 = float(data1.quantity_29) - float(data1.cutting_received_29)
        else:
            data1.cutting_received_29 = 0

        if data1.cutting_received_30:
            data1.balance_cutting_30 = float(data1.quantity_30) - float(data1.cutting_received_30)
        else:
            data1.cutting_received_30 = 0


        if data1.cutting_received_31:
            data1.balance_cutting_31 = float(data1.quantity_31) - float(data1.cutting_received_31)
        else:
            data1.cutting_received_31 = 0
        
        if data1.cutting_received_32:
            data1.balance_cutting_32 = float(data1.quantity_32) - float(data1.cutting_received_32)
        else:
            data1.cutting_received_32 = 0

        if data1.cutting_received_33:
            data1.balance_cutting_33 = float(data1.quantity_33) - float(data1.cutting_received_33)
        else:
            data1.cutting_received_33 = 0

        if data1.cutting_received_34:
            data1.balance_cutting_34 = float(data1.quantity_34) - float(data1.cutting_received_34)
        else:
            data1.cutting_received_34 = 0

        if data1.cutting_received_35:
            data1.balance_cutting_35 = float(data1.quantity_35) - float(data1.cutting_received_35)
        else:
            data1.cutting_received_35 = 0

        if data1.cutting_received_36:
            data1.balance_cutting_36 = float(data1.quantity_36) - float(data1.cutting_received_36)
        else:
            data1.cutting_received_36 = 0

        if data1.cutting_received_37:
            data1.balance_cutting_37 = float(data1.quantity_37) - float(data1.cutting_received_37)
        else:
            data1.cutting_received_37 = 0

        if data1.cutting_received_38:
            data1.balance_cutting_38 = float(data1.quantity_38) - float(data1.cutting_received_38)
        else:
            data1.cutting_received_38 = 0

        if data1.cutting_received_39:
            data1.balance_cutting_39 = float(data1.quantity_39) - float(data1.cutting_received_39)
        else:
            data1.cutting_received_39 = 0

        if data1.cutting_received_40:
            data1.balance_cutting_40 = float(data1.quantity_40) - float(data1.cutting_received_40)
        else:
            data1.cutting_received_40 = 0


        if data1.cutting_received_41:
            data1.balance_cutting_41 = float(data1.quantity_41) - float(data1.cutting_received_41)
        else:
            data1.cutting_received_41 = 0
        
        if data1.cutting_received_42:
            data1.balance_cutting_42 = float(data1.quantity_42) - float(data1.cutting_received_42)
        else:
            data1.cutting_received_42 = 0

        if data1.cutting_received_43:
            data1.balance_cutting_43 = float(data1.quantity_43) - float(data1.cutting_received_43)
        else:
            data1.cutting_received_43 = 0

        if data1.cutting_received_44:
            data1.balance_cutting_44 = float(data1.quantity_44) - float(data1.cutting_received_44)
        else:
            data1.cutting_received_44 = 0

        if data1.cutting_received_45:
            data1.balance_cutting_45 = float(data1.quantity_45) - float(data1.cutting_received_45)
        else:
            data1.cutting_received_45 = 0

        if data1.cutting_received_46:
            data1.balance_cutting_46 = float(data1.quantity_46) - float(data1.cutting_received_46)
        else:
            data1.cutting_received_46 = 0

        if data1.cutting_received_47:
            data1.balance_cutting_47 = float(data1.quantity_47) - float(data1.cutting_received_47)
        else:
            data1.cutting_received_47 = 0

        if data1.cutting_received_48:
            data1.balance_cutting_48 = float(data1.quantity_48) - float(data1.cutting_received_48)
        else:
            data1.cutting_received_48 = 0

        if data1.cutting_received_49:
            data1.balance_cutting_49 = float(data1.quantity_49) - float(data1.cutting_received_49)
        else:
            data1.cutting_received_49 = 0

        if data1.cutting_received_50:
            data1.balance_cutting_50 = float(data1.quantity_50) - float(data1.cutting_received_50)
        else:
            data1.cutting_received_50 = 0

        

        temp_cut=[]
        if data1.cutting_received_1:
            temp_cut.append(int(data1.cutting_received_1))
        if data1.cutting_received_2:
            temp_cut.append(int(data1.cutting_received_2))
        if data1.cutting_received_3:
            temp_cut.append(int(data1.cutting_received_3))
        if data1.cutting_received_4:
            temp_cut.append(int(data1.cutting_received_4))
        if data1.cutting_received_5:
            temp_cut.append(int(data1.cutting_received_5))
        if data1.cutting_received_6:
            temp_cut.append(int(data1.cutting_received_6))
        if data1.cutting_received_7:
            temp_cut.append(int(data1.cutting_received_7))
        if data1.cutting_received_8:
            temp_cut.append(int(data1.cutting_received_8))
        if data1.cutting_received_9:
            temp_cut.append(int(data1.cutting_received_9))
        if data1.cutting_received_10:
            temp_cut.append(int(data1.cutting_received_10))

        if data1.cutting_received_11:
            temp_cut.append(int(data1.cutting_received_11))
        if data1.cutting_received_12:
            temp_cut.append(int(data1.cutting_received_12))
        if data1.cutting_received_13:
            temp_cut.append(int(data1.cutting_received_13))
        if data1.cutting_received_14:
            temp_cut.append(int(data1.cutting_received_14))
        if data1.cutting_received_15:
            temp_cut.append(int(data1.cutting_received_15))
        if data1.cutting_received_16:
            temp_cut.append(int(data1.cutting_received_16))
        if data1.cutting_received_17:
            temp_cut.append(int(data1.cutting_received_17))
        if data1.cutting_received_18:
            temp_cut.append(int(data1.cutting_received_18))
        if data1.cutting_received_19:
            temp_cut.append(int(data1.cutting_received_19))
        if data1.cutting_received_20:
            temp_cut.append(int(data1.cutting_received_20))

        if data1.cutting_received_21:
            temp_cut.append(int(data1.cutting_received_21))
        if data1.cutting_received_22:
            temp_cut.append(int(data1.cutting_received_22))
        if data1.cutting_received_23:
            temp_cut.append(int(data1.cutting_received_23))
        if data1.cutting_received_24:
            temp_cut.append(int(data1.cutting_received_24))
        if data1.cutting_received_25:
            temp_cut.append(int(data1.cutting_received_25))
        if data1.cutting_received_26:
            temp_cut.append(int(data1.cutting_received_26))
        if data1.cutting_received_27:
            temp_cut.append(int(data1.cutting_received_27))
        if data1.cutting_received_28:
            temp_cut.append(int(data1.cutting_received_28))
        if data1.cutting_received_29:
            temp_cut.append(int(data1.cutting_received_29))
        if data1.cutting_received_30:
            temp_cut.append(int(data1.cutting_received_30))

        if data1.cutting_received_31:
            temp_cut.append(int(data1.cutting_received_31))
        if data1.cutting_received_32:
            temp_cut.append(int(data1.cutting_received_32))
        if data1.cutting_received_33:
            temp_cut.append(int(data1.cutting_received_33))
        if data1.cutting_received_34:
            temp_cut.append(int(data1.cutting_received_34))
        if data1.cutting_received_35:
            temp_cut.append(int(data1.cutting_received_35))
        if data1.cutting_received_36:
            temp_cut.append(int(data1.cutting_received_36))
        if data1.cutting_received_37:
            temp_cut.append(int(data1.cutting_received_37))
        if data1.cutting_received_38:
            temp_cut.append(int(data1.cutting_received_38))
        if data1.cutting_received_39:
            temp_cut.append(int(data1.cutting_received_39))
        if data1.cutting_received_40:
            temp_cut.append(int(data1.cutting_received_40))

        if data1.cutting_received_41:
            temp_cut.append(int(data1.cutting_received_41))
        if data1.cutting_received_42:
            temp_cut.append(int(data1.cutting_received_42))
        if data1.cutting_received_43:
            temp_cut.append(int(data1.cutting_received_43))
        if data1.cutting_received_44:
            temp_cut.append(int(data1.cutting_received_44))
        if data1.cutting_received_45:
            temp_cut.append(int(data1.cutting_received_45))
        if data1.cutting_received_46:
            temp_cut.append(int(data1.cutting_received_46))
        if data1.cutting_received_47:
            temp_cut.append(int(data1.cutting_received_47))
        if data1.cutting_received_48:
            temp_cut.append(int(data1.cutting_received_48))
        if data1.cutting_received_49:
            temp_cut.append(int(data1.cutting_received_49))
        if data1.cutting_received_50:
            temp_cut.append(int(data1.cutting_received_50))

        
        temp_cut=[i for i in temp_cut]
        data1.total_cutting=0
        for i in temp_cut:
            data1.total_cutting=data1.total_cutting+i
        

        if data1.total_cutting:
            data1.balance_cutting = float(data1.total_quantity) - float(data1.total_cutting)
        else:
            data1.balance_cutting = 0
        
        data1.save()
        messages.success(request, "Updated Successfully...!!")
        return redirect('/cutting-data/')
       
    context = {'data1':data1}
    return render(request, 'processing/edit_cutting.html', context)






 




@login_required(login_url="")
def binding_data(request):
    if request.method =='POST':
        id = request.POST.get('id')
        total_binding=request.POST.get('total_binding')
        balance_binding = request.POST.get('balance_binding')

        binding_received_1=request.POST.get('binding_received_1')
        balance_binding_1=request.POST.get('balance_binding_1')
        binding_received_2=request.POST.get('binding_received_2')
        balance_binding_2=request.POST.get('balance_binding_2')
        binding_received_3=request.POST.get('binding_received_3')
        balance_binding_3=request.POST.get('balance_binding_3')
        binding_received_4=request.POST.get('binding_received_4')
        balance_binding_4=request.POST.get('balance_binding_4')
        binding_received_5=request.POST.get('binding_received_5')
        balance_binding_5=request.POST.get('balance_binding_5')
        binding_received_6=request.POST.get('binding_received_6')
        balance_binding_6=request.POST.get('balance_binding_6')
        binding_received_7=request.POST.get('binding_received_7')
        balance_binding_7=request.POST.get('balance_binding_7')
        binding_received_8=request.POST.get('binding_received_8')
        balance_binding_8=request.POST.get('balance_binding_8')
        binding_received_9=request.POST.get('binding_received_9')
        balance_binding_9=request.POST.get('balance_binding_9')
        binding_received_10=request.POST.get('binding_received_10')
        balance_binding_10=request.POST.get('balance_binding_10')

        binding_received_11=request.POST.get('binding_received_11')
        balance_binding_11=request.POST.get('balance_binding_11')
        binding_received_12=request.POST.get('binding_received_12')
        balance_binding_12=request.POST.get('balance_binding_12')
        binding_received_13=request.POST.get('binding_received_13')
        balance_binding_13=request.POST.get('balance_binding_13')
        binding_received_14=request.POST.get('binding_received_14')
        balance_binding_14=request.POST.get('balance_binding_14')
        binding_received_15=request.POST.get('binding_received_15')
        balance_binding_15=request.POST.get('balance_binding_15')
        binding_received_16=request.POST.get('binding_received_16')
        balance_binding_16=request.POST.get('balance_binding_16')
        binding_received_17=request.POST.get('binding_received_17')
        balance_binding_17=request.POST.get('balance_binding_17')
        binding_received_18=request.POST.get('binding_received_18')
        balance_binding_18=request.POST.get('balance_binding_18')
        binding_received_19=request.POST.get('binding_received_19')
        balance_binding_19=request.POST.get('balance_binding_19')
        binding_received_20=request.POST.get('binding_received_20')
        balance_binding_20=request.POST.get('balance_binding_20')

        binding_received_21=request.POST.get('binding_received_21')
        balance_binding_21=request.POST.get('balance_binding_21')
        binding_received_22=request.POST.get('binding_received_22')
        balance_binding_22=request.POST.get('balance_binding_22')
        binding_received_23=request.POST.get('binding_received_23')
        balance_binding_23=request.POST.get('balance_binding_23')
        binding_received_24=request.POST.get('binding_received_24')
        balance_binding_24=request.POST.get('balance_binding_24')
        binding_received_25=request.POST.get('binding_received_25')
        balance_binding_25=request.POST.get('balance_binding_25')
        binding_received_26=request.POST.get('binding_received_26')
        balance_binding_26=request.POST.get('balance_binding_26')
        binding_received_27=request.POST.get('binding_received_27')
        balance_binding_27=request.POST.get('balance_binding_27')
        binding_received_28=request.POST.get('binding_received_28')
        balance_binding_28=request.POST.get('balance_binding_28')
        binding_received_29=request.POST.get('binding_received_29')
        balance_binding_29=request.POST.get('balance_binding_29')
        binding_received_30=request.POST.get('binding_received_30')
        balance_binding_30=request.POST.get('balance_binding_30')

        binding_received_31=request.POST.get('binding_received_31')
        balance_binding_31=request.POST.get('balance_binding_31')
        binding_received_32=request.POST.get('binding_received_32')
        balance_binding_32=request.POST.get('balance_binding_32')
        binding_received_33=request.POST.get('binding_received_33')
        balance_binding_33=request.POST.get('balance_binding_33')
        binding_received_34=request.POST.get('binding_received_34')
        balance_binding_34=request.POST.get('balance_binding_34')
        binding_received_35=request.POST.get('binding_received_35')
        balance_binding_35=request.POST.get('balance_binding_35')
        binding_received_36=request.POST.get('binding_received_36')
        balance_binding_36=request.POST.get('balance_binding_36')
        binding_received_37=request.POST.get('binding_received_37')
        balance_binding_37=request.POST.get('balance_binding_37')
        binding_received_38=request.POST.get('binding_received_38')
        balance_binding_38=request.POST.get('balance_binding_38')
        binding_received_39=request.POST.get('binding_received_39')
        balance_binding_39=request.POST.get('balance_binding_39')
        binding_received_40=request.POST.get('binding_received_40')
        balance_binding_40=request.POST.get('balance_binding_40')

        binding_received_41=request.POST.get('binding_received_41')
        balance_binding_41=request.POST.get('balance_binding_41')
        binding_received_42=request.POST.get('binding_received_42')
        balance_binding_42=request.POST.get('balance_binding_42')
        binding_received_43=request.POST.get('binding_received_43')
        balance_binding_43=request.POST.get('balance_binding_43')
        binding_received_44=request.POST.get('binding_received_44')
        balance_binding_44=request.POST.get('balance_binding_44')
        binding_received_45=request.POST.get('binding_received_45')
        balance_binding_45=request.POST.get('balance_binding_45')
        binding_received_46=request.POST.get('binding_received_46')
        balance_binding_46=request.POST.get('balance_binding_46')
        binding_received_47=request.POST.get('binding_received_47')
        balance_binding_47=request.POST.get('balance_binding_47')
        binding_received_48=request.POST.get('binding_received_48')
        balance_binding_48=request.POST.get('balance_binding_48')
        binding_received_49=request.POST.get('binding_received_49')
        balance_binding_49=request.POST.get('balance_binding_49')
        binding_received_50=request.POST.get('binding_received_50')
        balance_binding_50=request.POST.get('balance_binding_50')
        binding_date = request.POST.get('print_date')

        order = orders.objects.filter(order_id=id).get()
        print('order',order)
        order.binding_received_1=binding_received_1
        order.balance_binding_1=balance_binding_1
        order.binding_received_2=binding_received_2
        order.balance_binding_2=balance_binding_2
        order.binding_received_3=binding_received_3
        order.balance_binding_3=balance_binding_3
        order.binding_received_4=binding_received_4
        order.balance_binding_4=balance_binding_4
        order.binding_received_5=binding_received_5
        order.balance_binding_5=balance_binding_5
        order.binding_received_6=binding_received_6
        order.balance_binding_6=balance_binding_6
        order.binding_received_7=binding_received_7
        order.balance_binding_7=balance_binding_7
        order.binding_received_8=binding_received_8
        order.balance_binding_8=balance_binding_8
        order.binding_received_9=binding_received_9
        order.balance_binding_9=balance_binding_9
        order.binding_received_10=binding_received_10
        order.balance_binding_10=balance_binding_10

        order.binding_received_11=binding_received_11
        order.balance_binding_11=balance_binding_11
        order.binding_received_12=binding_received_12
        order.balance_binding_12=balance_binding_12
        order.binding_received_13=binding_received_13
        order.balance_binding_13=balance_binding_13
        order.binding_received_14=binding_received_14
        order.balance_binding_14=balance_binding_14
        order.binding_received_15=binding_received_15
        order.balance_binding_15=balance_binding_15
        order.binding_received_16=binding_received_16
        order.balance_binding_16=balance_binding_16
        order.binding_received_17=binding_received_17
        order.balance_binding_17=balance_binding_17
        order.binding_received_18=binding_received_18
        order.balance_binding_18=balance_binding_18
        order.binding_received_19=binding_received_19
        order.balance_binding_19=balance_binding_19
        order.binding_received_20=binding_received_20
        order.balance_binding_20=balance_binding_20

        order.binding_received_21=binding_received_21
        order.balance_binding_21=balance_binding_21
        order.binding_received_22=binding_received_22
        order.balance_binding_22=balance_binding_22
        order.binding_received_23=binding_received_23
        order.balance_binding_23=balance_binding_23
        order.binding_received_24=binding_received_24
        order.balance_binding_24=balance_binding_24
        order.binding_received_25=binding_received_25
        order.balance_binding_25=balance_binding_25
        order.binding_received_26=binding_received_26
        order.balance_binding_26=balance_binding_26
        order.binding_received_27=binding_received_27
        order.balance_binding_27=balance_binding_27
        order.binding_received_28=binding_received_28
        order.balance_binding_28=balance_binding_28
        order.binding_received_29=binding_received_29
        order.balance_binding_29=balance_binding_29
        order.binding_received_30=binding_received_30
        order.balance_binding_30=balance_binding_30

        order.binding_received_31=binding_received_31
        order.balance_binding_31=balance_binding_31
        order.binding_received_32=binding_received_32
        order.balance_binding_32=balance_binding_32
        order.binding_received_33=binding_received_33
        order.balance_binding_33=balance_binding_33
        order.binding_received_34=binding_received_34
        order.balance_binding_34=balance_binding_34
        order.binding_received_35=binding_received_35
        order.balance_binding_35=balance_binding_35
        order.binding_received_36=binding_received_36
        order.balance_binding_36=balance_binding_36
        order.binding_received_37=binding_received_37
        order.balance_binding_37=balance_binding_37
        order.binding_received_38=binding_received_38
        order.balance_binding_38=balance_binding_38
        order.binding_received_39=binding_received_39
        order.balance_binding_39=balance_binding_39
        order.binding_received_40=binding_received_40
        order.balance_binding_40=balance_binding_40

        order.binding_received_41=binding_received_41
        order.balance_binding_41=balance_binding_41
        order.binding_received_42=binding_received_42
        order.balance_binding_42=balance_binding_42
        order.binding_received_43=binding_received_43
        order.balance_binding_43=balance_binding_43
        order.binding_received_44=binding_received_44
        order.balance_binding_44=balance_binding_44
        order.binding_received_45=binding_received_45
        order.balance_binding_45=balance_binding_45
        order.binding_received_46=binding_received_46
        order.balance_binding_46=balance_binding_46
        order.binding_received_47=binding_received_47
        order.balance_binding_47=balance_binding_47
        order.binding_received_48=binding_received_48
        order.balance_binding_48=balance_binding_48
        order.binding_received_49=binding_received_49
        order.balance_binding_49=balance_binding_49
        order.binding_received_50=binding_received_50
        order.balance_binding_50=balance_binding_50

        order.total_binding=total_binding
        order.balance_binding=balance_binding 
        order.binding_date=datetime.datetime.now()
        order.save()

    data1 = orders.objects.all().order_by('-order_id')    
    context={
        'data1':data1,       
    }
    return render(request,'processing/bindings.html',context) 




@login_required(login_url="")
def edit_binding(request,order_id):
    data2 = orders.objects.get(order_id=order_id)
    print('gjhgjmgj',order_id)

    if request.method == 'POST':
        id = request.POST.get('id')
        data2.total_binding=request.POST.get('total_binding')
        data2.balance_binding = request.POST.get('balance_binding')

        data2.binding_received_1=request.POST.get('binding_received_1')
        data2.binding_received_2=request.POST.get('binding_received_2')
        data2.binding_received_3=request.POST.get('binding_received_3')
        data2.binding_received_4=request.POST.get('binding_received_4')
        data2.binding_received_5=request.POST.get('binding_received_5')
        data2.binding_received_6=request.POST.get('binding_received_6')
        data2.binding_received_7=request.POST.get('binding_received_7')
        data2.binding_received_8=request.POST.get('binding_received_8')
        data2.binding_received_9=request.POST.get('binding_received_9')
        data2.binding_received_10=request.POST.get('binding_received_10')
    

        data2.binding_received_11=request.POST.get('binding_received_11')
        data2.binding_received_12=request.POST.get('binding_received_12')
        data2.binding_received_13=request.POST.get('binding_received_13')
        data2.binding_received_14=request.POST.get('binding_received_14')
        data2.binding_received_15=request.POST.get('binding_received_15')
        data2.binding_received_16=request.POST.get('binding_received_16')
        data2.binding_received_17=request.POST.get('binding_received_17')
        data2.binding_received_18=request.POST.get('binding_received_18')
        data2.binding_received_19=request.POST.get('binding_received_19')
        data2.binding_received_20=request.POST.get('binding_received_20')
        

        data2.binding_received_21=request.POST.get('binding_received_21')
        data2.binding_received_22=request.POST.get('binding_received_22')
        data2.binding_received_23=request.POST.get('binding_received_23')
        data2.binding_received_24=request.POST.get('binding_received_24')
        data2.binding_received_25=request.POST.get('binding_received_25')
        data2.binding_received_26=request.POST.get('binding_received_26')
        data2.binding_received_27=request.POST.get('binding_received_27')
        data2.binding_received_28=request.POST.get('binding_received_28')
        data2.binding_received_29=request.POST.get('binding_received_29')
        data2.binding_received_30=request.POST.get('binding_received_30')
        

        data2.binding_received_31=request.POST.get('binding_received_31')
        data2.binding_received_32=request.POST.get('binding_received_32')
        data2.binding_received_33=request.POST.get('binding_received_33')
        data2.binding_received_34=request.POST.get('binding_received_34')
        data2.binding_received_35=request.POST.get('binding_received_35')
        data2.binding_received_36=request.POST.get('binding_received_36')
        data2.binding_received_37=request.POST.get('binding_received_37')
        data2.binding_received_38=request.POST.get('binding_received_38')
        data2.binding_received_39=request.POST.get('binding_received_39')
        data2.binding_received_40=request.POST.get('binding_received_40')
        

        data2.binding_received_41=request.POST.get('binding_received_41')
        data2.binding_received_42=request.POST.get('binding_received_42')
        data2.binding_received_43=request.POST.get('binding_received_43')
        data2.binding_received_44=request.POST.get('binding_received_44')
        data2.binding_received_45=request.POST.get('binding_received_45')
        data2.binding_received_46=request.POST.get('binding_received_46')
        data2.binding_received_47=request.POST.get('binding_received_47')
        data2.binding_received_48=request.POST.get('binding_received_48')
        data2.binding_received_49=request.POST.get('binding_received_49')
        data2.binding_received_40=request.POST.get('binding_received_50')
        

        
        data2.binding_date = datetime.datetime.now()

        if data2.binding_received_1:
            data2.balance_binding_1 = float(data2.quantity_1) - float(data2.binding_received_1)
        else:
            data2.balance_binding_1 = 0
        
        if data2.binding_received_2:
            data2.balance_binding_2 = float(data2.quantity_2) - float(data2.binding_received_2)
        else:
            data2.balance_binding_2 = 0
        
        if data2.binding_received_3:
            data2.balance_binding_3 = float(data2.quantity_3) - float(data2.binding_received_3)
        else:
            data2.balance_binding_3 = 0
        
        if data2.binding_received_4:
            data2.balance_binding_4 = float(data2.quantity_4) - float(data2.binding_received_4)
        else:
            data2.balance_binding_4 = 0
        
        if data2.binding_received_5:
            data2.balance_binding_5 = float(data2.quantity_5) - float(data2.binding_received_5)
        else:
            data2.balance_binding_5 = 0
        
        if data2.binding_received_6:
            data2.balance_binding_6 = float(data2.quantity_6) - float(data2.binding_received_6)
        else:
            data2.balance_binding_6 = 0
        
        if data2.binding_received_7:
            data2.balance_binding_7 = float(data2.quantity_7) - float(data2.binding_received_7)
        else:
            data2.balance_binding_7 = 0
        
        if data2.binding_received_8:
            data2.balance_binding_8 = float(data2.quantity_8) - float(data2.binding_received_8)
        else:
            data2.balance_binding_8 = 0
        
        if data2.binding_received_9:
            data2.balance_binding_9 = float(data2.quantity_9) - float(data2.binding_received_9)
        else:
            data2.balance_binding_9 = 0
        
        if data2.binding_received_10:
            data2.balance_binding_10 = float(data2.quantity_10) - float(data2.binding_received_10)
        else:
            data2.balance_binding_10 = 0


        
        if data2.binding_received_11:
            data2.balance_binding_11 = float(data2.quantity_11) - float(data2.binding_received_11)
        else:
            data2.balance_binding_11 = 0
        
        if data2.binding_received_12:
            data2.balance_binding_12 = float(data2.quantity_12) - float(data2.binding_received_12)
        else:
            data2.balance_binding_12 = 0
        
        if data2.binding_received_13:
            data2.balance_binding_13 = float(data2.quantity_13) - float(data2.binding_received_13)
        else:
            data2.balance_binding_13 = 0
        
        if data2.binding_received_14:
            data2.balance_binding_14 = float(data2.quantity_14) - float(data2.binding_received_14)
        else:
            data2.balance_binding_14 = 0
        
        if data2.binding_received_15:
            data2.balance_binding_15 = float(data2.quantity_15) - float(data2.binding_received_15)
        else:
            data2.balance_binding_15 = 0
        
        if data2.binding_received_16:
            data2.balance_binding_16 = float(data2.quantity_16) - float(data2.binding_received_16)
        else:
            data2.balance_binding_16 = 0
        
        if data2.binding_received_17:
            data2.balance_binding_17 = float(data2.quantity_17) - float(data2.binding_received_17)
        else:
            data2.balance_binding_17 = 0
        
        if data2.binding_received_18:
            data2.balance_binding_18 = float(data2.quantity_18) - float(data2.binding_received_18)
        else:
            data2.balance_binding_18 = 0
        
        if data2.binding_received_19:
            data2.balance_binding_19 = float(data2.quantity_19) - float(data2.binding_received_19)
        else:
            data2.balance_binding_19 = 0
        
        
        if data2.binding_received_20:
            data2.balance_binding_20 = float(data2.quantity_20) - float(data2.binding_received_20)
        else:
            data2.balance_binding_20 = 0

        if data2.binding_received_21:
            data2.balance_binding_21 = float(data2.quantity_21) - float(data2.binding_received_21)
        else:
            data2.balance_binding_21 = 0
        
        if data2.binding_received_22:
            data2.balance_binding_22 = float(data2.quantity_22) - float(data2.binding_received_22)
        else:
            data2.balance_binding_22 = 0
        
        if data2.binding_received_23:
            data2.balance_binding_23 = float(data2.quantity_23) - float(data2.binding_received_23)
        else:
            data2.balance_binding_23 = 0
        
        if data2.binding_received_24:
            data2.balance_binding_24 = float(data2.quantity_24) - float(data2.binding_received_24)
        else:
            data2.balance_binding_24 = 0
        
        if data2.binding_received_25:
            data2.balance_binding_25 = float(data2.quantity_25) - float(data2.binding_received_25)
        else:
            data2.balance_binding_25 = 0
        
        if data2.binding_received_26:
            data2.balance_binding_26 = float(data2.quantity_26) - float(data2.binding_received_26)
        else:
            data2.balance_binding_26 = 0
        
        if data2.binding_received_27:
            data2.balance_binding_27 = float(data2.quantity_27) - float(data2.binding_received_27)
        else:
            data2.balance_binding_27 = 0
        
        if data2.binding_received_28:
            data2.balance_binding_28 = float(data2.quantity_28) - float(data2.binding_received_28)
        else:
            data2.balance_binding_28 = 0
        
        if data2.binding_received_29:
            data2.balance_binding_29 = float(data2.quantity_29) - float(data2.binding_received_29)
        else:
            data2.balance_binding_29 = 0
        
        if data2.binding_received_30:
            data2.balance_binding_30 = float(data2.quantity_30) - float(data2.binding_received_30)
        else:
            data2.balance_binding_30 = 0

        if data2.binding_received_31:
            data2.balance_binding_31 = float(data2.quantity_31) - float(data2.binding_received_31)
        else:
            data2.balance_binding_31 = 0
        
        if data2.binding_received_32:
            data2.balance_binding_32 = float(data2.quantity_32) - float(data2.binding_received_32)
        else:
            data2.balance_binding_32 = 0
        
        if data2.binding_received_33:
            data2.balance_binding_33 = float(data2.quantity_33) - float(data2.binding_received_33)
        else:
            data2.balance_binding_33 = 0
        
        if data2.binding_received_34:
            data2.balance_binding_34 = float(data2.quantity_34) - float(data2.binding_received_34)
        else:
            data2.balance_binding_34 = 0
        
        if data2.binding_received_35:
            data2.balance_binding_35 = float(data2.quantity_35) - float(data2.binding_received_35)
        else:
            data2.balance_binding_35 = 0
        
        if data2.binding_received_36:
            data2.balance_binding_36 = float(data2.quantity_36) - float(data2.binding_received_36)
        else:
            data2.balance_binding_36 = 0
        
        if data2.binding_received_37:
            data2.balance_binding_37 = float(data2.quantity_37) - float(data2.binding_received_37)
        else:
            data2.balance_binding_37 = 0
        
        if data2.binding_received_38:
            data2.balance_binding_38 = float(data2.quantity_38) - float(data2.binding_received_38)
        else:
            data2.balance_binding_38 = 0
        
        if data2.binding_received_39:
            data2.balance_binding_39 = float(data2.quantity_39) - float(data2.binding_received_39)
        else:
            data2.balance_binding_39 = 0
        
        if data2.binding_received_40:
            data2.balance_binding_40 = float(data2.quantity_40) - float(data2.binding_received_40)
        else:
            data2.balance_binding_40 = 0

        if data2.binding_received_41:
            data2.balance_binding_41 = float(data2.quantity_41) - float(data2.binding_received_41)
        else:
            data2.balance_binding_41 = 0
        
        if data2.binding_received_42:
            data2.balance_binding_42 = float(data2.quantity_42) - float(data2.binding_received_42)
        else:
            data2.balance_binding_42 = 0
        
        if data2.binding_received_43:
            data2.balance_binding_43 = float(data2.quantity_43) - float(data2.binding_received_43)
        else:
            data2.balance_binding_43 = 0
        
        if data2.binding_received_44:
            data2.balance_binding_44 = float(data2.quantity_44) - float(data2.binding_received_44)
        else:
            data2.balance_binding_44 = 0
        
        if data2.binding_received_45:
            data2.balance_binding_45 = float(data2.quantity_45) - float(data2.binding_received_45)
        else:
            data2.balance_binding_45 = 0
        
        if data2.binding_received_46:
            data2.balance_binding_46 = float(data2.quantity_46) - float(data2.binding_received_46)
        else:
            data2.balance_binding_46 = 0
        
        if data2.binding_received_47:
            data2.balance_binding_47 = float(data2.quantity_47) - float(data2.binding_received_47)
        else:
            data2.balance_binding_47 = 0
        
        if data2.binding_received_48:
            data2.balance_binding_48 = float(data2.quantity_48) - float(data2.binding_received_48)
        else:
            data2.balance_binding_48 = 0
        
        if data2.binding_received_49:
            data2.balance_binding_49 = float(data2.quantity_49) - float(data2.binding_received_49)
        else:
            data2.balance_binding_49 = 0
        
        if data2.binding_received_50:
            data2.balance_binding_50 = float(data2.quantity_50) - float(data2.binding_received_50)
        else:
            data2.balance_binding_50 = 0


        
        
        temp_bind=[]
        if data2.binding_received_1:
            temp_bind.append(int(data2.binding_received_1))
        if data2.binding_received_2:
            temp_bind.append(int(data2.binding_received_2))
        if data2.binding_received_3:
            temp_bind.append(int(data2.binding_received_3))
        if data2.binding_received_4:
            temp_bind.append(int(data2.binding_received_4))
        if data2.binding_received_5:
            temp_bind.append(int(data2.binding_received_5))
        if data2.binding_received_6:
            temp_bind.append(int(data2.binding_received_6))
        if data2.binding_received_7:
            temp_bind.append(int(data2.binding_received_7))
        if data2.binding_received_8:
            temp_bind.append(int(data2.binding_received_8))
        if data2.binding_received_9:
            temp_bind.append(int(data2.binding_received_9))
        if data2.binding_received_10:
            temp_bind.append(int(data2.binding_received_10))

        if data2.binding_received_11:
            temp_bind.append(int(data2.binding_received_11))
        if data2.binding_received_12:
            temp_bind.append(int(data2.binding_received_12))
        if data2.binding_received_13:
            temp_bind.append(int(data2.binding_received_13))
        if data2.binding_received_14:
            temp_bind.append(int(data2.binding_received_14))
        if data2.binding_received_15:
            temp_bind.append(int(data2.binding_received_15))
        if data2.binding_received_16:
            temp_bind.append(int(data2.binding_received_16))
        if data2.binding_received_17:
            temp_bind.append(int(data2.binding_received_17))
        if data2.binding_received_18:
            temp_bind.append(int(data2.binding_received_18))
        if data2.binding_received_19:
            temp_bind.append(int(data2.binding_received_19))
        if data2.binding_received_20:
            temp_bind.append(int(data2.binding_received_20))

        if data2.binding_received_21:
            temp_bind.append(int(data2.binding_received_21))
        if data2.binding_received_22:
            temp_bind.append(int(data2.binding_received_22))
        if data2.binding_received_23:
            temp_bind.append(int(data2.binding_received_23))
        if data2.binding_received_24:
            temp_bind.append(int(data2.binding_received_24))
        if data2.binding_received_25:
            temp_bind.append(int(data2.binding_received_25))
        if data2.binding_received_26:
            temp_bind.append(int(data2.binding_received_26))
        if data2.binding_received_27:
            temp_bind.append(int(data2.binding_received_27))
        if data2.binding_received_28:
            temp_bind.append(int(data2.binding_received_28))
        if data2.binding_received_29:
            temp_bind.append(int(data2.binding_received_29))
        if data2.binding_received_30:
            temp_bind.append(int(data2.binding_received_30))

        if data2.binding_received_31:
            temp_bind.append(int(data2.binding_received_31))
        if data2.binding_received_32:
            temp_bind.append(int(data2.binding_received_32))
        if data2.binding_received_33:
            temp_bind.append(int(data2.binding_received_33))
        if data2.binding_received_34:
            temp_bind.append(int(data2.binding_received_34))
        if data2.binding_received_35:
            temp_bind.append(int(data2.binding_received_35))
        if data2.binding_received_36:
            temp_bind.append(int(data2.binding_received_36))
        if data2.binding_received_37:
            temp_bind.append(int(data2.binding_received_37))
        if data2.binding_received_38:
            temp_bind.append(int(data2.binding_received_38))
        if data2.binding_received_39:
            temp_bind.append(int(data2.binding_received_39))
        if data2.binding_received_40:
            temp_bind.append(int(data2.binding_received_40))

        if data2.binding_received_41:
            temp_bind.append(int(data2.binding_received_41))
        if data2.binding_received_42:
            temp_bind.append(int(data2.binding_received_42))
        if data2.binding_received_43:
            temp_bind.append(int(data2.binding_received_43))
        if data2.binding_received_44:
            temp_bind.append(int(data2.binding_received_44))
        if data2.binding_received_45:
            temp_bind.append(int(data2.binding_received_45))
        if data2.binding_received_46:
            temp_bind.append(int(data2.binding_received_46))
        if data2.binding_received_47:
            temp_bind.append(int(data2.binding_received_47))
        if data2.binding_received_48:
            temp_bind.append(int(data2.binding_received_48))
        if data2.binding_received_49:
            temp_bind.append(int(data2.binding_received_49))
        if data2.binding_received_50:
            temp_bind.append(int(data2.binding_received_50))
        
        temp_bind=[i for i in temp_bind]
        data2.total_binding=0
        for i in temp_bind:
            data2.total_binding=data2.total_binding+i
        
        if data2.total_binding:
            data2.balance_binding = float(data2.total_quantity) - float(data2.total_binding)
        else:
            data2.balance_binding = 0
        
        data2.save()
        messages.success(request, "Updated Successfully...!!")
        return redirect('/bindings-data/') 
    
       
    context = {
        'data2':data2,
    }
    return render(request, 'processing/edit-bindings.html', context)








@login_required(login_url="")
def gathering_info(request):
    if request.method =='POST':
        id = request.POST.get('id')
        
        item1_page1 = request.POST.get('item1_page1')
        item1_page2 = request.POST.get('item1_page2')
        item1_page3 = request.POST.get('item1_page3')
        item1_page4 = request.POST.get('item1_page4')
        item1_page5 = request.POST.get('item1_page5')
        item1_page6 = request.POST.get('item1_page6')
        item1_page7 = request.POST.get('item1_page7')
        item1_page8 = request.POST.get('item1_page8')
        item1_page9 = request.POST.get('item1_page9')
        item1_page10 = request.POST.get('item1_page10')

        item2_page1 = request.POST.get('item2_page1')
        item2_page2 = request.POST.get('item2_page2')
        item2_page3 = request.POST.get('item2_page3')
        item2_page4 = request.POST.get('item2_page4')
        item2_page5 = request.POST.get('item2_page5')
        item2_page6 = request.POST.get('item2_page6')
        item2_page7 = request.POST.get('item2_page7')
        item2_page8 = request.POST.get('item2_page8')
        item2_page9 = request.POST.get('item2_page9')
        item2_page10 = request.POST.get('item2_page10')

        item3_page1 = request.POST.get('item3_page1')
        item3_page2 = request.POST.get('item3_page2')
        item3_page3 = request.POST.get('item3_page3')
        item3_page4 = request.POST.get('item3_page4')
        item3_page5 = request.POST.get('item3_page5')
        item3_page6 = request.POST.get('item3_page6')
        item3_page7 = request.POST.get('item3_page7')
        item3_page8 = request.POST.get('item3_page8')
        item3_page9 = request.POST.get('item3_page9')
        item3_page10 = request.POST.get('item3_page10')

        item4_page1 = request.POST.get('item4_page1')
        item4_page2 = request.POST.get('item4_page2')
        item4_page3 = request.POST.get('item4_page3')
        item4_page4 = request.POST.get('item4_page4')
        item4_page5 = request.POST.get('item4_page5')
        item4_page6 = request.POST.get('item4_page6')
        item4_page7 = request.POST.get('item4_page7')
        item4_page8 = request.POST.get('item4_page8')
        item4_page9 = request.POST.get('item4_page9')
        item4_page10 = request.POST.get('item4_page10')

        item5_page1 = request.POST.get('item5_page1')
        item5_page2 = request.POST.get('item5_page2')
        item5_page3 = request.POST.get('item5_page3')
        item5_page4 = request.POST.get('item5_page4')
        item5_page5 = request.POST.get('item5_page5')
        item5_page6 = request.POST.get('item5_page6')
        item5_page7 = request.POST.get('item5_page7')
        item5_page8 = request.POST.get('item5_page8')
        item5_page9 = request.POST.get('item5_page9')
        item5_page10 = request.POST.get('item5_page10')

        item6_page1 = request.POST.get('item6_page1')
        item6_page2 = request.POST.get('item6_page2')
        item6_page3 = request.POST.get('item6_page3')
        item6_page4 = request.POST.get('item6_page4')
        item6_page5 = request.POST.get('item6_page5')
        item6_page6 = request.POST.get('item6_page6')
        item6_page7 = request.POST.get('item6_page7')
        item6_page8 = request.POST.get('item6_page8')
        item6_page9 = request.POST.get('item6_page9')
        item6_page10 = request.POST.get('item6_page10')

        item7_page1 = request.POST.get('item7_page1')
        item7_page2 = request.POST.get('item7_page2')
        item7_page3 = request.POST.get('item7_page3')
        item7_page4 = request.POST.get('item7_page4')
        item7_page5 = request.POST.get('item7_page5')
        item7_page6 = request.POST.get('item7_page6')
        item7_page7 = request.POST.get('item7_page7')
        item7_page8 = request.POST.get('item7_page8')
        item7_page9 = request.POST.get('item7_page9')
        item7_page10 = request.POST.get('item7_page10')

        item8_page1 = request.POST.get('item8_page1')
        item8_page2 = request.POST.get('item8_page2')
        item8_page3 = request.POST.get('item8_page3')
        item8_page4 = request.POST.get('item8_page4')
        item8_page5 = request.POST.get('item8_page5')
        item8_page6 = request.POST.get('item8_page6')
        item8_page7 = request.POST.get('item8_page7')
        item8_page8 = request.POST.get('item8_page8')
        item8_page9 = request.POST.get('item8_page9')
        item8_page10 = request.POST.get('item8_page10')

        item9_page1 = request.POST.get('item9_page1')
        item9_page2 = request.POST.get('item9_page2')
        item9_page3 = request.POST.get('item9_page3')
        item9_page4 = request.POST.get('item9_page4')
        item9_page5 = request.POST.get('item9_page5')
        item9_page6 = request.POST.get('item9_page6')
        item9_page7 = request.POST.get('item9_page7')
        item9_page8 = request.POST.get('item9_page8')
        item9_page9 = request.POST.get('item9_page9')
        item9_page10 = request.POST.get('item9_page10')

        item10_page1 = request.POST.get('item10_page1')
        item10_page2 = request.POST.get('item10_page2')
        item10_page3 = request.POST.get('item10_page3')
        item10_page4 = request.POST.get('item10_page4')
        item10_page5 = request.POST.get('item10_page5')
        item10_page6 = request.POST.get('item10_page6')
        item10_page7 = request.POST.get('item10_page7')
        item10_page8 = request.POST.get('item10_page8')
        item10_page9 = request.POST.get('item10_page9')
        item10_page10 = request.POST.get('item10_page10')
        
        item11_page1 = request.POST.get('item11_page1')
        item11_page2 = request.POST.get('item11_page2')
        item11_page3 = request.POST.get('item11_page3')
        item11_page4 = request.POST.get('item11_page4')
        item11_page5 = request.POST.get('item11_page5')
        item11_page6 = request.POST.get('item11_page6')
        item11_page7 = request.POST.get('item11_page7')
        item11_page8 = request.POST.get('item11_page8')
        item11_page9 = request.POST.get('item11_page9')
        item11_page10 = request.POST.get('item11_page10')

        item12_page1 = request.POST.get('item12_page1')
        item12_page2 = request.POST.get('item12_page2')
        item12_page3 = request.POST.get('item12_page3')
        item12_page4 = request.POST.get('item12_page4')
        item12_page5 = request.POST.get('item12_page5')
        item12_page6 = request.POST.get('item12_page6')
        item12_page7 = request.POST.get('item12_page7')
        item12_page8 = request.POST.get('item12_page8')
        item12_page9 = request.POST.get('item12_page9')
        item12_page10 = request.POST.get('item12_page10')

        item13_page1 = request.POST.get('item13_page1')
        item13_page2 = request.POST.get('item13_page2')
        item13_page3 = request.POST.get('item13_page3')
        item13_page4 = request.POST.get('item13_page4')
        item13_page5 = request.POST.get('item13_page5')
        item13_page6 = request.POST.get('item13_page6')
        item13_page7 = request.POST.get('item13_page7')
        item13_page8 = request.POST.get('item13_page8')
        item13_page9 = request.POST.get('item13_page9')
        item13_page10 = request.POST.get('item13_page10')

        item14_page1 = request.POST.get('item14_page1')
        item14_page2 = request.POST.get('item14_page2')
        item14_page3 = request.POST.get('item14_page3')
        item14_page4 = request.POST.get('item14_page4')
        item14_page5 = request.POST.get('item14_page5')
        item14_page6 = request.POST.get('item14_page6')
        item14_page7 = request.POST.get('item14_page7')
        item14_page8 = request.POST.get('item14_page8')
        item14_page9 = request.POST.get('item14_page9')
        item14_page10 = request.POST.get('item14_page10')

        item15_page1 = request.POST.get('item15_page1')
        item15_page2 = request.POST.get('item15_page2')
        item15_page3 = request.POST.get('item15_page3')
        item15_page4 = request.POST.get('item15_page4')
        item15_page5 = request.POST.get('item15_page5')
        item15_page6 = request.POST.get('item15_page6')
        item15_page7 = request.POST.get('item15_page7')
        item15_page8 = request.POST.get('item15_page8')
        item15_page9 = request.POST.get('item15_page9')
        item15_page10 = request.POST.get('item15_page10')

        item16_page1 = request.POST.get('item16_page1')
        item16_page2 = request.POST.get('item16_page2')
        item16_page3 = request.POST.get('item16_page3')
        item16_page4 = request.POST.get('item16_page4')
        item16_page5 = request.POST.get('item16_page5')
        item16_page6 = request.POST.get('item16_page6')
        item16_page7 = request.POST.get('item16_page7')
        item16_page8 = request.POST.get('item16_page8')
        item16_page9 = request.POST.get('item16_page9')
        item16_page10 = request.POST.get('item16_page10')

        item17_page1 = request.POST.get('item17_page1')
        item17_page2 = request.POST.get('item17_page2')
        item17_page3 = request.POST.get('item17_page3')
        item17_page4 = request.POST.get('item17_page4')
        item17_page5 = request.POST.get('item17_page5')
        item17_page6 = request.POST.get('item17_page6')
        item17_page7 = request.POST.get('item17_page7')
        item17_page8 = request.POST.get('item17_page8')
        item17_page9 = request.POST.get('item17_page9')
        item17_page10 = request.POST.get('item17_page10')

        item18_page1 = request.POST.get('item18_page1')
        item18_page2 = request.POST.get('item18_page2')
        item18_page3 = request.POST.get('item18_page3')
        item18_page4 = request.POST.get('item18_page4')
        item18_page5 = request.POST.get('item18_page5')
        item18_page6 = request.POST.get('item18_page6')
        item18_page7 = request.POST.get('item18_page7')
        item18_page8 = request.POST.get('item18_page8')
        item18_page9 = request.POST.get('item18_page9')
        item18_page10 = request.POST.get('item18_page10')

        item19_page1 = request.POST.get('item19_page1')
        item19_page2 = request.POST.get('item19_page2')
        item19_page3 = request.POST.get('item19_page3')
        item19_page4 = request.POST.get('item19_page4')
        item19_page5 = request.POST.get('item19_page5')
        item19_page6 = request.POST.get('item19_page6')
        item19_page7 = request.POST.get('item19_page7')
        item19_page8 = request.POST.get('item19_page8')
        item19_page9 = request.POST.get('item19_page9')
        item19_page10 = request.POST.get('item19_page10')

        item20_page1 = request.POST.get('item20_page1')
        item20_page2 = request.POST.get('item20_page2')
        item20_page3 = request.POST.get('item20_page3')
        item20_page4 = request.POST.get('item20_page4')
        item20_page5 = request.POST.get('item20_page5')
        item20_page6 = request.POST.get('item20_page6')
        item20_page7 = request.POST.get('item20_page7')
        item20_page8 = request.POST.get('item20_page8')
        item20_page9 = request.POST.get('item20_page9')
        item20_page10 = request.POST.get('item20_page10')

        item21_page1 = request.POST.get('item21_page1')
        item21_page2 = request.POST.get('item21_page2')
        item21_page3 = request.POST.get('item21_page3')
        item21_page4 = request.POST.get('item21_page4')
        item21_page5 = request.POST.get('item21_page5')
        item21_page6 = request.POST.get('item21_page6')
        item21_page7 = request.POST.get('item21_page7')
        item21_page8 = request.POST.get('item21_page8')
        item21_page9 = request.POST.get('item21_page9')
        item21_page10 = request.POST.get('item21_page10')

        item22_page1 = request.POST.get('item22_page1')
        item22_page2 = request.POST.get('item22_page2')
        item22_page3 = request.POST.get('item22_page3')
        item22_page4 = request.POST.get('item22_page4')
        item22_page5 = request.POST.get('item22_page5')
        item22_page6 = request.POST.get('item22_page6')
        item22_page7 = request.POST.get('item22_page7')
        item22_page8 = request.POST.get('item22_page8')
        item22_page9 = request.POST.get('item22_page9')
        item22_page10 = request.POST.get('item22_page10')

        item23_page1 = request.POST.get('item23_page1')
        item23_page2 = request.POST.get('item23_page2')
        item23_page3 = request.POST.get('item23_page3')
        item23_page4 = request.POST.get('item23_page4')
        item23_page5 = request.POST.get('item23_page5')
        item23_page6 = request.POST.get('item23_page6')
        item23_page7 = request.POST.get('item23_page7')
        item23_page8 = request.POST.get('item23_page8')
        item23_page9 = request.POST.get('item23_page9')
        item23_page10 = request.POST.get('item23_page10')

        item24_page1 = request.POST.get('item24_page1')
        item24_page2 = request.POST.get('item24_page2')
        item24_page3 = request.POST.get('item24_page3')
        item24_page4 = request.POST.get('item24_page4')
        item24_page5 = request.POST.get('item24_page5')
        item24_page6 = request.POST.get('item24_page6')
        item24_page7 = request.POST.get('item24_page7')
        item24_page8 = request.POST.get('item24_page8')
        item24_page9 = request.POST.get('item24_page9')
        item24_page10 = request.POST.get('item24_page10')

        item25_page1 = request.POST.get('item25_page1')
        item25_page2 = request.POST.get('item25_page2')
        item25_page3 = request.POST.get('item25_page3')
        item25_page4 = request.POST.get('item25_page4')
        item25_page5 = request.POST.get('item25_page5')
        item25_page6 = request.POST.get('item25_page6')
        item25_page7 = request.POST.get('item25_page7')
        item25_page8 = request.POST.get('item25_page8')
        item25_page9 = request.POST.get('item25_page9')
        item25_page10 = request.POST.get('item25_page10')

        item26_page1 = request.POST.get('item26_page1')
        item26_page2 = request.POST.get('item26_page2')
        item26_page3 = request.POST.get('item26_page3')
        item26_page4 = request.POST.get('item26_page4')
        item26_page5 = request.POST.get('item26_page5')
        item26_page6 = request.POST.get('item26_page6')
        item26_page7 = request.POST.get('item26_page7')
        item26_page8 = request.POST.get('item26_page8')
        item26_page9 = request.POST.get('item26_page9')
        item26_page10 = request.POST.get('item26_page10')

        item27_page1 = request.POST.get('item27_page1')
        item27_page2 = request.POST.get('item27_page2')
        item27_page3 = request.POST.get('item27_page3')
        item27_page4 = request.POST.get('item27_page4')
        item27_page5 = request.POST.get('item27_page5')
        item27_page6 = request.POST.get('item27_page6')
        item27_page7 = request.POST.get('item27_page7')
        item27_page8 = request.POST.get('item27_page8')
        item27_page9 = request.POST.get('item27_page9')
        item27_page10 = request.POST.get('item27_page10')

        item28_page1 = request.POST.get('item28_page1')
        item28_page2 = request.POST.get('item28_page2')
        item28_page3 = request.POST.get('item28_page3')
        item28_page4 = request.POST.get('item28_page4')
        item28_page5 = request.POST.get('item28_page5')
        item28_page6 = request.POST.get('item28_page6')
        item28_page7 = request.POST.get('item28_page7')
        item28_page8 = request.POST.get('item28_page8')
        item28_page9 = request.POST.get('item28_page9')
        item28_page10 = request.POST.get('item28_page10')

        item29_page1 = request.POST.get('item29_page1')
        item29_page2 = request.POST.get('item29_page2')
        item29_page3 = request.POST.get('item29_page3')
        item29_page4 = request.POST.get('item29_page4')
        item29_page5 = request.POST.get('item29_page5')
        item29_page6 = request.POST.get('item29_page6')
        item29_page7 = request.POST.get('item29_page7')
        item29_page8 = request.POST.get('item29_page8')
        item29_page8 = request.POST.get('item29_page8')
        item29_page8 = request.POST.get('item29_page8')
        item29_page9 = request.POST.get('item29_page9')
        item29_page10 = request.POST.get('item29_page10')

        item30_page1 = request.POST.get('item30_page1')
        item30_page2 = request.POST.get('item30_page2')
        item30_page3 = request.POST.get('item30_page3')
        item30_page4 = request.POST.get('item30_page4')
        item30_page5 = request.POST.get('item30_page5')
        item30_page6 = request.POST.get('item30_page6')
        item30_page7 = request.POST.get('item30_page7')
        item30_page8 = request.POST.get('item30_page8')
        item30_page9 = request.POST.get('item30_page9')
        item30_page10 = request.POST.get('item30_page10')

        item31_page1 = request.POST.get('item31_page1')
        item31_page2 = request.POST.get('item31_page2')
        item31_page3 = request.POST.get('item31_page3')
        item31_page4 = request.POST.get('item31_page4')
        item31_page5 = request.POST.get('item31_page5')
        item31_page6 = request.POST.get('item31_page6')
        item31_page7 = request.POST.get('item31_page7')
        item31_page8 = request.POST.get('item31_page8')
        item31_page9 = request.POST.get('item31_page9')
        item31_page10 = request.POST.get('item31_page10')

        item32_page1 = request.POST.get('item32_page1')
        item32_page2 = request.POST.get('item32_page2')
        item32_page3 = request.POST.get('item32_page3')
        item32_page4 = request.POST.get('item32_page4')
        item32_page5 = request.POST.get('item32_page5')
        item32_page6 = request.POST.get('item32_page6')
        item32_page7 = request.POST.get('item32_page7')
        item32_page8 = request.POST.get('item32_page8')
        item32_page9 = request.POST.get('item32_page9')
        item32_page10 = request.POST.get('item32_page10')

        item33_page1 = request.POST.get('item33_page1')
        item33_page2 = request.POST.get('item33_page2')
        item33_page3 = request.POST.get('item33_page3')
        item33_page4 = request.POST.get('item33_page4')
        item33_page5 = request.POST.get('item33_page5')
        item33_page6 = request.POST.get('item33_page6')
        item33_page7 = request.POST.get('item33_page7')
        item33_page8 = request.POST.get('item33_page8')
        item33_page9 = request.POST.get('item33_page9')
        item33_page10 = request.POST.get('item33_page10')

        item34_page1 = request.POST.get('item34_page1')
        item34_page2 = request.POST.get('item34_page2')
        item34_page3 = request.POST.get('item34_page3')
        item34_page4 = request.POST.get('item34_page4')
        item34_page5 = request.POST.get('item34_page5')
        item34_page6 = request.POST.get('item34_page6')
        item34_page7 = request.POST.get('item34_page7')
        item34_page8 = request.POST.get('item34_page8')
        item34_page9 = request.POST.get('item34_page9')
        item34_page10 = request.POST.get('item34_page10')

        item35_page1 = request.POST.get('item35_page1')
        item35_page2 = request.POST.get('item35_page2')
        item35_page3 = request.POST.get('item35_page3')
        item35_page4 = request.POST.get('item35_page4')
        item35_page5 = request.POST.get('item35_page5')
        item35_page6 = request.POST.get('item35_page6')
        item35_page7 = request.POST.get('item35_page7')
        item35_page8 = request.POST.get('item35_page8')
        item35_page9 = request.POST.get('item35_page9')
        item35_page10 = request.POST.get('item35_page10')

        item36_page1 = request.POST.get('item36_page1')
        item36_page2 = request.POST.get('item36_page2')
        item36_page3 = request.POST.get('item36_page3')
        item36_page4 = request.POST.get('item36_page4')
        item36_page5 = request.POST.get('item36_page5')
        item36_page6 = request.POST.get('item36_page6')
        item36_page7 = request.POST.get('item36_page7')
        item36_page8 = request.POST.get('item36_page8')
        item36_page9 = request.POST.get('item36_page9')
        item36_page10 = request.POST.get('item36_page10')

        item37_page1 = request.POST.get('item37_page1')
        item37_page2 = request.POST.get('item37_page2')
        item37_page3 = request.POST.get('item37_page3')
        item37_page4 = request.POST.get('item37_page4')
        item37_page5 = request.POST.get('item37_page5')
        item37_page6 = request.POST.get('item37_page6')
        item37_page7 = request.POST.get('item37_page7')
        item37_page8 = request.POST.get('item37_page8')
        item37_page9 = request.POST.get('item37_page9')
        item37_page10 = request.POST.get('item37_page10')

        item38_page1 = request.POST.get('item38_page1')
        item38_page2 = request.POST.get('item38_page2')
        item38_page3 = request.POST.get('item38_page3')
        item38_page4 = request.POST.get('item38_page4')
        item38_page5 = request.POST.get('item38_page5')
        item38_page6 = request.POST.get('item38_page6')
        item38_page7 = request.POST.get('item38_page7')
        item38_page8 = request.POST.get('item38_page8')
        item38_page9 = request.POST.get('item38_page9')
        item38_page10 = request.POST.get('item38_page10')

        item39_page1 = request.POST.get('item39_page1')
        item39_page2 = request.POST.get('item39_page2')
        item39_page3 = request.POST.get('item39_page3')
        item39_page4 = request.POST.get('item39_page4')
        item39_page5 = request.POST.get('item39_page5')
        item39_page6 = request.POST.get('item39_page6')
        item39_page7 = request.POST.get('item39_page7')
        item39_page8 = request.POST.get('item39_page8')
        item39_page9 = request.POST.get('item39_page9')
        item39_page10 = request.POST.get('item39_page10')

        item40_page1 = request.POST.get('item40_page1')
        item40_page2 = request.POST.get('item40_page2')
        item40_page3 = request.POST.get('item40_page3')
        item40_page4 = request.POST.get('item40_page4')
        item40_page5 = request.POST.get('item40_page5')
        item40_page6 = request.POST.get('item40_page6')
        item40_page7 = request.POST.get('item40_page7')
        item40_page8 = request.POST.get('item40_page8')
        item40_page9 = request.POST.get('item40_page9')
        item40_page10 = request.POST.get('item40_page10')

        item41_page1 = request.POST.get('item41_page1')
        item41_page2 = request.POST.get('item41_page2')
        item41_page3 = request.POST.get('item41_page3')
        item41_page4 = request.POST.get('item41_page4')
        item41_page5 = request.POST.get('item41_page5')
        item41_page6 = request.POST.get('item41_page6')
        item41_page7 = request.POST.get('item41_page7')
        item41_page8 = request.POST.get('item41_page8')
        item41_page9 = request.POST.get('item41_page9')
        item41_page10 = request.POST.get('item41_page10')

        item42_page1 = request.POST.get('item42_page1')
        item42_page2 = request.POST.get('item42_page2')
        item42_page3 = request.POST.get('item42_page3')
        item42_page4 = request.POST.get('item42_page4')
        item42_page5 = request.POST.get('item42_page5')
        item42_page6 = request.POST.get('item42_page6')
        item42_page7 = request.POST.get('item42_page7')
        item42_page8 = request.POST.get('item42_page8')
        item42_page9 = request.POST.get('item42_page9')
        item42_page10 = request.POST.get('item42_page10')

        item43_page1 = request.POST.get('item43_page1')
        item43_page2 = request.POST.get('item43_page2')
        item43_page3 = request.POST.get('item43_page3')
        item43_page4 = request.POST.get('item43_page4')
        item43_page5 = request.POST.get('item43_page5')
        item43_page6 = request.POST.get('item43_page6')
        item43_page7 = request.POST.get('item43_page7')
        item43_page8 = request.POST.get('item43_page8')
        item43_page9 = request.POST.get('item43_page9')
        item43_page10 = request.POST.get('item43_page10')

        item44_page1 = request.POST.get('item44_page1')
        item44_page2 = request.POST.get('item44_page2')
        item44_page3 = request.POST.get('item44_page3')
        item44_page4 = request.POST.get('item44_page4')
        item44_page5 = request.POST.get('item44_page5')
        item44_page6 = request.POST.get('item44_page6')
        item44_page7 = request.POST.get('item44_page7')
        item44_page8 = request.POST.get('item44_page8')
        item44_page9 = request.POST.get('item44_page9')
        item44_page10 = request.POST.get('item44_page10')

        item45_page1 = request.POST.get('item45_page1')
        item45_page2 = request.POST.get('item45_page2')
        item45_page3 = request.POST.get('item45_page3')
        item45_page4 = request.POST.get('item45_page4')
        item45_page5 = request.POST.get('item45_page5')
        item45_page6 = request.POST.get('item45_page6')
        item45_page7 = request.POST.get('item45_page7')
        item45_page8 = request.POST.get('item45_page8')
        item45_page9 = request.POST.get('item45_page9')
        item45_page10 = request.POST.get('item45_page10')

        item46_page1 = request.POST.get('item46_page1')
        item46_page2 = request.POST.get('item46_page2')
        item46_page3 = request.POST.get('item46_page3')
        item46_page4 = request.POST.get('item46_page4')
        item46_page5 = request.POST.get('item46_page5')
        item46_page6 = request.POST.get('item46_page6')
        item46_page7 = request.POST.get('item46_page7')
        item46_page8 = request.POST.get('item46_page8')
        item46_page9 = request.POST.get('item46_page9')
        item46_page10 = request.POST.get('item46_page10')

        item47_page1 = request.POST.get('item47_page1')
        item47_page2 = request.POST.get('item47_page2')
        item47_page3 = request.POST.get('item47_page3')
        item47_page4 = request.POST.get('item47_page4')
        item47_page5 = request.POST.get('item47_page5')
        item47_page6 = request.POST.get('item47_page6')
        item47_page7 = request.POST.get('item47_page7')
        item47_page8 = request.POST.get('item47_page8')
        item47_page9 = request.POST.get('item47_page9')
        item47_page10 = request.POST.get('item47_page10')

        item48_page1 = request.POST.get('item48_page1')
        item48_page2 = request.POST.get('item48_page2')
        item48_page3 = request.POST.get('item48_page3')
        item48_page4 = request.POST.get('item48_page4')
        item48_page5 = request.POST.get('item48_page5')
        item48_page6 = request.POST.get('item48_page6')
        item48_page7 = request.POST.get('item48_page7')
        item48_page8 = request.POST.get('item48_page8')
        item48_page9 = request.POST.get('item48_page9')
        item48_page10 = request.POST.get('item48_page10')

        item49_page1 = request.POST.get('item49_page1')
        item49_page2 = request.POST.get('item49_page2')
        item49_page3 = request.POST.get('item49_page3')
        item49_page3 = request.POST.get('item49_page3')
        item49_page3 = request.POST.get('item49_page3')
        item49_page4 = request.POST.get('item49_page4')
        item49_page5 = request.POST.get('item49_page5')
        item49_page6 = request.POST.get('item49_page6')
        item49_page7 = request.POST.get('item49_page7')
        item49_page8 = request.POST.get('item49_page8')
        item49_page9 = request.POST.get('item49_page9')
        item49_page10 = request.POST.get('item49_page10')

        item50_page1 = request.POST.get('item50_page1')
        item50_page2 = request.POST.get('item50_page2')
        item50_page3 = request.POST.get('item50_page3')
        item50_page4 = request.POST.get('item50_page4')
        item50_page5 = request.POST.get('item50_page5')
        item50_page6 = request.POST.get('item50_page6')
        item50_page7 = request.POST.get('item50_page7')
        item50_page8 = request.POST.get('item50_page8')
        item50_page9 = request.POST.get('item50_page9')
        item50_page10 = request.POST.get('item50_page10')

        
        total_gathering=request.POST.get('printing_received_form')
        wastage_form = request.POST.get('print_wastage_form')
        gathering_date = request.POST.get('print_date')
        order = orders.objects.filter(order_id=id).get()
        print('order',order)
        
        order.item1_page1=item1_page1
        order.item1_page2=item1_page2
        order.item1_page3=item1_page3
        order.item1_page4=item1_page4
        order.item1_page5=item1_page5
        order.item1_page6=item1_page6
        order.item1_page7=item1_page7
        order.item1_page8=item1_page8
        order.item1_page9=item1_page9
        order.item1_page10=item1_page10

        order.item2_page1=item2_page1
        order.item2_page2=item2_page2
        order.item2_page3=item2_page3
        order.item2_page4=item2_page4
        order.item2_page5=item2_page5
        order.item2_page6=item2_page6
        order.item2_page7=item2_page7
        order.item2_page8=item2_page8
        order.item2_page9=item2_page9
        order.item2_page10=item2_page10

        order.item3_page1=item3_page1
        order.item3_page2=item3_page2
        order.item3_page3=item3_page3
        order.item3_page4=item3_page4
        order.item3_page5=item3_page5
        order.item3_page6=item3_page6
        order.item3_page7=item3_page7
        order.item3_page8=item3_page8
        order.item3_page9=item3_page9
        order.item3_page10=item3_page10

        order.item4_page1=item4_page1
        order.item4_page2=item4_page2
        order.item4_page3=item4_page3
        order.item4_page4=item4_page4
        order.item4_page5=item4_page5
        order.item4_page6=item4_page6
        order.item4_page7=item4_page7
        order.item4_page8=item4_page8
        order.item4_page9=item4_page9
        order.item4_page10=item4_page10

        order.item5_page1=item5_page1
        order.item5_page2=item5_page2
        order.item5_page3=item5_page3
        order.item5_page4=item5_page4
        order.item5_page5=item5_page5
        order.item5_page6=item5_page6
        order.item5_page7=item5_page7
        order.item5_page8=item5_page8
        order.item5_page9=item5_page9
        order.item5_page10=item5_page10

        order.item6_page1=item6_page1
        order.item6_page2=item6_page2
        order.item6_page3=item6_page3
        order.item6_page4=item6_page4
        order.item6_page5=item6_page5
        order.item6_page6=item6_page6
        order.item6_page7=item6_page7
        order.item6_page8=item6_page8
        order.item6_page9=item6_page9
        order.item6_page10=item6_page10

        order.item7_page1=item7_page1
        order.item7_page2=item7_page2
        order.item7_page3=item7_page3
        order.item7_page4=item7_page4
        order.item7_page5=item7_page5
        order.item7_page6=item7_page6
        order.item7_page7=item7_page7
        order.item7_page8=item7_page8
        order.item7_page9=item7_page9
        order.item7_page10=item7_page10

        order.item8_page1=item8_page1
        order.item8_page2=item8_page2
        order.item8_page3=item8_page3
        order.item8_page4=item8_page4
        order.item8_page5=item8_page5
        order.item8_page6=item8_page6
        order.item8_page7=item8_page7
        order.item8_page8=item8_page8
        order.item8_page9=item8_page9
        order.item8_page10=item8_page10

        order.item9_page1=item9_page1
        order.item9_page2=item9_page2
        order.item9_page3=item9_page3
        order.item9_page4=item9_page4
        order.item9_page5=item9_page5
        order.item9_page6=item9_page6
        order.item9_page7=item9_page7
        order.item9_page8=item9_page8
        order.item9_page9=item9_page9
        order.item9_page10=item9_page10

        order.item10_page1=item10_page1
        order.item10_page2=item10_page2
        order.item10_page3=item10_page3
        order.item10_page4=item10_page4
        order.item10_page5=item10_page5
        order.item10_page6=item10_page6
        order.item10_page7=item10_page7
        order.item10_page8=item10_page8
        order.item10_page9=item10_page9
        order.item10_page10=item10_page10

        order.item11_page1=item11_page1
        order.item11_page2=item11_page2
        order.item11_page3=item11_page3
        order.item11_page4=item11_page4
        order.item11_page5=item11_page5
        order.item11_page6=item11_page6
        order.item11_page7=item11_page7
        order.item11_page8=item11_page8
        order.item11_page9=item11_page9
        order.item11_page10=item11_page10

        order.item12_page1=item12_page1
        order.item12_page2=item12_page2
        order.item12_page3=item12_page3
        order.item12_page4=item12_page4
        order.item12_page5=item12_page5
        order.item12_page6=item12_page6
        order.item12_page7=item12_page7
        order.item12_page8=item12_page8
        order.item12_page9=item12_page9
        order.item12_page10=item12_page10

        order.item13_page1=item13_page1
        order.item13_page2=item13_page2
        order.item13_page3=item13_page3
        order.item13_page4=item13_page4
        order.item13_page5=item13_page5
        order.item13_page6=item13_page6
        order.item13_page7=item13_page7
        order.item13_page8=item13_page8
        order.item13_page9=item13_page9
        order.item13_page10=item13_page10

        order.item14_page1=item14_page1
        order.item14_page2=item14_page2
        order.item14_page3=item14_page3
        order.item14_page4=item14_page4
        order.item14_page5=item14_page5
        order.item14_page6=item14_page6
        order.item14_page7=item14_page7
        order.item14_page8=item14_page8
        order.item14_page9=item14_page9
        order.item14_page10=item14_page10

        order.item15_page1=item15_page1
        order.item15_page2=item15_page2
        order.item15_page3=item15_page3
        order.item15_page4=item15_page4
        order.item15_page5=item15_page5
        order.item15_page6=item15_page6
        order.item15_page7=item15_page7
        order.item15_page8=item15_page8
        order.item15_page9=item15_page9
        order.item15_page10=item15_page10

        order.item16_page1=item16_page1
        order.item16_page2=item16_page2
        order.item16_page3=item16_page3
        order.item16_page4=item16_page4
        order.item16_page5=item16_page5
        order.item16_page6=item16_page6
        order.item16_page7=item16_page7
        order.item16_page8=item16_page8
        order.item16_page9=item16_page9
        order.item16_page10=item16_page10

        order.item17_page1=item17_page1
        order.item17_page2=item17_page2
        order.item17_page3=item17_page3
        order.item17_page4=item17_page4
        order.item17_page5=item17_page5
        order.item17_page6=item17_page6
        order.item17_page7=item17_page7
        order.item17_page8=item17_page8
        order.item17_page9=item17_page9
        order.item17_page10=item17_page10

        order.item18_page1=item18_page1
        order.item18_page2=item18_page2
        order.item18_page3=item18_page3
        order.item18_page4=item18_page4
        order.item18_page5=item18_page5
        order.item18_page6=item18_page6
        order.item18_page7=item18_page7
        order.item18_page8=item18_page8
        order.item18_page9=item18_page9
        order.item18_page10=item18_page10

        order.item19_page1=item19_page1
        order.item19_page2=item19_page2
        order.item19_page3=item19_page3
        order.item19_page4=item19_page4
        order.item19_page5=item19_page5
        order.item19_page6=item19_page6
        order.item19_page7=item19_page7
        order.item19_page8=item19_page8
        order.item19_page9=item19_page9
        order.item19_page10=item19_page10

        order.item20_page1=item20_page1
        order.item20_page2=item20_page2
        order.item20_page3=item20_page3
        order.item20_page4=item20_page4
        order.item20_page5=item20_page5
        order.item20_page6=item20_page6
        order.item20_page7=item20_page7
        order.item20_page8=item20_page8
        order.item20_page9=item20_page9
        order.item20_page10=item20_page10


        order.item21_page1=item21_page1
        order.item21_page2=item21_page2
        order.item21_page3=item21_page3
        order.item21_page4=item21_page4
        order.item21_page5=item21_page5
        order.item21_page6=item21_page6
        order.item21_page7=item21_page7
        order.item21_page8=item21_page8
        order.item21_page9=item21_page9
        order.item21_page10=item21_page10

        order.item22_page1=item22_page1
        order.item22_page2=item22_page2
        order.item22_page3=item22_page3
        order.item22_page4=item22_page4
        order.item22_page5=item22_page5
        order.item22_page6=item22_page6
        order.item22_page7=item22_page7
        order.item22_page8=item22_page8
        order.item22_page9=item22_page9
        order.item22_page10=item22_page10

        order.item23_page1=item23_page1
        order.item23_page2=item23_page2
        order.item23_page3=item23_page3
        order.item23_page4=item23_page4
        order.item23_page5=item23_page5
        order.item23_page6=item23_page6
        order.item23_page7=item23_page7
        order.item23_page8=item23_page8
        order.item23_page9=item23_page9
        order.item23_page10=item23_page10

        order.item24_page1=item24_page1
        order.item24_page2=item24_page2
        order.item24_page3=item24_page3
        order.item24_page4=item24_page4
        order.item24_page5=item24_page5
        order.item24_page6=item24_page6
        order.item24_page7=item24_page7
        order.item24_page8=item24_page8
        order.item24_page9=item24_page9
        order.item24_page10=item24_page10

        order.item25_page1=item25_page1
        order.item25_page2=item25_page2
        order.item25_page3=item25_page3
        order.item25_page4=item25_page4
        order.item25_page5=item25_page5
        order.item25_page6=item25_page6
        order.item25_page7=item25_page7
        order.item25_page8=item25_page8
        order.item25_page9=item25_page9
        order.item25_page10=item25_page10

        order.item26_page1=item26_page1
        order.item26_page2=item26_page2
        order.item26_page3=item26_page3
        order.item26_page4=item26_page4
        order.item26_page5=item26_page5
        order.item26_page6=item26_page6
        order.item26_page7=item26_page7
        order.item26_page8=item26_page8
        order.item26_page9=item26_page9
        order.item26_page10=item26_page10

        order.item27_page1=item27_page1
        order.item27_page2=item27_page2
        order.item27_page3=item27_page3
        order.item27_page4=item27_page4
        order.item27_page5=item27_page5
        order.item27_page6=item27_page6
        order.item27_page7=item27_page7
        order.item27_page8=item27_page8
        order.item27_page9=item27_page9
        order.item27_page10=item27_page10

        order.item28_page1=item28_page1
        order.item28_page2=item28_page2
        order.item28_page3=item28_page3
        order.item28_page4=item28_page4
        order.item28_page5=item28_page5
        order.item28_page6=item28_page6
        order.item28_page7=item28_page7
        order.item28_page8=item28_page8
        order.item28_page9=item28_page9
        order.item28_page10=item28_page10

        order.item29_page1=item29_page1
        order.item29_page2=item29_page2
        order.item29_page3=item29_page3
        order.item29_page4=item29_page4
        order.item29_page5=item29_page5
        order.item29_page6=item29_page6
        order.item29_page7=item29_page7
        order.item29_page8=item29_page8
        order.item29_page9=item29_page9
        order.item29_page10=item29_page10

        order.item30_page1=item30_page1
        order.item30_page2=item30_page2
        order.item30_page3=item30_page3
        order.item30_page4=item30_page4
        order.item30_page5=item30_page5
        order.item30_page6=item30_page6
        order.item30_page7=item30_page7
        order.item30_page8=item30_page8
        order.item30_page9=item30_page9
        order.item30_page10=item30_page10


        order.item31_page1=item31_page1
        order.item31_page2=item31_page2
        order.item31_page3=item31_page3
        order.item31_page4=item31_page4
        order.item31_page5=item31_page5
        order.item31_page6=item31_page6
        order.item31_page7=item31_page7
        order.item31_page8=item31_page8
        order.item31_page9=item31_page9
        order.item31_page10=item31_page10

        order.item32_page1=item32_page1
        order.item32_page2=item32_page2
        order.item32_page3=item32_page3
        order.item32_page4=item32_page4
        order.item32_page5=item32_page5
        order.item32_page6=item32_page6
        order.item32_page7=item32_page7
        order.item32_page8=item32_page8
        order.item32_page9=item32_page9
        order.item32_page10=item32_page10

        order.item33_page1=item33_page1
        order.item33_page2=item33_page2
        order.item33_page3=item33_page3
        order.item33_page4=item33_page4
        order.item33_page5=item33_page5
        order.item33_page6=item33_page6
        order.item33_page7=item33_page7
        order.item33_page8=item33_page8
        order.item33_page9=item33_page9
        order.item33_page10=item33_page10

        order.item34_page1=item34_page1
        order.item34_page2=item34_page2
        order.item34_page3=item34_page3
        order.item34_page4=item34_page4
        order.item34_page5=item34_page5
        order.item34_page6=item34_page6
        order.item34_page7=item34_page7
        order.item34_page8=item34_page8
        order.item34_page9=item34_page9
        order.item34_page10=item34_page10

        order.item35_page1=item35_page1
        order.item35_page2=item35_page2
        order.item35_page3=item35_page3
        order.item35_page4=item35_page4
        order.item35_page5=item35_page5
        order.item35_page6=item35_page6
        order.item35_page7=item35_page7
        order.item35_page8=item35_page8
        order.item35_page9=item35_page9
        order.item35_page10=item35_page10

        order.item36_page1=item36_page1
        order.item36_page2=item36_page2
        order.item36_page3=item36_page3
        order.item36_page4=item36_page4
        order.item36_page5=item36_page5
        order.item36_page6=item36_page6
        order.item36_page7=item36_page7
        order.item36_page8=item36_page8
        order.item36_page9=item36_page9
        order.item36_page10=item36_page10

        order.item37_page1=item37_page1
        order.item37_page2=item37_page2
        order.item37_page3=item37_page3
        order.item37_page4=item37_page4
        order.item37_page5=item37_page5
        order.item37_page6=item37_page6
        order.item37_page7=item37_page7
        order.item37_page8=item37_page8
        order.item37_page9=item37_page9
        order.item37_page10=item37_page10

        order.item38_page1=item38_page1
        order.item38_page2=item38_page2
        order.item38_page3=item38_page3
        order.item38_page4=item38_page4
        order.item38_page5=item38_page5
        order.item38_page6=item38_page6
        order.item38_page7=item38_page7
        order.item38_page8=item38_page8
        order.item38_page9=item38_page9
        order.item38_page10=item38_page10

        order.item39_page1=item39_page1
        order.item39_page2=item39_page2
        order.item39_page3=item39_page3
        order.item39_page4=item39_page4
        order.item39_page5=item39_page5
        order.item39_page6=item39_page6
        order.item39_page7=item39_page7
        order.item39_page8=item39_page8
        order.item39_page9=item39_page9
        order.item39_page10=item39_page10

        order.item40_page1=item40_page1
        order.item40_page2=item40_page2
        order.item40_page3=item40_page3
        order.item40_page4=item40_page4
        order.item40_page5=item40_page5
        order.item40_page6=item40_page6
        order.item40_page7=item40_page7
        order.item40_page8=item40_page8
        order.item40_page9=item40_page9
        order.item40_page10=item40_page10


        order.item41_page1=item41_page1
        order.item41_page2=item41_page2
        order.item41_page3=item41_page3
        order.item41_page4=item41_page4
        order.item41_page5=item41_page5
        order.item41_page6=item41_page6
        order.item41_page7=item41_page7
        order.item41_page8=item41_page8
        order.item41_page9=item41_page9
        order.item41_page10=item41_page10

        order.item42_page1=item42_page1
        order.item42_page2=item42_page2
        order.item42_page3=item42_page3
        order.item42_page4=item42_page4
        order.item42_page5=item42_page5
        order.item42_page6=item42_page6
        order.item42_page7=item42_page7
        order.item42_page8=item42_page8
        order.item42_page9=item42_page9
        order.item42_page10=item42_page10

        order.item43_page1=item43_page1
        order.item43_page2=item43_page2
        order.item43_page3=item43_page3
        order.item43_page4=item43_page4
        order.item43_page5=item43_page5
        order.item43_page6=item43_page6
        order.item43_page7=item43_page7
        order.item43_page8=item43_page8
        order.item43_page9=item43_page9
        order.item43_page10=item43_page10

        order.item44_page1=item44_page1
        order.item44_page2=item44_page2
        order.item44_page3=item44_page3
        order.item44_page4=item44_page4
        order.item44_page5=item44_page5
        order.item44_page6=item44_page6
        order.item44_page7=item44_page7
        order.item44_page8=item44_page8
        order.item44_page9=item44_page9
        order.item44_page10=item44_page10

        order.item45_page1=item45_page1
        order.item45_page2=item45_page2
        order.item45_page3=item45_page3
        order.item45_page4=item45_page4
        order.item45_page5=item45_page5
        order.item45_page6=item45_page6
        order.item45_page7=item45_page7
        order.item45_page8=item45_page8
        order.item45_page9=item45_page9
        order.item45_page10=item45_page10

        order.item46_page1=item46_page1
        order.item46_page2=item46_page2
        order.item46_page3=item46_page3
        order.item46_page4=item46_page4
        order.item46_page5=item46_page5
        order.item46_page6=item46_page6
        order.item46_page7=item46_page7
        order.item46_page8=item46_page8
        order.item46_page9=item46_page9
        order.item46_page10=item46_page10

        order.item47_page1=item47_page1
        order.item47_page2=item47_page2
        order.item47_page3=item47_page3
        order.item47_page4=item47_page4
        order.item47_page5=item47_page5
        order.item47_page6=item47_page6
        order.item47_page7=item47_page7
        order.item47_page8=item47_page8
        order.item47_page9=item47_page9
        order.item47_page10=item47_page10

        order.item48_page1=item48_page1
        order.item48_page2=item48_page2
        order.item48_page3=item48_page3
        order.item48_page4=item48_page4
        order.item48_page5=item48_page5
        order.item48_page6=item48_page6
        order.item48_page7=item48_page7
        order.item48_page8=item48_page8
        order.item48_page9=item48_page9
        order.item48_page10=item48_page10

        order.item49_page1=item49_page1
        order.item49_page2=item49_page2
        order.item49_page3=item49_page3
        order.item49_page4=item49_page4
        order.item49_page5=item49_page5
        order.item49_page6=item49_page6
        order.item49_page7=item49_page7
        order.item49_page8=item49_page8
        order.item49_page9=item49_page9
        order.item49_page10=item49_page10

        order.item50_page1=item50_page1
        order.item50_page2=item50_page2
        order.item50_page3=item50_page3
        order.item50_page4=item50_page4
        order.item50_page5=item50_page5
        order.item50_page6=item50_page6
        order.item50_page7=item50_page7
        order.item50_page8=item50_page8
        order.item50_page9=item50_page9
        order.item50_page10=item50_page10
        
        

        
        order.total_gathering=total_gathering 
        order.wastage_form=wastage_form 
        order.gathering_date=datetime.datetime.now()
        order.save()

    data1 = orders.objects.all().order_by('-order_id')    
    context={
        'data1':data1,       
    }
    return render(request,'processing/gathering-info.html',context) 








@login_required(login_url="")
def view_gathering_info(request,order_id):
    data1 = orders.objects.get(order_id=order_id)
    print('gjhgjmgj',order_id)
    # print('received print',data1.printing_received_form_11)
    

    # data1.printing_received_form_2=request.POST.get('printing_received_form_2')
    print('received print',data1.printing_received_form_1)




    if request.method == 'POST':
        data1.total_gathering = request.POST.get('total_gathering')
        data1.total_gathering_1=request.POST.get('total_gathering_1')
        data1.total_gathering_2=request.POST.get('total_gathering_2')
        data1.total_gathering_3=request.POST.get('total_gathering_3')
        data1.total_gathering_4=request.POST.get('total_gathering_4')
        data1.total_gathering_5=request.POST.get('total_gathering_5')
        data1.total_gathering_6=request.POST.get('total_gathering_6')
        data1.total_gathering_7=request.POST.get('total_gathering_7')
        data1.total_gathering_8=request.POST.get('total_gathering_8')
        data1.total_gathering_9=request.POST.get('total_gathering_9')
        data1.total_gathering_10=request.POST.get('total_gathering_10')
        data1.total_gathering_11=request.POST.get('total_gathering_11')
        data1.total_gathering_12=request.POST.get('total_gathering_12')
        data1.total_gathering_13=request.POST.get('total_gathering_13')
        data1.total_gathering_14=request.POST.get('total_gathering_14')
        data1.total_gathering_15=request.POST.get('total_gathering_15')
        data1.total_gathering_16=request.POST.get('total_gathering_16')
        data1.total_gathering_17=request.POST.get('total_gathering_17')
        data1.total_gathering_18=request.POST.get('total_gathering_18')
        data1.total_gathering_19=request.POST.get('total_gathering_19')
        data1.total_gathering_20=request.POST.get('total_gathering_20')
        data1.total_gathering_21=request.POST.get('total_gathering_21')
        data1.total_gathering_22=request.POST.get('total_gathering_22')
        data1.total_gathering_23=request.POST.get('total_gathering_23')
        data1.total_gathering_24=request.POST.get('total_gathering_24')
        data1.total_gathering_25=request.POST.get('total_gathering_25')
        data1.total_gathering_26=request.POST.get('total_gathering_26')
        data1.total_gathering_27=request.POST.get('total_gathering_27')
        data1.total_gathering_28=request.POST.get('total_gathering_28')
        data1.total_gathering_29=request.POST.get('total_gathering_29')
        data1.total_gathering_30=request.POST.get('total_gathering_30')
        data1.total_gathering_31=request.POST.get('total_gathering_31')
        data1.total_gathering_32=request.POST.get('total_gathering_32')
        data1.total_gathering_33=request.POST.get('total_gathering_33')
        data1.total_gathering_34=request.POST.get('total_gathering_34')
        data1.total_gathering_35=request.POST.get('total_gathering_35')
        data1.total_gathering_36=request.POST.get('total_gathering_36')
        data1.total_gathering_37=request.POST.get('total_gathering_37')
        data1.total_gathering_38=request.POST.get('total_gathering_38')
        data1.total_gathering_39=request.POST.get('total_gathering_39')
        data1.total_gathering_40=request.POST.get('total_gathering_40')
        data1.total_gathering_41=request.POST.get('total_gathering_41')
        data1.total_gathering_42=request.POST.get('total_gathering_42')
        data1.total_gathering_43=request.POST.get('total_gathering_43')
        data1.total_gathering_44=request.POST.get('total_gathering_44')
        data1.total_gathering_45=request.POST.get('total_gathering_45')
        data1.total_gathering_46=request.POST.get('total_gathering_46')
        data1.total_gathering_47=request.POST.get('total_gathering_47')
        data1.total_gathering_48=request.POST.get('total_gathering_48')
        data1.total_gathering_49=request.POST.get('total_gathering_49')
        data1.total_gathering_50=request.POST.get('total_gathering_50')
        data1.total_gathering_51 = request.POST.get('total_gathering_51')
        data1.total_gathering_52 = request.POST.get('total_gathering_52')
        data1.total_gathering_53 = request.POST.get('total_gathering_53')
        data1.total_gathering_54 = request.POST.get('total_gathering_54')
        data1.total_gathering_55 = request.POST.get('total_gathering_55')
        data1.total_gathering_56 = request.POST.get('total_gathering_56')
        data1.total_gathering_57 = request.POST.get('total_gathering_57')
        data1.total_gathering_58 = request.POST.get('total_gathering_58')
        data1.total_gathering_59 = request.POST.get('total_gathering_59')
        data1.total_gathering_60 = request.POST.get('total_gathering_60')



        # data1.complete_book_gathered_1 = request.POST.get('complete_book_gathered_1')

        # print('complete_book_gathered_1',data1.complete_book_gathered_1)


        # data1.complete_book_gathered_1 = request.POST.get('complete_book_gathered_1')
        # print('book',data1.complete_book_gathered_1)

        

        
        
        data1.gathering_date = datetime.datetime.now()
        
        if data1.total_gathering_1:
            data1.wastage_form_1 = float(data1.pform_1) - float(data1.total_gathering_1)
        else:
            data1.wastage_form_1 = 0

        if data1.total_gathering_2:
            data1.wastage_form_2 = float(data1.pform_1) - float(data1.total_gathering_2)
        else:
            data1.wastage_form_2 = 0

        if data1.total_gathering_3:
            data1.wastage_form_3 = float(data1.pform_1) - float(data1.total_gathering_3)
        else:
            data1.wastage_form_3 = 0

        if data1.total_gathering_4:
            data1.wastage_form_4 = float(data1.pform_1) - float(data1.total_gathering_4)
        else:
            data1.wastage_form_4 = 0

        if data1.total_gathering_5:
            data1.wastage_form_5 = float(data1.pform_1) - float(data1.total_gathering_5)
            
        else:
            data1.wastage_form_5 = 0
        print('data1.wastage',data1.wastage_form_5)    

        if data1.total_gathering_6:
            data1.wastage_form_6 = float(data1.pform_1) - float(data1.total_gathering_6)
        else:
            data1.wastage_form_6 = 0

        if data1.total_gathering_7:
            data1.wastage_form_7 = float(data1.pform_1) - float(data1.total_gathering_7)
        else:
            data1.wastage_form_7 = 0

        if data1.total_gathering_8:
            data1.wastage_form_8 = float(data1.pform_1) - float(data1.total_gathering_8)
        else:
            data1.wastage_form_8 = 0

        if data1.total_gathering_9:
            data1.wastage_form_9 = float(data1.pform_1) - float(data1.total_gathering_9)
        else:
            data1.wastage_form_9 = 0

        if data1.total_gathering_10:
            data1.wastage_form_10 = float(data1.pform_1) - float(data1.total_gathering_10)
        else:
            data1.wastage_form_10 = 0  




        if data1.total_gathering_11:
            data1.wastage_form_11 = float(data1.pform_2) - float(data1.total_gathering_11)
        else:
            data1.wastage_form_11 = 0

        if data1.total_gathering_12:
            data1.wastage_form_12 = float(data1.pform_2) - float(data1.total_gathering_12)
        else:
            data1.wastage_form_12 = 0

        if data1.total_gathering_13:
            data1.wastage_form_13 = float(data1.pform_2) - float(data1.total_gathering_13)
        else:
            data1.wastage_form_13 = 0

        if data1.total_gathering_14:
            data1.wastage_form_14 = float(data1.pform_2) - float(data1.total_gathering_14)
        else:
            data1.wastage_form_14 = 0

        if data1.total_gathering_15:
            data1.wastage_form_15 = float(data1.pform_2) - float(data1.total_gathering_15)
        else:
            data1.wastage_form_15 = 0

        if data1.total_gathering_16:
            data1.wastage_form_16 = float(data1.pform_2) - float(data1.total_gathering_16)
        else:
            data1.wastage_form_16 = 0

        if data1.total_gathering_17:
            data1.wastage_form_17 = float(data1.pform_2) - float(data1.total_gathering_17)
        else:
            data1.wastage_form_17 = 0

        if data1.total_gathering_18:
            data1.wastage_form_18 = float(data1.pform_2) - float(data1.total_gathering_18)
        else:
            data1.wastage_form_18 = 0

        if data1.total_gathering_19:
            data1.wastage_form_19 = float(data1.pform_2) - float(data1.total_gathering_19)
        else:
            data1.wastage_form_19 = 0

        if data1.total_gathering_20:
            data1.wastage_form_20 = float(data1.pform_2) - float(data1.total_gathering_20)
        else:
            data1.wastage_form_20 = 0




        if data1.total_gathering_21:
            data1.wastage_form_21 = float(data1.pform_3) - float(data1.total_gathering_21)
        else:
            data1.wastage_form_21 = 0

        if data1.total_gathering_22:
            data1.wastage_form_22 = float(data1.pform_3) - float(data1.total_gathering_22)
        else:
            data1.wastage_form_22 = 0

        if data1.total_gathering_23:
            data1.wastage_form_23 = float(data1.pform_3) - float(data1.total_gathering_23)
        else:
            data1.wastage_form_23 = 0

        if data1.total_gathering_24:
            data1.wastage_form_24 = float(data1.pform_3) - float(data1.total_gathering_24)
        else:
            data1.wastage_form_24 = 0

        if data1.total_gathering_25:
            data1.wastage_form_25 = float(data1.pform_3) - float(data1.total_gathering_25)
        else:
            data1.wastage_form_25 = 0

        if data1.total_gathering_26:
            data1.wastage_form_26 = float(data1.pform_3) - float(data1.total_gathering_26)
        else:
            data1.wastage_form_26 = 0

        if data1.total_gathering_27:
            data1.wastage_form_27 = float(data1.pform_3) - float(data1.total_gathering_27)
        else:
            data1.wastage_form_27 = 0

        if data1.total_gathering_28:
            data1.wastage_form_28 = float(data1.pform_3) - float(data1.total_gathering_28)
        else:
            data1.wastage_form_28 = 0

        if data1.total_gathering_29:
            data1.wastage_form_29 = float(data1.pform_3) - float(data1.total_gathering_29)
        else:
            data1.wastage_form_29 = 0

        if data1.total_gathering_30:
            data1.wastage_form_30 = float(data1.pform_3) - float(data1.total_gathering_30)
        else:
            data1.wastage_form_30 = 0



        if data1.total_gathering_31:
            data1.wastage_form_31 = float(data1.pform_4) - float(data1.total_gathering_31)
        else:
            data1.wastage_form_31 = 0

        if data1.total_gathering_32:
            data1.wastage_form_32 = float(data1.pform_4) - float(data1.total_gathering_32)
        else:
            data1.wastage_form_32 = 0

        if data1.total_gathering_33:
            data1.wastage_form_33 = float(data1.pform_4) - float(data1.total_gathering_33)
        else:
            data1.wastage_form_33 = 0

        if data1.total_gathering_34:
            data1.wastage_form_34 = float(data1.pform_4) - float(data1.total_gathering_34)
        else:
            data1.wastage_form_34 = 0

        if data1.total_gathering_35:
            data1.wastage_form_35 = float(data1.pform_4) - float(data1.total_gathering_35)
        else:
            data1.wastage_form_35 = 0

        if data1.total_gathering_36:
            data1.wastage_form_36 = float(data1.pform_4) - float(data1.total_gathering_36)
        else:
            data1.wastage_form_36 = 0

        if data1.total_gathering_37:
            data1.wastage_form_37 = float(data1.pform_4) - float(data1.total_gathering_37)
        else:
            data1.wastage_form_37 = 0

        if data1.total_gathering_38:
            data1.wastage_form_38 = float(data1.pform_4) - float(data1.total_gathering_38)
        else:
            data1.wastage_form_38 = 0

        if data1.total_gathering_39:
            data1.wastage_form_39 = float(data1.pform_4) - float(data1.total_gathering_39)
        else:
            data1.wastage_form_39 = 0

        if data1.total_gathering_40:
            data1.wastage_form_40 = float(data1.pform_4) - float(data1.total_gathering_40)
        else:
            data1.wastage_form_40 = 0




        if data1.total_gathering_41:
            data1.wastage_form_41 = float(data1.pform_5) - float(data1.total_gathering_41)
        else:
            data1.wastage_form_41 = 0

        if data1.total_gathering_42:
            data1.wastage_form_42 = float(data1.pform_5) - float(data1.total_gathering_42)
        else:
            data1.wastage_form_42 = 0

        if data1.total_gathering_43:
            data1.wastage_form_43 = float(data1.pform_5) - float(data1.total_gathering_43)
        else:
            data1.wastage_form_43 = 0

        if data1.total_gathering_44:
            data1.wastage_form_44 = float(data1.pform_5) - float(data1.total_gathering_44)
        else:
            data1.wastage_form_44 = 0

        if data1.total_gathering_45:
            data1.wastage_form_45 = float(data1.pform_5) - float(data1.total_gathering_45)
        else:
            data1.wastage_form_45 = 0

        if data1.total_gathering_46:
            data1.wastage_form_46 = float(data1.pform_5) - float(data1.total_gathering_46)
        else:
            data1.wastage_form_46 = 0

        if data1.total_gathering_47:
            data1.wastage_form_47 = float(data1.pform_5) - float(data1.total_gathering_47)
        else:
            data1.wastage_form_47 = 0

        if data1.total_gathering_48:
            data1.wastage_form_48 = float(data1.pform_5) - float(data1.total_gathering_48)
        else:
            data1.wastage_form_48 = 0

        if data1.total_gathering_49:
            data1.wastage_form_49 = float(data1.pform_5) - float(data1.total_gathering_49)
        else:
            data1.wastage_form_49 = 0

        if data1.total_gathering_50:
            data1.wastage_form_50 = float(data1.pform_5) - float(data1.total_gathering_50)
        else:
            data1.wastage_form_50 = 0





        if data1.total_gathering_51:
            data1.wastage_form_51 = float(data1.pform_6) - float(data1.total_gathering_51)
        else:
            data1.wastage_form_51 = 0

        if data1.total_gathering_52:
            data1.wastage_form_52 = float(data1.pform_6) - float(data1.total_gathering_52)
        else:
            data1.wastage_form_52 = 0

        if data1.total_gathering_53:
            data1.wastage_form_53 = float(data1.pform_6) - float(data1.total_gathering_53)
        else:
            data1.wastage_form_53 = 0

        if data1.total_gathering_54:
            data1.wastage_form_54 = float(data1.pform_6) - float(data1.total_gathering_54)
        else:
            data1.wastage_form_54 = 0

        if data1.total_gathering_55:
            data1.wastage_form_55 = float(data1.pform_6) - float(data1.total_gathering_55)
        else:
            data1.wastage_form_55 = 0

        if data1.total_gathering_56:
            data1.wastage_form_56 = float(data1.pform_6) - float(data1.total_gathering_56)
        else:
            data1.wastage_form_56 = 0

        if data1.total_gathering_57:
            data1.wastage_form_57 = float(data1.pform_6) - float(data1.total_gathering_57)
        else:
            data1.wastage_form_57 = 0

        if data1.total_gathering_58:
            data1.wastage_form_58 = float(data1.pform_6) - float(data1.total_gathering_58)
        else:
            data1.wastage_form_58 = 0

        if data1.total_gathering_59:
            data1.wastage_form_59 = float(data1.pform_6) - float(data1.total_gathering_59)
        else:
            data1.wastage_form_59 = 0

        if data1.total_gathering_60:
            data1.wastage_form_60 = float(data1.pform_6) - float(data1.total_gathering_60)
        else:
            data1.wastage_form_60 = 0




        temp_print=[]
        if data1.total_gathering_1:
            temp_print.append(float(data1.total_gathering_1))
        if data1.total_gathering_2:
            temp_print.append(float(data1.total_gathering_2))
        if data1.total_gathering_3:
            temp_print.append(float(data1.total_gathering_3))
        if data1.total_gathering_4:
            temp_print.append(float(data1.total_gathering_4))
        if data1.total_gathering_5:
            temp_print.append(float(data1.total_gathering_5))
        if data1.total_gathering_6:
            temp_print.append(float(data1.total_gathering_6))
        if data1.total_gathering_7:
            temp_print.append(float(data1.total_gathering_7))
        if data1.total_gathering_8:
            temp_print.append(float(data1.total_gathering_8))
        if data1.total_gathering_9:
            temp_print.append(float(data1.total_gathering_9))
        if data1.total_gathering_10:
            temp_print.append(float(data1.total_gathering_10))

        if data1.total_gathering_11:
            temp_print.append(float(data1.total_gathering_11))
        if data1.total_gathering_12:
            temp_print.append(float(data1.total_gathering_12))
        if data1.total_gathering_13:
            temp_print.append(float(data1.total_gathering_13))
        if data1.total_gathering_14:
            temp_print.append(float(data1.total_gathering_14))
        if data1.total_gathering_15:
            temp_print.append(float(data1.total_gathering_15))
        if data1.total_gathering_16:
            temp_print.append(float(data1.total_gathering_16))
        if data1.total_gathering_17:
            temp_print.append(float(data1.total_gathering_17))
        if data1.total_gathering_18:
            temp_print.append(float(data1.total_gathering_18))
        if data1.total_gathering_19:
            temp_print.append(float(data1.total_gathering_19))
        if data1.total_gathering_20:
            temp_print.append(float(data1.total_gathering_20))

        if data1.total_gathering_21:
            temp_print.append(float(data1.total_gathering_21))
        if data1.total_gathering_22:
            temp_print.append(float(data1.total_gathering_22))
        if data1.total_gathering_23:
            temp_print.append(float(data1.total_gathering_23))
        if data1.total_gathering_24:
            temp_print.append(float(data1.total_gathering_24))
        if data1.total_gathering_25:
            temp_print.append(float(data1.total_gathering_25))
        if data1.total_gathering_26:
            temp_print.append(float(data1.total_gathering_26))
        if data1.total_gathering_27:
            temp_print.append(float(data1.total_gathering_27))
        if data1.total_gathering_28:
            temp_print.append(float(data1.total_gathering_28))
        if data1.total_gathering_29:
            temp_print.append(float(data1.total_gathering_29))
        if data1.total_gathering_30:
            temp_print.append(float(data1.total_gathering_30))

        if data1.total_gathering_31:
            temp_print.append(float(data1.total_gathering_31))
        if data1.total_gathering_32:
            temp_print.append(float(data1.total_gathering_32))
        if data1.total_gathering_33:
            temp_print.append(float(data1.total_gathering_33))
        if data1.total_gathering_34:
            temp_print.append(float(data1.total_gathering_34))
        if data1.total_gathering_35:
            temp_print.append(float(data1.total_gathering_35))
        if data1.total_gathering_36:
            temp_print.append(float(data1.total_gathering_36))
        if data1.total_gathering_37:
            temp_print.append(float(data1.total_gathering_37))
        if data1.total_gathering_38:
            temp_print.append(float(data1.total_gathering_38))
        if data1.total_gathering_39:
            temp_print.append(float(data1.total_gathering_39))
        if data1.total_gathering_40:
            temp_print.append(float(data1.total_gathering_40))


        if data1.total_gathering_41:
            temp_print.append(float(data1.total_gathering_41))
        if data1.total_gathering_42:
            temp_print.append(float(data1.total_gathering_42))
        if data1.total_gathering_43:
            temp_print.append(float(data1.total_gathering_43))
        if data1.total_gathering_44:
            temp_print.append(float(data1.total_gathering_44))
        if data1.total_gathering_45:
            temp_print.append(float(data1.total_gathering_45))
        if data1.total_gathering_46:
            temp_print.append(float(data1.total_gathering_46))
        if data1.total_gathering_47:
            temp_print.append(float(data1.total_gathering_47))
        if data1.total_gathering_48:
            temp_print.append(float(data1.total_gathering_48))
        if data1.total_gathering_49:
            temp_print.append(float(data1.total_gathering_49))
        if data1.total_gathering_50:
            temp_print.append(float(data1.total_gathering_50))



        if data1.total_gathering_51:
            temp_print.append(float(data1.total_gathering_51))
        if data1.total_gathering_52:
            temp_print.append(float(data1.total_gathering_52))
        if data1.total_gathering_53:
            temp_print.append(float(data1.total_gathering_53))
        if data1.total_gathering_54:
            temp_print.append(float(data1.total_gathering_54))
        if data1.total_gathering_55:
            temp_print.append(float(data1.total_gathering_55))
        if data1.total_gathering_56:
            temp_print.append(float(data1.total_gathering_56))
        if data1.total_gathering_57:
            temp_print.append(float(data1.total_gathering_57))
        if data1.total_gathering_58:
            temp_print.append(float(data1.total_gathering_58))
        if data1.total_gathering_59:
            temp_print.append(float(data1.total_gathering_59))
        if data1.total_gathering_60:
            temp_print.append(float(data1.total_gathering_60))



        temp_print=[i for i in temp_print]
        print('temp_print',temp_print, len(temp_print))
        data1.total_gathering=0
        for i in temp_print:
            data1.total_gathering=data1.total_gathering+i
        print('data1.total_gathering',data1.total_gathering)


        # Finding the minimum value among the total_gathering values

        # min_total_gathering = min(temp_print)
        # print('min_total_gathering',min_total_gathering)
        # data1.complete_book_gathered_1 = min_total_gathering
        # data1.save()

        
        if data1.total_gathering:
            sum_wastage_form = 0
            for p in range(1,51):
                sum_wastage_form +=float(getattr(data1,f"wastage_form_{p}",0))
                data1.wastage_form = sum_wastage_form
            print('data1.wastage_form',data1.wastage_form)
        else:
            data1.wastage_form = 0

        
        data1.save()

        messages.success(request, "Updated Successfully...!!")
        if request.method == 'POST':
            if request.POST.get("gather_approved") == "approval_button":
                orders.objects.filter(Q(order_id=order_id) & Q(gather_approved=False)).update(gather_approved=True)
                return redirect('/gathering-info/')
            else:
                pass   


        # return redirect('/gathering-info/') 
    data5 = orders.objects.filter(order_id = order_id)

    for i in data5:
        print()
        

        
    
    min_total_gathering = ""   
    context = {
        'data1':data1,
        #'min_total_gathering':min_total_gathering,
        'data5':data5,
    }
    return render(request, 'processing/view-gathering.html', context)





































    # if request.method == 'POST':
    #     id = request.POST.get('id')

    #     gathering.item1_page1 = request.POST.get('item1_page1')
    #     gathering.item1_page2 = request.POST.get('item1_page2')
    #     gathering.item1_page3 = request.POST.get('item1_page3')
    #     gathering.item1_page4 = request.POST.get('item1_page4')
    #     gathering.item1_page5 = request.POST.get('item1_page5')
    #     gathering.item1_page6 = request.POST.get('item1_page6')
    #     gathering.item1_page7 = request.POST.get('item1_page7')
    #     gathering.item1_page8 = request.POST.get('item1_page8')
    #     gathering.item1_page9 = request.POST.get('item1_page9')
    #     gathering.item1_page10 = request.POST.get('item1_page10')

    #     gathering.item2_page1 = request.POST.get('item2_page1')
    #     gathering.item2_page2 = request.POST.get('item2_page2')
    #     gathering.item2_page3 = request.POST.get('item2_page3')
    #     gathering.item2_page4 = request.POST.get('item2_page4')
    #     gathering.item2_page5 = request.POST.get('item2_page5')
    #     gathering.item2_page6 = request.POST.get('item2_page6')
    #     gathering.item2_page7 = request.POST.get('item2_page7')
    #     gathering.item2_page8 = request.POST.get('item2_page8')
    #     gathering.item2_page9 = request.POST.get('item2_page9')
    #     gathering.item2_page10 = request.POST.get('item2_page10')

    #     gathering.item3_page1 = request.POST.get('item3_page1')
    #     gathering.item3_page2 = request.POST.get('item3_page2')
    #     gathering.item3_page3 = request.POST.get('item3_page3')
    #     gathering.item3_page4 = request.POST.get('item3_page4')
    #     gathering.item3_page5 = request.POST.get('item3_page5')
    #     gathering.item3_page6 = request.POST.get('item3_page6')
    #     gathering.item3_page7 = request.POST.get('item3_page7')
    #     gathering.item3_page8 = request.POST.get('item3_page8')
    #     gathering.item3_page9 = request.POST.get('item3_page9')
    #     gathering.item3_page10 = request.POST.get('item3_page10')

    #     gathering.item4_page1 = request.POST.get('item4_page1')
    #     gathering.item4_page2 = request.POST.get('item4_page2')
    #     gathering.item4_page3 = request.POST.get('item4_page3')
    #     gathering.item4_page4 = request.POST.get('item4_page4')
    #     gathering.item4_page5 = request.POST.get('item4_page5')
    #     gathering.item4_page6 = request.POST.get('item4_page6')
    #     gathering.item4_page7 = request.POST.get('item4_page7')
    #     gathering.item4_page8 = request.POST.get('item4_page8')
    #     gathering.item4_page9 = request.POST.get('item4_page9')
    #     gathering.item4_page10 = request.POST.get('item4_page10')

    #     gathering.item5_page1 = request.POST.get('item5_page1')
    #     gathering.item5_page2 = request.POST.get('item5_page2')
    #     gathering.item5_page3 = request.POST.get('item5_page3')
    #     gathering.item5_page4 = request.POST.get('item5_page4')
    #     gathering.item5_page5 = request.POST.get('item5_page5')
    #     gathering.item5_page6 = request.POST.get('item5_page6')
    #     gathering.item5_page7 = request.POST.get('item5_page7')
    #     gathering.item5_page8 = request.POST.get('item5_page8')
    #     gathering.item5_page9 = request.POST.get('item5_page9')
    #     gathering.item5_page10 = request.POST.get('item5_page10')

    #     gathering.item6_page1 = request.POST.get('item6_page1')
    #     gathering.item6_page2 = request.POST.get('item6_page2')
    #     gathering.item6_page3 = request.POST.get('item6_page3')
    #     gathering.item6_page4 = request.POST.get('item6_page4')
    #     gathering.item6_page5 = request.POST.get('item6_page5')
    #     gathering.item6_page6 = request.POST.get('item6_page6')
    #     gathering.item6_page7 = request.POST.get('item6_page7')
    #     gathering.item6_page8 = request.POST.get('item6_page8')
    #     gathering.item6_page9 = request.POST.get('item6_page9')
    #     gathering.item6_page10 = request.POST.get('item6_page10')

    #     gathering.item7_page1 = request.POST.get('item7_page1')
    #     gathering.item7_page2 = request.POST.get('item7_page2')
    #     gathering.item7_page3 = request.POST.get('item7_page3')
    #     gathering.item7_page4 = request.POST.get('item7_page4')
    #     gathering.item7_page5 = request.POST.get('item7_page5')
    #     gathering.item7_page6 = request.POST.get('item7_page6')
    #     gathering.item7_page7 = request.POST.get('item7_page7')
    #     gathering.item7_page8 = request.POST.get('item7_page8')
    #     gathering.item7_page9 = request.POST.get('item7_page9')
    #     gathering.item7_page10 = request.POST.get('item7_page10')

    #     gathering.item8_page1 = request.POST.get('item8_page1')
    #     gathering.item8_page2 = request.POST.get('item8_page2')
    #     gathering.item8_page3 = request.POST.get('item8_page3')
    #     gathering.item8_page4 = request.POST.get('item8_page4')
    #     gathering.item8_page5 = request.POST.get('item8_page5')
    #     gathering.item8_page6 = request.POST.get('item8_page6')
    #     gathering.item8_page7 = request.POST.get('item8_page7')
    #     gathering.item8_page8 = request.POST.get('item8_page8')
    #     gathering.item8_page9 = request.POST.get('item8_page9')
    #     gathering.item8_page10 = request.POST.get('item8_page10')

    #     gathering.item9_page1 = request.POST.get('item9_page1')
    #     gathering.item9_page2 = request.POST.get('item9_page2')
    #     gathering.item9_page3 = request.POST.get('item9_page3')
    #     gathering.item9_page4 = request.POST.get('item9_page4')
    #     gathering.item9_page5 = request.POST.get('item9_page5')
    #     gathering.item9_page6 = request.POST.get('item9_page6')
    #     gathering.item9_page7 = request.POST.get('item9_page7')
    #     gathering.item9_page8 = request.POST.get('item9_page8')
    #     gathering.item9_page9 = request.POST.get('item9_page9')
    #     gathering.item9_page10 = request.POST.get('item9_page10')

    #     gathering.item10_page1 = request.POST.get('item10_page1')
    #     gathering.item10_page2 = request.POST.get('item10_page2')
    #     gathering.item10_page3 = request.POST.get('item10_page3')
    #     gathering.item10_page4 = request.POST.get('item10_page4')
    #     gathering.item10_page5 = request.POST.get('item10_page5')
    #     gathering.item10_page6 = request.POST.get('item10_page6')
    #     gathering.item10_page7 = request.POST.get('item10_page7')
    #     gathering.item10_page8 = request.POST.get('item10_page8')
    #     gathering.item10_page9 = request.POST.get('item10_page9')
    #     gathering.item10_page10 = request.POST.get('item10_page10')
        
    #     gathering.item11_page1 = request.POST.get('item11_page1')
    #     gathering.item11_page2 = request.POST.get('item11_page2')
    #     gathering.item11_page3 = request.POST.get('item11_page3')
    #     gathering.item11_page4 = request.POST.get('item11_page4')
    #     gathering.item11_page5 = request.POST.get('item11_page5')
    #     gathering.item11_page6 = request.POST.get('item11_page6')
    #     gathering.item11_page7 = request.POST.get('item11_page7')
    #     gathering.item11_page8 = request.POST.get('item11_page8')
    #     gathering.item11_page9 = request.POST.get('item11_page9')
    #     gathering.item11_page10 = request.POST.get('item11_page10')

    #     gathering.item12_page1 = request.POST.get('item12_page1')
    #     gathering.item12_page2 = request.POST.get('item12_page2')
    #     gathering.item12_page3 = request.POST.get('item12_page3')
    #     gathering.item12_page4 = request.POST.get('item12_page4')
    #     gathering.item12_page5 = request.POST.get('item12_page5')
    #     gathering.item12_page6 = request.POST.get('item12_page6')
    #     gathering.item12_page7 = request.POST.get('item12_page7')
    #     gathering.item12_page8 = request.POST.get('item12_page8')
    #     gathering.item12_page9 = request.POST.get('item12_page9')
    #     gathering.item12_page10 = request.POST.get('item12_page10')

    #     gathering.item13_page1 = request.POST.get('item13_page1')
    #     gathering.item13_page2 = request.POST.get('item13_page2')
    #     gathering.item13_page3 = request.POST.get('item13_page3')
    #     gathering.item13_page4 = request.POST.get('item13_page4')
    #     gathering.item13_page5 = request.POST.get('item13_page5')
    #     gathering.item13_page6 = request.POST.get('item13_page6')
    #     gathering.item13_page7 = request.POST.get('item13_page7')
    #     gathering.item13_page8 = request.POST.get('item13_page8')
    #     gathering.item13_page9 = request.POST.get('item13_page9')
    #     gathering.item13_page10 = request.POST.get('item13_page10')

    #     gathering.item14_page1 = request.POST.get('item14_page1')
    #     gathering.item14_page2 = request.POST.get('item14_page2')
    #     gathering.item14_page3 = request.POST.get('item14_page3')
    #     gathering.item14_page4 = request.POST.get('item14_page4')
    #     gathering.item14_page5 = request.POST.get('item14_page5')
    #     gathering.item14_page6 = request.POST.get('item14_page6')
    #     gathering.item14_page7 = request.POST.get('item14_page7')
    #     gathering.item14_page8 = request.POST.get('item14_page8')
    #     gathering.item14_page9 = request.POST.get('item14_page9')
    #     gathering.item14_page10 = request.POST.get('item14_page10')

    #     gathering.item15_page1 = request.POST.get('item15_page1')
    #     gathering.item15_page2 = request.POST.get('item15_page2')
    #     gathering.item15_page3 = request.POST.get('item15_page3')
    #     gathering.item15_page4 = request.POST.get('item15_page4')
    #     gathering.item15_page5 = request.POST.get('item15_page5')
    #     gathering.item15_page6 = request.POST.get('item15_page6')
    #     gathering.item15_page7 = request.POST.get('item15_page7')
    #     gathering.item15_page8 = request.POST.get('item15_page8')
    #     gathering.item15_page9 = request.POST.get('item15_page9')
    #     gathering.item15_page10 = request.POST.get('item15_page10')

    #     gathering.item16_page1 = request.POST.get('item16_page1')
    #     gathering.item16_page2 = request.POST.get('item16_page2')
    #     gathering.item16_page3 = request.POST.get('item16_page3')
    #     gathering.item16_page4 = request.POST.get('item16_page4')
    #     gathering.item16_page5 = request.POST.get('item16_page5')
    #     gathering.item16_page6 = request.POST.get('item16_page6')
    #     gathering.item16_page7 = request.POST.get('item16_page7')
    #     gathering.item16_page8 = request.POST.get('item16_page8')
    #     gathering.item16_page9 = request.POST.get('item16_page9')
    #     gathering.item16_page10 = request.POST.get('item16_page10')

    #     gathering.item17_page1 = request.POST.get('item17_page1')
    #     gathering.item17_page2 = request.POST.get('item17_page2')
    #     gathering.item17_page3 = request.POST.get('item17_page3')
    #     gathering.item17_page4 = request.POST.get('item17_page4')
    #     gathering.item17_page5 = request.POST.get('item17_page5')
    #     gathering.item17_page6 = request.POST.get('item17_page6')
    #     gathering.item17_page7 = request.POST.get('item17_page7')
    #     gathering.item17_page8 = request.POST.get('item17_page8')
    #     gathering.item17_page9 = request.POST.get('item17_page9')
    #     gathering.item17_page10 = request.POST.get('item17_page10')

    #     gathering.item18_page1 = request.POST.get('item18_page1')
    #     gathering.item18_page2 = request.POST.get('item18_page2')
    #     gathering.item18_page3 = request.POST.get('item18_page3')
    #     gathering.item18_page4 = request.POST.get('item18_page4')
    #     gathering.item18_page5 = request.POST.get('item18_page5')
    #     gathering.item18_page6 = request.POST.get('item18_page6')
    #     gathering.item18_page7 = request.POST.get('item18_page7')
    #     gathering.item18_page8 = request.POST.get('item18_page8')
    #     gathering.item18_page9 = request.POST.get('item18_page9')
    #     gathering.item18_page10 = request.POST.get('item18_page10')

    #     gathering.item19_page1 = request.POST.get('item19_page1')
    #     gathering.item19_page2 = request.POST.get('item19_page2')
    #     gathering.item19_page3 = request.POST.get('item19_page3')
    #     gathering.item19_page4 = request.POST.get('item19_page4')
    #     gathering.item19_page5 = request.POST.get('item19_page5')
    #     gathering.item19_page6 = request.POST.get('item19_page6')
    #     gathering.item19_page7 = request.POST.get('item19_page7')
    #     gathering.item19_page8 = request.POST.get('item19_page8')
    #     gathering.item19_page9 = request.POST.get('item19_page9')
    #     gathering.item19_page10 = request.POST.get('item19_page10')

    #     gathering.item20_page1 = request.POST.get('item20_page1')
    #     gathering.item20_page2 = request.POST.get('item20_page2')
    #     gathering.item20_page3 = request.POST.get('item20_page3')
    #     gathering.item20_page4 = request.POST.get('item20_page4')
    #     gathering.item20_page5 = request.POST.get('item20_page5')
    #     gathering.item20_page6 = request.POST.get('item20_page6')
    #     gathering.item20_page7 = request.POST.get('item20_page7')
    #     gathering.item20_page8 = request.POST.get('item20_page8')
    #     gathering.item20_page9 = request.POST.get('item20_page9')
    #     gathering.item20_page10 = request.POST.get('item20_page10')

    #     gathering.item21_page1 = request.POST.get('item21_page1')
    #     gathering.item21_page2 = request.POST.get('item21_page2')
    #     gathering.item21_page3 = request.POST.get('item21_page3')
    #     gathering.item21_page4 = request.POST.get('item21_page4')
    #     gathering.item21_page5 = request.POST.get('item21_page5')
    #     gathering.item21_page6 = request.POST.get('item21_page6')
    #     gathering.item21_page7 = request.POST.get('item21_page7')
    #     gathering.item21_page8 = request.POST.get('item21_page8')
    #     gathering.item21_page9 = request.POST.get('item21_page9')
    #     gathering.item21_page10 = request.POST.get('item21_page10')

    #     gathering.item22_page1 = request.POST.get('item22_page1')
    #     gathering.item22_page2 = request.POST.get('item22_page2')
    #     gathering.item22_page3 = request.POST.get('item22_page3')
    #     gathering.item22_page4 = request.POST.get('item22_page4')
    #     gathering.item22_page5 = request.POST.get('item22_page5')
    #     gathering.item22_page6 = request.POST.get('item22_page6')
    #     gathering.item22_page7 = request.POST.get('item22_page7')
    #     gathering.item22_page8 = request.POST.get('item22_page8')
    #     gathering.item22_page9 = request.POST.get('item22_page9')
    #     gathering.item22_page10 = request.POST.get('item22_page10')

    #     gathering.item23_page1 = request.POST.get('item23_page1')
    #     gathering.item23_page2 = request.POST.get('item23_page2')
    #     gathering.item23_page3 = request.POST.get('item23_page3')
    #     gathering.item23_page4 = request.POST.get('item23_page4')
    #     gathering.item23_page5 = request.POST.get('item23_page5')
    #     gathering.item23_page6 = request.POST.get('item23_page6')
    #     gathering.item23_page7 = request.POST.get('item23_page7')
    #     gathering.item23_page8 = request.POST.get('item23_page8')
    #     gathering.item23_page9 = request.POST.get('item23_page9')
    #     gathering.item23_page10 = request.POST.get('item23_page10')

    #     gathering.item24_page1 = request.POST.get('item24_page1')
    #     gathering.item24_page2 = request.POST.get('item24_page2')
    #     gathering.item24_page3 = request.POST.get('item24_page3')
    #     gathering.item24_page4 = request.POST.get('item24_page4')
    #     gathering.item24_page5 = request.POST.get('item24_page5')
    #     gathering.item24_page6 = request.POST.get('item24_page6')
    #     gathering.item24_page7 = request.POST.get('item24_page7')
    #     gathering.item24_page8 = request.POST.get('item24_page8')
    #     gathering.item24_page9 = request.POST.get('item24_page9')
    #     gathering.item24_page10 = request.POST.get('item24_page10')

    #     gathering.item25_page1 = request.POST.get('item25_page1')
    #     gathering.item25_page2 = request.POST.get('item25_page2')
    #     gathering.item25_page3 = request.POST.get('item25_page3')
    #     gathering.item25_page4 = request.POST.get('item25_page4')
    #     gathering.item25_page5 = request.POST.get('item25_page5')
    #     gathering.item25_page6 = request.POST.get('item25_page6')
    #     gathering.item25_page7 = request.POST.get('item25_page7')
    #     gathering.item25_page8 = request.POST.get('item25_page8')
    #     gathering.item25_page9 = request.POST.get('item25_page9')
    #     gathering.item25_page10 = request.POST.get('item25_page10')

    #     gathering.item26_page1 = request.POST.get('item26_page1')
    #     gathering.item26_page2 = request.POST.get('item26_page2')
    #     gathering.item26_page3 = request.POST.get('item26_page3')
    #     gathering.item26_page4 = request.POST.get('item26_page4')
    #     gathering.item26_page5 = request.POST.get('item26_page5')
    #     gathering.item26_page6 = request.POST.get('item26_page6')
    #     gathering.item26_page7 = request.POST.get('item26_page7')
    #     gathering.item26_page8 = request.POST.get('item26_page8')
    #     gathering.item26_page9 = request.POST.get('item26_page9')
    #     gathering.item26_page10 = request.POST.get('item26_page10')

    #     gathering.item27_page1 = request.POST.get('item27_page1')
    #     gathering.item27_page2 = request.POST.get('item27_page2')
    #     gathering.item27_page3 = request.POST.get('item27_page3')
    #     gathering.item27_page4 = request.POST.get('item27_page4')
    #     gathering.item27_page5 = request.POST.get('item27_page5')
    #     gathering.item27_page6 = request.POST.get('item27_page6')
    #     gathering.item27_page7 = request.POST.get('item27_page7')
    #     gathering.item27_page8 = request.POST.get('item27_page8')
    #     gathering.item27_page9 = request.POST.get('item27_page9')
    #     gathering.item27_page10 = request.POST.get('item27_page10')

    #     gathering.item28_page1 = request.POST.get('item28_page1')
    #     gathering.item28_page2 = request.POST.get('item28_page2')
    #     gathering.item28_page3 = request.POST.get('item28_page3')
    #     gathering.item28_page4 = request.POST.get('item28_page4')
    #     gathering.item28_page5 = request.POST.get('item28_page5')
    #     gathering.item28_page6 = request.POST.get('item28_page6')
    #     gathering.item28_page7 = request.POST.get('item28_page7')
    #     gathering.item28_page8 = request.POST.get('item28_page8')
    #     gathering.item28_page9 = request.POST.get('item28_page9')
    #     gathering.item28_page10 = request.POST.get('item28_page10')

    #     gathering.item29_page1 = request.POST.get('item29_page1')
    #     gathering.item29_page2 = request.POST.get('item29_page2')
    #     gathering.item29_page3 = request.POST.get('item29_page3')
    #     gathering.item29_page4 = request.POST.get('item29_page4')
    #     gathering.item29_page5 = request.POST.get('item29_page5')
    #     gathering.item29_page6 = request.POST.get('item29_page6')
    #     gathering.item29_page7 = request.POST.get('item29_page7')
    #     gathering.item29_page8 = request.POST.get('item29_page8')
    #     gathering.item29_page8 = request.POST.get('item29_page8')
    #     gathering.item29_page8 = request.POST.get('item29_page8')
    #     gathering.item29_page9 = request.POST.get('item29_page9')
    #     gathering.item29_page10 = request.POST.get('item29_page10')

    #     gathering.item30_page1 = request.POST.get('item30_page1')
    #     gathering.item30_page2 = request.POST.get('item30_page2')
    #     gathering.item30_page3 = request.POST.get('item30_page3')
    #     gathering.item30_page4 = request.POST.get('item30_page4')
    #     gathering.item30_page5 = request.POST.get('item30_page5')
    #     gathering.item30_page6 = request.POST.get('item30_page6')
    #     gathering.item30_page7 = request.POST.get('item30_page7')
    #     gathering.item30_page8 = request.POST.get('item30_page8')
    #     gathering.item30_page9 = request.POST.get('item30_page9')
    #     gathering.item30_page10 = request.POST.get('item30_page10')

    #     gathering.item31_page1 = request.POST.get('item31_page1')
    #     gathering.item31_page2 = request.POST.get('item31_page2')
    #     gathering.item31_page3 = request.POST.get('item31_page3')
    #     gathering.item31_page4 = request.POST.get('item31_page4')
    #     gathering.item31_page5 = request.POST.get('item31_page5')
    #     gathering.item31_page6 = request.POST.get('item31_page6')
    #     gathering.item31_page7 = request.POST.get('item31_page7')
    #     gathering.item31_page8 = request.POST.get('item31_page8')
    #     gathering.item31_page9 = request.POST.get('item31_page9')
    #     gathering.item31_page10 = request.POST.get('item31_page10')

    #     gathering.item32_page1 = request.POST.get('item32_page1')
    #     gathering.item32_page2 = request.POST.get('item32_page2')
    #     gathering.item32_page3 = request.POST.get('item32_page3')
    #     gathering.item32_page4 = request.POST.get('item32_page4')
    #     gathering.item32_page5 = request.POST.get('item32_page5')
    #     gathering.item32_page6 = request.POST.get('item32_page6')
    #     gathering.item32_page7 = request.POST.get('item32_page7')
    #     gathering.item32_page8 = request.POST.get('item32_page8')
    #     gathering.item32_page9 = request.POST.get('item32_page9')
    #     gathering.item32_page10 = request.POST.get('item32_page10')

    #     gathering.item33_page1 = request.POST.get('item33_page1')
    #     gathering.item33_page2 = request.POST.get('item33_page2')
    #     gathering.item33_page3 = request.POST.get('item33_page3')
    #     gathering.item33_page4 = request.POST.get('item33_page4')
    #     gathering.item33_page5 = request.POST.get('item33_page5')
    #     gathering.item33_page6 = request.POST.get('item33_page6')
    #     gathering.item33_page7 = request.POST.get('item33_page7')
    #     gathering.item33_page8 = request.POST.get('item33_page8')
    #     gathering.item33_page9 = request.POST.get('item33_page9')
    #     gathering.item33_page10 = request.POST.get('item33_page10')

    #     gathering.item34_page1 = request.POST.get('item34_page1')
    #     gathering.item34_page2 = request.POST.get('item34_page2')
    #     gathering.item34_page3 = request.POST.get('item34_page3')
    #     gathering.item34_page4 = request.POST.get('item34_page4')
    #     gathering.item34_page5 = request.POST.get('item34_page5')
    #     gathering.item34_page6 = request.POST.get('item34_page6')
    #     gathering.item34_page7 = request.POST.get('item34_page7')
    #     gathering.item34_page8 = request.POST.get('item34_page8')
    #     gathering.item34_page9 = request.POST.get('item34_page9')
    #     gathering.item34_page10 = request.POST.get('item34_page10')

    #     gathering.item35_page1 = request.POST.get('item35_page1')
    #     gathering.item35_page2 = request.POST.get('item35_page2')
    #     gathering.item35_page3 = request.POST.get('item35_page3')
    #     gathering.item35_page4 = request.POST.get('item35_page4')
    #     gathering.item35_page5 = request.POST.get('item35_page5')
    #     gathering.item35_page6 = request.POST.get('item35_page6')
    #     gathering.item35_page7 = request.POST.get('item35_page7')
    #     gathering.item35_page8 = request.POST.get('item35_page8')
    #     gathering.item35_page9 = request.POST.get('item35_page9')
    #     gathering.item35_page10 = request.POST.get('item35_page10')

    #     gathering.item36_page1 = request.POST.get('item36_page1')
    #     gathering.item36_page2 = request.POST.get('item36_page2')
    #     gathering.item36_page3 = request.POST.get('item36_page3')
    #     gathering.item36_page4 = request.POST.get('item36_page4')
    #     gathering.item36_page5 = request.POST.get('item36_page5')
    #     gathering.item36_page6 = request.POST.get('item36_page6')
    #     gathering.item36_page7 = request.POST.get('item36_page7')
    #     gathering.item36_page8 = request.POST.get('item36_page8')
    #     gathering.item36_page9 = request.POST.get('item36_page9')
    #     gathering.item36_page10 = request.POST.get('item36_page10')

    #     gathering.item37_page1 = request.POST.get('item37_page1')
    #     gathering.item37_page2 = request.POST.get('item37_page2')
    #     gathering.item37_page3 = request.POST.get('item37_page3')
    #     gathering.item37_page4 = request.POST.get('item37_page4')
    #     gathering.item37_page5 = request.POST.get('item37_page5')
    #     gathering.item37_page6 = request.POST.get('item37_page6')
    #     gathering.item37_page7 = request.POST.get('item37_page7')
    #     gathering.item37_page8 = request.POST.get('item37_page8')
    #     gathering.item37_page9 = request.POST.get('item37_page9')
    #     gathering.item37_page10 = request.POST.get('item37_page10')

    #     gathering.item38_page1 = request.POST.get('item38_page1')
    #     gathering.item38_page2 = request.POST.get('item38_page2')
    #     gathering.item38_page3 = request.POST.get('item38_page3')
    #     gathering.item38_page4 = request.POST.get('item38_page4')
    #     gathering.item38_page5 = request.POST.get('item38_page5')
    #     gathering.item38_page6 = request.POST.get('item38_page6')
    #     gathering.item38_page7 = request.POST.get('item38_page7')
    #     gathering.item38_page8 = request.POST.get('item38_page8')
    #     gathering.item38_page9 = request.POST.get('item38_page9')
    #     gathering.item38_page10 = request.POST.get('item38_page10')

    #     gathering.item39_page1 = request.POST.get('item39_page1')
    #     gathering.item39_page2 = request.POST.get('item39_page2')
    #     gathering.item39_page3 = request.POST.get('item39_page3')
    #     gathering.item39_page4 = request.POST.get('item39_page4')
    #     gathering.item39_page5 = request.POST.get('item39_page5')
    #     gathering.item39_page6 = request.POST.get('item39_page6')
    #     gathering.item39_page7 = request.POST.get('item39_page7')
    #     gathering.item39_page8 = request.POST.get('item39_page8')
    #     gathering.item39_page9 = request.POST.get('item39_page9')
    #     gathering.item39_page10 = request.POST.get('item39_page10')

    #     gathering.item40_page1 = request.POST.get('item40_page1')
    #     gathering.item40_page2 = request.POST.get('item40_page2')
    #     gathering.item40_page3 = request.POST.get('item40_page3')
    #     gathering.item40_page4 = request.POST.get('item40_page4')
    #     gathering.item40_page5 = request.POST.get('item40_page5')
    #     gathering.item40_page6 = request.POST.get('item40_page6')
    #     gathering.item40_page7 = request.POST.get('item40_page7')
    #     gathering.item40_page8 = request.POST.get('item40_page8')
    #     gathering.item40_page9 = request.POST.get('item40_page9')
    #     gathering.item40_page10 = request.POST.get('item40_page10')

    #     gathering.item41_page1 = request.POST.get('item41_page1')
    #     gathering.item41_page2 = request.POST.get('item41_page2')
    #     gathering.item41_page3 = request.POST.get('item41_page3')
    #     gathering.item41_page4 = request.POST.get('item41_page4')
    #     gathering.item41_page5 = request.POST.get('item41_page5')
    #     gathering.item41_page6 = request.POST.get('item41_page6')
    #     gathering.item41_page7 = request.POST.get('item41_page7')
    #     gathering.item41_page8 = request.POST.get('item41_page8')
    #     gathering.item41_page9 = request.POST.get('item41_page9')
    #     gathering.item41_page10 = request.POST.get('item41_page10')

    #     gathering.item42_page1 = request.POST.get('item42_page1')
    #     gathering.item42_page2 = request.POST.get('item42_page2')
    #     gathering.item42_page3 = request.POST.get('item42_page3')
    #     gathering.item42_page4 = request.POST.get('item42_page4')
    #     gathering.item42_page5 = request.POST.get('item42_page5')
    #     gathering.item42_page6 = request.POST.get('item42_page6')
    #     gathering.item42_page7 = request.POST.get('item42_page7')
    #     gathering.item42_page8 = request.POST.get('item42_page8')
    #     gathering.item42_page9 = request.POST.get('item42_page9')
    #     gathering.item42_page10 = request.POST.get('item42_page10')

    #     gathering.item43_page1 = request.POST.get('item43_page1')
    #     gathering.item43_page2 = request.POST.get('item43_page2')
    #     gathering.item43_page3 = request.POST.get('item43_page3')
    #     gathering.item43_page4 = request.POST.get('item43_page4')
    #     gathering.item43_page5 = request.POST.get('item43_page5')
    #     gathering.item43_page6 = request.POST.get('item43_page6')
    #     gathering.item43_page7 = request.POST.get('item43_page7')
    #     gathering.item43_page8 = request.POST.get('item43_page8')
    #     gathering.item43_page9 = request.POST.get('item43_page9')
    #     gathering.item43_page10 = request.POST.get('item43_page10')

    #     gathering.item44_page1 = request.POST.get('item44_page1')
    #     gathering.item44_page2 = request.POST.get('item44_page2')
    #     gathering.item44_page3 = request.POST.get('item44_page3')
    #     gathering.item44_page4 = request.POST.get('item44_page4')
    #     gathering.item44_page5 = request.POST.get('item44_page5')
    #     gathering.item44_page6 = request.POST.get('item44_page6')
    #     gathering.item44_page7 = request.POST.get('item44_page7')
    #     gathering.item44_page8 = request.POST.get('item44_page8')
    #     gathering.item44_page9 = request.POST.get('item44_page9')
    #     gathering.item44_page10 = request.POST.get('item44_page10')

    #     gathering.item45_page1 = request.POST.get('item45_page1')
    #     gathering.item45_page2 = request.POST.get('item45_page2')
    #     gathering.item45_page3 = request.POST.get('item45_page3')
    #     gathering.item45_page4 = request.POST.get('item45_page4')
    #     gathering.item45_page5 = request.POST.get('item45_page5')
    #     gathering.item45_page6 = request.POST.get('item45_page6')
    #     gathering.item45_page7 = request.POST.get('item45_page7')
    #     gathering.item45_page8 = request.POST.get('item45_page8')
    #     gathering.item45_page9 = request.POST.get('item45_page9')
    #     gathering.item45_page10 = request.POST.get('item45_page10')

    #     gathering.item46_page1 = request.POST.get('item46_page1')
    #     gathering.item46_page2 = request.POST.get('item46_page2')
    #     gathering.item46_page3 = request.POST.get('item46_page3')
    #     gathering.item46_page4 = request.POST.get('item46_page4')
    #     gathering.item46_page5 = request.POST.get('item46_page5')
    #     gathering.item46_page6 = request.POST.get('item46_page6')
    #     gathering.item46_page7 = request.POST.get('item46_page7')
    #     gathering.item46_page8 = request.POST.get('item46_page8')
    #     gathering.item46_page9 = request.POST.get('item46_page9')
    #     gathering.item46_page10 = request.POST.get('item46_page10')

    #     gathering.item47_page1 = request.POST.get('item47_page1')
    #     gathering.item47_page2 = request.POST.get('item47_page2')
    #     gathering.item47_page3 = request.POST.get('item47_page3')
    #     gathering.item47_page4 = request.POST.get('item47_page4')
    #     gathering.item47_page5 = request.POST.get('item47_page5')
    #     gathering.item47_page6 = request.POST.get('item47_page6')
    #     gathering.item47_page7 = request.POST.get('item47_page7')
    #     gathering.item47_page8 = request.POST.get('item47_page8')
    #     gathering.item47_page9 = request.POST.get('item47_page9')
    #     gathering.item47_page10 = request.POST.get('item47_page10')

    #     gathering.item48_page1 = request.POST.get('item48_page1')
    #     gathering.item48_page2 = request.POST.get('item48_page2')
    #     gathering.item48_page3 = request.POST.get('item48_page3')
    #     gathering.item48_page4 = request.POST.get('item48_page4')
    #     gathering.item48_page5 = request.POST.get('item48_page5')
    #     gathering.item48_page6 = request.POST.get('item48_page6')
    #     gathering.item48_page7 = request.POST.get('item48_page7')
    #     gathering.item48_page8 = request.POST.get('item48_page8')
    #     gathering.item48_page9 = request.POST.get('item48_page9')
    #     gathering.item48_page10 = request.POST.get('item48_page10')

    #     gathering.item49_page1 = request.POST.get('item49_page1')
    #     gathering.item49_page2 = request.POST.get('item49_page2')
    #     gathering.item49_page3 = request.POST.get('item49_page3')
    #     gathering.item49_page3 = request.POST.get('item49_page3')
    #     gathering.item49_page3 = request.POST.get('item49_page3')
    #     gathering.item49_page4 = request.POST.get('item49_page4')
    #     gathering.item49_page5 = request.POST.get('item49_page5')
    #     gathering.item49_page6 = request.POST.get('item49_page6')
    #     gathering.item49_page7 = request.POST.get('item49_page7')
    #     gathering.item49_page8 = request.POST.get('item49_page8')
    #     gathering.item49_page9 = request.POST.get('item49_page9')
    #     gathering.item49_page10 = request.POST.get('item49_page10')

    #     gathering.item50_page1 = request.POST.get('item50_page1')
    #     gathering.item50_page2 = request.POST.get('item50_page2')
    #     gathering.item50_page3 = request.POST.get('item50_page3')
    #     gathering.item50_page4 = request.POST.get('item50_page4')
    #     gathering.item50_page5 = request.POST.get('item50_page5')
    #     gathering.item50_page6 = request.POST.get('item50_page6')
    #     gathering.item50_page7 = request.POST.get('item50_page7')
    #     gathering.item50_page8 = request.POST.get('item50_page8')
    #     gathering.item50_page9 = request.POST.get('item50_page9')
    #     gathering.item50_page10 = request.POST.get('item50_page10')

    #     gathering.total_gathering=request.POST.get('printing_received_form')
    #     gathering.wastage_form = request.POST.get('print_wastage_form')
    #     gathering.gathering_date = request.POST.get('print_date')
    #     gathering.gathering_date = datetime.datetime.now()
    #     temp_page1=[]
    #     if gathering.item1_page1:
    #         temp_page1.append(gathering.item1_page1)
    #     if gathering.item1_page2:
    #         temp_page1.append(gathering.item1_page2)
    #     if gathering.item1_page3:
    #         temp_page1.append(gathering.item1_page3)
    #     if gathering.item1_page4:
    #         temp_page1.append(gathering.item1_page4)
    #     if gathering.item1_page5:
    #         temp_page1.append(gathering.item1_page5)
    #     if gathering.item1_page6:
    #         temp_page1.append(gathering.item1_page6)
    #     if gathering.item1_page7:
    #         temp_page1.append(gathering.item1_page7)
    #     if gathering.item1_page8:
    #         temp_page1.append(gathering.item1_page8)
    #     if gathering.item1_page9:
    #         temp_page1.append(gathering.item1_page9)
    #     if gathering.item1_page10:
    #         temp_page1.append(gathering.item1_page10)
        
    #     temp_page1=[int(i) for i in temp_page1] 
    #     temp_page1.sort(reverse=False)
    
    #     if temp_page1:
    #         gathering.total_gathering_1=temp_page1[0]
    #         gathering.wastage_form_1 = float(gathering.quantity_1) - float(gathering.total_gathering_1)
    #     else:
    #         gathering.item1_page1=0
    #         gathering.item1_page2=0
    #         gathering.item1_page3=0
    #         gathering.item1_page4=0
    #         gathering.item1_page5=0
    #         gathering.item1_page6=0
    #         gathering.item1_page7=0
    #         gathering.item1_page8=0
    #         gathering.item1_page9=0
    #         gathering.item1_page10=0

    


    #     temp_page2=[]
    #     if gathering.item2_page1:
    #         temp_page2.append(gathering.item2_page1)
    #     if gathering.item2_page2:
    #         temp_page2.append(gathering.item2_page2)
    #     if gathering.item2_page3:
    #         temp_page2.append(gathering.item2_page3)
    #     if gathering.item2_page4:
    #         temp_page2.append(gathering.item2_page4)
    #     if gathering.item2_page5:
    #         temp_page2.append(gathering.item2_page5)
    #     if gathering.item2_page6:
    #         temp_page2.append(gathering.item2_page6)
    #     if gathering.item2_page7:
    #         temp_page2.append(gathering.item2_page7)
    #     if gathering.item2_page8:
    #         temp_page2.append(gathering.item2_page8)
    #     if gathering.item2_page9:
    #         temp_page2.append(gathering.item2_page9)
    #     if gathering.item2_page10:
    #         temp_page2.append(gathering.item2_page10)
    #     temp_page2=[int(i) for i in temp_page2]
    #     temp_page2.sort(reverse=False)
        
    
        
    #     if temp_page2:
    #         gathering.total_gathering_2=temp_page2[0]
    #         gathering.wastage_form_2 = float(gathering.quantity_2) - float(gathering.total_gathering_2)
    #     else:
    #         gathering.item2_page1=0
    #         gathering.item2_page2=0
    #         gathering.item2_page3=0
    #         gathering.item2_page4=0
    #         gathering.item2_page5=0
    #         gathering.item2_page6=0
    #         gathering.item2_page7=0
    #         gathering.item2_page8=0
    #         gathering.item2_page9=0
    #         gathering.item2_page10=0


    #     temp_page3=[]
    #     if gathering.item3_page1:
    #         temp_page3.append(gathering.item3_page1)
    #     if gathering.item3_page2:
    #         temp_page3.append(gathering.item3_page2)
    #     if gathering.item3_page3:
    #         temp_page3.append(gathering.item3_page3)
    #     if gathering.item3_page4:
    #         temp_page3.append(gathering.item3_page4)
    #     if gathering.item3_page5:
    #         temp_page3.append(gathering.item3_page5)
    #     if gathering.item3_page6:
    #         temp_page3.append(gathering.item3_page6)
    #     if gathering.item3_page7:
    #         temp_page3.append(gathering.item3_page7)
    #     if gathering.item3_page8:
    #         temp_page3.append(gathering.item3_page8)
    #     if gathering.item3_page9:
    #         temp_page3.append(gathering.item3_page9)
    #     if gathering.item3_page10:
    #         temp_page3.append(gathering.item3_page10)
    #     temp_page3=[int(i) for i in temp_page3]
    #     temp_page3.sort(reverse=False)
        
        
        
    #     if temp_page3:
    #         gathering.total_gathering_3=temp_page3[0]
    #         gathering.wastage_form_3 = float(gathering.quantity_3) - float(gathering.total_gathering_3)
    #     else:
    #         gathering.item3_page1=0
    #         gathering.item3_page2=0
    #         gathering.item3_page3=0
    #         gathering.item3_page4=0
    #         gathering.item3_page5=0
    #         gathering.item3_page6=0
    #         gathering.item3_page7=0
    #         gathering.item3_page8=0
    #         gathering.item3_page9=0
    #         gathering.item3_page10=0


    #     temp_page4=[]
    #     if gathering.item4_page1:
    #         temp_page4.append(gathering.item4_page1)
    #     if gathering.item4_page2:
    #         temp_page4.append(gathering.item4_page2)
    #     if gathering.item4_page3:
    #         temp_page4.append(gathering.item4_page3)
    #     if gathering.item4_page4:
    #         temp_page4.append(gathering.item4_page4)
    #     if gathering.item4_page5:
    #         temp_page4.append(gathering.item4_page5)
    #     if gathering.item4_page6:
    #         temp_page4.append(gathering.item4_page6)
    #     if gathering.item4_page7:
    #         temp_page4.append(gathering.item4_page7)
    #     if gathering.item4_page8:
    #         temp_page4.append(gathering.item4_page8)
    #     if gathering.item4_page9:
    #         temp_page4.append(gathering.item4_page9)
    #     if gathering.item4_page10:
    #         temp_page4.append(gathering.item4_page10)
    #     temp_page4=[int(i) for i in temp_page4]
    #     temp_page4.sort(reverse=False)
    
    
        
    #     if temp_page4:
    #         gathering.total_gathering_4=temp_page4[0]
    #         gathering.wastage_form_4 = float(gathering.quantity_4) - float(gathering.total_gathering_4)
    #     else:
    #         gathering.item4_page1=0
    #         gathering.item4_page2=0
    #         gathering.item4_page3=0
    #         gathering.item4_page4=0
    #         gathering.item4_page5=0
    #         gathering.item4_page6=0
    #         gathering.item4_page7=0
    #         gathering.item4_page8=0
    #         gathering.item4_page9=0
    #         gathering.item4_page10=0



    #     temp_page5=[]
    #     if gathering.item5_page1:
    #         temp_page5.append(gathering.item5_page1)
    #     if gathering.item5_page2:
    #         temp_page5.append(gathering.item5_page2)
    #     if gathering.item5_page3:
    #         temp_page5.append(gathering.item5_page3)
    #     if gathering.item5_page4:
    #         temp_page5.append(gathering.item5_page4)
    #     if gathering.item5_page5:
    #         temp_page5.append(gathering.item5_page5)
    #     if gathering.item5_page6:
    #         temp_page5.append(gathering.item5_page6)
    #     if gathering.item5_page7:
    #         temp_page5.append(gathering.item5_page7)
    #     if gathering.item5_page8:
    #         temp_page5.append(gathering.item5_page8)
    #     if gathering.item5_page9:
    #         temp_page5.append(gathering.item5_page9)
    #     if gathering.item5_page10:
    #         temp_page5.append(gathering.item5_page10)
    #     temp_page5=[int(i) for i in temp_page5]
    #     temp_page5.sort(reverse=False)
    

        
    #     if temp_page5:
    #         gathering.total_gathering_5=temp_page5[0]
    #         gathering.wastage_form_5 = float(gathering.quantity_5) - float(gathering.total_gathering_5)
    #     else:
    #         gathering.item5_page1=0
    #         gathering.item5_page2=0
    #         gathering.item5_page3=0
    #         gathering.item5_page4=0
    #         gathering.item5_page5=0
    #         gathering.item5_page6=0
    #         gathering.item5_page7=0
    #         gathering.item5_page8=0
    #         gathering.item5_page9=0
    #         gathering.item5_page10=0



    #     temp_page6=[]
    #     if gathering.item6_page1:
    #         temp_page6.append(gathering.item6_page1)
    #     if gathering.item6_page2:
    #         temp_page6.append(gathering.item6_page2)
    #     if gathering.item6_page3:
    #         temp_page6.append(gathering.item6_page3)
    #     if gathering.item6_page4:
    #         temp_page6.append(gathering.item6_page4)
    #     if gathering.item6_page5:
    #         temp_page6.append(gathering.item6_page5)
    #     if gathering.item6_page6:
    #         temp_page6.append(gathering.item6_page6)
    #     if gathering.item6_page7:
    #         temp_page6.append(gathering.item6_page7)
    #     if gathering.item6_page8:
    #         temp_page6.append(gathering.item6_page8)
    #     if gathering.item6_page9:
    #         temp_page6.append(gathering.item6_page9)
    #     if gathering.item6_page10:
    #         temp_page6.append(gathering.item6_page10)
    #     temp_page6=[int(i) for i in temp_page6]
    #     temp_page6.sort(reverse=False)
    
        
        
    #     if temp_page6:
    #         gathering.total_gathering_6=temp_page6[0]
    #         gathering.wastage_form_6 = float(gathering.quantity_6) - float(gathering.total_gathering_6)
    #     else:
    #         gathering.item6_page1=0
    #         gathering.item6_page2=0
    #         gathering.item6_page3=0
    #         gathering.item6_page4=0
    #         gathering.item6_page5=0
    #         gathering.item6_page6=0
    #         gathering.item6_page7=0
    #         gathering.item6_page8=0
    #         gathering.item6_page9=0
    #         gathering.item6_page10=0


    #     temp_page7=[]
    #     if gathering.item7_page1:
    #         temp_page7.append(gathering.item7_page1)
    #     if gathering.item7_page2:
    #         temp_page7.append(gathering.item7_page2)
    #     if gathering.item7_page3:
    #         temp_page7.append(gathering.item7_page3)
    #     if gathering.item7_page4:
    #         temp_page7.append(gathering.item7_page4)
    #     if gathering.item7_page5:
    #         temp_page7.append(gathering.item7_page5)
    #     if gathering.item7_page6:
    #         temp_page7.append(gathering.item7_page6)
    #     if gathering.item7_page7:
    #         temp_page7.append(gathering.item7_page7)
    #     if gathering.item7_page8:
    #         temp_page7.append(gathering.item7_page8)
    #     if gathering.item7_page9:
    #         temp_page7.append(gathering.item7_page9)
    #     if gathering.item7_page10:
    #         temp_page7.append(gathering.item7_page10)
    #     temp_page7=[int(i) for i in temp_page7]
    #     temp_page7.sort(reverse=False)
        
        
    #     if temp_page7:
    #         gathering.total_gathering_7=temp_page7[0]
    #         gathering.wastage_form_7 = float(gathering.quantity_7) - float(gathering.total_gathering_7)
    #     else:
    #         gathering.item7_page1=0
    #         gathering.item7_page2=0
    #         gathering.item7_page3=0
    #         gathering.item7_page4=0
    #         gathering.item7_page5=0
    #         gathering.item7_page6=0
    #         gathering.item7_page7=0
    #         gathering.item7_page8=0
    #         gathering.item7_page9=0
    #         gathering.item7_page10=0



    #     temp_page8=[]
    #     if gathering.item8_page1:
    #         temp_page8.append(gathering.item8_page1)
    #     if gathering.item8_page2:
    #         temp_page8.append(gathering.item8_page2)
    #     if gathering.item8_page3:
    #         temp_page8.append(gathering.item8_page3)
    #     if gathering.item8_page4:
    #         temp_page8.append(gathering.item8_page4)
    #     if gathering.item8_page5:
    #         temp_page8.append(gathering.item8_page5)
    #     if gathering.item8_page6:
    #         temp_page8.append(gathering.item8_page6)
    #     if gathering.item8_page7:
    #         temp_page8.append(gathering.item8_page7)
    #     if gathering.item8_page8:
    #         temp_page8.append(gathering.item8_page8)
    #     if gathering.item8_page9:
    #         temp_page8.append(gathering.item8_page9)
    #     if gathering.item8_page10:
    #         temp_page8.append(gathering.item8_page10)
    #     temp_page8=[int(i) for i in temp_page8]
    #     temp_page8.sort(reverse=False)
        
        
    #     if temp_page8:
    #         gathering.total_gathering_8=temp_page8[0]
    #         gathering.wastage_form_8 = float(gathering.quantity_8) - float(gathering.total_gathering_8)
    #     else:
    #         gathering.item8_page1=0
    #         gathering.item8_page2=0
    #         gathering.item8_page3=0
    #         gathering.item8_page4=0
    #         gathering.item8_page5=0
    #         gathering.item8_page6=0
    #         gathering.item8_page7=0
    #         gathering.item8_page8=0
    #         gathering.item8_page9=0
    #         gathering.item8_page10=0



    #     temp_page9=[]
    #     if gathering.item9_page1:
    #         temp_page9.append(gathering.item9_page1)
    #     if gathering.item9_page2:
    #         temp_page9.append(gathering.item9_page2)
    #     if gathering.item9_page3:
    #         temp_page9.append(gathering.item9_page3)
    #     if gathering.item9_page4:
    #         temp_page9.append(gathering.item9_page4)
    #     if gathering.item9_page5:
    #         temp_page9.append(gathering.item9_page5)
    #     if gathering.item9_page6:
    #         temp_page9.append(gathering.item9_page6)
    #     if gathering.item9_page7:
    #         temp_page9.append(gathering.item9_page7)
    #     if gathering.item9_page8:
    #         temp_page9.append(gathering.item9_page8)
    #     if gathering.item9_page9:
    #         temp_page9.append(gathering.item9_page9)
    #     if gathering.item9_page10:
    #         temp_page9.append(gathering.item9_page10)
    #     temp_page9=[int(i) for i in temp_page9]
    #     temp_page9.sort(reverse=False)
    
    
        
    #     if temp_page9:
    #         gathering.total_gathering_9=temp_page9[0]
    #         gathering.wastage_form_9 = float(gathering.quantity_9) - float(gathering.total_gathering_9)
    #     else:
    #         gathering.item9_page1=0
    #         gathering.item9_page2=0
    #         gathering.item9_page3=0
    #         gathering.item9_page4=0
    #         gathering.item9_page5=0
    #         gathering.item9_page6=0
    #         gathering.item9_page7=0
    #         gathering.item9_page8=0
    #         gathering.item9_page9=0
    #         gathering.item9_page10=0




    #     temp_page10=[]
    #     if gathering.item10_page1:
    #         temp_page10.append(gathering.item10_page1)
    #     if gathering.item10_page2:
    #         temp_page10.append(gathering.item10_page2)
    #     if gathering.item10_page3:
    #         temp_page10.append(gathering.item10_page3)
    #     if gathering.item10_page4:
    #         temp_page10.append(gathering.item10_page4)
    #     if gathering.item10_page5:
    #         temp_page10.append(gathering.item10_page5)
    #     if gathering.item10_page6:
    #         temp_page10.append(gathering.item10_page6)
    #     if gathering.item10_page7:
    #         temp_page10.append(gathering.item10_page7)
    #     if gathering.item10_page8:
    #         temp_page10.append(gathering.item10_page8)
    #     if gathering.item10_page9:
    #         temp_page10.append(gathering.item10_page9)
    #     if gathering.item10_page10:
    #         temp_page10.append(gathering.item10_page10)
    #     temp_page10=[int(i) for i in temp_page10]
    #     temp_page10.sort(reverse=False)
    
    
        
    #     if temp_page10:
    #         gathering.total_gathering_10=temp_page10[0]
    #         gathering.wastage_form_10 = float(gathering.quantity_10) - float(gathering.total_gathering_10)
    #     else:
    #         gathering.item10_page1=0
    #         gathering.item10_page2=0
    #         gathering.item10_page3=0
    #         gathering.item10_page4=0
    #         gathering.item10_page5=0
    #         gathering.item10_page6=0
    #         gathering.item10_page7=0
    #         gathering.item10_page8=0
    #         gathering.item10_page9=0
    #         gathering.item10_page10=0



    #     temp_page11=[]
    #     if gathering.item11_page1:
    #         temp_page11.append(gathering.item11_page1)
    #     if gathering.item11_page2:
    #         temp_page11.append(gathering.item11_page2)
    #     if gathering.item11_page3:
    #         temp_page11.append(gathering.item11_page3)
    #     if gathering.item11_page4:
    #         temp_page11.append(gathering.item11_page4)
    #     if gathering.item11_page5:
    #         temp_page11.append(gathering.item11_page5)
    #     if gathering.item11_page6:
    #         temp_page11.append(gathering.item11_page6)
    #     if gathering.item11_page7:
    #         temp_page11.append(gathering.item11_page7)
    #     if gathering.item11_page8:
    #         temp_page11.append(gathering.item11_page8)
    #     if gathering.item11_page9:
    #         temp_page11.append(gathering.item11_page9)
    #     if gathering.item11_page10:
    #         temp_page11.append(gathering.item11_page10)
    #     temp_page11=[int(i) for i in temp_page11]
    #     temp_page11.sort(reverse=False)

    #     if temp_page11:
    #         gathering.total_gathering_11=temp_page11[0]
    #         gathering.wastage_form_11 = float(gathering.quantity_11) - float(gathering.total_gathering_11)
    #     else:
    #         gathering.item11_page1=0
    #         gathering.item11_page2=0
    #         gathering.item11_page3=0
    #         gathering.item11_page4=0
    #         gathering.item11_page5=0
    #         gathering.item11_page6=0
    #         gathering.item11_page7=0
    #         gathering.item11_page8=0
    #         gathering.item11_page9=0
    #         gathering.item11_page10=0



    #     temp_page12=[]
    #     if gathering.item12_page1:
    #         temp_page12.append(gathering.item12_page1)
    #     if gathering.item12_page2:
    #         temp_page12.append(gathering.item12_page2)
    #     if gathering.item12_page3:
    #         temp_page12.append(gathering.item12_page3)
    #     if gathering.item12_page4:
    #         temp_page12.append(gathering.item12_page4)
    #     if gathering.item12_page5:
    #         temp_page12.append(gathering.item12_page5)
    #     if gathering.item12_page6:
    #         temp_page12.append(gathering.item12_page6)
    #     if gathering.item12_page7:
    #         temp_page12.append(gathering.item12_page7)
    #     if gathering.item12_page8:
    #         temp_page12.append(gathering.item12_page8)
    #     if gathering.item12_page9:
    #         temp_page12.append(gathering.item12_page9)
    #     if gathering.item12_page10:
    #         temp_page12.append(gathering.item12_page10)
        
    #     temp_page12=[int(i) for i in temp_page12] 
    #     temp_page12.sort(reverse=False)

    #     if temp_page12:
    #         gathering.total_gathering_12=temp_page1[0]
    #         gathering.wastage_form_12 = float(gathering.quantity_12) - float(gathering.total_gathering_12)
    #     else:
    #         gathering.item12_page1=0
    #         gathering.item12_page2=0
    #         gathering.item12_page3=0
    #         gathering.item12_page4=0
    #         gathering.item12_page5=0
    #         gathering.item12_page6=0
    #         gathering.item12_page7=0
    #         gathering.item12_page8=0
    #         gathering.item12_page9=0
    #         gathering.item12_page10=0

    


    #     temp_page13=[]
    #     if gathering.item13_page1:
    #         temp_page13.append(gathering.item13_page1)
    #     if gathering.item13_page2:
    #         temp_page13.append(gathering.item13_page2)
    #     if gathering.item13_page3:
    #         temp_page13.append(gathering.item13_page3)
    #     if gathering.item13_page4:
    #         temp_page13.append(gathering.item13_page4)
    #     if gathering.item13_page5:
    #         temp_page13.append(gathering.item13_page5)
    #     if gathering.item13_page6:
    #         temp_page13.append(gathering.item13_page6)
    #     if gathering.item13_page7:
    #         temp_page13.append(gathering.item13_page7)
    #     if gathering.item13_page8:
    #         temp_page13.append(gathering.item13_page8)
    #     if gathering.item13_page9:
    #         temp_page13.append(gathering.item13_page9)
    #     if gathering.item13_page10:
    #         temp_page13.append(gathering.item13_page10)
    #     temp_page13=[int(i) for i in temp_page13]
    #     temp_page13.sort(reverse=False)
        
    
        
    #     if temp_page13:
    #         gathering.total_gathering_13=temp_page13[0]
    #         gathering.wastage_form_13 = float(gathering.quantity_13) - float(gathering.total_gathering_13)
    #     else:
    #         gathering.item13_page1=0
    #         gathering.item13_page2=0
    #         gathering.item13_page3=0
    #         gathering.item13_page4=0
    #         gathering.item13_page5=0
    #         gathering.item13_page6=0
    #         gathering.item13_page7=0
    #         gathering.item13_page8=0
    #         gathering.item13_page9=0
    #         gathering.item13_page10=0


    #     temp_page14=[]
    #     if gathering.item14_page1:
    #         temp_page14.append(gathering.item14_page1)
    #     if gathering.item14_page2:
    #         temp_page14.append(gathering.item14_page2)
    #     if gathering.item14_page3:
    #         temp_page14.append(gathering.item14_page3)
    #     if gathering.item14_page4:
    #         temp_page14.append(gathering.item14_page4)
    #     if gathering.item14_page5:
    #         temp_page14.append(gathering.item14_page5)
    #     if gathering.item14_page6:
    #         temp_page14.append(gathering.item14_page6)
    #     if gathering.item14_page7:
    #         temp_page14.append(gathering.item14_page7)
    #     if gathering.item14_page8:
    #         temp_page14.append(gathering.item14_page8)
    #     if gathering.item14_page9:
    #         temp_page14.append(gathering.item14_page9)
    #     if gathering.item14_page10:
    #         temp_page14.append(gathering.item14_page10)
    #     temp_page14=[int(i) for i in temp_page14]
    #     temp_page14.sort(reverse=False)
        
        
        
    #     if temp_page14:
    #         gathering.total_gathering_14=temp_page14[0]
    #         gathering.wastage_form_14 = float(gathering.quantity_14) - float(gathering.total_gathering_14)
    #     else:
    #         gathering.item14_page1=0
    #         gathering.item14_page2=0
    #         gathering.item14_page3=0
    #         gathering.item14_page4=0
    #         gathering.item14_page5=0
    #         gathering.item14_page6=0
    #         gathering.item14_page7=0
    #         gathering.item14_page8=0
    #         gathering.item14_page9=0
    #         gathering.item14_page10=0


    #     temp_page15=[]
    #     if gathering.item15_page1:
    #         temp_page15.append(gathering.item15_page1)
    #     if gathering.item15_page2:
    #         temp_page15.append(gathering.item15_page2)
    #     if gathering.item15_page3:
    #         temp_page15.append(gathering.item15_page3)
    #     if gathering.item15_page4:
    #         temp_page15.append(gathering.item15_page4)
    #     if gathering.item15_page5:
    #         temp_page15.append(gathering.item15_page5)
    #     if gathering.item15_page6:
    #         temp_page15.append(gathering.item15_page6)
    #     if gathering.item15_page7:
    #         temp_page15.append(gathering.item15_page7)
    #     if gathering.item15_page8:
    #         temp_page15.append(gathering.item15_page8)
    #     if gathering.item15_page9:
    #         temp_page15.append(gathering.item15_page9)
    #     if gathering.item15_page10:
    #         temp_page15.append(gathering.item15_page10)
    #     temp_page15=[int(i) for i in temp_page15]
    #     temp_page15.sort(reverse=False)
    
    
        
    #     if temp_page15:
    #         gathering.total_gathering_15=temp_page15[0]
    #         gathering.wastage_form_15 = float(gathering.quantity_15) - float(gathering.total_gathering_15)
    #     else:
    #         gathering.item15_page1=0
    #         gathering.item15_page2=0
    #         gathering.item15_page3=0
    #         gathering.item15_page4=0
    #         gathering.item15_page5=0
    #         gathering.item15_page6=0
    #         gathering.item15_page7=0
    #         gathering.item15_page8=0
    #         gathering.item15_page9=0
    #         gathering.item15_page10=0




        

    #     temp_page16=[]
    #     if gathering.item16_page1:
    #         temp_page16.append(gathering.item16_page1)
    #     if gathering.item16_page2:
    #         temp_page16.append(gathering.item16_page2)
    #     if gathering.item16_page3:
    #         temp_page16.append(gathering.item16_page3)
    #     if gathering.item16_page4:
    #         temp_page16.append(gathering.item16_page4)
    #     if gathering.item16_page5:
    #         temp_page16.append(gathering.item16_page5)
    #     if gathering.item16_page6:
    #         temp_page16.append(gathering.item16_page6)
    #     if gathering.item16_page7:
    #         temp_page16.append(gathering.item16_page7)
    #     if gathering.item16_page8:
    #         temp_page16.append(gathering.item16_page8)
    #     if gathering.item16_page9:
    #         temp_page16.append(gathering.item16_page9)
    #     if gathering.item16_page10:
    #         temp_page16.append(gathering.item16_page10)
    #     temp_page16=[int(i) for i in temp_page16]
    #     temp_page16.sort(reverse=False)
    
        
        
    #     if temp_page16:
    #         gathering.total_gathering_16=temp_page16[0]
    #         gathering.wastage_form_16 = float(gathering.quantity_16) - float(gathering.total_gathering_16)
    #     else:
    #         gathering.item16_page1=0
    #         gathering.item16_page2=0
    #         gathering.item16_page3=0
    #         gathering.item16_page4=0
    #         gathering.item16_page5=0
    #         gathering.item16_page6=0
    #         gathering.item16_page7=0
    #         gathering.item16_page8=0
    #         gathering.item16_page9=0
    #         gathering.item16_page10=0


    #     temp_page17=[]
    #     if gathering.item17_page1:
    #         temp_page17.append(gathering.item17_page1)
    #     if gathering.item17_page2:
    #         temp_page17.append(gathering.item17_page2)
    #     if gathering.item17_page3:
    #         temp_page17.append(gathering.item17_page3)
    #     if gathering.item7_page4:
    #         temp_page17.append(gathering.item17_page4)
    #     if gathering.item17_page5:
    #         temp_page17.append(gathering.item17_page5)
    #     if gathering.item17_page6:
    #         temp_page17.append(gathering.item17_page6)
    #     if gathering.item17_page7:
    #         temp_page17.append(gathering.item17_page7)
    #     if gathering.item17_page8:
    #         temp_page17.append(gathering.item17_page8)
    #     if gathering.item17_page9:
    #         temp_page17.append(gathering.item17_page9)
    #     if gathering.item17_page10:
    #         temp_page17.append(gathering.item17_page10)
    #     temp_page17=[int(i) for i in temp_page17]
    #     temp_page17.sort(reverse=False)
        
        
    #     if temp_page17:
    #         gathering.total_gathering_17=temp_page17[0]
    #         gathering.wastage_form_17 = float(gathering.quantity_17) - float(gathering.total_gathering_17)
    #     else:
    #         gathering.item17_page1=0
    #         gathering.item17_page2=0
    #         gathering.item17_page3=0
    #         gathering.item17_page4=0
    #         gathering.item17_page5=0
    #         gathering.item17_page6=0
    #         gathering.item17_page7=0
    #         gathering.item17_page8=0
    #         gathering.item17_page9=0
    #         gathering.item17_page10=0



    #     temp_page18=[]
    #     if gathering.item18_page1:
    #         temp_page18.append(gathering.item18_page1)
    #     if gathering.item18_page2:
    #         temp_page18.append(gathering.item18_page2)
    #     if gathering.item18_page3:
    #         temp_page18.append(gathering.item18_page3)
    #     if gathering.item18_page4:
    #         temp_page18.append(gathering.item18_page4)
    #     if gathering.item18_page5:
    #         temp_page18.append(gathering.item18_page5)
    #     if gathering.item18_page6:
    #         temp_page18.append(gathering.item18_page6)
    #     if gathering.item18_page7:
    #         temp_page18.append(gathering.item18_page7)
    #     if gathering.item18_page8:
    #         temp_page18.append(gathering.item18_page8)
    #     if gathering.item18_page9:
    #         temp_page18.append(gathering.item18_page9)
    #     if gathering.item18_page10:
    #         temp_page18.append(gathering.item18_page10)
    #     temp_page18=[int(i) for i in temp_page18]
    #     temp_page18.sort(reverse=False)
        
        
    #     if temp_page18:
    #         gathering.total_gathering_18=temp_page18[0]
    #         gathering.wastage_form_18 = float(gathering.quantity_18) - float(gathering.total_gathering_18)
    #     else:
    #         gathering.item18_page1=0
    #         gathering.item18_page2=0
    #         gathering.item18_page3=0
    #         gathering.item18_page4=0
    #         gathering.item18_page5=0
    #         gathering.item18_page6=0
    #         gathering.item18_page7=0
    #         gathering.item18_page8=0
    #         gathering.item18_page9=0
    #         gathering.item18_page10=0



    #     temp_page19=[]
    #     if gathering.item19_page1:
    #         temp_page19.append(gathering.item19_page1)
    #     if gathering.item19_page2:
    #         temp_page19.append(gathering.item19_page2)
    #     if gathering.item19_page3:
    #         temp_page19.append(gathering.item19_page3)
    #     if gathering.item19_page4:
    #         temp_page19.append(gathering.item19_page4)
    #     if gathering.item19_page5:
    #         temp_page19.append(gathering.item19_page5)
    #     if gathering.item19_page6:
    #         temp_page19.append(gathering.item19_page6)
    #     if gathering.item19_page7:
    #         temp_page19.append(gathering.item19_page7)
    #     if gathering.item19_page8:
    #         temp_page19.append(gathering.item19_page8)
    #     if gathering.item19_page9:
    #         temp_page19.append(gathering.item19_page9)
    #     if gathering.item19_page10:
    #         temp_page19.append(gathering.item19_page10)
    #     temp_page19=[int(i) for i in temp_page19]
    #     temp_page19.sort(reverse=False)
    
    
        
    #     if temp_page19:
    #         gathering.total_gathering_19=temp_page19[0]
    #         gathering.wastage_form_19 = float(gathering.quantity_19) - float(gathering.total_gathering_19)
    #     else:
    #         gathering.item19_page1=0
    #         gathering.item19_page2=0
    #         gathering.item19_page3=0
    #         gathering.item19_page4=0
    #         gathering.item19_page5=0
    #         gathering.item19_page6=0
    #         gathering.item19_page7=0
    #         gathering.item19_page8=0
    #         gathering.item19_page9=0
    #         gathering.item19_page10=0




    #     temp_page20=[]
    #     if gathering.item20_page1:
    #         temp_page20.append(gathering.item20_page1)
    #     if gathering.item20_page2:
    #         temp_page20.append(gathering.item20_page2)
    #     if gathering.item20_page3:
    #         temp_page20.append(gathering.item20_page3)
    #     if gathering.item20_page4:
    #         temp_page20.append(gathering.item20_page4)
    #     if gathering.item20_page5:
    #         temp_page20.append(gathering.item20_page5)
    #     if gathering.item20_page6:
    #         temp_page20.append(gathering.item20_page6)
    #     if gathering.item20_page7:
    #         temp_page20.append(gathering.item20_page7)
    #     if gathering.item20_page8:
    #         temp_page20.append(gathering.item20_page8)
    #     if gathering.item20_page9:
    #         temp_page20.append(gathering.item20_page9)
    #     if gathering.item20_page10:
    #         temp_page20.append(gathering.item20_page10)
    #     temp_page20=[int(i) for i in temp_page20]
    #     temp_page20.sort(reverse=False)
    
    
        
    #     if temp_page20:
    #         gathering.total_gathering_20=temp_page20[0]
    #         gathering.wastage_form_20 = float(gathering.quantity_20) - float(gathering.total_gathering_20)
    #     else:
    #         gathering.item20_page1=0
    #         gathering.item20_page2=0
    #         gathering.item20_page3=0
    #         gathering.item20_page4=0
    #         gathering.item20_page5=0
    #         gathering.item20_page6=0
    #         gathering.item20_page7=0
    #         gathering.item20_page8=0
    #         gathering.item20_page9=0
    #         gathering.item20_page10=0
    
    
        
    #     temp_page21=[]
    #     if gathering.item21_page1:
    #         temp_page21.append(gathering.item21_page1)
    #     if gathering.item21_page2:
    #         temp_page21.append(gathering.item21_page2)
    #     if gathering.item21_page3:
    #         temp_page21.append(gathering.item21_page3)
    #     if gathering.item21_page4:
    #         temp_page21.append(gathering.item21_page4)
    #     if gathering.item21_page5:
    #         temp_page21.append(gathering.item21_page5)
    #     if gathering.item21_page6:
    #         temp_page21.append(gathering.item21_page6)
    #     if gathering.item21_page7:
    #         temp_page21.append(gathering.item21_page7)
    #     if gathering.item21_page8:
    #         temp_page21.append(gathering.item21_page8)
    #     if gathering.item21_page9:
    #         temp_page21.append(gathering.item21_page9)
    #     if gathering.item21_page10:
    #         temp_page21.append(gathering.item21_page10)
    #     temp_page21=[int(i) for i in temp_page21]
    #     temp_page21.sort(reverse=False)
        
    
        
    #     if temp_page21:
    #         gathering.total_gathering_21=temp_page21[0]
    #         gathering.wastage_form_21 = float(gathering.quantity_21) - float(gathering.total_gathering_21)
    #     else:
    #         gathering.item21_page1=0
    #         gathering.item21_page2=0
    #         gathering.item21_page3=0
    #         gathering.item21_page4=0
    #         gathering.item21_page5=0
    #         gathering.item21_page6=0
    #         gathering.item21_page7=0
    #         gathering.item21_page8=0
    #         gathering.item21_page9=0
    #         gathering.item21_page10=0
        
            

    #     # temp_page21=[]
    #     # if gathering.item21_page1:
    #     #     temp_page21.append(gathering.item21_page1)
    #     # if gathering.item21_page2:
    #     #     temp_page21.append(gathering.item21_page2)
    #     # if gathering.item21_page3:
    #     #     temp_page21.append(gathering.item21_page3)
    #     # if gathering.item21_page4:
    #     #     temp_page21.append(gathering.item21_page4)
    #     # if gathering.item21_page5:
    #     #     temp_page21.append(gathering.item21_page5)
    #     # if gathering.item21_page6:
    #     #     temp_page21.append(gathering.item21_page6)
    #     # if gathering.item21_page7:
    #     #     temp_page21.append(gathering.item21_page7)
    #     # if gathering.item21_page8:
    #     #     temp_page21.append(gathering.item21_page8)
    #     # if gathering.item21_page9:
    #     #     temp_page21.append(gathering.item21_page9)
    #     # if gathering.item21_page10:
    #     #     temp_page21.append(gathering.item21_page10)
    #     # temp_page21=[int(i) for i in temp_page21]
    #     # temp_page21.sort(reverse=False)
        
    
        
    #     # if temp_page21:
    #     #     gathering.total_gathering_21=temp_page21[0]
    #     #     gathering.wastage_form_21 = float(gathering.quantity_21) - float(gathering.total_gathering_21)
    #     # else:
    #     #     gathering.item21_page1=0
    #     #     gathering.item21_page2=0
    #     #     gathering.item21_page3=0
    #     #     gathering.item21_page4=0
    #     #     gathering.item21_page5=0


    #     temp_page22=[]
    #     if gathering.item22_page1:
    #         temp_page22.append(gathering.item22_page1)
    #     if gathering.item22_page2:
    #         temp_page22.append(gathering.item22_page2)
    #     if gathering.item22_page3:
    #         temp_page22.append(gathering.item22_page3)
    #     if gathering.item22_page4:
    #         temp_page22.append(gathering.item22_page4)
    #     if gathering.item22_page5:
    #         temp_page22.append(gathering.item22_page5)
    #     if gathering.item22_page6:
    #         temp_page22.append(gathering.item22_page6)
    #     if gathering.item22_page7:
    #         temp_page22.append(gathering.item22_page7)
    #     if gathering.item22_page8:
    #         temp_page22.append(gathering.item22_page8)
    #     if gathering.item22_page9:
    #         temp_page22.append(gathering.item22_page9)
    #     if gathering.item22_page10:
    #         temp_page22.append(gathering.item22_page10)
    #     temp_page22=[int(i) for i in temp_page22]
    #     temp_page22.sort(reverse=False)
        
    
        
    #     if temp_page22:
    #         gathering.total_gathering_22=temp_page22[0]
    #         gathering.wastage_form_22 = float(gathering.quantity_22) - float(gathering.total_gathering_22)
    #     else:
    #         gathering.item22_page1=0
    #         gathering.item22_page2=0
    #         gathering.item22_page3=0
    #         gathering.item22_page4=0
    #         gathering.item22_page5=0
    #         gathering.item22_page6=0
    #         gathering.item22_page7=0
    #         gathering.item22_page8=0
    #         gathering.item22_page9=0
    #         gathering.item22_page10=0



    #     temp_page23=[]
    #     if gathering.item23_page1:
    #         temp_page23.append(gathering.item23_page1)
    #     if gathering.item23_page2:
    #         temp_page23.append(gathering.item23_page2)
    #     if gathering.item23_page3:
    #         temp_page23.append(gathering.item23_page3)
    #     if gathering.item23_page4:
    #         temp_page23.append(gathering.item23_page4)
    #     if gathering.item23_page5:
    #         temp_page23.append(gathering.item23_page5)
    #     if gathering.item23_page6:
    #         temp_page23.append(gathering.item23_page6)
    #     if gathering.item23_page7:
    #         temp_page23.append(gathering.item23_page7)
    #     if gathering.item23_page8:
    #         temp_page23.append(gathering.item23_page8)
    #     if gathering.item23_page9:
    #         temp_page23.append(gathering.item23_page9)
    #     if gathering.item23_page10:
    #         temp_page23.append(gathering.item23_page10)
    #     temp_page23=[int(i) for i in temp_page23]
    #     temp_page23.sort(reverse=False)
        
    
        
    #     if temp_page23:
    #         gathering.total_gathering_23=temp_page23[0]
    #         gathering.wastage_form_23 = float(gathering.quantity_23) - float(gathering.total_gathering_23)
    #     else:
    #         gathering.item23_page1=0
    #         gathering.item23_page2=0
    #         gathering.item23_page3=0
    #         gathering.item23_page4=0
    #         gathering.item23_page5=0
    #         gathering.item23_page6=0
    #         gathering.item23_page7=0
    #         gathering.item23_page8=0
    #         gathering.item23_page9=0
    #         gathering.item23_page10=0


    #     temp_page24=[]
    #     if gathering.item24_page1:
    #         temp_page24.append(gathering.item24_page1)
    #     if gathering.item24_page2:
    #         temp_page24.append(gathering.item24_page2)
    #     if gathering.item24_page3:
    #         temp_page24.append(gathering.item24_page3)
    #     if gathering.item24_page4:
    #         temp_page24.append(gathering.item24_page4)
    #     if gathering.item24_page5:
    #         temp_page24.append(gathering.item24_page5)
    #     if gathering.item24_page6:
    #         temp_page24.append(gathering.item24_page6)
    #     if gathering.item24_page7:
    #         temp_page24.append(gathering.item24_page7)
    #     if gathering.item24_page8:
    #         temp_page24.append(gathering.item24_page8)
    #     if gathering.item24_page9:
    #         temp_page24.append(gathering.item24_page9)
    #     if gathering.item24_page10:
    #         temp_page24.append(gathering.item24_page10)
    #     temp_page24=[int(i) for i in temp_page24]
    #     temp_page24.sort(reverse=False)
        
    
        
    #     if temp_page24:
    #         gathering.total_gathering_24=temp_page24[0]
    #         gathering.wastage_form_24 = float(gathering.quantity_24) - float(gathering.total_gathering_24)
    #     else:
    #         gathering.item24_page1=0
    #         gathering.item24_page2=0
    #         gathering.item24_page3=0
    #         gathering.item24_page4=0
    #         gathering.item24_page5=0
    #         gathering.item24_page6=0
    #         gathering.item24_page7=0
    #         gathering.item24_page8=0
    #         gathering.item24_page9=0
    #         gathering.item24_page10=0


    #     temp_page25=[]
    #     if gathering.item25_page1:
    #         temp_page25.append(gathering.item25_page1)
    #     if gathering.item25_page2:
    #         temp_page25.append(gathering.item25_page2)
    #     if gathering.item25_page3:
    #         temp_page25.append(gathering.item25_page3)
    #     if gathering.item25_page4:
    #         temp_page25.append(gathering.item25_page4)
    #     if gathering.item25_page5:
    #         temp_page25.append(gathering.item25_page5)
    #     if gathering.item25_page6:
    #         temp_page25.append(gathering.item25_page6)
    #     if gathering.item25_page7:
    #         temp_page25.append(gathering.item25_page7)
    #     if gathering.item25_page8:
    #         temp_page25.append(gathering.item25_page8)
    #     if gathering.item25_page9:
    #         temp_page25.append(gathering.item25_page9)
    #     if gathering.item25_page10:
    #         temp_page25.append(gathering.item25_page10)
    #     temp_page25=[int(i) for i in temp_page25]
    #     temp_page25.sort(reverse=False)
        
    
        
    #     if temp_page25:
    #         gathering.total_gathering_25=temp_page25[0]
    #         gathering.wastage_form_25 = float(gathering.quantity_25) - float(gathering.total_gathering_25)
    #     else:
    #         gathering.item25_page1=0
    #         gathering.item25_page2=0
    #         gathering.item25_page3=0
    #         gathering.item25_page4=0
    #         gathering.item25_page5=0
    #         gathering.item25_page6=0
    #         gathering.item25_page7=0
    #         gathering.item25_page8=0
    #         gathering.item25_page9=0
    #         gathering.item25_page10=0


    #     temp_page26=[]
    #     if gathering.item26_page1:
    #         temp_page26.append(gathering.item26_page1)
    #     if gathering.item26_page2:
    #         temp_page26.append(gathering.item26_page2)
    #     if gathering.item26_page3:
    #         temp_page26.append(gathering.item26_page3)
    #     if gathering.item26_page4:
    #         temp_page26.append(gathering.item26_page4)
    #     if gathering.item26_page5:
    #         temp_page26.append(gathering.item26_page5)
    #     if gathering.item26_page6:
    #         temp_page26.append(gathering.item26_page6)
    #     if gathering.item26_page7:
    #         temp_page26.append(gathering.item26_page7)
    #     if gathering.item26_page8:
    #         temp_page26.append(gathering.item26_page8)
    #     if gathering.item26_page9:
    #         temp_page26.append(gathering.item26_page9)
    #     if gathering.item26_page10:
    #         temp_page26.append(gathering.item26_page10)
    #     temp_page26=[int(i) for i in temp_page26]
    #     temp_page26.sort(reverse=False)
        
    
        
    #     if temp_page26:
    #         gathering.total_gathering_26=temp_page26[0]
    #         gathering.wastage_form_26 = float(gathering.quantity_26) - float(gathering.total_gathering_26)
    #     else:
    #         gathering.item26_page1=0
    #         gathering.item26_page2=0
    #         gathering.item26_page3=0
    #         gathering.item26_page4=0
    #         gathering.item26_page5=0
    #         gathering.item26_page6=0
    #         gathering.item26_page7=0
    #         gathering.item26_page8=0
    #         gathering.item26_page9=0
    #         gathering.item26_page10=0



    #     temp_page27=[]
    #     if gathering.item27_page1:
    #         temp_page27.append(gathering.item27_page1)
    #     if gathering.item27_page2:
    #         temp_page27.append(gathering.item27_page2)
    #     if gathering.item27_page3:
    #         temp_page27.append(gathering.item27_page3)
    #     if gathering.item27_page4:
    #         temp_page27.append(gathering.item27_page4)
    #     if gathering.item27_page5:
    #         temp_page27.append(gathering.item27_page5)
    #     if gathering.item27_page6:
    #         temp_page27.append(gathering.item27_page6)
    #     if gathering.item27_page7:
    #         temp_page27.append(gathering.item27_page7)
    #     if gathering.item27_page8:
    #         temp_page27.append(gathering.item27_page8)
    #     if gathering.item27_page9:
    #         temp_page27.append(gathering.item27_page9)
    #     if gathering.item27_page10:
    #         temp_page27.append(gathering.item27_page10)
    #     temp_page27=[int(i) for i in temp_page27]
    #     temp_page27.sort(reverse=False)
        
    
        
    #     if temp_page27:
    #         gathering.total_gathering_27=temp_page27[0]
    #         gathering.wastage_form_27 = float(gathering.quantity_27) - float(gathering.total_gathering_27)
    #     else:
    #         gathering.item27_page1=0
    #         gathering.item27_page2=0
    #         gathering.item27_page3=0
    #         gathering.item27_page4=0
    #         gathering.item27_page5=0
    #         gathering.item27_page6=0
    #         gathering.item27_page7=0
    #         gathering.item27_page8=0
    #         gathering.item27_page9=0
    #         gathering.item27_page10=0



    #     temp_page28=[]
    #     if gathering.item28_page1:
    #         temp_page28.append(gathering.item28_page1)
    #     if gathering.item28_page2:
    #         temp_page28.append(gathering.item28_page2)
    #     if gathering.item28_page3:
    #         temp_page28.append(gathering.item28_page3)
    #     if gathering.item28_page4:
    #         temp_page28.append(gathering.item28_page4)
    #     if gathering.item28_page5:
    #         temp_page28.append(gathering.item28_page5)
    #     if gathering.item28_page6:
    #         temp_page28.append(gathering.item28_page6)
    #     if gathering.item28_page7:
    #         temp_page28.append(gathering.item28_page7)
    #     if gathering.item28_page8:
    #         temp_page28.append(gathering.item28_page8)
    #     if gathering.item28_page9:
    #         temp_page28.append(gathering.item28_page9)
    #     if gathering.item28_page10:
    #         temp_page28.append(gathering.item28_page10)
    #     temp_page28=[int(i) for i in temp_page28]
    #     temp_page28.sort(reverse=False)
        
    
        
    #     if temp_page28:
    #         gathering.total_gathering_28=temp_page28[0]
    #         gathering.wastage_form_28 = float(gathering.quantity_28) - float(gathering.total_gathering_28)
    #     else:
    #         gathering.item28_page1=0
    #         gathering.item28_page2=0
    #         gathering.item28_page3=0
    #         gathering.item28_page4=0
    #         gathering.item28_page5=0
    #         gathering.item28_page6=0
    #         gathering.item28_page7=0
    #         gathering.item28_page8=0
    #         gathering.item28_page9=0
    #         gathering.item28_page10=0


    #     temp_page29=[]
    #     if gathering.item29_page1:
    #         temp_page29.append(gathering.item29_page1)
    #     if gathering.item29_page2:
    #         temp_page29.append(gathering.item29_page2)
    #     if gathering.item29_page3:
    #         temp_page29.append(gathering.item29_page3)
    #     if gathering.item29_page4:
    #         temp_page29.append(gathering.item29_page4)
    #     if gathering.item29_page5:
    #         temp_page29.append(gathering.item29_page5)
    #     if gathering.item29_page6:
    #         temp_page29.append(gathering.item29_page6)
    #     if gathering.item29_page7:
    #         temp_page29.append(gathering.item29_page7)
    #     if gathering.item29_page8:
    #         temp_page29.append(gathering.item29_page8)
    #     if gathering.item29_page9:
    #         temp_page29.append(gathering.item29_page9)
    #     if gathering.item29_page10:
    #         temp_page29.append(gathering.item29_page10)
    #     temp_page29=[int(i) for i in temp_page29]
    #     temp_page29.sort(reverse=False)
        
    
        
    #     if temp_page29:
    #         gathering.total_gathering_29=temp_page29[0]
    #         gathering.wastage_form_29 = float(gathering.quantity_29) - float(gathering.total_gathering_29)
    #     else:
    #         gathering.item29_page1=0
    #         gathering.item29_page2=0
    #         gathering.item29_page3=0
    #         gathering.item29_page4=0
    #         gathering.item29_page5=0
    #         gathering.item29_page6=0
    #         gathering.item29_page7=0
    #         gathering.item29_page8=0
    #         gathering.item29_page9=0
    #         gathering.item29_page10=0



    #     temp_page30=[]
    #     if gathering.item30_page1:
    #         temp_page30.append(gathering.item30_page1)
    #     if gathering.item30_page2:
    #         temp_page30.append(gathering.item30_page2)
    #     if gathering.item30_page3:
    #         temp_page30.append(gathering.item30_page3)
    #     if gathering.item30_page4:
    #         temp_page30.append(gathering.item30_page4)
    #     if gathering.item30_page5:
    #         temp_page30.append(gathering.item30_page5)
    #     if gathering.item30_page6:
    #         temp_page30.append(gathering.item30_page6)
    #     if gathering.item30_page7:
    #         temp_page30.append(gathering.item30_page7)
    #     if gathering.item30_page8:
    #         temp_page30.append(gathering.item30_page8)
    #     if gathering.item30_page9:
    #         temp_page30.append(gathering.item30_page9)
    #     if gathering.item30_page10:
    #         temp_page30.append(gathering.item30_page10)
    #     temp_page30=[int(i) for i in temp_page30]
    #     temp_page30.sort(reverse=False)
        
        
        
    #     if temp_page30:
    #         gathering.total_gathering_30=temp_page30[0]
    #         gathering.wastage_form_30 = float(gathering.quantity_30) - float(gathering.total_gathering_30)
    #     else:
    #         gathering.item30_page1=0
    #         gathering.item30_page2=0
    #         gathering.item30_page3=0
    #         gathering.item30_page4=0
    #         gathering.item30_page5=0
    #         gathering.item30_page6=0
    #         gathering.item30_page7=0
    #         gathering.item30_page8=0
    #         gathering.item30_page9=0
    #         gathering.item30_page10=0



    #     temp_page31=[]
    #     if gathering.item31_page1:
    #         temp_page31.append(gathering.item31_page1)
    #     if gathering.item31_page2:
    #         temp_page31.append(gathering.item31_page2)
    #     if gathering.item31_page3:
    #         temp_page31.append(gathering.item31_page3)
    #     if gathering.item31_page4:
    #         temp_page31.append(gathering.item31_page4)
    #     if gathering.item31_page5:
    #         temp_page31.append(gathering.item31_page5)
    #     if gathering.item31_page6:
    #         temp_page31.append(gathering.item31_page6)
    #     if gathering.item31_page7:
    #         temp_page31.append(gathering.item31_page7)
    #     if gathering.item31_page8:
    #         temp_page31.append(gathering.item31_page8)
    #     if gathering.item31_page9:
    #         temp_page31.append(gathering.item31_page9)
    #     if gathering.item31_page10:
    #         temp_page31.append(gathering.item31_page10)
    #     temp_page31=[int(i) for i in temp_page31]
    #     temp_page31.sort(reverse=False)
        
        
        
    #     if temp_page31:
    #         gathering.total_gathering_31=temp_page31[0]
    #         gathering.wastage_form_31 = float(gathering.quantity_31) - float(gathering.total_gathering_31)
    #     else:
    #         gathering.item31_page1=0
    #         gathering.item31_page2=0
    #         gathering.item31_page3=0
    #         gathering.item31_page4=0
    #         gathering.item31_page5=0
    #         gathering.item31_page6=0
    #         gathering.item31_page7=0
    #         gathering.item31_page8=0
    #         gathering.item31_page9=0
    #         gathering.item31_page10=0


    #     temp_page32=[]
    #     if gathering.item3_page1:
    #         temp_page32.append(gathering.item32_page1)
    #     if gathering.item3_page2:
    #         temp_page32.append(gathering.item32_page2)
    #     if gathering.item3_page3:
    #         temp_page32.append(gathering.item32_page3)
    #     if gathering.item3_page4:
    #         temp_page32.append(gathering.item32_page4)
    #     if gathering.item3_page5:
    #         temp_page32.append(gathering.item32_page5)
    #     if gathering.item3_page6:
    #         temp_page32.append(gathering.item32_page6)
    #     if gathering.item3_page7:
    #         temp_page32.append(gathering.item32_page7)
    #     if gathering.item3_page8:
    #         temp_page32.append(gathering.item32_page8)
    #     if gathering.item3_page9:
    #         temp_page32.append(gathering.item32_page9)
    #     if gathering.item3_page10:
    #         temp_page32.append(gathering.item32_page10)
    #     temp_page32=[int(i) for i in temp_page32]
    #     temp_page32.sort(reverse=False)
        
        
        
    #     if temp_page32:
    #         gathering.total_gathering_32=temp_page32[0]
    #         gathering.wastage_form_32 = float(gathering.quantity_32) - float(gathering.total_gathering_32)
    #     else:
    #         gathering.item32_page1=0
    #         gathering.item32_page2=0
    #         gathering.item32_page3=0
    #         gathering.item32_page4=0
    #         gathering.item32_page5=0
    #         gathering.item32_page6=0
    #         gathering.item32_page7=0
    #         gathering.item32_page8=0
    #         gathering.item32_page9=0
    #         gathering.item32_page10=0



    #     temp_page33=[]
    #     if gathering.item33_page1:
    #         temp_page33.append(gathering.item33_page1)
    #     if gathering.item33_page2:
    #         temp_page33.append(gathering.item33_page2)
    #     if gathering.item33_page3:
    #         temp_page33.append(gathering.item33_page3)
    #     if gathering.item33_page4:
    #         temp_page33.append(gathering.item33_page4)
    #     if gathering.item33_page5:
    #         temp_page33.append(gathering.item33_page5)
    #     if gathering.item33_page6:
    #         temp_page33.append(gathering.item33_page6)
    #     if gathering.item33_page7:
    #         temp_page33.append(gathering.item33_page7)
    #     if gathering.item33_page8:
    #         temp_page33.append(gathering.item33_page8)
    #     if gathering.item33_page9:
    #         temp_page33.append(gathering.item33_page9)
    #     if gathering.item33_page10:
    #         temp_page33.append(gathering.item33_page10)
    #     temp_page33=[int(i) for i in temp_page33]
    #     temp_page33.sort(reverse=False)
        
        
        
    #     if temp_page33:
    #         gathering.total_gathering_33=temp_page33[0]
    #         gathering.wastage_form_33 = float(gathering.quantity_33) - float(gathering.total_gathering_33)
    #     else:
    #         gathering.item33_page1=0
    #         gathering.item33_page2=0
    #         gathering.item33_page3=0
    #         gathering.item33_page4=0
    #         gathering.item33_page5=0
    #         gathering.item33_page6=0
    #         gathering.item33_page7=0
    #         gathering.item33_page8=0
    #         gathering.item33_page9=0
    #         gathering.item33_page10=0


    #     temp_page34=[]
    #     if gathering.item34_page1:
    #         temp_page34.append(gathering.item34_page1)
    #     if gathering.item34_page2:
    #         temp_page34.append(gathering.item34_page2)
    #     if gathering.item34_page3:
    #         temp_page34.append(gathering.item34_page3)
    #     if gathering.item34_page4:
    #         temp_page34.append(gathering.item34_page4)
    #     if gathering.item34_page5:
    #         temp_page34.append(gathering.item34_page5)
    #     if gathering.item34_page6:
    #         temp_page34.append(gathering.item34_page6)
    #     if gathering.item34_page7:
    #         temp_page34.append(gathering.item34_page7)
    #     if gathering.item34_page8:
    #         temp_page34.append(gathering.item34_page8)
    #     if gathering.item34_page9:
    #         temp_page34.append(gathering.item34_page9)
    #     if gathering.item34_page10:
    #         temp_page34.append(gathering.item34_page10)
    #     temp_page34=[int(i) for i in temp_page34]
    #     temp_page34.sort(reverse=False)
        
        
        
    #     if temp_page34:
    #         gathering.total_gathering_34=temp_page34[0]
    #         gathering.wastage_form_34 = float(gathering.quantity_34) - float(gathering.total_gathering_34)
    #     else:
    #         gathering.item34_page1=0
    #         gathering.item34_page2=0
    #         gathering.item34_page3=0
    #         gathering.item34_page4=0
    #         gathering.item34_page5=0
    #         gathering.item34_page6=0
    #         gathering.item34_page7=0
    #         gathering.item34_page8=0
    #         gathering.item34_page9=0
    #         gathering.item34_page10=0



    #     temp_page35=[]
    #     if gathering.item35_page1:
    #         temp_page35.append(gathering.item35_page1)
    #     if gathering.item35_page2:
    #         temp_page35.append(gathering.item35_page2)
    #     if gathering.item35_page3:
    #         temp_page35.append(gathering.item35_page3)
    #     if gathering.item35_page4:
    #         temp_page35.append(gathering.item35_page4)
    #     if gathering.item35_page5:
    #         temp_page35.append(gathering.item35_page5)
    #     if gathering.item35_page6:
    #         temp_page35.append(gathering.item35_page6)
    #     if gathering.item35_page7:
    #         temp_page35.append(gathering.item35_page7)
    #     if gathering.item35_page8:
    #         temp_page35.append(gathering.item35_page8)
    #     if gathering.item35_page9:
    #         temp_page35.append(gathering.item35_page9)
    #     if gathering.item35_page10:
    #         temp_page35.append(gathering.item35_page10)
    #     temp_page35=[int(i) for i in temp_page35]
    #     temp_page35.sort(reverse=False)
        
        
        
    #     if temp_page35:
    #         gathering.total_gathering_35=temp_page35[0]
    #         gathering.wastage_form_35 = float(gathering.quantity_35) - float(gathering.total_gathering_35)
    #     else:
    #         gathering.item35_page1=0
    #         gathering.item35_page2=0
    #         gathering.item35_page3=0
    #         gathering.item35_page4=0
    #         gathering.item35_page5=0
    #         gathering.item35_page6=0
    #         gathering.item35_page7=0
    #         gathering.item35_page8=0
    #         gathering.item35_page9=0
    #         gathering.item35_page10=0



    #     temp_page36=[]
    #     if gathering.item36_page1:
    #         temp_page36.append(gathering.item36_page1)
    #     if gathering.item36_page2:
    #         temp_page36.append(gathering.item36_page2)
    #     if gathering.item36_page3:
    #         temp_page36.append(gathering.item36_page3)
    #     if gathering.item36_page4:
    #         temp_page36.append(gathering.item36_page4)
    #     if gathering.item36_page5:
    #         temp_page36.append(gathering.item36_page5)
    #     if gathering.item36_page6:
    #         temp_page36.append(gathering.item36_page6)
    #     if gathering.item36_page7:
    #         temp_page36.append(gathering.item36_page7)
    #     if gathering.item36_page8:
    #         temp_page36.append(gathering.item36_page8)
    #     if gathering.item36_page9:
    #         temp_page36.append(gathering.item36_page9)
    #     if gathering.item36_page10:
    #         temp_page36.append(gathering.item36_page10)
    #     temp_page36=[int(i) for i in temp_page36]
    #     temp_page36.sort(reverse=False)
        
        
        
    #     if temp_page36:
    #         gathering.total_gathering_36=temp_page36[0]
    #         gathering.wastage_form_36 = float(gathering.quantity_36) - float(gathering.total_gathering_36)
    #     else:
    #         gathering.item36_page1=0
    #         gathering.item36_page2=0
    #         gathering.item36_page3=0
    #         gathering.item36_page4=0
    #         gathering.item36_page5=0
    #         gathering.item36_page6=0
    #         gathering.item36_page7=0
    #         gathering.item36_page8=0
    #         gathering.item36_page9=0
    #         gathering.item36_page10=0



    #     temp_page37=[]
    #     if gathering.item37_page1:
    #         temp_page37.append(gathering.item37_page1)
    #     if gathering.item37_page2:
    #         temp_page37.append(gathering.item37_page2)
    #     if gathering.item37_page3:
    #         temp_page37.append(gathering.item37_page3)
    #     if gathering.item37_page4:
    #         temp_page37.append(gathering.item37_page4)
    #     if gathering.item37_page5:
    #         temp_page37.append(gathering.item37_page5)
    #     if gathering.item37_page6:
    #         temp_page37.append(gathering.item37_page6)
    #     if gathering.item37_page7:
    #         temp_page37.append(gathering.item37_page7)
    #     if gathering.item37_page8:
    #         temp_page37.append(gathering.item37_page8)
    #     if gathering.item37_page9:
    #         temp_page37.append(gathering.item37_page9)
    #     if gathering.item37_page10:
    #         temp_page37.append(gathering.item37_page10)
    #     temp_page37=[int(i) for i in temp_page37]
    #     temp_page37.sort(reverse=False)
        
        
        
    #     if temp_page37:
    #         gathering.total_gathering_37=temp_page37[0]
    #         gathering.wastage_form_37 = float(gathering.quantity_37) - float(gathering.total_gathering_37)
    #     else:
    #         gathering.item37_page1=0
    #         gathering.item37_page2=0
    #         gathering.item37_page3=0
    #         gathering.item37_page4=0
    #         gathering.item37_page5=0
    #         gathering.item37_page6=0
    #         gathering.item37_page7=0
    #         gathering.item37_page8=0
    #         gathering.item37_page9=0
    #         gathering.item37_page10=0



    #     temp_page38=[]
    #     if gathering.item38_page1:
    #         temp_page38.append(gathering.item38_page1)
    #     if gathering.item38_page2:
    #         temp_page38.append(gathering.item38_page2)
    #     if gathering.item38_page3:
    #         temp_page38.append(gathering.item38_page3)
    #     if gathering.item38_page4:
    #         temp_page38.append(gathering.item38_page4)
    #     if gathering.item38_page5:
    #         temp_page38.append(gathering.item38_page5)
    #     if gathering.item38_page6:
    #         temp_page38.append(gathering.item38_page6)
    #     if gathering.item38_page7:
    #         temp_page38.append(gathering.item38_page7)
    #     if gathering.item38_page8:
    #         temp_page38.append(gathering.item38_page8)
    #     if gathering.item38_page9:
    #         temp_page38.append(gathering.item38_page9)
    #     if gathering.item38_page10:
    #         temp_page38.append(gathering.item38_page10)
    #     temp_page38=[int(i) for i in temp_page38]
    #     temp_page38.sort(reverse=False)
        
        
        
    #     if temp_page38:
    #         gathering.total_gathering_38=temp_page38[0]
    #         gathering.wastage_form_38 = float(gathering.quantity_38) - float(gathering.total_gathering_38)
    #     else:
    #         gathering.item38_page1=0
    #         gathering.item38_page2=0
    #         gathering.item38_page3=0
    #         gathering.item38_page4=0
    #         gathering.item38_page5=0
    #         gathering.item38_page6=0
    #         gathering.item38_page7=0
    #         gathering.item38_page8=0
    #         gathering.item38_page9=0
    #         gathering.item38_page10=0



    #     temp_page39=[]
    #     if gathering.item39_page1:
    #         temp_page39.append(gathering.item39_page1)
    #     if gathering.item39_page2:
    #         temp_page39.append(gathering.item39_page2)
    #     if gathering.item39_page3:
    #         temp_page39.append(gathering.item39_page3)
    #     if gathering.item39_page4:
    #         temp_page39.append(gathering.item39_page4)
    #     if gathering.item39_page5:
    #         temp_page39.append(gathering.item39_page5)
    #     if gathering.item39_page6:
    #         temp_page39.append(gathering.item39_page6)
    #     if gathering.item39_page7:
    #         temp_page39.append(gathering.item39_page7)
    #     if gathering.item39_page8:
    #         temp_page39.append(gathering.item39_page8)
    #     if gathering.item39_page9:
    #         temp_page39.append(gathering.item39_page9)
    #     if gathering.item39_page10:
    #         temp_page39.append(gathering.item39_page10)
    #     temp_page39=[int(i) for i in temp_page39]
    #     temp_page39.sort(reverse=False)
        
        
        
    #     if temp_page39:
    #         gathering.total_gathering_39=temp_page39[0]
    #         gathering.wastage_form_39 = float(gathering.quantity_39) - float(gathering.total_gathering_39)
    #     else:
    #         gathering.item39_page1=0
    #         gathering.item39_page2=0
    #         gathering.item39_page3=0
    #         gathering.item39_page4=0
    #         gathering.item39_page5=0
    #         gathering.item39_page6=0
    #         gathering.item39_page7=0
    #         gathering.item39_page8=0
    #         gathering.item39_page9=0
    #         gathering.item39_page10=0



    #     temp_page40=[]
    #     if gathering.item40_page1:
    #         temp_page40.append(gathering.item40_page1)
    #     if gathering.item40_page2:
    #         temp_page40.append(gathering.item40_page2)
    #     if gathering.item40_page3:
    #         temp_page40.append(gathering.item40_page3)
    #     if gathering.item40_page4:
    #         temp_page40.append(gathering.item40_page4)
    #     if gathering.item40_page5:
    #         temp_page40.append(gathering.item40_page5)
    #     if gathering.item40_page6:
    #         temp_page40.append(gathering.item40_page6)
    #     if gathering.item40_page7:
    #         temp_page40.append(gathering.item40_page7)
    #     if gathering.item40_page8:
    #         temp_page40.append(gathering.item40_page8)
    #     if gathering.item40_page9:
    #         temp_page40.append(gathering.item40_page9)
    #     if gathering.item40_page10:
    #         temp_page40.append(gathering.item40_page10)
    #     temp_page40=[int(i) for i in temp_page40]
    #     temp_page40.sort(reverse=False)
        
        
        
    #     if temp_page40:
    #         gathering.total_gathering_40=temp_page40[0]
    #         gathering.wastage_form_40 = float(gathering.quantity_40) - float(gathering.total_gathering_40)
    #     else:
    #         gathering.item40_page1=0
    #         gathering.item40_page2=0
    #         gathering.item40_page3=0
    #         gathering.item40_page4=0
    #         gathering.item40_page5=0
    #         gathering.item40_page6=0
    #         gathering.item40_page7=0
    #         gathering.item40_page8=0
    #         gathering.item40_page9=0
    #         gathering.item40_page10=0


    #     temp_page41=[]
    #     if gathering.item41_page1:
    #         temp_page41.append(gathering.item41_page1)
    #     if gathering.item41_page2:
    #         temp_page41.append(gathering.item41_page2)
    #     if gathering.item41_page3:
    #         temp_page41.append(gathering.item41_page3)
    #     if gathering.item41_page4:
    #         temp_page41.append(gathering.item41_page4)
    #     if gathering.item41_page5:
    #         temp_page41.append(gathering.item41_page5)
    #     if gathering.item41_page6:
    #         temp_page41.append(gathering.item41_page6)
    #     if gathering.item41_page7:
    #         temp_page41.append(gathering.item41_page7)
    #     if gathering.item41_page8:
    #         temp_page41.append(gathering.item41_page8)
    #     if gathering.item41_page9:
    #         temp_page41.append(gathering.item41_page9)
    #     if gathering.item41_page10:
    #         temp_page41.append(gathering.item41_page10)
    #     temp_page41=[int(i) for i in temp_page41]
    #     temp_page41.sort(reverse=False)
    
    
        
    #     if temp_page41:
    #         gathering.total_gathering_41=temp_page41[0]
    #         gathering.wastage_form_41 = float(gathering.quantity_41) - float(gathering.total_gathering_41)
    #     else:
    #         gathering.item41_page1=0
    #         gathering.item41_page2=0
    #         gathering.item41_page3=0
    #         gathering.item41_page4=0
    #         gathering.item41_page5=0
    #         gathering.item41_page6=0
    #         gathering.item41_page7=0
    #         gathering.item41_page8=0
    #         gathering.item41_page9=0
    #         gathering.item41_page10=0



    #     temp_page42=[]
    #     if gathering.item42_page1:
    #         temp_page42.append(gathering.item42_page1)
    #     if gathering.item42_page2:
    #         temp_page42.append(gathering.item42_page2)
    #     if gathering.item42_page3:
    #         temp_page42.append(gathering.item42_page3)
    #     if gathering.item42_page4:
    #         temp_page42.append(gathering.item42_page4)
    #     if gathering.item42_page5:
    #         temp_page42.append(gathering.item42_page5)
    #     if gathering.item42_page6:
    #         temp_page42.append(gathering.item42_page6)
    #     if gathering.item42_page7:
    #         temp_page42.append(gathering.item42_page7)
    #     if gathering.item42_page8:
    #         temp_page42.append(gathering.item42_page8)
    #     if gathering.item42_page9:
    #         temp_page42.append(gathering.item42_page9)
    #     if gathering.item42_page10:
    #         temp_page42.append(gathering.item42_page10)
    #     temp_page42=[int(i) for i in temp_page42]
    #     temp_page42.sort(reverse=False)
    
    
        
    #     if temp_page42:
    #         gathering.total_gathering_42=temp_page42[0]
    #         gathering.wastage_form_42 = float(gathering.quantity_42) - float(gathering.total_gathering_42)
    #     else:
    #         gathering.item42_page1=0
    #         gathering.item42_page2=0
    #         gathering.item42_page3=0
    #         gathering.item42_page4=0
    #         gathering.item42_page5=0
    #         gathering.item42_page6=0
    #         gathering.item42_page7=0
    #         gathering.item42_page8=0
    #         gathering.item42_page9=0
    #         gathering.item42_page10=0



    #     temp_page43=[]
    #     if gathering.item43_page1:
    #         temp_page43.append(gathering.item43_page1)
    #     if gathering.item43_page2:
    #         temp_page43.append(gathering.item43_page2)
    #     if gathering.item43_page3:
    #         temp_page43.append(gathering.item43_page3)
    #     if gathering.item43_page4:
    #         temp_page43.append(gathering.item43_page4)
    #     if gathering.item43_page5:
    #         temp_page43.append(gathering.item43_page5)
    #     if gathering.item43_page6:
    #         temp_page43.append(gathering.item43_page6)
    #     if gathering.item43_page7:
    #         temp_page43.append(gathering.item43_page7)
    #     if gathering.item43_page8:
    #         temp_page43.append(gathering.item43_page8)
    #     if gathering.item43_page9:
    #         temp_page43.append(gathering.item43_page9)
    #     if gathering.item43_page10:
    #         temp_page43.append(gathering.item43_page10)
    #     temp_page43=[int(i) for i in temp_page43]
    #     temp_page43.sort(reverse=False)
    
    
        
    #     if temp_page43:
    #         gathering.total_gathering_43=temp_page43[0]
    #         gathering.wastage_form_43 = float(gathering.quantity_43) - float(gathering.total_gathering_43)
    #     else:
    #         gathering.item43_page1=0
    #         gathering.item43_page2=0
    #         gathering.item43_page3=0
    #         gathering.item43_page4=0
    #         gathering.item43_page5=0
    #         gathering.item43_page6=0
    #         gathering.item43_page7=0
    #         gathering.item43_page8=0
    #         gathering.item43_page9=0
    #         gathering.item43_page10=0



    #     temp_page44=[]
    #     if gathering.item44_page1:
    #         temp_page44.append(gathering.item44_page1)
    #     if gathering.item44_page2:
    #         temp_page44.append(gathering.item44_page2)
    #     if gathering.item44_page3:
    #         temp_page44.append(gathering.item44_page3)
    #     if gathering.item44_page4:
    #         temp_page44.append(gathering.item44_page4)
    #     if gathering.item44_page5:
    #         temp_page44.append(gathering.item44_page5)
    #     if gathering.item44_page6:
    #         temp_page44.append(gathering.item44_page6)
    #     if gathering.item44_page7:
    #         temp_page44.append(gathering.item44_page7)
    #     if gathering.item44_page8:
    #         temp_page44.append(gathering.item44_page8)
    #     if gathering.item44_page9:
    #         temp_page44.append(gathering.item44_page9)
    #     if gathering.item44_page10:
    #         temp_page44.append(gathering.item44_page10)
    #     temp_page44=[int(i) for i in temp_page44]
    #     temp_page44.sort(reverse=False)
    
    
        
    #     if temp_page44:
    #         gathering.total_gathering_44=temp_page44[0]
    #         gathering.wastage_form_44 = float(gathering.quantity_44) - float(gathering.total_gathering_44)
    #     else:
    #         gathering.item44_page1=0
    #         gathering.item44_page2=0
    #         gathering.item44_page3=0
    #         gathering.item44_page4=0
    #         gathering.item44_page5=0
    #         gathering.item44_page6=0
    #         gathering.item44_page7=0
    #         gathering.item44_page8=0
    #         gathering.item44_page9=0
    #         gathering.item44_page10=0



    #     temp_page45=[]
    #     if gathering.item45_page1:
    #         temp_page45.append(gathering.item45_page1)
    #     if gathering.item45_page2:
    #         temp_page45.append(gathering.item45_page2)
    #     if gathering.item45_page3:
    #         temp_page45.append(gathering.item45_page3)
    #     if gathering.item45_page4:
    #         temp_page45.append(gathering.item45_page4)
    #     if gathering.item45_page5:
    #         temp_page45.append(gathering.item45_page5)
    #     if gathering.item45_page6:
    #         temp_page45.append(gathering.item45_page6)
    #     if gathering.item45_page7:
    #         temp_page45.append(gathering.item45_page7)
    #     if gathering.item45_page8:
    #         temp_page45.append(gathering.item45_page8)
    #     if gathering.item45_page9:
    #         temp_page45.append(gathering.item45_page9)
    #     if gathering.item45_page10:
    #         temp_page45.append(gathering.item45_page10)
    #     temp_page45=[int(i) for i in temp_page45]
    #     temp_page45.sort(reverse=False)
    
    
        
    #     if temp_page45:
    #         gathering.total_gathering_45=temp_page45[0]
    #         gathering.wastage_form_45 = float(gathering.quantity_45) - float(gathering.total_gathering_45)
    #     else:
    #         gathering.item45_page1=0
    #         gathering.item45_page2=0
    #         gathering.item45_page3=0
    #         gathering.item45_page4=0
    #         gathering.item45_page5=0
    #         gathering.item45_page6=0
    #         gathering.item45_page7=0
    #         gathering.item45_page8=0
    #         gathering.item45_page9=0
    #         gathering.item45_page10=0



    #     temp_page46=[]
    #     if gathering.item46_page1:
    #         temp_page46.append(gathering.item46_page1)
    #     if gathering.item46_page2:
    #         temp_page46.append(gathering.item46_page2)
    #     if gathering.item46_page3:
    #         temp_page46.append(gathering.item46_page3)
    #     if gathering.item46_page4:
    #         temp_page46.append(gathering.item46_page4)
    #     if gathering.item46_page5:
    #         temp_page46.append(gathering.item46_page5)
    #     if gathering.item46_page6:
    #         temp_page46.append(gathering.item46_page6)
    #     if gathering.item46_page7:
    #         temp_page46.append(gathering.item46_page7)
    #     if gathering.item46_page8:
    #         temp_page46.append(gathering.item46_page8)
    #     if gathering.item46_page9:
    #         temp_page46.append(gathering.item46_page9)
    #     if gathering.item46_page10:
    #         temp_page46.append(gathering.item46_page10)
    #     temp_page46=[int(i) for i in temp_page46]
    #     temp_page46.sort(reverse=False)
    
    
        
    #     if temp_page46:
    #         gathering.total_gathering_46=temp_page46[0]
    #         gathering.wastage_form_46 = float(gathering.quantity_46) - float(gathering.total_gathering_46)
    #     else:
    #         gathering.item46_page1=0
    #         gathering.item46_page2=0
    #         gathering.item46_page3=0
    #         gathering.item46_page4=0
    #         gathering.item46_page5=0
    #         gathering.item46_page6=0
    #         gathering.item46_page7=0
    #         gathering.item46_page8=0
    #         gathering.item46_page9=0
    #         gathering.item46_page10=0


    #     temp_page47=[]
    #     if gathering.item47_page1:
    #         temp_page47.append(gathering.item47_page1)
    #     if gathering.item47_page2:
    #         temp_page47.append(gathering.item47_page2)
    #     if gathering.item47_page3:
    #         temp_page47.append(gathering.item47_page3)
    #     if gathering.item47_page4:
    #         temp_page47.append(gathering.item47_page4)
    #     if gathering.item47_page5:
    #         temp_page47.append(gathering.item47_page5)
    #     if gathering.item47_page6:
    #         temp_page47.append(gathering.item47_page6)
    #     if gathering.item47_page7:
    #         temp_page47.append(gathering.item47_page7)
    #     if gathering.item47_page8:
    #         temp_page47.append(gathering.item47_page8)
    #     if gathering.item47_page9:
    #         temp_page47.append(gathering.item47_page9)
    #     if gathering.item47_page10:
    #         temp_page47.append(gathering.item47_page10)
    #     temp_page47=[int(i) for i in temp_page47]
    #     temp_page47.sort(reverse=False)
    
    
        
    #     if temp_page47:
    #         gathering.total_gathering_47=temp_page47[0]
    #         gathering.wastage_form_47 = float(gathering.quantity_47) - float(gathering.total_gathering_47)
    #     else:
    #         gathering.item47_page1=0
    #         gathering.item47_page2=0
    #         gathering.item47_page3=0
    #         gathering.item47_page4=0
    #         gathering.item47_page5=0
    #         gathering.item47_page6=0
    #         gathering.item47_page7=0
    #         gathering.item47_page8=0
    #         gathering.item47_page9=0
    #         gathering.item47_page10=0


    #     temp_page48=[]
    #     if gathering.item48_page1:
    #         temp_page48.append(gathering.item48_page1)
    #     if gathering.item48_page2:
    #         temp_page48.append(gathering.item48_page2)
    #     if gathering.item48_page3:
    #         temp_page48.append(gathering.item48_page3)
    #     if gathering.item48_page4:
    #         temp_page48.append(gathering.item48_page4)
    #     if gathering.item48_page5:
    #         temp_page48.append(gathering.item48_page5)
    #     if gathering.item48_page6:
    #         temp_page48.append(gathering.item48_page6)
    #     if gathering.item48_page7:
    #         temp_page48.append(gathering.item48_page7)
    #     if gathering.item48_page8:
    #         temp_page48.append(gathering.item48_page8)
    #     if gathering.item48_page9:
    #         temp_page48.append(gathering.item48_page9)
    #     if gathering.item48_page10:
    #         temp_page48.append(gathering.item48_page10)
    #     temp_page48=[int(i) for i in temp_page48]
    #     temp_page48.sort(reverse=False)
    
    
        
    #     if temp_page48:
    #         gathering.total_gathering_48=temp_page48[0]
    #         gathering.wastage_form_48 = float(gathering.quantity_48) - float(gathering.total_gathering_48)
    #     else:
    #         gathering.item48_page1=0
    #         gathering.item48_page2=0
    #         gathering.item48_page3=0
    #         gathering.item48_page4=0
    #         gathering.item48_page5=0
    #         gathering.item48_page6=0
    #         gathering.item48_page7=0
    #         gathering.item48_page8=0
    #         gathering.item48_page9=0
    #         gathering.item48_page10=0

        
            
    #     temp_page49=[]
    #     if gathering.item49_page1:
    #         temp_page49.append(gathering.item49_page1)
    #     if gathering.item49_page2:
    #         temp_page49.append(gathering.item49_page2)
    #     if gathering.item49_page3:
    #         temp_page49.append(gathering.item49_page3)
    #     if gathering.item49_page4:
    #         temp_page49.append(gathering.item49_page4)
    #     if gathering.item49_page5:
    #         temp_page49.append(gathering.item49_page5)
    #     if gathering.item49_page6:
    #         temp_page49.append(gathering.item49_page6)
    #     if gathering.item49_page7:
    #         temp_page49.append(gathering.item49_page7)
    #     if gathering.item49_page8:
    #         temp_page49.append(gathering.item49_page8)
    #     if gathering.item49_page9:
    #         temp_page49.append(gathering.item49_page9)
    #     if gathering.item49_page10:
    #         temp_page49.append(gathering.item49_page10)
    #     temp_page49=[int(i) for i in temp_page49]
    #     temp_page49.sort(reverse=False)
    
    
        
    #     if temp_page49:
    #         gathering.total_gathering_49=temp_page49[0]
    #         gathering.wastage_form_49 = float(gathering.quantity_49) - float(gathering.total_gathering_49)
    #     else:
    #         gathering.item49_page1=0
    #         gathering.item49_page2=0
    #         gathering.item49_page3=0
    #         gathering.item49_page4=0
    #         gathering.item49_page5=0
    #         gathering.item49_page6=0
    #         gathering.item49_page7=0
    #         gathering.item49_page8=0
    #         gathering.item49_page9=0
    #         gathering.item49_page10=0



    #     temp_page50=[]
    #     if gathering.item50_page1:
    #         temp_page50.append(gathering.item50_page1)
    #     if gathering.item50_page2:
    #         temp_page50.append(gathering.item50_page2)
    #     if gathering.item50_page3:
    #         temp_page50.append(gathering.item50_page3)
    #     if gathering.item50_page4:
    #         temp_page50.append(gathering.item50_page4)
    #     if gathering.item50_page5:
    #         temp_page50.append(gathering.item50_page5)
    #     if gathering.item50_page6:
    #         temp_page50.append(gathering.item50_page6)
    #     if gathering.item50_page7:
    #         temp_page50.append(gathering.item50_page7)
    #     if gathering.item50_page8:
    #         temp_page50.append(gathering.item50_page8)
    #     if gathering.item50_page9:
    #         temp_page50.append(gathering.item50_page9)
    #     if gathering.item50_page10:
    #         temp_page50.append(gathering.item50_page10)
    #     temp_page50=[int(i) for i in temp_page50]
    #     temp_page50.sort(reverse=False)
    
    
        
    #     if temp_page50:
    #         gathering.total_gathering_50=temp_page50[0]
    #         gathering.wastage_form_50 = float(gathering.quantity_50) - float(gathering.total_gathering_50)
    #     else:
    #         gathering.item50_page1=0
    #         gathering.item50_page2=0
    #         gathering.item50_page3=0
    #         gathering.item50_page4=0
    #         gathering.item50_page5=0
    #         gathering.item50_page6=0
    #         gathering.item50_page7=0
    #         gathering.item50_page8=0
    #         gathering.item50_page9=0
    #         gathering.item50_page10=0




        
        
        
    #     temp_gather=[]
    #     if gathering.total_gathering_1:
    #         temp_gather.append(int(gathering.total_gathering_1))
    #     if gathering.total_gathering_2:
    #         temp_gather.append(int(gathering.total_gathering_2))
    #     if gathering.total_gathering_3:
    #         temp_gather.append(int(gathering.total_gathering_3))
    #     if gathering.total_gathering_4:
    #         temp_gather.append(int(gathering.total_gathering_4))
    #     if gathering.total_gathering_5:
    #         temp_gather.append(int(gathering.total_gathering_5))
    #     if gathering.total_gathering_6:
    #         temp_gather.append(int(gathering.total_gathering_6))
    #     if gathering.total_gathering_7:
    #         temp_gather.append(int(gathering.total_gathering_7))
    #     if gathering.total_gathering_8:
    #         temp_gather.append(int(gathering.total_gathering_8))
    #     if gathering.total_gathering_9:
    #         temp_gather.append(int(gathering.total_gathering_9))
    #     if gathering.total_gathering_10:
    #         temp_gather.append(int(gathering.total_gathering_10))
        
    #     if gathering.total_gathering_11:
    #         temp_gather.append(int(gathering.total_gathering_11))
    #     if gathering.total_gathering_12:
    #         temp_gather.append(int(gathering.total_gathering_12))
    #     if gathering.total_gathering_13:
    #         temp_gather.append(int(gathering.total_gathering_13))
    #     if gathering.total_gathering_14:
    #         temp_gather.append(int(gathering.total_gathering_14))
    #     if gathering.total_gathering_15:
    #         temp_gather.append(int(gathering.total_gathering_15))
    #     if gathering.total_gathering_16:
    #         temp_gather.append(int(gathering.total_gathering_16))
    #     if gathering.total_gathering_17:
    #         temp_gather.append(int(gathering.total_gathering_17))
    #     if gathering.total_gathering_18:
    #         temp_gather.append(int(gathering.total_gathering_18))
    #     if gathering.total_gathering_19:
    #         temp_gather.append(int(gathering.total_gathering_19))
    #     if gathering.total_gathering_20:
    #         temp_gather.append(int(gathering.total_gathering_20))
        
    #     if gathering.total_gathering_21:
    #         temp_gather.append(int(gathering.total_gathering_21))
    #     if gathering.total_gathering_22:
    #         temp_gather.append(int(gathering.total_gathering_22))
    #     if gathering.total_gathering_23:
    #         temp_gather.append(int(gathering.total_gathering_23))
    #     if gathering.total_gathering_24:
    #         temp_gather.append(int(gathering.total_gathering_24))
    #     if gathering.total_gathering_25:
    #         temp_gather.append(int(gathering.total_gathering_25))
    #     if gathering.total_gathering_26:
    #         temp_gather.append(int(gathering.total_gathering_26))
    #     if gathering.total_gathering_27:
    #         temp_gather.append(int(gathering.total_gathering_27))
    #     if gathering.total_gathering_28:
    #         temp_gather.append(int(gathering.total_gathering_28))
    #     if gathering.total_gathering_29:
    #         temp_gather.append(int(gathering.total_gathering_29))
    #     if gathering.total_gathering_30:
    #         temp_gather.append(int(gathering.total_gathering_30))

    #     if gathering.total_gathering_31:
    #         temp_gather.append(int(gathering.total_gathering_31))
    #     if gathering.total_gathering_32:
    #         temp_gather.append(int(gathering.total_gathering_32))
    #     if gathering.total_gathering_33:
    #         temp_gather.append(int(gathering.total_gathering_33))
    #     if gathering.total_gathering_34:
    #         temp_gather.append(int(gathering.total_gathering_34))
    #     if gathering.total_gathering_35:
    #         temp_gather.append(int(gathering.total_gathering_35))
    #     if gathering.total_gathering_36:
    #         temp_gather.append(int(gathering.total_gathering_36))
    #     if gathering.total_gathering_37:
    #         temp_gather.append(int(gathering.total_gathering_37))
    #     if gathering.total_gathering_38:
    #         temp_gather.append(int(gathering.total_gathering_38))
    #     if gathering.total_gathering_39:
    #         temp_gather.append(int(gathering.total_gathering_39))
    #     if gathering.total_gathering_40:
    #         temp_gather.append(int(gathering.total_gathering_40))

    #     if gathering.total_gathering_41:
    #         temp_gather.append(int(gathering.total_gathering_41))
    #     if gathering.total_gathering_42:
    #         temp_gather.append(int(gathering.total_gathering_42))
    #     if gathering.total_gathering_43:
    #         temp_gather.append(int(gathering.total_gathering_43))
    #     if gathering.total_gathering_44:
    #         temp_gather.append(int(gathering.total_gathering_44))
    #     if gathering.total_gathering_45:
    #         temp_gather.append(int(gathering.total_gathering_45))
    #     if gathering.total_gathering_46:
    #         temp_gather.append(int(gathering.total_gathering_46))
    #     if gathering.total_gathering_47:
    #         temp_gather.append(int(gathering.total_gathering_47))
    #     if gathering.total_gathering_48:
    #         temp_gather.append(int(gathering.total_gathering_48))
    #     if gathering.total_gathering_49:
    #         temp_gather.append(int(gathering.total_gathering_49))
    #     if gathering.total_gathering_50:
    #         temp_gather.append(int(gathering.total_gathering_50))

    #     temp_gather=[i for i in temp_gather]
    #     gathering.total_gathering=0
    #     for i in temp_gather:
    #         gathering.total_gathering=gathering.total_gathering+float(i)
    #     if gathering.total_gathering:
    #         gathering.wastage_form = float(gathering.total_quantity) - float(gathering.total_gathering)
    #         gathering.total_gathering= float(gathering.total_quantity)-gathering.wastage_form
        
    #     gathering.save()
        
        








from django.db.models import Q
from functools import reduce
import operator
@login_required(login_url="")
def binding_spark(request):
    if request.method =='POST':
        id = request.POST.get('id')
        total_binding=request.POST.get('total_binding')
        balance_binding = request.POST.get('balance_binding')
        binding_received_1=request.POST.get('binding_received_1')
        balance_binding_1=request.POST.get('balance_binding_1')
        binding_received_2=request.POST.get('binding_received_2')
        balance_binding_2=request.POST.get('balance_binding_2')
        binding_received_3=request.POST.get('binding_received_3')
        balance_binding_3=request.POST.get('balance_binding_3')
        binding_received_4=request.POST.get('binding_received_4')
        balance_binding_4=request.POST.get('balance_binding_4')
        binding_received_5=request.POST.get('binding_received_5')
        balance_binding_5=request.POST.get('balance_binding_5')
        binding_received_6=request.POST.get('binding_received_6')
        balance_binding_6=request.POST.get('balance_binding_6')
        binding_received_7=request.POST.get('binding_received_7')
        balance_binding_7=request.POST.get('balance_binding_7')
        binding_received_8=request.POST.get('binding_received_8')
        balance_binding_8=request.POST.get('balance_binding_8')
        binding_received_9=request.POST.get('binding_received_9')
        balance_binding_9=request.POST.get('balance_binding_9')
        binding_received_10=request.POST.get('binding_received_10')
        balance_binding_10=request.POST.get('balance_binding_10')

        binding_received_11=request.POST.get('binding_received_11')
        balance_binding_11=request.POST.get('balance_binding_11')
        binding_received_12=request.POST.get('binding_received_12')
        balance_binding_12=request.POST.get('balance_binding_12')
        binding_received_13=request.POST.get('binding_received_13')
        balance_binding_13=request.POST.get('balance_binding_13')
        binding_received_14=request.POST.get('binding_received_14')
        balance_binding_14=request.POST.get('balance_binding_14')
        binding_received_15=request.POST.get('binding_received_15')
        balance_binding_15=request.POST.get('balance_binding_15')
        binding_received_16=request.POST.get('binding_received_16')
        balance_binding_16=request.POST.get('balance_binding_16')
        binding_received_17=request.POST.get('binding_received_17')
        balance_binding_17=request.POST.get('balance_binding_17')
        binding_received_18=request.POST.get('binding_received_18')
        balance_binding_18=request.POST.get('balance_binding_18')
        binding_received_19=request.POST.get('binding_received_19')
        balance_binding_19=request.POST.get('balance_binding_19')
        binding_received_20=request.POST.get('binding_received_20')
        balance_binding_20=request.POST.get('balance_binding_20')

        binding_received_21=request.POST.get('binding_received_21')
        balance_binding_21=request.POST.get('balance_binding_21')
        binding_received_22=request.POST.get('binding_received_22')
        balance_binding_22=request.POST.get('balance_binding_22')
        binding_received_23=request.POST.get('binding_received_23')
        balance_binding_23=request.POST.get('balance_binding_23')
        binding_received_24=request.POST.get('binding_received_24')
        balance_binding_24=request.POST.get('balance_binding_24')
        binding_received_25=request.POST.get('binding_received_25')
        balance_binding_25=request.POST.get('balance_binding_25')
        binding_received_26=request.POST.get('binding_received_26')
        balance_binding_26=request.POST.get('balance_binding_26')
        binding_received_27=request.POST.get('binding_received_27')
        balance_binding_27=request.POST.get('balance_binding_27')
        binding_received_28=request.POST.get('binding_received_28')
        balance_binding_28=request.POST.get('balance_binding_28')
        binding_received_29=request.POST.get('binding_received_29')
        balance_binding_29=request.POST.get('balance_binding_29')
        binding_received_30=request.POST.get('binding_received_30')
        balance_binding_30=request.POST.get('balance_binding_30')

        binding_received_31=request.POST.get('binding_received_31')
        balance_binding_31=request.POST.get('balance_binding_31')
        binding_received_32=request.POST.get('binding_received_32')
        balance_binding_32=request.POST.get('balance_binding_32')
        binding_received_33=request.POST.get('binding_received_33')
        balance_binding_33=request.POST.get('balance_binding_33')
        binding_received_34=request.POST.get('binding_received_34')
        balance_binding_34=request.POST.get('balance_binding_34')
        binding_received_35=request.POST.get('binding_received_35')
        balance_binding_35=request.POST.get('balance_binding_35')
        binding_received_36=request.POST.get('binding_received_36')
        balance_binding_36=request.POST.get('balance_binding_36')
        binding_received_37=request.POST.get('binding_received_37')
        balance_binding_37=request.POST.get('balance_binding_37')
        binding_received_38=request.POST.get('binding_received_38')
        balance_binding_38=request.POST.get('balance_binding_38')
        binding_received_39=request.POST.get('binding_received_39')
        balance_binding_39=request.POST.get('balance_binding_39')
        binding_received_40=request.POST.get('binding_received_40')
        balance_binding_40=request.POST.get('balance_binding_40')

        binding_received_41=request.POST.get('binding_received_41')
        balance_binding_41=request.POST.get('balance_binding_41')
        binding_received_42=request.POST.get('binding_received_42')
        balance_binding_42=request.POST.get('balance_binding_42')
        binding_received_43=request.POST.get('binding_received_43')
        balance_binding_43=request.POST.get('balance_binding_43')
        binding_received_44=request.POST.get('binding_received_44')
        balance_binding_44=request.POST.get('balance_binding_44')
        binding_received_45=request.POST.get('binding_received_45')
        balance_binding_45=request.POST.get('balance_binding_45')
        binding_received_46=request.POST.get('binding_received_46')
        balance_binding_46=request.POST.get('balance_binding_46')
        binding_received_47=request.POST.get('binding_received_47')
        balance_binding_47=request.POST.get('balance_binding_47')
        binding_received_48=request.POST.get('binding_received_48')
        balance_binding_48=request.POST.get('balance_binding_48')
        binding_received_49=request.POST.get('binding_received_49')
        balance_binding_49=request.POST.get('balance_binding_49')
        binding_received_50=request.POST.get('binding_received_50')
        balance_binding_50=request.POST.get('balance_binding_50')
        binding_date = request.POST.get('print_date')

        order = orders.objects.filter(order_id=id).get()
        print('order',order)
        order.binding_received_1=binding_received_1
        order.balance_binding_1=balance_binding_1
        order.binding_received_2=binding_received_2
        order.balance_binding_2=balance_binding_2
        order.binding_received_3=binding_received_3
        order.balance_binding_3=balance_binding_3
        order.binding_received_4=binding_received_4
        order.balance_binding_4=balance_binding_4
        order.binding_received_5=binding_received_5
        order.balance_binding_5=balance_binding_5
        order.binding_received_6=binding_received_6
        order.balance_binding_6=balance_binding_6
        order.binding_received_7=binding_received_7
        order.balance_binding_7=balance_binding_7
        order.binding_received_8=binding_received_8
        order.balance_binding_8=balance_binding_8
        order.binding_received_9=binding_received_9
        order.balance_binding_9=balance_binding_9
        order.binding_received_10=binding_received_10
        order.balance_binding_10=balance_binding_10

        order.binding_received_11=binding_received_11
        order.balance_binding_11=balance_binding_11
        order.binding_received_12=binding_received_12
        order.balance_binding_12=balance_binding_12
        order.binding_received_13=binding_received_13
        order.balance_binding_13=balance_binding_13
        order.binding_received_14=binding_received_14
        order.balance_binding_14=balance_binding_14
        order.binding_received_15=binding_received_15
        order.balance_binding_15=balance_binding_15
        order.binding_received_16=binding_received_16
        order.balance_binding_16=balance_binding_16
        order.binding_received_17=binding_received_17
        order.balance_binding_17=balance_binding_17
        order.binding_received_18=binding_received_18
        order.balance_binding_18=balance_binding_18
        order.binding_received_19=binding_received_19
        order.balance_binding_19=balance_binding_19
        order.binding_received_20=binding_received_20
        order.balance_binding_20=balance_binding_20

        order.binding_received_21=binding_received_21
        order.balance_binding_21=balance_binding_21
        order.binding_received_22=binding_received_22
        order.balance_binding_22=balance_binding_22
        order.binding_received_23=binding_received_23
        order.balance_binding_23=balance_binding_23
        order.binding_received_24=binding_received_24
        order.balance_binding_24=balance_binding_24
        order.binding_received_25=binding_received_25
        order.balance_binding_25=balance_binding_25
        order.binding_received_26=binding_received_26
        order.balance_binding_26=balance_binding_26
        order.binding_received_27=binding_received_27
        order.balance_binding_27=balance_binding_27
        order.binding_received_28=binding_received_28
        order.balance_binding_28=balance_binding_28
        order.binding_received_29=binding_received_29
        order.balance_binding_29=balance_binding_29
        order.binding_received_30=binding_received_30
        order.balance_binding_30=balance_binding_30

        order.binding_received_31=binding_received_31
        order.balance_binding_31=balance_binding_31
        order.binding_received_32=binding_received_32
        order.balance_binding_32=balance_binding_32
        order.binding_received_33=binding_received_33
        order.balance_binding_33=balance_binding_33
        order.binding_received_34=binding_received_34
        order.balance_binding_34=balance_binding_34
        order.binding_received_35=binding_received_35
        order.balance_binding_35=balance_binding_35
        order.binding_received_36=binding_received_36
        order.balance_binding_36=balance_binding_36
        order.binding_received_37=binding_received_37
        order.balance_binding_37=balance_binding_37
        order.binding_received_38=binding_received_38
        order.balance_binding_38=balance_binding_38
        order.binding_received_39=binding_received_39
        order.balance_binding_39=balance_binding_39
        order.binding_received_40=binding_received_40
        order.balance_binding_40=balance_binding_40

        order.binding_received_41=binding_received_41
        order.balance_binding_41=balance_binding_41
        order.binding_received_42=binding_received_42
        order.balance_binding_42=balance_binding_42
        order.binding_received_43=binding_received_43
        order.balance_binding_43=balance_binding_43
        order.binding_received_44=binding_received_44
        order.balance_binding_44=balance_binding_44
        order.binding_received_45=binding_received_45
        order.balance_binding_45=balance_binding_45
        order.binding_received_46=binding_received_46
        order.balance_binding_46=balance_binding_46
        order.binding_received_47=binding_received_47
        order.balance_binding_47=balance_binding_47
        order.binding_received_48=binding_received_48
        order.balance_binding_48=balance_binding_48
        order.binding_received_49=binding_received_49
        order.balance_binding_49=balance_binding_49
        order.binding_received_50=binding_received_50
        order.balance_binding_50=balance_binding_50

        order.total_binding=total_binding
        order.balance_binding=balance_binding 
        order.binding_date=datetime.datetime.now()
        order.save()
    data1 = orders.objects.filter(brand_name_1='Spark',brand_name_2='Spark').order_by('-order_id')
    
    # List of all brand_name fields (brand_name_1 to brand_name_50)
    brand_name_fields = [f'brand_name_{i}' for i in range(1, 51)]

    # Create a list of Q objects for each brand_name field
    brand_name_queries = [Q(**{field: 'Spark'}) for field in brand_name_fields]

    # Use reduce and operator.or_ to combine the Q objects using OR operator
    combined_query = reduce(operator.or_, brand_name_queries)

    # Fetch the filtered data
    data_spark = orders.objects.filter(combined_query).order_by('-order_id')    
    print('data_spark',data_spark)
    context={
        'data1':data_spark,       
    }
    return render(request,'processing/bindings_spark.html',context) 





from django.db import IntegrityError
@login_required(login_url="")
def edit_spark_binding(request,order_id):
    data2 = orders.objects.get(order_id=order_id)
    print('gjhgjmgj',order_id)
    
    # List of all brand_name fields (brand_name_1 to brand_name_50)
    brand_name_fields = [f'brand_name_{i}' for i in range(1, 51)]

    # Initialize an empty list to store the filtered brand_names
    filtered_brand_names = []

    # Loop through each brand_name field and check if it is 'Spark'
    for field in brand_name_fields:
        brand_name_value = getattr(data2, field)  # Get the value of the brand_name field
        if brand_name_value == 'Spark':
            filtered_brand_names.append(field)
    brand_name_value = 'Spark'
    for i in filtered_brand_names:        
        print('filtered_brand_names',i,brand_name_value)
        
    # data3 = Manual_binding(striching1=striching1)
    if request.method == 'POST':
       
        data2.striching1=request.POST.get('striching1')
        print('oooooooooooooo',data2.striching1)
        data2.pasting1=request.POST.get('pasting1')
        print('bbbbbbbbbbbbbbbbb',data2.pasting1)
        data2.cutting1=request.POST.get('cutting1')
        print('cccccccccccccccccccc',data2.cutting1)
        data2.striching2=request.POST.get('striching2')
        data2.pasting2=request.POST.get('pasting2')
        data2.cutting2=request.POST.get('cutting2')
        data2.striching3=request.POST.get('striching3')
        data2.pasting3=request.POST.get('pasting3')
        data2.cutting3=request.POST.get('cutting3')
        data2.striching4=request.POST.get('striching4')
        data2.pasting4=request.POST.get('pasting4')
        data2.cutting4=request.POST.get('cutting4')
        data2.striching5=request.POST.get('striching5')
        data2.pasting5=request.POST.get('pasting5')
        data2.cutting5=request.POST.get('cutting5')
        data2.striching6=request.POST.get('striching6')
        data2.pasting6=request.POST.get('pasting6')
        data2.cutting6=request.POST.get('cutting6')
        data2.striching7=request.POST.get('striching7')
        data2.pasting7=request.POST.get('pasting7')
        data2.cutting7=request.POST.get('cutting7')
        data2.striching8=request.POST.get('striching8')
        data2.pasting8=request.POST.get('pasting8')
        data2.cutting8=request.POST.get('cutting8')
        data2.striching9=request.POST.get('striching9')
        data2.pasting9=request.POST.get('pasting9')
        data2.cutting9=request.POST.get('cutting9')
        data2.striching10=request.POST.get('striching10')
        data2.pasting10=request.POST.get('pasting10')
        data2.cutting10=request.POST.get('cutting10')
        
        data2.striching11=request.POST.get('striching11')
        data2.pasting11=request.POST.get('pasting11')
        data2.cutting11=request.POST.get('cutting11')
        data2.striching12=request.POST.get('striching12')
        data2.pasting12=request.POST.get('pasting12')
        data2.cutting12=request.POST.get('cutting12')
        data2.striching13=request.POST.get('striching13')
        data2.pasting13=request.POST.get('pasting13')
        data2.cutting13=request.POST.get('cutting13')
        data2.striching14=request.POST.get('striching14')
        data2.pasting14=request.POST.get('pasting14')
        data2.cutting14=request.POST.get('cutting14')
        data2.striching15=request.POST.get('striching15')
        data2.pasting15=request.POST.get('pasting15')
        data2.cutting15=request.POST.get('cutting15')
        data2.striching16=request.POST.get('striching16')
        data2.pasting16=request.POST.get('pasting16')
        data2.cutting16=request.POST.get('cutting16')
        data2.striching17=request.POST.get('striching17')
        data2.pasting17=request.POST.get('pasting17')
        data2.cutting17=request.POST.get('cutting17')
        data2.striching18=request.POST.get('striching18')
        data2.pasting18=request.POST.get('pasting18')
        data2.cutting18=request.POST.get('cutting18')
        data2.striching19=request.POST.get('striching19')
        data2.pasting19=request.POST.get('pasting19')
        data2.cutting19=request.POST.get('cutting19')
        data2.striching19=request.POST.get('striching19')
        data2.pasting19=request.POST.get('pasting19')
        data2.cutting19=request.POST.get('cutting19')
        data2.striching20=request.POST.get('striching20')
        data2.pasting20=request.POST.get('pasting20')
        data2.cutting20=request.POST.get('cutting20')
        
        data2.striching21=request.POST.get('striching21')
        data2.pasting21=request.POST.get('pasting21')
        data2.cutting21=request.POST.get('cutting21')
        data2.striching22=request.POST.get('striching22')
        data2.pasting22=request.POST.get('pasting22')
        data2.cutting22=request.POST.get('cutting22')
        data2.striching23=request.POST.get('striching23')
        data2.pasting23=request.POST.get('pasting23')
        data2.cutting23=request.POST.get('cutting23')
        data2.striching24=request.POST.get('striching24')
        data2.pasting24=request.POST.get('pasting24')
        data2.cutting24=request.POST.get('cutting24')
        data2.striching25=request.POST.get('striching25')
        data2.pasting25=request.POST.get('pasting25')
        data2.cutting25=request.POST.get('cutting25')
        data2.striching26=request.POST.get('striching26')
        data2.pasting26=request.POST.get('pasting26')
        data2.cutting26=request.POST.get('cutting26')
        data2.striching27=request.POST.get('striching27')
        data2.pasting27=request.POST.get('pasting27')
        data2.cutting27=request.POST.get('cutting27')
        data2.striching28=request.POST.get('striching28')
        data2.pasting28=request.POST.get('pasting28')
        data2.cutting28=request.POST.get('cutting28')
        data2.striching29=request.POST.get('striching29')
        data2.pasting29=request.POST.get('pasting29')
        data2.cutting29=request.POST.get('cutting29')
        data2.striching30=request.POST.get('striching30')
        data2.pasting30=request.POST.get('pasting30')
        data2.cutting30=request.POST.get('cutting30')

        data2.striching31=request.POST.get('striching31')
        data2.pasting31=request.POST.get('pasting31')
        data2.cutting31=request.POST.get('cutting31')
        data2.striching32=request.POST.get('striching32')
        data2.pasting32=request.POST.get('pasting32')
        data2.cutting32=request.POST.get('cutting32')
        data2.striching33=request.POST.get('striching33')
        data2.pasting33=request.POST.get('pasting33')
        data2.cutting33=request.POST.get('cutting33')
        data2.striching34=request.POST.get('striching34')
        data2.pasting34=request.POST.get('pasting34')
        data2.cutting34=request.POST.get('cutting34')
        data2.striching35=request.POST.get('striching35')
        data2.pasting35=request.POST.get('pasting35')
        data2.cutting35=request.POST.get('cutting35')
        data2.striching36=request.POST.get('striching36')
        data2.pasting36=request.POST.get('pasting36')
        data2.cutting36=request.POST.get('cutting36')
        data2.striching37=request.POST.get('striching37')
        data2.pasting37=request.POST.get('pasting37')
        data2.cutting37=request.POST.get('cutting37')
        data2.striching38=request.POST.get('striching38')
        data2.pasting38=request.POST.get('pasting38')
        data2.cutting38=request.POST.get('cutting38')
        data2.striching39=request.POST.get('striching39')
        data2.pasting39=request.POST.get('pasting39')
        data2.cutting39=request.POST.get('cutting39')
        data2.striching40=request.POST.get('striching40')
        data2.pasting40=request.POST.get('pasting40')
        data2.cutting40=request.POST.get('cutting40')

        data2.striching41=request.POST.get('striching41')
        data2.pasting41=request.POST.get('pasting41')
        data2.cutting41=request.POST.get('cutting41')
        data2.striching42=request.POST.get('striching42')
        data2.pasting42=request.POST.get('pasting42')
        data2.cutting42=request.POST.get('cutting42')
        data2.striching43=request.POST.get('striching43')
        data2.pasting43=request.POST.get('pasting43')
        data2.cutting43=request.POST.get('cutting43')
        data2.striching44=request.POST.get('striching44')
        data2.pasting44=request.POST.get('pasting44')
        data2.cutting44=request.POST.get('cutting44')
        data2.striching45=request.POST.get('striching45')
        data2.pasting45=request.POST.get('pasting45')
        data2.cutting45=request.POST.get('cutting45')
        data2.striching46=request.POST.get('striching46')
        data2.pasting46=request.POST.get('pasting46')
        data2.cutting46=request.POST.get('cutting46')
        data2.striching47=request.POST.get('striching47')
        data2.pasting47=request.POST.get('pasting47')
        data2.cutting47=request.POST.get('cutting47')
        data2.striching48=request.POST.get('striching48')
        data2.pasting48=request.POST.get('pasting48')
        data2.cutting48=request.POST.get('cutting48')
        data2.striching49=request.POST.get('striching49')
        data2.pasting49=request.POST.get('pasting49')
        data2.cutting49=request.POST.get('cutting49')
        data2.striching50=request.POST.get('striching50')
        data2.pasting50=request.POST.get('pasting50')
        data2.cutting50=request.POST.get('cutting50')


        try:
            # Try to get an existing object with the given order_id
            data6, created = Manual_binding.objects.get_or_create(order_id=order_id)

            # If the object was created, update the fields with the new values
            if created:
                data6 = Manual_binding(order_id = order_id, striching1 = data2.striching1,pasting1= data2.pasting1,cutting1= data2.cutting1,striching2= data2.striching2,pasting2= data2.pasting2,
                cutting2=data2.cutting2,
                striching3=data2.striching3,
                pasting3= data2.pasting3,
                cutting3= data2.cutting3,
                striching4= data2.striching4,
                pasting4= data2.pasting4,
                cutting4= data2.cutting4,
                striching5= data2.striching5,
                pasting5= data2.pasting5,
                cutting5= data2.cutting5,
                striching6= data2.striching6,
                pasting6= data2.pasting6,
                cutting6= data2.cutting6,
                striching7= data2.striching7,
                pasting7= data2.pasting7,
                cutting7= data2.cutting7,
                striching8=data2.striching8,
                pasting8=data2.pasting8,
                cutting8= data2.cutting8,
                striching9=data2.striching9,
                pasting9=data2.pasting9,
                cutting9= data2.cutting9,
                striching10= data2.striching10,
                pasting10= data2.pasting10,
                cutting10= data2.cutting10,
                striching11= data2.striching11,
                pasting11= data2.pasting11,
                cutting11= data2.cutting11)
                # data6.striching12= data2.striching12
                # data6.pasting12= data2.pasting12
                # data6.cutting12= data2.cutting12
                # data6.striching13= data2.striching13
                # data6.pasting13= data2.pasting13
                # data6.cutting13= data2.cutting13
                # data6.striching14= data2.striching14
                # data6.pasting14= data2.pasting14
                # data6.cutting14= data2.cutting14
                # data6.striching15= data2.striching15
                # data6.pasting15= data2.pasting15
                # data6.cutting15= data2.cutting15
                # data6.striching16= data2.striching16
                # data6.pasting16= data2.pasting16
                # data6.cutting16= data2.cutting16
                # data6.striching17= data2.striching17
                # data6.pasting17= data2.pasting17
                # data6.cutting17= data2.cutting17
                # data6.striching18= data2.striching18
                # data6.pasting18= data2.pasting18
                # data6.cutting18= data2.cutting18
                # data6.striching19= data2.striching19
                # data6.pasting19= data2.pasting19
                # data6.cutting19= data2.cutting19
                # data6.striching20= data2.striching20
                # data6.pasting20= data2.pasting20
                # data6.cutting20= data2.cutting20
                # data6.striching21= data2.striching21
                # data6.pasting21= data2.pasting21
                # data6.cutting21= data2.cutting21
                # data6.striching22= data2.striching22
                # data6.pasting22= data2.pasting22
                # data6.cutting22= data2.cutting22
                # data6.striching23= data2.striching23
                # data6.pasting23= data2.pasting23
                # data6.cutting23= data2.cutting23
                # data6.striching24= data2.striching24
                # data6.pasting24= data2.pasting24
                # data6.cutting24= data2.cutting24
                # data6.striching25= data2.striching25
                # data6.pasting25= data2.pasting25
                # data6.cutting25= data2.cutting25
                # data6.striching26= data2.striching26
                # data6.pasting26= data2.pasting26
                # data6.cutting26= data2.cutting26
                # data6.striching27= data2.striching27
                # data6.pasting27= data2.pasting27
                # data6.cutting27= data2.cutting27
                # data6.striching28= data2.striching28
                # data6.pasting28= data2.pasting28
                # data6.cutting28= data2.cutting28
                # data6.striching29= data2.striching29
                # data6.pasting29= data2.pasting29
                # data6.cutting29= data2.cutting29
                # data6.striching30= data2.striching30
                # data6.pasting30= data2.pasting30
                # data6.cutting30= data2.cutting30
                # data6.striching31= data2.striching31
                # data6.pasting31= data2.pasting31
                # data6.cutting31= data2.cutting31
                # data6.striching32= data2.striching32
                # data6.pasting32= data2.pasting32
                # data6.cutting32= data2.cutting32
                # data6.striching33= data2.striching33
                # data6.pasting33= data2.pasting33
                # data6.cutting33= data2.cutting33
                # data6.striching34= data2.striching34
                # data6.pasting34= data2.pasting34
                # data6.cutting34= data2.cutting34
                # data6.striching35= data2.striching35
                # data6.pasting35= data2.pasting35
                # data6.cutting35= data2.cutting35
                # data6.striching36= data2.striching36
                # data6.pasting36= data2.pasting36
                # data6.cutting36= data2.cutting36
                # data6.striching37= data2.striching37
                # data6.pasting37= data2.pasting37
                # data6.cutting37= data2.cutting37
                # data6.striching38= data2.striching38
                # data6.pasting38= data2.pasting38
                # data6.cutting38= data2.cutting38
                # data6.striching39= data2.striching39
                # data6.pasting39= data2.pasting39
                # data6.cutting39= data2.cutting39
                # data6.striching40= data2.striching40
                # data6.pasting40= data2.pasting40
                # data6.cutting40= data2.cutting40
                # data6.striching41= data2.striching41
                # data6.pasting41= data2.pasting41
                # data6.cutting41= data2.cutting41
                # data6.striching42= data2.striching42
                # data6.pasting42= data2.pasting42
                # data6.cutting42= data2.cutting42
                # data6.striching43= data2.striching43
                # data6.pasting43= data2.pasting43
                # data6.cutting43= data2.cutting43
                # data6.striching44= data2.striching44
                # data6.pasting44= data2.pasting44,
                # data6.cutting44= data2.cutting44,
                # data6.striching45= data2.striching45,
                # data6.pasting45= data2.pasting45,
                # data6.cutting45= data2.cutting45,
                # data6.striching46= data2.striching46,
                # data6.pasting46= data2.pasting46,
                # data6.cutting46= data2.cutting46,
                # data6.striching47= data2.striching47,
                # data6.pasting47= data2.pasting47,
                # data6.cutting47= data2.cutting47,
                # data6.striching48=data2.striching48,
                # data6.pasting48= data2.pasting48,
                # data6.cutting48= data2.cutting48,
                # data6.striching49= data2.striching49,
                # data6.pasting49= data2.pasting49,
                # data6.cutting49= data2.cutting49,
                # data6.striching50= data2.striching50,
                # data6.pasting50= data2.pasting50,
                # data6.cutting50= data2.cutting50,
            

                data6.save()
        except IntegrityError:
            # Handle the case where there's an IntegrityError (e.g., if order_id is not unique)
            # You can raise an exception, log an error, or perform any other actions as needed.
            pass
        
         
        
        
        
        
        
        
        
        data2.total_binding=request.POST.get('total_binding')
        data2.balance_binding = request.POST.get('balance_binding')

        data2.binding_received_1=request.POST.get('binding_received_1')
        data2.binding_received_2=request.POST.get('binding_received_2')
        data2.binding_received_3=request.POST.get('binding_received_3')
        data2.binding_received_4=request.POST.get('binding_received_4')
        data2.binding_received_5=request.POST.get('binding_received_5')
        data2.binding_received_6=request.POST.get('binding_received_6')
        data2.binding_received_7=request.POST.get('binding_received_7')
        data2.binding_received_8=request.POST.get('binding_received_8')
        data2.binding_received_9=request.POST.get('binding_received_9')
        data2.binding_received_10=request.POST.get('binding_received_10')
    

        data2.binding_received_11=request.POST.get('binding_received_11')
        data2.binding_received_12=request.POST.get('binding_received_12')
        data2.binding_received_13=request.POST.get('binding_received_13')
        data2.binding_received_14=request.POST.get('binding_received_14')
        data2.binding_received_15=request.POST.get('binding_received_15')
        data2.binding_received_16=request.POST.get('binding_received_16')
        data2.binding_received_17=request.POST.get('binding_received_17')
        data2.binding_received_18=request.POST.get('binding_received_18')
        data2.binding_received_19=request.POST.get('binding_received_19')
        data2.binding_received_20=request.POST.get('binding_received_20')
        

        data2.binding_received_21=request.POST.get('binding_received_21')
        data2.binding_received_22=request.POST.get('binding_received_22')
        data2.binding_received_23=request.POST.get('binding_received_23')
        data2.binding_received_24=request.POST.get('binding_received_24')
        data2.binding_received_25=request.POST.get('binding_received_25')
        data2.binding_received_26=request.POST.get('binding_received_26')
        data2.binding_received_27=request.POST.get('binding_received_27')
        data2.binding_received_28=request.POST.get('binding_received_28')
        data2.binding_received_29=request.POST.get('binding_received_29')
        data2.binding_received_30=request.POST.get('binding_received_30')
        

        data2.binding_received_31=request.POST.get('binding_received_31')
        data2.binding_received_32=request.POST.get('binding_received_32')
        data2.binding_received_33=request.POST.get('binding_received_33')
        data2.binding_received_34=request.POST.get('binding_received_34')
        data2.binding_received_35=request.POST.get('binding_received_35')
        data2.binding_received_36=request.POST.get('binding_received_36')
        data2.binding_received_37=request.POST.get('binding_received_37')
        data2.binding_received_38=request.POST.get('binding_received_38')
        data2.binding_received_39=request.POST.get('binding_received_39')
        data2.binding_received_40=request.POST.get('binding_received_40')
        

        data2.binding_received_41=request.POST.get('binding_received_41')
        data2.binding_received_42=request.POST.get('binding_received_42')
        data2.binding_received_43=request.POST.get('binding_received_43')
        data2.binding_received_44=request.POST.get('binding_received_44')
        data2.binding_received_45=request.POST.get('binding_received_45')
        data2.binding_received_46=request.POST.get('binding_received_46')
        data2.binding_received_47=request.POST.get('binding_received_47')
        data2.binding_received_48=request.POST.get('binding_received_48')
        data2.binding_received_49=request.POST.get('binding_received_49')
        data2.binding_received_40=request.POST.get('binding_received_50')
        

        
        data2.binding_date = datetime.datetime.now()

        if data2.binding_received_1:
            data2.balance_binding_1 = float(data2.quantity_1) - float(data2.binding_received_1)
        else:
            data2.balance_binding_1 = 0
        
        if data2.binding_received_2:
            data2.balance_binding_2 = float(data2.quantity_2) - float(data2.binding_received_2)
        else:
            data2.balance_binding_2 = 0
        
        if data2.binding_received_3:
            data2.balance_binding_3 = float(data2.quantity_3) - float(data2.binding_received_3)
        else:
            data2.balance_binding_3 = 0
        
        if data2.binding_received_4:
            data2.balance_binding_4 = float(data2.quantity_4) - float(data2.binding_received_4)
        else:
            data2.balance_binding_4 = 0
        
        if data2.binding_received_5:
            data2.balance_binding_5 = float(data2.quantity_5) - float(data2.binding_received_5)
        else:
            data2.balance_binding_5 = 0
        
        if data2.binding_received_6:
            data2.balance_binding_6 = float(data2.quantity_6) - float(data2.binding_received_6)
        else:
            data2.balance_binding_6 = 0
        
        if data2.binding_received_7:
            data2.balance_binding_7 = float(data2.quantity_7) - float(data2.binding_received_7)
        else:
            data2.balance_binding_7 = 0
        
        if data2.binding_received_8:
            data2.balance_binding_8 = float(data2.quantity_8) - float(data2.binding_received_8)
        else:
            data2.balance_binding_8 = 0
        
        if data2.binding_received_9:
            data2.balance_binding_9 = float(data2.quantity_9) - float(data2.binding_received_9)
        else:
            data2.balance_binding_9 = 0
        
        if data2.binding_received_10:
            data2.balance_binding_10 = float(data2.quantity_10) - float(data2.binding_received_10)
        else:
            data2.balance_binding_10 = 0


        
        if data2.binding_received_11:
            data2.balance_binding_11 = float(data2.quantity_11) - float(data2.binding_received_11)
        else:
            data2.balance_binding_11 = 0
        
        if data2.binding_received_12:
            data2.balance_binding_12 = float(data2.quantity_12) - float(data2.binding_received_12)
        else:
            data2.balance_binding_12 = 0
        
        if data2.binding_received_13:
            data2.balance_binding_13 = float(data2.quantity_13) - float(data2.binding_received_13)
        else:
            data2.balance_binding_13 = 0
        
        if data2.binding_received_14:
            data2.balance_binding_14 = float(data2.quantity_14) - float(data2.binding_received_14)
        else:
            data2.balance_binding_14 = 0
        
        if data2.binding_received_15:
            data2.balance_binding_15 = float(data2.quantity_15) - float(data2.binding_received_15)
        else:
            data2.balance_binding_15 = 0
        
        if data2.binding_received_16:
            data2.balance_binding_16 = float(data2.quantity_16) - float(data2.binding_received_16)
        else:
            data2.balance_binding_16 = 0
        
        if data2.binding_received_17:
            data2.balance_binding_17 = float(data2.quantity_17) - float(data2.binding_received_17)
        else:
            data2.balance_binding_17 = 0
        
        if data2.binding_received_18:
            data2.balance_binding_18 = float(data2.quantity_18) - float(data2.binding_received_18)
        else:
            data2.balance_binding_18 = 0
        
        if data2.binding_received_19:
            data2.balance_binding_19 = float(data2.quantity_19) - float(data2.binding_received_19)
        else:
            data2.balance_binding_19 = 0
        
        
        if data2.binding_received_20:
            data2.balance_binding_20 = float(data2.quantity_20) - float(data2.binding_received_20)
        else:
            data2.balance_binding_20 = 0

        if data2.binding_received_21:
            data2.balance_binding_21 = float(data2.quantity_21) - float(data2.binding_received_21)
        else:
            data2.balance_binding_21 = 0
        
        if data2.binding_received_22:
            data2.balance_binding_22 = float(data2.quantity_22) - float(data2.binding_received_22)
        else:
            data2.balance_binding_22 = 0
        
        if data2.binding_received_23:
            data2.balance_binding_23 = float(data2.quantity_23) - float(data2.binding_received_23)
        else:
            data2.balance_binding_23 = 0
        
        if data2.binding_received_24:
            data2.balance_binding_24 = float(data2.quantity_24) - float(data2.binding_received_24)
        else:
            data2.balance_binding_24 = 0
        
        if data2.binding_received_25:
            data2.balance_binding_25 = float(data2.quantity_25) - float(data2.binding_received_25)
        else:
            data2.balance_binding_25 = 0
        
        if data2.binding_received_26:
            data2.balance_binding_26 = float(data2.quantity_26) - float(data2.binding_received_26)
        else:
            data2.balance_binding_26 = 0
        
        if data2.binding_received_27:
            data2.balance_binding_27 = float(data2.quantity_27) - float(data2.binding_received_27)
        else:
            data2.balance_binding_27 = 0
        
        if data2.binding_received_28:
            data2.balance_binding_28 = float(data2.quantity_28) - float(data2.binding_received_28)
        else:
            data2.balance_binding_28 = 0
        
        if data2.binding_received_29:
            data2.balance_binding_29 = float(data2.quantity_29) - float(data2.binding_received_29)
        else:
            data2.balance_binding_29 = 0
        
        if data2.binding_received_30:
            data2.balance_binding_30 = float(data2.quantity_30) - float(data2.binding_received_30)
        else:
            data2.balance_binding_30 = 0

        if data2.binding_received_31:
            data2.balance_binding_31 = float(data2.quantity_31) - float(data2.binding_received_31)
        else:
            data2.balance_binding_31 = 0
        
        if data2.binding_received_32:
            data2.balance_binding_32 = float(data2.quantity_32) - float(data2.binding_received_32)
        else:
            data2.balance_binding_32 = 0
        
        if data2.binding_received_33:
            data2.balance_binding_33 = float(data2.quantity_33) - float(data2.binding_received_33)
        else:
            data2.balance_binding_33 = 0
        
        if data2.binding_received_34:
            data2.balance_binding_34 = float(data2.quantity_34) - float(data2.binding_received_34)
        else:
            data2.balance_binding_34 = 0
        
        if data2.binding_received_35:
            data2.balance_binding_35 = float(data2.quantity_35) - float(data2.binding_received_35)
        else:
            data2.balance_binding_35 = 0
        
        if data2.binding_received_36:
            data2.balance_binding_36 = float(data2.quantity_36) - float(data2.binding_received_36)
        else:
            data2.balance_binding_36 = 0
        
        if data2.binding_received_37:
            data2.balance_binding_37 = float(data2.quantity_37) - float(data2.binding_received_37)
        else:
            data2.balance_binding_37 = 0
        
        if data2.binding_received_38:
            data2.balance_binding_38 = float(data2.quantity_38) - float(data2.binding_received_38)
        else:
            data2.balance_binding_38 = 0
        
        if data2.binding_received_39:
            data2.balance_binding_39 = float(data2.quantity_39) - float(data2.binding_received_39)
        else:
            data2.balance_binding_39 = 0
        
        if data2.binding_received_40:
            data2.balance_binding_40 = float(data2.quantity_40) - float(data2.binding_received_40)
        else:
            data2.balance_binding_40 = 0

        if data2.binding_received_41:
            data2.balance_binding_41 = float(data2.quantity_41) - float(data2.binding_received_41)
        else:
            data2.balance_binding_41 = 0
        
        if data2.binding_received_42:
            data2.balance_binding_42 = float(data2.quantity_42) - float(data2.binding_received_42)
        else:
            data2.balance_binding_42 = 0
        
        if data2.binding_received_43:
            data2.balance_binding_43 = float(data2.quantity_43) - float(data2.binding_received_43)
        else:
            data2.balance_binding_43 = 0
        
        if data2.binding_received_44:
            data2.balance_binding_44 = float(data2.quantity_44) - float(data2.binding_received_44)
        else:
            data2.balance_binding_44 = 0
        
        if data2.binding_received_45:
            data2.balance_binding_45 = float(data2.quantity_45) - float(data2.binding_received_45)
        else:
            data2.balance_binding_45 = 0
        
        if data2.binding_received_46:
            data2.balance_binding_46 = float(data2.quantity_46) - float(data2.binding_received_46)
        else:
            data2.balance_binding_46 = 0
        
        if data2.binding_received_47:
            data2.balance_binding_47 = float(data2.quantity_47) - float(data2.binding_received_47)
        else:
            data2.balance_binding_47 = 0
        
        if data2.binding_received_48:
            data2.balance_binding_48 = float(data2.quantity_48) - float(data2.binding_received_48)
        else:
            data2.balance_binding_48 = 0
        
        if data2.binding_received_49:
            data2.balance_binding_49 = float(data2.quantity_49) - float(data2.binding_received_49)
        else:
            data2.balance_binding_49 = 0
        
        if data2.binding_received_50:
            data2.balance_binding_50 = float(data2.quantity_50) - float(data2.binding_received_50)
        else:
            data2.balance_binding_50 = 0


        
        
        temp_bind=[]
        if data2.binding_received_1:
            temp_bind.append(int(data2.binding_received_1))
        if data2.binding_received_2:
            temp_bind.append(int(data2.binding_received_2))
        if data2.binding_received_3:
            temp_bind.append(int(data2.binding_received_3))
        if data2.binding_received_4:
            temp_bind.append(int(data2.binding_received_4))
        if data2.binding_received_5:
            temp_bind.append(int(data2.binding_received_5))
        if data2.binding_received_6:
            temp_bind.append(int(data2.binding_received_6))
        if data2.binding_received_7:
            temp_bind.append(int(data2.binding_received_7))
        if data2.binding_received_8:
            temp_bind.append(int(data2.binding_received_8))
        if data2.binding_received_9:
            temp_bind.append(int(data2.binding_received_9))
        if data2.binding_received_10:
            temp_bind.append(int(data2.binding_received_10))

        if data2.binding_received_11:
            temp_bind.append(int(data2.binding_received_11))
        if data2.binding_received_12:
            temp_bind.append(int(data2.binding_received_12))
        if data2.binding_received_13:
            temp_bind.append(int(data2.binding_received_13))
        if data2.binding_received_14:
            temp_bind.append(int(data2.binding_received_14))
        if data2.binding_received_15:
            temp_bind.append(int(data2.binding_received_15))
        if data2.binding_received_16:
            temp_bind.append(int(data2.binding_received_16))
        if data2.binding_received_17:
            temp_bind.append(int(data2.binding_received_17))
        if data2.binding_received_18:
            temp_bind.append(int(data2.binding_received_18))
        if data2.binding_received_19:
            temp_bind.append(int(data2.binding_received_19))
        if data2.binding_received_20:
            temp_bind.append(int(data2.binding_received_20))

        if data2.binding_received_21:
            temp_bind.append(int(data2.binding_received_21))
        if data2.binding_received_22:
            temp_bind.append(int(data2.binding_received_22))
        if data2.binding_received_23:
            temp_bind.append(int(data2.binding_received_23))
        if data2.binding_received_24:
            temp_bind.append(int(data2.binding_received_24))
        if data2.binding_received_25:
            temp_bind.append(int(data2.binding_received_25))
        if data2.binding_received_26:
            temp_bind.append(int(data2.binding_received_26))
        if data2.binding_received_27:
            temp_bind.append(int(data2.binding_received_27))
        if data2.binding_received_28:
            temp_bind.append(int(data2.binding_received_28))
        if data2.binding_received_29:
            temp_bind.append(int(data2.binding_received_29))
        if data2.binding_received_30:
            temp_bind.append(int(data2.binding_received_30))

        if data2.binding_received_31:
            temp_bind.append(int(data2.binding_received_31))
        if data2.binding_received_32:
            temp_bind.append(int(data2.binding_received_32))
        if data2.binding_received_33:
            temp_bind.append(int(data2.binding_received_33))
        if data2.binding_received_34:
            temp_bind.append(int(data2.binding_received_34))
        if data2.binding_received_35:
            temp_bind.append(int(data2.binding_received_35))
        if data2.binding_received_36:
            temp_bind.append(int(data2.binding_received_36))
        if data2.binding_received_37:
            temp_bind.append(int(data2.binding_received_37))
        if data2.binding_received_38:
            temp_bind.append(int(data2.binding_received_38))
        if data2.binding_received_39:
            temp_bind.append(int(data2.binding_received_39))
        if data2.binding_received_40:
            temp_bind.append(int(data2.binding_received_40))

        if data2.binding_received_41:
            temp_bind.append(int(data2.binding_received_41))
        if data2.binding_received_42:
            temp_bind.append(int(data2.binding_received_42))
        if data2.binding_received_43:
            temp_bind.append(int(data2.binding_received_43))
        if data2.binding_received_44:
            temp_bind.append(int(data2.binding_received_44))
        if data2.binding_received_45:
            temp_bind.append(int(data2.binding_received_45))
        if data2.binding_received_46:
            temp_bind.append(int(data2.binding_received_46))
        if data2.binding_received_47:
            temp_bind.append(int(data2.binding_received_47))
        if data2.binding_received_48:
            temp_bind.append(int(data2.binding_received_48))
        if data2.binding_received_49:
            temp_bind.append(int(data2.binding_received_49))
        if data2.binding_received_50:
            temp_bind.append(int(data2.binding_received_50))
        
        temp_bind=[i for i in temp_bind]
        data2.total_binding=0
        for i in temp_bind:
            data2.total_binding=data2.total_binding+i
        
        if data2.total_binding:
            data2.balance_binding = float(data2.total_quantity) - float(data2.total_binding)
        else:
            data2.balance_binding = 0
        
        data2.save()
        messages.success(request, "Updated Successfully...!!")
        return redirect('/manual-binding/') 
    
    data4=Manual_binding.objects.filter(order_id=order_id)
    print('kiih',data4)
    for i in data4:
        print('cfu',i.striching1)

    context = {
        'data2':data2,
        'data4':data4,
       
    }
    return render(request, 'processing/edit-spark-bindings.html', context)





def new_binding_spark(request):
    data1=Manual_binding.objects.all()
    context={'data1':data1}
    return render(request,'processing/bindings_spark.html',context) 

@login_required(login_url="")
def newedit_spark_binding(request,order_id):
    data2 = Manual_binding.objects.get(order_id=order_id)
    print('swddddddd',data2.brand_name1)
    
    if request.method == 'POST':
        data2.striching1=request.POST.get('striching1')
        print('oooooooooooooo',data2.striching1)
        data2.pasting1=request.POST.get('pasting1')
        print('bbbbbbbbbbbbbbbbb',data2.pasting1)
        data2.cutting1=request.POST.get('cutting1')
        print('cccccccccccccccccccc',data2.cutting1)
        data2.striching2=request.POST.get('striching2')
        data2.pasting2=request.POST.get('pasting2')
        data2.cutting2=request.POST.get('cutting2')
        data2.striching3=request.POST.get('striching3')
        data2.pasting3=request.POST.get('pasting3')
        data2.cutting3=request.POST.get('cutting3')
        data2.striching4=request.POST.get('striching4')
        data2.pasting4=request.POST.get('pasting4')
        data2.cutting4=request.POST.get('cutting4')
        data2.striching5=request.POST.get('striching5')
        data2.pasting5=request.POST.get('pasting5')
        data2.cutting5=request.POST.get('cutting5')
        data2.striching6=request.POST.get('striching6')
        data2.pasting6=request.POST.get('pasting6')
        data2.cutting6=request.POST.get('cutting6')
        data2.striching7=request.POST.get('striching7')
        data2.pasting7=request.POST.get('pasting7')
        data2.cutting7=request.POST.get('cutting7')
        data2.striching8=request.POST.get('striching8')
        data2.pasting8=request.POST.get('pasting8')
        data2.cutting8=request.POST.get('cutting8')
        data2.striching9=request.POST.get('striching9')
        data2.pasting9=request.POST.get('pasting9')
        data2.cutting9=request.POST.get('cutting9')
        data2.striching10=request.POST.get('striching10')
        data2.pasting10=request.POST.get('pasting10')
        data2.cutting10=request.POST.get('cutting10')
        
        data2.striching11=request.POST.get('striching11')
        data2.pasting11=request.POST.get('pasting11')
        data2.cutting11=request.POST.get('cutting11')
        data2.striching12=request.POST.get('striching12')
        data2.pasting12=request.POST.get('pasting12')
        data2.cutting12=request.POST.get('cutting12')
        data2.striching13=request.POST.get('striching13')
        data2.pasting13=request.POST.get('pasting13')
        data2.cutting13=request.POST.get('cutting13')
        data2.striching14=request.POST.get('striching14')
        data2.pasting14=request.POST.get('pasting14')
        data2.cutting14=request.POST.get('cutting14')
        data2.striching15=request.POST.get('striching15')
        data2.pasting15=request.POST.get('pasting15')
        data2.cutting15=request.POST.get('cutting15')
        data2.striching16=request.POST.get('striching16')
        data2.pasting16=request.POST.get('pasting16')
        data2.cutting16=request.POST.get('cutting16')
        data2.striching17=request.POST.get('striching17')
        data2.pasting17=request.POST.get('pasting17')
        data2.cutting17=request.POST.get('cutting17')
        data2.striching18=request.POST.get('striching18')
        data2.pasting18=request.POST.get('pasting18')
        data2.cutting18=request.POST.get('cutting18')
        data2.striching19=request.POST.get('striching19')
        data2.pasting19=request.POST.get('pasting19')
        data2.cutting19=request.POST.get('cutting19')
        data2.striching19=request.POST.get('striching19')
        data2.pasting19=request.POST.get('pasting19')
        data2.cutting19=request.POST.get('cutting19')
        data2.striching20=request.POST.get('striching20')
        data2.pasting20=request.POST.get('pasting20')
        data2.cutting20=request.POST.get('cutting20')
        
        data2.striching21=request.POST.get('striching21')
        data2.pasting21=request.POST.get('pasting21')
        data2.cutting21=request.POST.get('cutting21')
        data2.striching22=request.POST.get('striching22')
        data2.pasting22=request.POST.get('pasting22')
        data2.cutting22=request.POST.get('cutting22')
        data2.striching23=request.POST.get('striching23')
        data2.pasting23=request.POST.get('pasting23')
        data2.cutting23=request.POST.get('cutting23')
        data2.striching24=request.POST.get('striching24')
        data2.pasting24=request.POST.get('pasting24')
        data2.cutting24=request.POST.get('cutting24')
        data2.striching25=request.POST.get('striching25')
        data2.pasting25=request.POST.get('pasting25')
        data2.cutting25=request.POST.get('cutting25')
        data2.striching26=request.POST.get('striching26')
        data2.pasting26=request.POST.get('pasting26')
        data2.cutting26=request.POST.get('cutting26')
        data2.striching27=request.POST.get('striching27')
        data2.pasting27=request.POST.get('pasting27')
        data2.cutting27=request.POST.get('cutting27')
        data2.striching28=request.POST.get('striching28')
        data2.pasting28=request.POST.get('pasting28')
        data2.cutting28=request.POST.get('cutting28')
        data2.striching29=request.POST.get('striching29')
        data2.pasting29=request.POST.get('pasting29')
        data2.cutting29=request.POST.get('cutting29')
        data2.striching30=request.POST.get('striching30')
        data2.pasting30=request.POST.get('pasting30')
        data2.cutting30=request.POST.get('cutting30')

        data2.striching31=request.POST.get('striching31')
        data2.pasting31=request.POST.get('pasting31')
        data2.cutting31=request.POST.get('cutting31')
        data2.striching32=request.POST.get('striching32')
        data2.pasting32=request.POST.get('pasting32')
        data2.cutting32=request.POST.get('cutting32')
        data2.striching33=request.POST.get('striching33')
        data2.pasting33=request.POST.get('pasting33')
        data2.cutting33=request.POST.get('cutting33')
        data2.striching34=request.POST.get('striching34')
        data2.pasting34=request.POST.get('pasting34')
        data2.cutting34=request.POST.get('cutting34')
        data2.striching35=request.POST.get('striching35')
        data2.pasting35=request.POST.get('pasting35')
        data2.cutting35=request.POST.get('cutting35')
        data2.striching36=request.POST.get('striching36')
        data2.pasting36=request.POST.get('pasting36')
        data2.cutting36=request.POST.get('cutting36')
        data2.striching37=request.POST.get('striching37')
        data2.pasting37=request.POST.get('pasting37')
        data2.cutting37=request.POST.get('cutting37')
        data2.striching38=request.POST.get('striching38')
        data2.pasting38=request.POST.get('pasting38')
        data2.cutting38=request.POST.get('cutting38')
        data2.striching39=request.POST.get('striching39')
        data2.pasting39=request.POST.get('pasting39')
        data2.cutting39=request.POST.get('cutting39')
        data2.striching40=request.POST.get('striching40')
        data2.pasting40=request.POST.get('pasting40')
        data2.cutting40=request.POST.get('cutting40')

        data2.striching41=request.POST.get('striching41')
        data2.pasting41=request.POST.get('pasting41')
        data2.cutting41=request.POST.get('cutting41')
        data2.striching42=request.POST.get('striching42')
        data2.pasting42=request.POST.get('pasting42')
        data2.cutting42=request.POST.get('cutting42')
        data2.striching43=request.POST.get('striching43')
        data2.pasting43=request.POST.get('pasting43')
        data2.cutting43=request.POST.get('cutting43')
        data2.striching44=request.POST.get('striching44')
        data2.pasting44=request.POST.get('pasting44')
        data2.cutting44=request.POST.get('cutting44')
        data2.striching45=request.POST.get('striching45')
        data2.pasting45=request.POST.get('pasting45')
        data2.cutting45=request.POST.get('cutting45')
        data2.striching46=request.POST.get('striching46')
        data2.pasting46=request.POST.get('pasting46')
        data2.cutting46=request.POST.get('cutting46')
        data2.striching47=request.POST.get('striching47')
        data2.pasting47=request.POST.get('pasting47')
        data2.cutting47=request.POST.get('cutting47')
        data2.striching48=request.POST.get('striching48')
        data2.pasting48=request.POST.get('pasting48')
        data2.cutting48=request.POST.get('cutting48')
        data2.striching49=request.POST.get('striching49')
        data2.pasting49=request.POST.get('pasting49')
        data2.cutting49=request.POST.get('cutting49')
        data2.striching50=request.POST.get('striching50')
        data2.pasting50=request.POST.get('pasting50')
        data2.cutting50=request.POST.get('cutting50')
    
        data2.save()
        messages.success(request, "Updated Successfully...!!")
        return redirect('/manual-binding/')

    print('data2.brand_name_1',data2.brand_name1)
    context={
        'data2':data2,
    }
    return render(request, 'processing/edit-spark-bindings.html', context)
