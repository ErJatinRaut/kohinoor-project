from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin,BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile,**extra_fields):
        if not email:
            raise ValueError("Email Must Be Provided")
        if not password:
            raise ValueError("Password Must Be Provided")    

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )
        user.set_password(password)
        user.save(using  = self.db)
        return user

    def create_user(self, email, password, first_name,last_name,mobile,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,first_name,last_name,mobile,password,**extra_fields)    
    
    def create_superuser(self, email, password, first_name,last_name,mobile,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,first_name,last_name,mobile,**extra_fields)    



class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(db_index=True,unique = True,max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    mobile = models.CharField(max_length=50)
    user_roll=models.CharField(max_length=200,default='',null=True)
    password=models.CharField(max_length=200,default='',null=True)
    allow_master=models.CharField(max_length=200,default='',null=True)
   

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_printing = models.BooleanField(default=False)
    is_gathering = models.BooleanField(default=False)
    is_binding = models.BooleanField(default=False)
    is_cutting = models.BooleanField(default=False)
    is_packing = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    is_master= models.BooleanField(default=False)
    is_master_deletion= models.BooleanField(default=False)
    is_master_listing= models.BooleanField(default=False)
    is_voucher= models.BooleanField(default=False)
    is_voucher_deletion= models.BooleanField(default=False)
    is_voucher_viewing= models.BooleanField(default=False)
    is_voucher_listing= models.BooleanField(default=False)
    is_company= models.BooleanField(default=False)
    is_voucher_price= models.BooleanField(default=False)
    is_change_discount= models.BooleanField(default=False)
    is_back_date= models.BooleanField(default=False)
    is_repenting_document= models.BooleanField(default=False)
    is_email_reporting= models.BooleanField(default=False)
    is_sms_reporting= models.BooleanField(default=False)
    is_backup_data= models.BooleanField(default=False)
    is_data_check= models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# class Ownerinfo(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField()
#     mobile_number = models.CharField(max_length=20)

class Role_data(models.Model):
    user_roles = models.CharField(max_length=50,default="",null=True,blank=True)