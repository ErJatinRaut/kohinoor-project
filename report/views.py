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
from report.models import *
from cover_app.models import *
from packing_app.models import *
# Create your views here.

@login_required(login_url="")
def reports_data(request):
    search_query = request.GET.get('search')
    print("111",search_query)

    data1 = printing.objects.filter(print_approved_1=True)

    data2 = Binding.objects.filter(binding_approved_1=True)
    data3 = Gathering.objects.filter(gather_approved_1=True)
    data4 = Cuttting.objects.filter(machine_cutting_approved_1=True)
    data5 = Pasting.objects.filter(pasting_approved_1=True)
    data6= Manual.objects.filter(stiching_approved_1=True)
    data7= Bittipacking.objects.all()
    data8= Packing.objects.all()
    books_data= books.objects.all()
    data9= Cover_lamination.objects.all()
    data10= Cover_texture.objects.all()
    data11= Bindingvender.objects.all()
    data12= Cuttingvender.objects.all()
    data13= Packingvender.objects.all()
    data14= Gatheringvender.objects.all()
    data15= Covervender.objects.all()
    data16= venders.objects.all()


    order_book= orders.objects.all()
    print("54675477",order_book)
   
    
    context = {
        'books_data':books_data,
        'order_book':order_book,
        'data5':data5,
        'data1':data1,
        'data2':data2,
        'data3':data3,
        'data4':data4,
        'data6':data6,
        'data7':data7,
        'data8':data8,
        'data9':data9,
        'data10':data10,
        'data11':data11,
        'data12':data12,
        'data13':data13,
        'data14':data14,
        'data15':data15,
        'data16':data16,
    }
    return render(request,'reports/reports.html',{'context':context},)





def reports_view(request,id):
    order = orders.objects.all()
    book = books.objects.all()
    clas = classes.objects.all()
    data = orders.objects.filter(order_id=id)
    for i in data:
        print(i.brand_name_1)
    print('data',data)
    vendor = venders.objects.all()
    # print('otytrthdcghnfvnh',data)

    
    context = {
        'order':order,
        'book':book,
        'data':data,
        'vendor':vendor,
        'clas':clas,
        'data':data,

    }  
    return render(request, 'reports/reports1.html',context)  

def forms_report(request):
    e_list1 = set()
    e_list2 = list()
    if request.method == 'POST':
        brand_namee = request.POST.get('sub_brand')
        mediumm = request.POST.get('med')
        class_namee = request.POST.get('stand')
        subjectt = request.POST.get('subject')
        print('requsttttttttttttt',brand_namee,mediumm,class_namee)
        data1 = orders.objects.all()

        
        for i in data1:
            if i.brand_name_1 == brand_namee and i.class_name_1 == class_namee and i.medium_1 == mediumm and i.subject_1 == subjectt  :
                e_listt = i.order_id,i.brand_name_1,i.gathering_date,i.class_name_1,i.medium_1,i.subject_1,i.pages_1,i.wastage_form_1,i.wastage_form_2,i.wastage_form_3,i.wastage_form_4,i.wastage_form_5,i.wastage_form_6,i.wastage_form_7,i.wastage_form_8,i.wastage_form_9
                e_listtt = i.wastage_form_1,i.wastage_form_2,i.wastage_form_3,i.wastage_form_4,i.wastage_form_5,i.wastage_form_6,i.wastage_form_7,i.wastage_form_8,i.wastage_form_9
                print()
                print('formmmmmmmmmmmm',e_listtt)
                print()
                if e_listt :
                    e_list1.add(e_listt)
                if e_listtt :
                    e_list2.append(e_listtt)
                print('5555555555555')
                print('elisttttttttttttt',e_list1)
                # print('sataaaaaaaaaaaaaaaaa',i.brand_name_1,i.class_name_1,i.medium_1,i.subject_1,i.pages_1,i.wastage_form_1,
                #     i.wastage_form_2,i.wastage_form_3,i.wastage_form_4,i.wastage_form_5,i.wastage_form_6,i.wastage_form_7,i.wastage_form_8,i.wastage_form_9)
                print()
    print('list11111111111111111111',e_list1)
    print()
    print('list222222222222222',e_list2)
    print()

    
    form1 = 0
    for i in e_list2:
        form1 = form1 + float(i[0])
        
    
    form2 = 0
    for i in e_list2:
        form2 = form2 + float(i[1])
    form3 = 0
    for i in e_list2:
        form3 = form3 + float(i[2])
    form4 = 0
    for i in e_list2:
        form4 = form4 + float(i[3])
    form5 = 0
    for i in e_list2:
        form5 = form5 + float(i[4])
    form6 = 0    
    for i in e_list2:
        form6 = form6 + float(i[5])
    form7 = 0    
    for i in e_list2:
        form7 = form7 + float(i[6])
    form8 = 0    
    for i in e_list2:
        form8 = form8 + float(i[7])
    form9 = 0    
    for i in e_list2:
        form9 = form9 + float(i[7])
    form10 = 0    
    for i in e_list2:
        form10 = form10 + float(i[7])


    data0 = brands.objects.all()
    data2 = classes.objects.all()
    data3 = mediums.objects.all()
    data5 = orders.objects.values('subject_1').distinct()
    context = {
        'data0':data0,
        'data2':data2, 
        'data3':data3,
        'data5':data5,   
        'e_list1':e_list1,'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'form6':form6,
        'form7':form7,'form8':form8,'form9':form9,
    }
    return render(request,'reports/forms_report.html',context) 





def extra_form(request):
    e_list =[]
    e_list3 = []
    set_1 = set()    
    if request.method == 'POST':  
        brand = request.POST.get('sub_brand')
        standard= request.POST.get('stand')
        medium = request.POST.get('med')
        subject = request.POST.get('subject')
        print('ooooooooooooooooooo',brand,standard,medium,subject)

        data5 = orders.objects.all()
        for i in data5:
            if i.brand_name_1==brand and i.class_name_1==standard and i.medium_1==medium and i.subject_1==subject:
                e_list1 = (i.printing_received_form_1,i.printing_received_form_2,i.printing_received_form_3,i.printing_received_form_4,
                            i.printing_received_form_5,i.printing_received_form_6,i.printing_received_form_7,i.printing_received_form_8,
                            i.printing_received_form_9,i.printing_received_form_10)
                # form_data = ExtraForm(order_id=i.order_id,brand_name=i.brand_name_1,standard=i.class_name_1,medium=i.medium_1,subject=i.subject_1)    
                # form_data.save()
                data5 = orders.objects.all()
                count_orders = data5.filter(
                brand_name_1=brand,
                class_name_1=standard,
                medium_1=medium,
                subject_1=subject
                ).count()
                print("iiiiiiiiiii",count_orders)

                print('ppppppppppppppppp',e_list1)
                n=0
                m = len(e_list1) 
                print('gggggggg',m)
                while n<=m:
                    if e_list1[n] == None:
                        break
                    e_list.append(int(e_list1[n]))
                    n = n+1
                
        
                #print('ssssssssssssssssssssssss',e_list)
        
                a=int(i.pages_1)/32
                ranges = [e_list[i:i + int(a)] for i in range(0, len(e_list), int(a))]
                tuples_in_range = tuple(tuple(sub_list) for sub_list in ranges)

               

                for original_list in tuples_in_range:
                    min_value = min(original_list)
                    new_list = []

                    for j in range(len(original_list)):
                        new_list.append(abs(min_value - original_list[j]))

                    # Get the length of new_list
                    new_list_length = len(new_list)

                    
                    #yha data dynamically save ho rha hai
                    form_data = {
                        'order_id': i.order_id,
                        'brand_name_1': i.brand_name_1,
                        'class_name_1': i.class_name_1,
                        'medium_1': i.medium_1,
                        'subject_1': i.subject_1
                    }

                    for idx in range(new_list_length):
                        form_data[f'form{idx + 1}'] = new_list[idx]

                    
                    data9 = ExtraForm(**form_data)
                    data9.save()

             
        data14 = ExtraForm.objects.all()
        for k in data14:
            if k.brand_name_1==brand and k.class_name_1==standard and k.medium_1==medium and k.subject_1==subject:
                set_2 = k.brand_name_1,k.class_name_1,k.medium_1,k.subject_1 
                set_3 = k.form1,k.form2,k.form3,k.form4,k.form5,k.form6,k.form7,k.form8,k.form9,k.form10,k.form11,k.form12
                
                if set_2:
                    set_1.add(set_2)
                   
                    
                if set_3:
                    e_list3.append(set_3)
                                

                # print("***********************************************************************")
                # print("Original List:", original_list)
                # print("Minimum value:", min_value)
                print("New List (min value minus index values):", new_list)
    
    
    print('setttttttttttttttttttttttt',set_1)
    
    print('zzzzzzzzzzazzzzzzzz',e_list3)
    form_1 = 0
    form_2 = 0
    form_3 = 0
    form_4 = 0
    form_5 = 0
    form_6 = 0
    form_7 = 0
    form_8 = 0
    form_9 = 0
    form_10 = 0
    form_11 = 0
    form_12 = 0
    for l in e_list3:
        form_1 = form_1 + l[0]
        form_2 = form_2 + l[1]
        form_3 = form_3 + l[2]
        form_4 = form_4 + l[3]
        form_5 = form_5 + l[4]
        form_6 = form_6 + l[5]
        form_7 = form_7 + l[6]
        form_8 = form_8 + l[7]
        form_9 = form_9 + l[8]
        form_10 = form_10 + l[9]
        form_11 = form_11 + l[10]
        form_12 = form_12 + l[11]


    print('ggggggggggggggg',form_1,form_2,form_3,form_4,form_5,form_6,form_7,form_8,form_9,form_10,form_11,form_12)

    print('vvvvvvvvvvvvvv',len(set_1))
    
    set_5 = list(set_1)
   
    
    data13 = ExtraForm.objects.all()
    

    data1 = brands.objects.all()
    data2 = classes.objects.all()
    data3 = mediums.objects.all()
    data4 = books.objects.values('subject').distinct()  
    data6 = venders.objects.all() 
    context={
        'data1':data1,
        'data2':data2,
        'data3' : data3,'set_1':set_5,
        'data4': data4,'form_11':form_11,'form_12':form_12,
        'data6':data6,'form_1':form_1,'form_2':form_2,'form_3':form_3,'form_4':form_4,'form_5':form_5,
        'data13':data13,'form_6':form_6,'form_7':form_7,'form_8':form_8,'form_9':form_9,'form_10':form_10,
    }
    return render(request,'reports/extra_form.html',context) 


# def extra_form(request):
    # e_list =[]
    # e_list3 = []
    # set_1 = set()
    # if request.method == 'POST':  
    #     brand = request.POST.get('sub_brand')
    #     standard= request.POST.get('stand')
    #     medium = request.POST.get('med')
    #     subject = request.POST.get('subject')
    #     print('ooooooooooooooooooo',brand,standard,medium,subject)

    #     data5 = orders.objects.all()
    #     for i in data5:
    #         if i.brand_name_1==brand and i.class_name_1==standard and i.medium_1==medium and i.subject_1==subject:
    #             e_list1 = (i.printing_received_form_1,i.printing_received_form_2,i.printing_received_form_3,i.printing_received_form_4,
    #                         i.printing_received_form_5,i.printing_received_form_6,i.printing_received_form_7,i.printing_received_form_8,
    #                         i.printing_received_form_9,i.printing_received_form_10)
    #             # form_data = ExtraForm(order_id=i.order_id,brand_name=i.brand_name_1,standard=i.class_name_1,medium=i.medium_1,subject=i.subject_1)    
    #             # form_data.save()
    #             data5 = orders.objects.all()
    #             count_orders = data5.filter(
    #             brand_name_1=brand,
    #             class_name_1=standard,
    #             medium_1=medium,
    #             subject_1=subject
    #             ).count()
    #             print("iiiiiiiiiii",count_orders)

    #             print('ppppppppppppppppp',e_list1)
    #             n=0
    #             m = len(e_list1) 
    #             print('gggggggg',m)
    #             while n<=m:
    #                 if e_list1[n] == None:
    #                     break
    #                 e_list.append(int(e_list1[n]))
    #                 n = n+1
                
        
    #             #print('ssssssssssssssssssssssss',e_list)
        
    #             a=int(i.pages_1)/32
    #             ranges = [e_list[i:i + int(a)] for i in range(0, len(e_list), int(a))]
    #             tuples_in_range = tuple(tuple(sub_list) for sub_list in ranges)

    #             # for original_list in tuples_in_range:
    #             #     min_value = min(original_list)
                          
    #             #     new_list = []
    #             #     for j in range(len(original_list)):
    #             #         new_list.append(abs(min_value - original_list[j]))
                        
    #             #     data9 = ExtraForm(order_id=i.order_id,brand_name=i.brand_name_1,standard=i.class_name_1,medium=i.medium_1,subject=i.subject_1,form1=new_list[0],form2=new_list[1],form3=new_list[2],form4=new_list[3],form5=new_list[4],form6=new_list[5],
    #             #                       form7=new_list[6],form8=new_list[7],form9=new_list[8],form10=new_list[9],form11=new_list[10],
    #             #                       form12=new_list[11])                 
    #             #     data9.save() 

    #             for original_list in tuples_in_range:
    #                 min_value = min(original_list)
    #                 new_list = []

    #                 for j in range(len(original_list)):
    #                     new_list.append(abs(min_value - original_list[j]))

    #                 # Get the length of new_list
    #                 new_list_length = len(new_list)

    #                 # Prepare form data dynamically based on new_list_length
                    
    #                 form_data = {
    #                     'order_id': i.order_id,
    #                     'brand_name_1': i.brand_name_1,
    #                     'class_name_1': i.class_name_1,
    #                     'medium_1': i.medium_1,
    #                     'subject_1': i.subject_1
    #                 }

    #                 for idx in range(new_list_length):
    #                     form_data[f'form{idx + 1}'] = new_list[idx]

    #                 # Save the form data
    #                 data9 = ExtraForm(**form_data)
    #                 data9.save()

                    
    #                 data14 = ExtraForm.objects.all()
    #                 for i in data14:
    #                     if i.brand_name_1==brand and i.class_name_1==standard and i.medium_1==medium and i.subject_1==subject:
    #                         set_2 = i.brand_name_1,i.class_name_1,i.medium_1,i.subject_1 
    #                         set_3 = i.form1,i.form2,i.form3,i.form4,i.form5,i.form6,i.form7,i.form8,i.form9,i.form10,i.form11,i.form12

    #                         if set_2:
    #                             set_1.add(set_2)
    #                         if set_3:
    #                             e_list3.append(set_3)
                
                





    #             # print("***********************************************************************")
    #             # print("Original List:", original_list)
    #             # print("Minimum value:", min_value)
    #             # print("New List (min value minus index values):", new_list)
    
    # # print('setttttttttttttttttttttttt',set_1)
    
    # # form1 = 0
    # # for i in e_list3:
    # #     form1 = form1+i[0]
    # # print('summmmmmmmmmmmmmmm',form1)
    # data13 = ExtraForm.objects.all()
    # for i in data13:
    #     print('idddddddddddddddddddd',i.order_id)

    # data1 = brands.objects.all()
    # data2 = classes.objects.all()
    # data3 = mediums.objects.all()
    # data4 = books.objects.values('subject').distinct()  
    # data6 = venders.objects.all() 
    # context={
    #     'data1':data1,
    #     'data2':data2,
    #     'data3' : data3,
    #     'data4': data4,
    #     'data6':data6,
    #     'data13':data13,
    # }
    # return render(request,'reports/extra_form.html',context)