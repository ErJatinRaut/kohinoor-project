from django.db import models

# Create your models here.

class ExtraForm(models.Model):
    order_id = models.CharField(primary_key=True,max_length=200)
    brand_name_1 = models.CharField(max_length=200,null=True,blank=True)
    class_name_1 = models.CharField(max_length=200,null=True,blank=True)
    medium_1 = models.CharField(max_length=200,null=True,blank=True)
    subject_1 = models.CharField(max_length=200,null=True,blank=True)
    form1 = models.IntegerField(null=True,default=0,blank=True)
    form2 = models.IntegerField(null=True,default=0,blank=True)
    form3 = models.IntegerField(null=True,default=0,blank=True)
    form4 = models.IntegerField(null=True,default=0,blank=True)
    form5 = models.IntegerField(null=True,default=0,blank=True)
    form6 = models.IntegerField(null=True,default=0,blank=True)
    form7 = models.IntegerField(null=True,default=0,blank=True)
    form8 = models.IntegerField(null=True,default=0,blank=True)
    form9 = models.IntegerField(null=True,default=0,blank=True)
    form10 = models.IntegerField(null=True,default=0,blank=True)
    form11 = models.IntegerField(null=True,default=0,blank=True)
    form12 = models.IntegerField(null=True,default=0,blank=True)
    
    








