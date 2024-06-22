from django.shortcuts import render, redirect
from testapp.forms import signupform ,EditProfileForm ,PasswordChangingForm ,UserChangeForm ,UserChangePass
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from testapp.models import User
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView 
from django.contrib.auth.forms import  PasswordChangeForm , UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
import sweetify



# Create your views here.

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')
    print("111111",form_class)


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'testapp/profile.html'
    success_url = reverse_lazy('dashboard')
    

    def get_object(self):
        # sweetify.success(self.request, 'You successfully changed your password')
        return self.request.user

def home_view(request):
    return render(request, 'testapp/home.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print("sdfghj",email)
        password = request.POST.get('password')
        user = authenticate(email = email, password=password)
        print("dfghj",user)
        if user is not None:
            
            login(request, user)
            if request.user.is_authenticated and request.user.is_superuser:
                print("dfghj",request.user.is_superuser)
                return redirect('/dashboard')
            elif request.user.is_authenticated and request.user.is_printing:

                return redirect('/dash_printing/')
            elif request.user.is_authenticated and request.user.is_gathering:
                print("dfghj",request.user.is_gathering)
                return redirect('/dash_printing/')
            elif request.user.is_authenticated and request.user.is_binding:
                print("dfghj",request.user.is_binding)
                return redirect('/dash_printing/')
            elif request.user.is_authenticated and request.user.is_cutting:
                print("dfghj",request.user.is_cutting)
                return redirect('/dash_printing/')
            elif request.user.is_authenticated and request.user.is_packing:
                print("dfghj",request.user.is_packing)
                return redirect('/dash_printing/')
  
            # return redirect('/dashboard')
        else:
            print('invalid User')
    return render(request, 'testapp/login.html')



def dash_printing(request):
    return render(request, 'base.html')

# def dash_gathering(request):
#     return render(request, 'testapp/dash_printing.html')


# def dash_packing(request):
#     return render(request, 'testapp/dash_packing.html')













def signup_view(request):
    form = signupform()
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        email = request.POST['email']
        form = signupform(request.POST)
        if form.is_valid():

            send_mail('USER ID AND PASSWORD',
                      f'Here is your Id and Password \n\nId : {email} \nPassword : {password}',
                      'pranavpanch28@gmail.com',
                      [email],
                      fail_silently=False,)

            user = form.save()
            user.set_password(user.password)
            user.save()
        return redirect('/')

    return render(request, 'testapp/signup.html', {'form': form})

@login_required
def student_view(request):
    printing_book = printing.objects.filter(print_approved_1=False).count()
    p_data = printing.objects.filter(print_approved_1=False).values('p_code', 'p_brand_name_1').annotate(count=Count('p_code'))
    print("123",p_data)
    labels = [f"{item['p_brand_name_1']} - {item['p_code']}" for item in p_data]
    brand_names = [item['p_brand_name_1'] for item in p_data]
    p_codes = [item['p_code'] for item in p_data]
    data_values = [item['count'] for item in p_data]
    # data1 = printing.objects.filter(p_brand_name_1="Kohinoor").count()
    # data2 = printing.objects.filter(p_brand_name_1="Vidya Mitra").count()
    # data3 = printing.objects.filter(p_brand_name_1="Abhiyashika").count()
    gathering_book = Gathering.objects.filter(gather_approved_1=False).count()
    g_data= Gathering.objects.filter(gather_approved_1=False).values('code_g','brand_name').annotate(count=Count('code_g'))
    print("11111",g_data)
    labels_gather = [f"{item['brand_name']} - {item['code_g']}" for item in g_data]
    print("11111",labels_gather)
    brand_names1 = [item['brand_name'] for item in g_data]
    g_codes = [item['code_g'] for item in g_data]
    data_values1 = [item['count'] for item in g_data]
    print("11111",data_values1 )
    # data4 = Gathering.objects.filter(brand_name="Spark").count()
    # data5 = Gathering.objects.filter(brand_name="Kohinoor").count()
    # data6 = Gathering.objects.filter(brand_name="Vidya Mitra").count()
    # data7 = Gathering.objects.filter(brand_name="Abhiyashika").count()
    binding_book = Binding.objects.filter(binding_approved_1=False).count()
    b_data= Binding.objects.filter(binding_approved_1=False).values('b_code','b_brand_name').annotate(count=Count('b_code'))
    print("11111",g_data)
    labels_binding = [f"{item['b_brand_name']} - {item['b_code']}" for item in b_data]
    print("11111",labels_gather)
    brand_names2 = [item['b_brand_name'] for item in b_data]
    b_codes = [item['b_code'] for item in b_data]
    data_values2 = [item['count'] for item in b_data]
    print("11111",data_values2 )
    # data8 = Binding.objects.filter(b_brand_name="Spark").count()
    # data9 = Binding.objects.filter(b_brand_name="Kohinoor").count()
    # data10 = Binding.objects.filter(b_brand_name="Vidya Mitra").count()
    # data11 = Binding.objects.filter(b_brand_name="Abhiyashika").count()
    stitching_book = Manual.objects.filter(stiching_approved_1=False).count()
    s_data= Manual.objects.filter(stiching_approved_1=False).values('m_code','m_brand_name1').annotate(count=Count('m_code'))
    print("11111",b_data)
    labels_stitching = [f"{item['m_brand_name1']} - {item['m_code']}" for item in s_data]
    print("11111",labels_stitching)
    brand_names3 = [item['m_brand_name1'] for item in s_data]
    s_codes = [item['m_code'] for item in s_data]
    data_values3 = [item['count'] for item in s_data]
    print("11111",data_values3 )
    # data12= Manual.objects.filter(m_brand_name1="Spark").count()
    # data13 = Manual.objects.filter(m_brand_name1="Kohinoor").count()
    # data14 = Manual.objects.filter(m_brand_name1="Vidya Mitra").count()
    # data15 = Manual.objects.filter(m_brand_name1="Abhiyashika").count()
    pasting_book = Pasting.objects.filter(pasting_approved_1=False).count()
    pasting_data= Pasting.objects.filter(pasting_approved_1=False).values('pasting_code','pasting_brand_name1').annotate(count=Count('pasting_code'))
    print("11111",pasting_data)
    labels_pasting= [f"{item['pasting_brand_name1']} - {item['pasting_code']}" for item in pasting_data]
    print("11111",labels_pasting)
    brand_names4 = [item['pasting_brand_name1'] for item in pasting_data]
    pasting_codes = [item['pasting_code'] for item in pasting_data]
    data_values4 = [item['count'] for item in pasting_data]
    print("11111",data_values4 )
    # data16= Pasting.objects.filter( pasting_brand_name1="Spark").count()
    # data17 = Pasting.objects.filter( pasting_brand_name1="Kohinoor").count()
    # data18 = Pasting.objects.filter( pasting_brand_name1="Vidya Mitra").count()
    # data19 = Pasting.objects.filter( pasting_brand_name1="Abhiyashika").count()
    cutting_book = Cuttting.objects.filter(machine_cutting_approved_1=False).count()
    c_data= Cuttting.objects.filter(machine_cutting_approved_1=False).values('c_code','c_brand_name').annotate(count=Count('c_code'))
    print("11111",c_data)
    labels_cutting= [f"{item['c_brand_name']} - {item['c_code']}" for item in c_data]
    print("11111",labels_cutting)
    brand_names5= [item['c_brand_name'] for item in c_data]
    c_codes = [item['c_code'] for item in c_data]
    data_values5 = [item['count'] for item in c_data] 
    print("11111",data_values5 )
    # data20= Cuttting.objects.filter( c_brand_name="Spark").count()
    # data21 = Cuttting.objects.filter( c_brand_name="Kohinoor").count()
    # data22 = Cuttting.objects.filter( c_brand_name="Vidya Mitra").count()
    # data23 = Cuttting.objects.filter( c_brand_name="Abhiyashika").count()
    shinkpack_book = Packing.objects.filter(shrink_approved=False).count()
    shinkpack_data= Packing.objects.filter(shrink_approved=False).values('p_book_code','p_brand_name').annotate(count=Count('p_book_code'))
    print("11111",shinkpack_data)
    labels_shinkpack= [f"{item['p_brand_name']} - {item['p_book_code']}" for item in shinkpack_data]
    print("11111",labels_shinkpack)
    brand_names6= [item['p_brand_name'] for item in shinkpack_data]
    shinkpack_codes = [item['p_book_code'] for item in shinkpack_data]
    data_values6 = [item['count'] for item in shinkpack_data]
    print("11111",data_values5 )
    # data24= Packing.objects.filter( p_brand_name="Spark").count()
    # data25 = Packing.objects.filter( p_brand_name="Kohinoor").count()
    # data26 = Packing.objects.filter( p_brand_name="Vidya Mitra").count()
    # data27 = Packing.objects.filter( p_brand_name="Abhiyashika").count()
    bittipack_book = Bittipacking.objects.all().count()
    bittipack_data= Bittipacking.objects.values('bitti_book_code','bitti_brand_name').annotate(count=Count('bitti_book_code'))
    print("11111",bittipack_data)
    labels_bittipack= [f"{item['bitti_brand_name']} - {item['bitti_book_code']}" for item in bittipack_data]
    print("11111",labels_bittipack)
    brand_names7= [item['bitti_brand_name'] for item in bittipack_data]
    bittipack_codes = [item['bitti_book_code'] for item in bittipack_data]
    data_values7 = [item['count'] for item in bittipack_data]
    print("11111",data_values7 )


    book = Cuttting.objects.filter(machine_cutting_approved_1=False).count

    complete_data = Cuttting.objects.filter(machine_cutting_approved_1=False).values('c_code', 'c_brand_name','complete_book').annotate(count=Count('c_code'))
    print("9999999999", complete_data)
    labels_book = [f"{item['c_brand_name']} - {item['c_code']} -{item['complete_book']}" for item in complete_data]
    print("11111", labels_cutting)

    brand_names8 = [item['c_brand_name'] for item in complete_data]
    c_codes1 = [item['c_code'] for item in complete_data]
    complete_books = [int(item['complete_book']) if item['complete_book'].isdigit() else 0 for item in complete_data]
    total_complete_books = sum(complete_books)
    print("complete_books", complete_books)
    print("Total Complete Books:", total_complete_books)

    data_values8 = [item['count'] for item in complete_data]
    print("11111", data_values8)


    cover = Cover_Printing.objects.all().count()
    cover_data= Cover_Printing.objects.all().values('plate_no').annotate(count=Count('plate_no'))
    print("11111",cover_data)
    labels_cover = [f"{item['plate_no']} " for item in cover_data]
    print("11111", labels_cover)
   
    cover_plate= [item['plate_no'] for item in cover_data]
    data_values9 = [item['count'] for item in cover_data]
    print("11111",data_values9 )
    context={
       
        'printing_book':printing_book,
        'gathering_book':gathering_book,
        'binding_book':binding_book,
        'stitching_book':stitching_book,
        'pasting_book':pasting_book,
        'cutting_book':cutting_book,
        'shinkpack_book':shinkpack_book,
        'bittipack_book':bittipack_book,
        'cover':cover,
        'p_codes':p_codes,
        'labels':labels,
        'brand_names': brand_names,
        'g_data':g_data,
        'g_codes':g_codes,
        'labels_gather':labels_gather,
        'brand_names1':brand_names1,
        'data_values1':data_values1,
        'data_values':data_values,
        'b_data':b_data,
        'labels_binding':labels_binding,
        'brand_names2':brand_names2,
        'b_codes':b_codes,
        'data_values2':data_values2,
        's_data':s_data,
        'labels_stitching':labels_stitching,
        'brand_names3':brand_names3,
        's_codes':s_codes,
        'data_values3':data_values3,
        'labels_pasting':labels_pasting,
        'brand_names4':brand_names4,
        'pasting_codes':pasting_codes,
        'data_values4':data_values4,
        'labels_cutting':labels_cutting,
        'brand_names5':brand_names5,
        'c_codes':c_codes,
        'data_values5':data_values5,
        'labels_shinkpack':labels_shinkpack,
        'brand_names6':brand_names6,
        'shinkpack_codes':shinkpack_codes,
        'data_values6':data_values6,
        'labels_bittipack':labels_bittipack,
        'brand_names7':brand_names7,
        'bittipack_codes':bittipack_codes,
        'data_values7':data_values7,
        'labels_book':labels_book,
        'brand_names8':brand_names8,
        'c_codes1':c_codes1,
        'book':book,
        'complete_books':complete_books,
        'data_values8':data_values8,
        'total_complete_books':total_complete_books,
        'cover_plate':cover_plate,
        'data_values9':data_values9,
        'labels_cover':labels_cover,
    }
    return render(request,'testapp/welcome.html',context)

from django.db.models import Count
from packing_app.models import Packing,Bittipacking
def logout_view(request):
    logout(request)
    return redirect("login")

# def forgot_pass_view(request):
#     p = User.objects.filter()
#     print(( '---------------------------------------',p))
    

#     email1= User.objects.all()
#     print(( '-----------------email1----------------------',email1))
#     mail1 = str(email1)
    
#     if request.method == "POST":
#         email = request.POST.get('email')
        
#         if email in mail1:
#             send_mail('USER ID AND PASSWORD',
#                       f'Here is your Id and Password \n\nId : {email} \nPassword :12312345',
#                       'pranavpanch28@gmail.com',
#                       [email], 
#                       fail_silently=False,)
#             return redirect('forgot-success')
#         else:
#             print("Enter Valid Email address")              
#     return render(request,'testapp/enteremail.html')

# def forgotsuccess(request):
#     return render(request,'testapp/forgotpass.html')




def forgot_pass_view(request):
    p = User.objects.filter()
    email1= User.objects.filter().last()
    print('email1----------',email1.email)
    mail1 = str(email1)
     
    if request.method == "POST":
        email = request.POST.get('email')
        p = User.objects.filter(email=email).last()
        print( 'user_id--------------------',p.password)
        send_mail('USER ID AND PASSWORD',
                    f'Here is your Id and Password \n\nId : {email} \nPassword :12312345',
                    'pranavpanch28@gmail.com',
                    [email], 
                    fail_silently=False,)
        pwd = 'pbkdf2_sha256$390000$8ii3Uo7YnSUMw6zh9HdOgd$MVAmQH90i+Wh5S6FtrDl80iJtQIfHEUulgAiQo0I2B4='       
        p.password=pwd
        p.save()
        return redirect('forgot-success')
                 
    return render(request,'testapp/enteremail.html')



def forgotsuccess(request):
    return render(request,'testapp/forgotpass.html')



def changepass(request):
    if request.method == 'POST':
        fm = UserChangePass(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['new_pass1'])
            print(fm.cleaned_data['new_pass2'])

    return render(request,'testapp/changepass.html')




from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render
from testapp.models import User ,Role_data
# Create your views here.
def role(request):
    if request.method == 'POST':
        user_roles= request.POST.get('user_roles')
        role1=Role_data(user_roles=user_roles)
        role1.save()
    data=Role_data.objects.all()
    context={
        'data':data,
    }
    return render(request, 'testapp/role.html', context)

import secrets
import string
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse

def generate_random_password(length=6):
    characters = string.ascii_letters + string.digits 
    return ''.join(secrets.choice(characters) for _ in range(length))

def create_user(request, user_roles):
    if user_roles == 'Printing' and request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_roll = request.POST.get('user_roll') 
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        
        # Generate a random password
        random_password = generate_random_password()
        print("random_password",random_password)
        # Hash the password
        hashed_password = make_password(random_password)
        if User.objects.filter(email=email).exists():
            error_message = f"A email id  '{email}' already exists."
            sweetify.error(request, error_message, timer=8000, button='OK')
        # Create the User object with the hashed password
        else:       
            auditor = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    user_roll="Printing",
                    mobile=mobile,
                    password=hashed_password,
                    is_printing=True,
                    is_staff = True,
                    is_active = True,
                    is_user = True,
                   
            )
            auditor.save()
            sweetify.success(request, " Your email send successfully.", timer=8000,button='OK')
    
        subject = 'Registration Confirmation'
        message = f'Hello {first_name} {last_name},\n\nThank you for registering on our website.\n\n Your User Id is: {email}, \n\nYour Password is: {random_password}\n\nBest regards,\nzappkode solutions'  # Different variable name for email body
        
        from_email = 'zappkodesolutions@gmail.com'  # Replace this with your desired 'from' email address
        recipient_list = [email]
        
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
        
    elif user_roles == 'Gathering':
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            # middle_name = request.POST.get('middle_name')
            last_name= request.POST.get('last_name')
            user_roll= request.POST.get('user_roll') 
            mobile= request.POST.get('mobile')
            email =request.POST.get('email')
            password =request.POST.get('password')
            random_password = generate_random_password()
            print("random_password",random_password)
            hashed_password = make_password(random_password)
            print("random_password",random_password)
            if User.objects.filter(email=email).exists():
               error_message = f"A email id  '{email}' already exists."
               sweetify.error(request, error_message, timer=8000, button='OK')
            else:
                auditor=User(first_name=first_name,
                last_name=last_name,email=email,user_roll=user_roll,mobile=mobile,password=hashed_password,is_superuser=False,is_gathering=True,is_staff = True,
                is_active = True,is_user = True,
                )
                auditor.save()
                sweetify.success(request, " Your email send successfully.", timer=8000,button='OK')
            subject = 'Registration Confirmation'
            message = f'Hello {first_name} {last_name},\n\nThank you for registering on our website.\n\n Your User Id is: {email}, \n\nYour Password is: {random_password}\n\nBest regards,\nzappkode solutions'  # Different variable name for email body
            
            from_email = 'zappkodesolutions@gmail.com'  # Replace this with your desired 'from' email address
            recipient_list = [email]
            
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            
    elif user_roles == 'Binding':
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            # middle_name = request.POST.get('middle_name')
            last_name= request.POST.get('last_name')
            user_roll= request.POST.get('user_roll') 
            mobile= request.POST.get('mobile')
            email =request.POST.get('email')
            password =request.POST.get('password')
            random_password = generate_random_password()
            print("random_password",random_password)
            hashed_password = make_password(random_password)
            if User.objects.filter(email=email).exists():
               error_message = f"A email id  '{email}' already exists."
               sweetify.error(request, error_message, timer=8000, button='OK')
            else:
                auditor=User(first_name=first_name,
                last_name=last_name,email=email,user_roll=user_roll,mobile=mobile,password=hashed_password,is_superuser=False,is_binding=True,is_staff = True,
                is_active = True,is_user = True,
                )
                auditor.save()
                sweetify.success(request, " Your email send successfully.", timer=8000,button='OK')
            subject = 'Registration Confirmation'
            message = f'Hello {first_name} {last_name},\n\nThank you for registering on our website.\n\n Your User Id is: {email}, \n\nYour Password is: {random_password}\n\nBest regards,\nzappkode solutions'  # Different variable name for email body
            
            from_email = 'zappkodesolutions@gmail.com'  # Replace this with your desired 'from' email address
            recipient_list = [email]
            
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
            
    elif user_roles == 'Cutting':
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            # middle_name = request.POST.get('middle_name')
            last_name= request.POST.get('last_name')
            user_roll= request.POST.get('user_roll') 
            mobile= request.POST.get('mobile')
            email =request.POST.get('email')
            password =request.POST.get('password')
            random_password = generate_random_password()
            print("random_password",random_password)
            hashed_password = make_password(random_password)
            if User.objects.filter(email=email).exists():
               error_message = f"A email id  '{email}' already exists."
               sweetify.error(request, error_message, timer=8000, button='OK')
            else:
                auditor=User(first_name=first_name,
                last_name=last_name,email=email,user_roll=user_roll,mobile=mobile,password=hashed_password,is_superuser=False,is_cutting=True,is_staff = True,
                is_active = True,is_user = True,
                )
                auditor.save()
                sweetify.success(request, " Your email send successfully.", timer=8000,button='OK')

            subject = 'Registration Confirmation'
            message = f'Hello {first_name} {last_name},\n\nThank you for registering on our website.\n\n Your User Id is: {email}, \n\nYour Password is: {random_password}\n\nBest regards,\nzappkode solutions'  # Different variable name for email body
            
            from_email = 'zappkodesolutions@gmail.com'  # Replace this with your desired 'from' email address
            recipient_list = [email]
            
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            # if User.objects.filter().exists():
            #     error_message = f"your login credential send to your email."
            #     sweetify.error(request, error_message, timer=2000, button='OK')
            # # return HttpResponseBadRequest(error_message)
            # else:
            # # brand_code = generate_brand_code()
            
            #     sweetify.success(request, "your login credential send to your email", timer=2000)
            
    else:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            # middle_name = request.POST.get('middle_name')
            last_name= request.POST.get('last_name')
            user_roll= request.POST.get('user_roll') 
            mobile= request.POST.get('mobile')
            email =request.POST.get('email')
            password =request.POST.get('password')
            random_password = generate_random_password()
            print("random_password",random_password)
            hashed_password = make_password(random_password)
            if User.objects.filter(email=email).exists():
               error_message = f"A email id  '{email}' already exists."
               sweetify.error(request, error_message, timer=8000, button='OK')
            else:
                auditor=User(first_name=first_name,
                last_name=last_name,email=email,user_roll=user_roll,mobile=mobile,password=hashed_password,is_staff = True,is_packing = True,
                is_active = True,is_user = True,
                )
                auditor.save()
                sweetify.success(request, " Your email send successfully.", timer=8000,button='OK')

            subject = 'Registration Confirmation'
            message = f'Hello {first_name} {last_name},\n\nThank you for registering on our website.\n\n Your User Id is: {email}, \n\nYour Password is: {random_password}\n\nBest regards,\nzappkode solutions'  # Different variable name for email body
            
            from_email = 'zappkodesolutions@gmail.com'  # Replace this with your desired 'from' email address
            recipient_list = [email]
            
            
           
            
            return HttpResponse('your login credential send to your email')
    daa=Role_data.objects.filter(user_roles=user_roles)
    for i in daa:
         print("23433",i.user_roles)
   
    data1 =User.objects.filter(user_roll=i.user_roles)   
    
    

    context={ 
        "data1":data1,  
        "daa":daa, 
        
    } 

    return render(request, 'testapp/user_info.html', context)


    


from django.shortcuts import render, redirect
import datetime
from brand_app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


def edit_user(request, id):
    data =User.objects.get(id=id) 
    if request.method == 'POST':
        
        data.firstname = request.POST.get('first_name')
        data.lastname = request.POST.get('last_name')
        data.mobileno = request.POST.get('mobile_no')
        data.email_id = request.POST.get('email_id')
        data.user_roll = request.POST.get('user_roll')
        
       
        data.save()
        messages.success(request,"Updated Successfully")
        return redirect('/role/')
        
    context={"data":data,}

    return render(request, 'testapp/edit_user.html',context)














def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/role/')




def user_resetpassword(request):

    if request.method == "POST":
        email = request.POST['eid']
        new_password = request.POST['edit_password']

        # print(new_password)
        # print(user_id)

        if email is not None:
            user_object = User.objects.get(id=email)
            user_object.set_password(new_password)
            user_object.save()
            sweetify.success(request, title="Success", icon='success', text='Password Changed Successfully', timer=1500)
    
    all_user = User.objects.filter(is_superuser=False)
   

    context = {
        "user_list": all_user,
        
        'myteamNavActiveClass': "active",
        'myteamInfoCollapseShow': "show",
        'myteamByUserNavClass': "active",
    }
    return render(request, 'testapp/user_resetpassword.html', context) 




from django.contrib.auth.hashers import make_password

def user_pass(request, id):
    data = User.objects.get(id=id)
    print('ddddd',data.first_name)
    
    if request.method == 'POST':
        new_password = request.POST.get('password')
        data.password = make_password(new_password)  # Password ko hash format mein convert karen
        
        subject = 'Reset Password'
        message = f'Hello {data.first_name} {data.last_name},\n\nThank you for reset password on our website.\n\n Your User Id is: {data.email}, \n\nYour Password is: {new_password}\n\nBest regards,\nzappkode solutions'  # Different variable name for email body
        
        from_email = 'zappkodesolutions@gmail.com'  # Replace this with your desired 'from' email address
        recipient_list = [data.email]
        
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        data.save()  
        messages.success(request, "Updated Successfully...!!")
        return redirect('/user_resetpassword/')
    
    context = {'data': data}
    return render(request, 'testapp/user_editpass.html', context)


from django.db.models import Q
def master_permission(request, user_roles):
    data = Role_data.objects.get(user_roles=user_roles)

    if data.user_roles == 'Printing' and request.method == 'POST':
        is_master = request.POST.get('is_master')
        is_master_deletion=request.POST.get('is_master_deletion')
        is_master_listing=request.POST.get('is_master_listing')
        is_voucher_deletion=request.POST.get('is_voucher_deletion')
        is_voucher_viewing=request.POST.get('is_voucher_viewing')
        is_voucher_listing=request.POST.get('is_voucher_listing')
        
        is_voucher = request.POST.get('is_voucher')
        is_voucher = request.POST.get('is_voucher')
        is_company = request.POST.get('is_company')
        is_voucher_price = request.POST.get('is_voucher_price')
        is_change_discount = request.POST.get('is_change_discount')
        is_back_date = request.POST.get('is_back_date')
        is_repenting_document= request.POST.get('is_repenting_document')
        is_email_reporting= request.POST.get('is_email_reporting')
        is_sms_reporting= request.POST.get('is_sms_reporting')
        is_backup_data= request.POST.get('is_backup_data')
        is_data_check= request.POST.get('is_data_check')

        if is_master == 'true' :
            data1=User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_master=True )
            print("11111111111111",data1)
        if is_voucher == 'true':
            data6=User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher=True )
            print("PPPPPPPPPPPPPPPPP",data6)
        if is_master == 'false' :
           data8= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_master=False)
           print("44444444444",data8)
        if is_voucher == 'false' :
           data7= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher=False)
           print("44444444444",data7)
        if is_company == 'true' :
           data9= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_company=True)
           print("666666666666",data9)
        if is_company == 'false' :
           data9= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_company=False)
           print("666666666666",data9)
        if is_voucher_price == 'true' :
           data10= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_price=True)
           print("7777777777",data10)
        if is_voucher_price == 'false' :
           data10= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_price=False)
           print("67676767676",data10)
        if is_change_discount == 'true' :
           data10= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_change_discount=True)
           print("7777777777",data10)
        if is_change_discount == 'false' :
           data10= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_change_discount=False)
           print("67676767676",data10)
        if is_back_date == 'true' :
           data11= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_back_date=True)
           print("56565656565",data11)
        if is_back_date == 'false' :
           data11= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_back_date=False)
           print("9898989898898",data11)
        if is_repenting_document == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_repenting_document=True)
           print("1212121212121212",data12)
        if is_repenting_document == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_repenting_document=False)
           print("434343434333434",data12)
        if is_email_reporting == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_email_reporting=True)
           print("1212121212121212",data12)
        if is_email_reporting == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_email_reporting=False)
           print("434343434333434",data12)
        if is_sms_reporting == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_sms_reporting=True)
           print("1212121212121212",data12)
        if is_sms_reporting == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_sms_reporting=False)
           print("434343434333434",data12)
        if is_backup_data == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_backup_data=True)
           print("1212121212121212",data12)
        if is_backup_data == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_backup_data=False)
           print("434343434333434",data12)
        if is_data_check == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_data_check=True)
           print("1212121212121212",data12)
        if is_data_check == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_data_check=False)
           print("434343434333434",data12)
        if is_master_deletion == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_master_deletion=True)
           print("1212121212121212",data12)
        if is_master_deletion == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_master_deletion=False)
           print("434343434333434",data12)
        if is_master_listing == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_master_listing=True)
           print("1212121212121212",data12)
        if is_master_listing == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_master_listing=False)
           print("434343434333434",data12)
        if is_voucher_deletion == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_deletion=True)
           print("1212121212121212",data12)
        if is_voucher_deletion == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_deletion=False)
           print("434343434333434",data12)
        if is_voucher_viewing == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_viewing=True)
           print("1212121212121212",data12)
        if is_voucher_viewing == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_viewing=False)
           print("434343434333434",data12)
        if is_voucher_listing == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_listing=True)
           print("1212121212121212",data12)
        if is_voucher_listing == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_listing=False)
           print("434343434333434",data12)
         
        return redirect("/role_permission/")
        
    elif data.user_roles == 'Gathering' and request.method == 'POST':
        is_master=request.POST.get('is_master')
        is_master_deletion=request.POST.get('is_master_deletion')
        is_master_listing=request.POST.get('is_master_listing')
        is_voucher_deletion=request.POST.get('is_voucher_deletion')
        is_voucher_viewing=request.POST.get('is_voucher_viewing')
        is_voucher_listing=request.POST.get('is_voucher_listing')
        
        is_voucher = request.POST.get('is_voucher')
        is_voucher = request.POST.get('is_voucher')
        is_company = request.POST.get('is_company')
        is_voucher_price = request.POST.get('is_voucher_price')
        is_change_discount = request.POST.get('is_change_discount')
        is_back_date = request.POST.get('is_back_date')
        is_repenting_document= request.POST.get('is_repenting_document')
        is_email_reporting= request.POST.get('is_email_reporting')
        is_sms_reporting= request.POST.get('is_sms_reporting')
        is_backup_data= request.POST.get('is_backup_data')
        is_data_check= request.POST.get('is_data_check')

        if is_master == 'true':
            data3= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_master=True)
            print("mmmmmmmmm",data3)
        if is_master == 'false':
            data4= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_master=False)
            print("88888888888",data4)
        
        if is_voucher == 'true':
            data6=User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher=True )
            print("PPPPPPPPPPPPPPPPP",data6)
       
        if is_voucher == 'false' :
           data7= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher=False)
           print("44444444444",data7)
        if is_company == 'true' :
           data9= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_company=True)
           print("666666666666",data9)
        if is_company == 'false' :
           data9= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_company=False)
           print("666666666666",data9)
        if is_voucher_price == 'true' :
           data10= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher_price=True)
           print("7777777777",data10)
        if is_voucher_price == 'false' :
           data10= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher_price=False)
           print("67676767676",data10)
        if is_change_discount == 'true' :
           data10= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_change_discount=True)
           print("7777777777",data10)
        if is_change_discount == 'false' :
           data10= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_change_discount=False)
           print("67676767676",data10)
        if is_back_date == 'true' :
           data11= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_back_date=True)
           print("56565656565",data11)
        if is_back_date == 'false' :
           data11= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_back_date=False)
           print("9898989898898",data11)
        if is_repenting_document == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_repenting_document=True)
           print("1212121212121212",data12)
        if is_repenting_document == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_repenting_document=False)
           print("434343434333434",data12)
        if is_email_reporting == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_email_reporting=True)
           print("1212121212121212",data12)
        if is_email_reporting == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_email_reporting=False)
           print("434343434333434",data12)
        if is_sms_reporting == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_sms_reporting=True)
           print("1212121212121212",data12)
        if is_sms_reporting == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_sms_reporting=False)
           print("434343434333434",data12)
        if is_backup_data == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_backup_data=True)
           print("1212121212121212",data12)
        if is_backup_data == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_backup_data=False)
           print("434343434333434",data12)
        if is_data_check == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_data_check=True)
           print("1212121212121212",data12)
        if is_data_check == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_data_check=False)
           print("434343434333434",data12)
        if is_master_deletion == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_master_deletion=True)
           print("1212121212121212",data12)
        if is_master_deletion == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_master_deletion=False)
           print("434343434333434",data12)
        if is_master_listing == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_master_listing=True)
           print("1212121212121212",data12)
        if is_master_listing == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_master_listing=False)
           print("434343434333434",data12)
        if is_voucher_deletion == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher_deletion=True)
           print("1212121212121212",data12)
        if is_voucher_deletion == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher_deletion=False)
           print("434343434333434",data12)
        if is_voucher_viewing == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher_viewing=True)
           print("1212121212121212",data12)
        if is_voucher_viewing == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher_viewing=False)
           print("434343434333434",data12)
        if is_voucher_listing == 'true' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher_listing=True)
           print("1212121212121212",data12)
        if is_voucher_listing == 'false' :
           data12= User.objects.filter(is_gathering=True, user_roll=data.user_roles).update(is_voucher_listing=False)
           print("434343434333434",data12)
        return redirect("/role_permission/")



    elif data.user_roles == 'Binding' and request.method == 'POST':
        is_master=request.POST.get('is_master')
        is_master_deletion=request.POST.get('is_master_deletion')
        is_master_listing=request.POST.get('is_master_listing')
        is_voucher_deletion=request.POST.get('is_voucher_deletion')
        is_voucher_viewing=request.POST.get('is_voucher_viewing')
        is_voucher_listing=request.POST.get('is_voucher_listing')
        
        is_voucher = request.POST.get('is_voucher')
        is_voucher = request.POST.get('is_voucher')
        is_company = request.POST.get('is_company')
        is_voucher_price = request.POST.get('is_voucher_price')
        is_change_discount = request.POST.get('is_change_discount')
        is_back_date = request.POST.get('is_back_date')
        is_repenting_document= request.POST.get('is_repenting_document')
        is_email_reporting= request.POST.get('is_email_reporting')
        is_sms_reporting= request.POST.get('is_sms_reporting')
        is_backup_data= request.POST.get('is_backup_data')
        is_data_check= request.POST.get('is_data_check')

        if is_master == 'true':
            data5= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_master=True)
            print("99999999999",data5)
        if is_master == 'false':
            data6= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_master=False)
            print("0000000000000000000",data6)
        if is_voucher == 'true':
            data6=User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher=True )
            print("PPPPPPPPPPPPPPPPP",data6)
       
        if is_voucher == 'false' :
           data7= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher=False)
           print("44444444444",data7)
        if is_company == 'true' :
           data9= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_company=True)
           print("666666666666",data9)
        if is_company == 'false' :
           data9= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_company=False)
           print("666666666666",data9)
        if is_voucher_price == 'true' :
           data10= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher_price=True)
           print("7777777777",data10)
        if is_voucher_price == 'false' :
           data10= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher_price=False)
           print("67676767676",data10)
        if is_change_discount == 'true' :
           data10= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_change_discount=True)
           print("7777777777",data10)
        if is_change_discount == 'false' :
           data10= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_change_discount=False)
           print("67676767676",data10)
        if is_back_date == 'true' :
           data11= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_back_date=True)
           print("56565656565",data11)
        if is_back_date == 'false' :
           data11= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_back_date=False)
           print("9898989898898",data11)
        if is_repenting_document == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_repenting_document=True)
           print("1212121212121212",data12)
        if is_repenting_document == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_repenting_document=False)
           print("434343434333434",data12)
        if is_email_reporting == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_email_reporting=True)
           print("1212121212121212",data12)
        if is_email_reporting == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_email_reporting=False)
           print("434343434333434",data12)
        if is_sms_reporting == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_sms_reporting=True)
           print("1212121212121212",data12)
        if is_sms_reporting == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_sms_reporting=False)
           print("434343434333434",data12)
        if is_backup_data == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_backup_data=True)
           print("1212121212121212",data12)
        if is_backup_data == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_backup_data=False)
           print("434343434333434",data12)
        if is_data_check == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_data_check=True)
           print("1212121212121212",data12)
        if is_data_check == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_data_check=False)
           print("434343434333434",data12)
        if is_master_deletion == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_master_deletion=True)
           print("1212121212121212",data12)
        if is_master_deletion == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_master_deletion=False)
           print("434343434333434",data12)
        if is_master_listing == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_master_listing=True)
           print("1212121212121212",data12)
        if is_master_listing == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_master_listing=False)
           print("434343434333434",data12)
        if is_voucher_deletion == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher_deletion=True)
           print("1212121212121212",data12)
        if is_voucher_deletion == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher_deletion=False)
           print("434343434333434",data12)
        if is_voucher_viewing == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher_viewing=True)
           print("1212121212121212",data12)
        if is_voucher_viewing == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher_viewing=False)
           print("434343434333434",data12)
        if is_voucher_listing == 'true' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher_listing=True)
           print("1212121212121212",data12)
        if is_voucher_listing == 'false' :
           data12= User.objects.filter(is_binding=True, user_roll=data.user_roles).update(is_voucher_listing=False)
           print("434343434333434",data12)
        return redirect("/role_permission/")

    elif data.user_roles == 'Cutting' and request.method == 'POST':
        is_master=request.POST.get('is_master')
        is_master_deletion=request.POST.get('is_master_deletion')
        is_master_listing=request.POST.get('is_master_listing')
        is_voucher_deletion=request.POST.get('is_voucher_deletion')
        is_voucher_viewing=request.POST.get('is_voucher_viewing')
        is_voucher_listing=request.POST.get('is_voucher_listing')
        
        is_voucher = request.POST.get('is_voucher')
        is_voucher = request.POST.get('is_voucher')
        is_company = request.POST.get('is_company')
        is_voucher_price = request.POST.get('is_voucher_price')
        is_change_discount = request.POST.get('is_change_discount')
        is_back_date = request.POST.get('is_back_date')
        is_repenting_document= request.POST.get('is_repenting_document')
        is_email_reporting= request.POST.get('is_email_reporting')
        is_sms_reporting= request.POST.get('is_sms_reporting')
        is_backup_data= request.POST.get('is_backup_data')
        is_data_check= request.POST.get('is_data_check')

        if is_master == 'true':
            data5= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_master=True)
            print("77777777777",data5)
        if is_master == 'false':
            data6= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_master=False)
            print("6666666666666",data6)
        if is_voucher == 'true':
            data6=User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher=True )
            print("PPPPPPPPPPPPPPPPP",data6)
       
        if is_voucher == 'false' :
           data7= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher=False)
           print("44444444444",data7)
        if is_company == 'true' :
           data9= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_company=True)
           print("666666666666",data9)
        if is_company == 'false' :
           data9= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_company=False)
           print("666666666666",data9)
        if is_voucher_price == 'true' :
           data10= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher_price=True)
           print("7777777777",data10)
        if is_voucher_price == 'false' :
           data10= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher_price=False)
           print("67676767676",data10)
        if is_change_discount == 'true' :
           data10= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_change_discount=True)
           print("7777777777",data10)
        if is_change_discount == 'false' :
           data10= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_change_discount=False)
           print("67676767676",data10)
        if is_back_date == 'true' :
           data11= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_back_date=True)
           print("56565656565",data11)
        if is_back_date == 'false' :
           data11= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_back_date=False)
           print("9898989898898",data11)
        if is_repenting_document == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_repenting_document=True)
           print("1212121212121212",data12)
        if is_repenting_document == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_repenting_document=False)
           print("434343434333434",data12)
        if is_email_reporting == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_email_reporting=True)
           print("1212121212121212",data12)
        if is_email_reporting == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_email_reporting=False)
           print("434343434333434",data12)
        if is_sms_reporting == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_sms_reporting=True)
           print("1212121212121212",data12)
        if is_sms_reporting == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_sms_reporting=False)
           print("434343434333434",data12)
        if is_backup_data == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_backup_data=True)
           print("1212121212121212",data12)
        if is_backup_data == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_backup_data=False)
           print("434343434333434",data12)
        if is_data_check == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_data_check=True)
           print("1212121212121212",data12)
        if is_data_check == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_data_check=False)
           print("434343434333434",data12)
        if is_master_deletion == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_master_deletion=True)
           print("1212121212121212",data12)
        if is_master_deletion == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_master_deletion=False)
           print("434343434333434",data12)
        if is_master_listing == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_master_listing=True)
           print("1212121212121212",data12)
        if is_master_listing == 'false' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_master_listing=False)
           print("434343434333434",data12)
        if is_voucher_deletion == 'true' :
           data12= User.objects.filter(is_printing=True, user_roll=data.user_roles).update(is_voucher_deletion=True)
           print("1212121212121212",data12)
        if is_voucher_deletion == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher_deletion=False)
           print("434343434333434",data12)
        if is_voucher_viewing == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher_viewing=True)
           print("1212121212121212",data12)
        if is_voucher_viewing == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher_viewing=False)
           print("434343434333434",data12)
        if is_voucher_listing == 'true' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher_listing=True)
           print("1212121212121212",data12)
        if is_voucher_listing == 'false' :
           data12= User.objects.filter(is_cutting=True, user_roll=data.user_roles).update(is_voucher_listing=False)
           print("434343434333434",data12)
        return redirect("/role_permission/")

    elif data.user_roles == 'Packing' and request.method == 'POST':
        is_master=request.POST.get('is_master')
        is_master_deletion=request.POST.get('is_master_deletion')
        is_master_listing=request.POST.get('is_master_listing')
        is_voucher_deletion=request.POST.get('is_voucher_deletion')
        is_voucher_viewing=request.POST.get('is_voucher_viewing')
        is_voucher_listing=request.POST.get('is_voucher_listing')
        
        is_voucher = request.POST.get('is_voucher')
        is_voucher = request.POST.get('is_voucher')
        is_company = request.POST.get('is_company')
        is_voucher_price = request.POST.get('is_voucher_price')
        is_change_discount = request.POST.get('is_change_discount')
        is_back_date = request.POST.get('is_back_date')
        is_repenting_document= request.POST.get('is_repenting_document')
        is_email_reporting= request.POST.get('is_email_reporting')
        is_sms_reporting= request.POST.get('is_sms_reporting')
        is_backup_data= request.POST.get('is_backup_data')
        is_data_check= request.POST.get('is_data_check')

        if is_master == 'true':
            data5= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_master=True)
            print("22222222222222222",data5)
        if is_master == 'false':
            data6= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_master=False)
            print("3333333333333",data6)
        if is_voucher == 'true':
            data6=User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher=True )
            print("PPPPPPPPPPPPPPPPP",data6)
       
        if is_voucher == 'false' :
           data7= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher=False)
           print("44444444444",data7)
        if is_company == 'true' :
           data9= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_company=True)
           print("666666666666",data9)
        if is_company == 'false' :
           data9= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_company=False)
           print("666666666666",data9)
        if is_voucher_price == 'true' :
           data10= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher_price=True)
           print("7777777777",data10)
        if is_voucher_price == 'false' :
           data10= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher_price=False)
           print("67676767676",data10)
        if is_change_discount == 'true' :
           data10= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_change_discount=True)
           print("7777777777",data10)
        if is_change_discount == 'false' :
           data10= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_change_discount=False)
           print("67676767676",data10)
        if is_back_date == 'true' :
           data11= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_back_date=True)
           print("56565656565",data11)
        if is_back_date == 'false' :
           data11= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_back_date=False)
           print("9898989898898",data11)
        if is_repenting_document == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_repenting_document=True)
           print("1212121212121212",data12)
        if is_repenting_document == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_repenting_document=False)
           print("434343434333434",data12)
        if is_email_reporting == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_email_reporting=True)
           print("1212121212121212",data12)
        if is_email_reporting == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_email_reporting=False)
           print("434343434333434",data12)
        if is_sms_reporting == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_sms_reporting=True)
           print("1212121212121212",data12)
        if is_sms_reporting == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_sms_reporting=False)
           print("434343434333434",data12)
        if is_backup_data == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_backup_data=True)
           print("1212121212121212",data12)
        if is_backup_data == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_backup_data=False)
           print("434343434333434",data12)
        if is_data_check == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_data_check=True)
           print("1212121212121212",data12)
        if is_data_check == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_data_check=False)
           print("434343434333434",data12)
        if is_master_deletion == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_master_deletion=True)
           print("1212121212121212",data12)
        if is_master_deletion == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_master_deletion=False)
           print("434343434333434",data12)
        if is_master_listing == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_master_listing=True)
           print("1212121212121212",data12)
        if is_master_listing == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_master_listing=False)
           print("434343434333434",data12)
        if is_voucher_deletion == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher_deletion=True)
           print("1212121212121212",data12)
        if is_voucher_deletion == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher_deletion=False)
           print("434343434333434",data12)
        if is_voucher_viewing == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher_viewing=True)
           print("1212121212121212",data12)
        if is_voucher_viewing == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher_viewing=False)
           print("434343434333434",data12)
        if is_voucher_listing == 'true' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher_listing=True)
           print("1212121212121212",data12)
        if is_voucher_listing == 'false' :
           data12= User.objects.filter(is_packing=True, user_roll=data.user_roles).update(is_voucher_listing=False)
           print("434343434333434",data12)
        return redirect("/role_permission/")
        
    elif data.user_roles == 'Sale' and request.method == 'POST':
        is_master=request.POST.get('is_master')
        is_master_deletion=request.POST.get('is_master_deletion')
        is_master_listing=request.POST.get('is_master_listing')
        is_voucher_deletion=request.POST.get('is_voucher_deletion')
        is_voucher_viewing=request.POST.get('is_voucher_viewing')
        is_voucher_listing=request.POST.get('is_voucher_listing')
        

        is_voucher = request.POST.get('is_voucher')
        is_voucher = request.POST.get('is_voucher')
        is_company = request.POST.get('is_company')
        is_voucher_price = request.POST.get('is_voucher_price')
        is_change_discount = request.POST.get('is_change_discount')
        is_back_date = request.POST.get('is_back_date')
        is_repenting_document= request.POST.get('is_repenting_document')
        is_email_reporting= request.POST.get('is_email_reporting')
        is_sms_reporting= request.POST.get('is_sms_reporting')
        is_backup_data= request.POST.get('is_backup_data')
        is_data_check= request.POST.get('is_data_check')

        if is_master == 'true':
            data5= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_master=True)
            print("22222222222222222",data5)
        if is_master == 'false':
            data6= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_master=False)
            print("3333333333333",data6)
        if is_voucher == 'true':
            data6=User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher=True )
            print("PPPPPPPPPPPPPPPPP",data6)
       
        if is_voucher == 'false' :
           data7= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher=False)
           print("44444444444",data7)
        if is_company == 'true' :
           data9= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_company=True)
           print("666666666666",data9)
        if is_company == 'false' :
           data9= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_company=False)
           print("666666666666",data9)
        if is_voucher_price == 'true' :
           data10= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher_price=True)
           print("7777777777",data10)
        if is_voucher_price == 'false' :
           data10= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher_price=False)
           print("67676767676",data10)
        if is_change_discount == 'true' :
           data10= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_change_discount=True)
           print("7777777777",data10)
        if is_change_discount == 'false' :
           data10= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_change_discount=False)
           print("67676767676",data10)
        if is_back_date == 'true' :
           data11= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_back_date=True)
           print("56565656565",data11)
        if is_back_date == 'false' :
           data11= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_back_date=False)
           print("9898989898898",data11)
        if is_repenting_document == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_repenting_document=True)
           print("1212121212121212",data12)
        if is_repenting_document == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_repenting_document=False)
           print("434343434333434",data12)
        if is_email_reporting == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_email_reporting=True)
           print("1212121212121212",data12)
        if is_email_reporting == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_email_reporting=False)
           print("434343434333434",data12)
        if is_sms_reporting == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_sms_reporting=True)
           print("1212121212121212",data12)
        if is_sms_reporting == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_sms_reporting=False)
           print("434343434333434",data12)
        if is_backup_data == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_backup_data=True)
           print("1212121212121212",data12)
        if is_backup_data == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_backup_data=False)
           print("434343434333434",data12)
        if is_data_check == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_data_check=True)
           print("1212121212121212",data12)
        if is_data_check == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_data_check=False)
           print("434343434333434",data12)
        if is_master_deletion == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_master_deletion=True)
           print("1212121212121212",data12)
        if is_master_deletion == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_master_deletion=False)
           print("434343434333434",data12)
        if is_master_listing == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_master_listing=True)
           print("1212121212121212",data12)
        if is_master_listing == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_master_listing=False)
           print("434343434333434",data12)
        if is_voucher_deletion == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher_deletion=True)
           print("1212121212121212",data12)
        if is_voucher_deletion == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher_deletion=False)
           print("434343434333434",data12)
        if is_voucher_viewing == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher_viewing=True)
           print("1212121212121212",data12)
        if is_voucher_viewing == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher_viewing=False)
           print("434343434333434",data12)
        if is_voucher_listing == 'true' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher_listing=True)
           print("1212121212121212",data12)
        if is_voucher_listing == 'false' :
           data12= User.objects.filter(is_sale=True, user_roll=data.user_roles).update(is_voucher_listing=False)
           print("434343434333434",data12)
        return redirect("/role_permission/")
       
        

    
    
    context = {'data': data, }
    return render(request, 'testapp/master_permission.html', context)


def role_permission(request):
    
    data=Role_data.objects.all()
    context={
        'data':data,
    }
    return render(request, 'testapp/role_permission.html', context)

def role_permission_show(request):
    
    data=Role_data.objects.all()
    context={
        'data':data,
    }
    return render(request, 'testapp/role_permission_show.html', context)


def master_permission_show(request):
    if request.method == "POST":
        email = request.POST['eid']
        new_password = request.POST['edit_password']

        # print(new_password)
        # print(user_id)

        if email is not None:
            user_object = User.objects.get(id=email)
            user_object.set_password(new_password)
            user_object.save()
            sweetify.success(request, title="Success", icon='success', text='Password Changed Successfully', timer=1500)
    
    all_user = User.objects.filter(is_superuser=False)
   

    context = {
        "user_list": all_user,
        
        'myteamNavActiveClass': "active",
        'myteamInfoCollapseShow': "show",
        'myteamByUserNavClass': "active",
    }
    return render(request, 'testapp/master_permission_show.html', context)

