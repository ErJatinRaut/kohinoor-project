from django.db import models

# Create your models here.

class Packing(models.Model):
    p_book_code = models.CharField(max_length=200,default='', null=True)
    p_brand_name = models.CharField(max_length=200,default='', null=True)
    p_medium = models.CharField(max_length=200,default='', null=True)
    p_quantity =  models.CharField(max_length=200,default='', null=True)
    pack_quantity =  models.CharField(max_length=200,default='', null=True)
    packing_size = models.CharField(max_length=200,default='', null=True)
    p_standard = models.CharField(max_length=200,default='', null=True)
    p_subject = models.CharField(max_length=200,default='', null=True)
    bundle_size = models.CharField(max_length=200,default='', null=True)
    p_date=models.CharField(max_length=200,default='',null=True)
    shrink_pack_size = models.CharField(max_length=200,default='', null=True)
    to_shrink=models.CharField(max_length=200,default='', null=True)
    tra_from_shrink= models.CharField(max_length=200,default='', null=True)
    shrink_approved=models.BooleanField(default=False)
    transfer=models.CharField(max_length=200,default='',null=True)
    transfer_pending=models.CharField(max_length=200,default='0',null=True)

    # pack_size = models.CharField(max_length=200,default='', null=True)
class Bittipacking(models.Model):
    bitti_book_code= models.CharField(max_length=200,default='', null=True)
    bitti_medium= models.CharField(max_length=200,default='', null=True)
    bitti_brand_name = models.CharField(max_length=200,default='', null=True)
    bitti_quantity =  models.CharField(max_length=200,default='', null=True)
    bitti_packing_size = models.CharField(max_length=200,default='', null=True)
    bitti_standard = models.CharField(max_length=200,default='', null=True)
    bitti_subject = models.CharField(max_length=200,default='', null=True)
    bitti_bundle_size = models.CharField(max_length=200,default='', null=True)
    bitti_date=models.CharField(max_length=200,default='',null=True)
    transfer=models.CharField(max_length=200,default='',null=True)
    transfer_pending=models.CharField(max_length=200,default='',null=True)
    bitti_pack_size = models.CharField(max_length=200,default='', null=True)