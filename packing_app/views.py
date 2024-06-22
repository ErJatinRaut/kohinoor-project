from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from packing_app.models import *

# from Packing.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from brand_app.models import books , Bindingvender
from brand_app.models import Packingvender

def packing_view(request):
    shrink_size=books.objects.filter()
    print("shrink pack size",)
    data = Packing.objects.all()
    if request.method == 'POST':
        p_book_code = request.POST.get('p_book_code')
        p_brand_name = request.POST.get('p_brand_name')
        p_standard = request.POST.get('p_standard')
        p_subject = request.POST.get('p_subject')
        p_medium = request.POST.get('p_medium')
        bundle_size = float(request.POST.get('bundle_size'))
        p_quantity = float(request.POST.get('p_quantity'))
        pack_quantity = float(request.POST.get('pack_quantity'))
        shrink_pack_size = float(request.POST.get('shrink_pack_size'))
        packing_size = request.POST.get('packing_size')
        packing_size = (p_quantity/bundle_size) 
        p_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        brands_data = Packing(p_brand_name=p_brand_name,p_book_code=p_book_code,p_medium=p_medium,p_standard=p_standard,p_subject=p_subject,bundle_size=bundle_size, p_quantity=p_quantity, packing_size=packing_size,p_date=p_date,shrink_pack_size=shrink_pack_size)
        brands_data.save()
    book = books.objects.all()
    data97=Bindingvender.objects.all()
    context = {
        'data': data,
        'book': book,
        'data97':data97,
    }
    return render(request, 'packing/packing.html', context)




@login_required(login_url="")
def delete_packing(request, id):
    cus = Packing.objects.get(id=id)
    cus.delete()
    return redirect('/shrink-packing/')





@login_required(login_url="") 
def edit_packing(request, id):
    data1 = Packing.objects.get(id=id)
    if request.method == 'POST':
        data1.p_brand_name = request.POST.get('p_brand_name')
        data1.p_quantity = request.POST.get('p_quantity')
        data1.packing_size = request.POST.get('packing_size')
        data1.save()
        messages.success(request, "Updated Successfully...!!")
        return redirect('/shrink-packing/')
    
    context = {'data1':data1,}
    return render(request, 'packing/edit_packing.html', context)


def bitti_packing(request):
    data = Bittipacking.objects.all()
    if request.method == 'POST':
        bitti_book_code = request.POST.get('bitti_book_code')
        bitti_brand_name = request.POST.get('bitti_brand_name')
        bitti_standard = request.POST.get('bitti_standard')
        bitti_subject = request.POST.get('bitti_subject')
        bitti_medium = request.POST.get('bitti_medium')
        bitti_bundle_size = float(request.POST.get('bitti_bundle_size'))
        bitti_quantity = float(request.POST.get('bitti_quantity'))
        bitti_packing_size = request.POST.get('bitti_packing_size')
        bitti_pack_size = request.POST.get('bitti_pack_size')
        bitti_packing_size = (bitti_quantity/bitti_bundle_size) 
        p_date = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
        # brands_data = Packing(bitti_brand_name=bitti_brand_name,bitti_quantity=bitti_quantity,bitti_book_code=bitti_book_code,bitti_book_code_book_code=bitti_book_code,bitti_medium_medium=bitti_medium,bitti_standard=bitti_standard,bitti_subject=bitti_subject,bitti_bundle_size=bitti_bundle_size, bitti_packing_size=bitti_packing_size)
        bitti_data = Bittipacking(
        bitti_brand_name=bitti_brand_name,
        bitti_quantity=bitti_quantity,
        bitti_book_code=bitti_book_code,
        bitti_medium=bitti_medium,
        bitti_standard=bitti_standard,
        bitti_subject=bitti_subject,
        bitti_bundle_size=bitti_bundle_size,
        bitti_packing_size=bitti_packing_size,
        bitti_pack_size=bitti_pack_size
        )
        bitti_data.save()
    book=books.objects.all()
    data96=Bindingvender.objects.all()
    context = {
        'data': data,
        'book':book,
        'data96':data96,
    }
    return render(request, 'packing/bitti.html', context)

def edit_bitti(request, id):
    data1 = Bittipacking.objects.get(id=id)
    if request.method == 'POST':
        data1.bitti_brand_name = request.POST.get('bitti_brand_name')
        data1.bitti_quantity = request.POST.get('bitti_quantity')
        data1.bitti_packing_size = request.POST.get('bitti_packing_size')
        data1.save()
        messages.success(request, "Updated Successfully...!!")
        return redirect('/bitti-packing/')
    
    context = {'data1':data1,}
    return render(request, 'packing/edit_bitti.html', context)

@login_required(login_url="")
def delete_bitti(request, id):
    cus = Bittipacking.objects.get(id=id)
    cus.delete()
    return redirect('/bitti_packing/')

from django.db.models import Q
def shrink_transfer(request,id):
    data = Packing.objects.get(id=id)

    if request.method == 'POST':
            data.tra_from_shrink=request.POST.get("tra_from_shrink")
            data.to_shrink=request.POST.get("to_shrink")
            print("1234",data.to_shrink)
            # data.voucher_1=request.POST.get("voucher_1")
            data.p_vender_name=request.POST.get("p_vender_name")
            data.p_book_code=request.POST.get("p_book_code")
            data.p_vender_address =request.POST.get("p_vender_address")
            data.p_vender_mob=request.POST.get("p_vender_mob")
            data.p_brand_name=request.POST.get("p_brand_name")
            data.p_standard=request.POST.get("p_standard")
            data.p_medium_1=request.POST.get("p_medium_1")
            
            data.p_subject=request.POST.get("p_subject")
            data.p_quantity=request.POST.get("p_quantity")
            data.transfer=request.POST.get("transfer")
            data.pending=request.POST.get("transfer_pending")
            transfer = int(data.transfer) if data.transfer else 0
            data.pending=float(data.p_quantity) - int(transfer)
            print("ppppppppppeeending",data.pending)
            data.transfer_pending = data.pending
            data.save()
            if request.method == 'POST':
                if request.POST.get("shrink_approved") == "approval_button":
                    Packing.objects.filter(Q(id=id) & Q( shrink_approved=False)).update( shrink_approved=True)
                    return redirect('/shrink-packing/')
                else:
                    pass  

    
    data.total_transfer_form = data.transfer
    data.total_remaining = data.transfer_pending
    data.save()
    context={
        'data':data,
    }
    return render(request, 'packing/packing_transfer.html',context)


from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
def shrink_transfer_to(request):
    # data1 =printing.objects.all().values()
    data1 = Packing.objects.filter(shrink_approved=True)
    print("data1",data1)
   
    template=loader.get_template('packing/shrink_transfer_to.html')
    context={
      'data1':data1,
    }
    return HttpResponse(template.render(context,request)) 


def pending_shrink_transfer(request,id):
    data = Packing.objects.get(id=id)

    if request.method == 'POST':
            data.tra_from_shrink=request.POST.get("tra_from_shrink")
            data.to_shrink=request.POST.get("to_shrink")
            print("1234",data.to_shrink)
            # data.voucher_1=request.POST.get("voucher_1")
            data.p_vender_name=request.POST.get("p_vender_name")
            data.p_book_code=request.POST.get("p_book_code")
            data.p_vender_address =request.POST.get("p_vender_address")
            data.p_vender_mob=request.POST.get("p_vender_mob")
            data.p_brand_name=request.POST.get("p_brand_name")
            data.p_standard=request.POST.get("p_standard")
            data.p_medium_1=request.POST.get("p_medium_1")
            
            data.p_subject=request.POST.get("p_subject")
            data.p_quantity=request.POST.get("p_quantity")
            data.transfer=request.POST.get("transfer")
            data.pending=request.POST.get("transfer_pending")
            transfer = int(data.transfer) if data.transfer else 0
            transfer1=request.POST.get("transfer1")
            
            total_form =int(data.total_transfer_form or '0')
            data.total_transfer_form =total_form + int(transfer1 or '0')
            total_shrink = int(float(data.p_quantity or '0'))
            data.total_remaining=total_shrink - int(data.total_transfer_form or 0)
        
        
            data.pending=data.total_remaining
            print("ppppppppppeeending",data.pending)
            data.transfer_pending = data.total_remaining
            data.save()
            if request.method == 'POST':
                if request.POST.get("shrink_approved") == "approval_button":
                    Packing.objects.filter(Q(id=id) & Q( shrink_approved=False)).update( shrink_approved=True)
                    return redirect('/shrink-packing/')
                else:
                    pass  
    context={
        'data':data,
    }
    return render(request, 'packing/pending_shrink_transfer.html',context)
