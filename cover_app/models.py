from django.db import models

# Create your models here.
class Cover_record(models.Model):
   
    plate_record = models.CharField(max_length=200,default='', null=True)
    quantity_record = models.CharField(max_length=200,default='', null=True)
    unit_record = models.CharField(max_length=200,default='', null=True)
    date_record=models.CharField(max_length=200,default='', null=True)
    vender_record = models.CharField(max_length=200,default='',null=True)
    

    
    def __str__(self):
        return self.plate_record
    
class Cover_lamination(models.Model):
   
    plate_lamination = models.CharField(max_length=200,default='', null=True)
    quantity_lamination = models.CharField(max_length=200,default='', null=True)
    unit_lamination = models.CharField(max_length=200,default='', null=True)
    date_lamination=models.CharField(max_length=200,default='', null=True)
    vender_lamination = models.CharField(max_length=200,default='',null=True)


    plate_lamination1 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination1 = models.CharField(max_length=200,default='', null=True)
    unit_lamination1 = models.CharField(max_length=200,default='', null=True)

    plate_lamination2 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination2 = models.CharField(max_length=200,default='', null=True)
    unit_lamination2 = models.CharField(max_length=200,default='', null=True)

    plate_lamination3 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination3 = models.CharField(max_length=200,default='', null=True)
    unit_lamination3 = models.CharField(max_length=200,default='', null=True)

    plate_lamination4 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination4 = models.CharField(max_length=200,default='', null=True)
    unit_lamination4 = models.CharField(max_length=200,default='', null=True)

    plate_lamination5 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination5 = models.CharField(max_length=200,default='', null=True)
    unit_lamination5 = models.CharField(max_length=200,default='', null=True)


    plate_lamination6 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination6 = models.CharField(max_length=200,default='', null=True)
    unit_lamination6 = models.CharField(max_length=200,default='', null=True)
    
    plate_lamination7  = models.CharField(max_length=200,default='', null=True)
    quantity_lamination7 = models.CharField(max_length=200,default='', null=True)
    unit_lamination7 = models.CharField(max_length=200,default='', null=True)

    plate_lamination8 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination8 = models.CharField(max_length=200,default='', null=True)
    unit_lamination8 = models.CharField(max_length=200,default='', null=True)

    plate_lamination9 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination9 = models.CharField(max_length=200,default='', null=True)
    unit_lamination9 = models.CharField(max_length=200,default='', null=True)

    plate_lamination10 = models.CharField(max_length=200,default='', null=True)
    quantity_lamination10 = models.CharField(max_length=200,default='', null=True)
    unit_lamination10 = models.CharField(max_length=200,default='', null=True)

    
    

    
    def __str__(self):
        return self.plate_lamination1
    

class Cover_texture(models.Model):
   
    plate_texture = models.CharField(max_length=200,default='', null=True)
    quantity_texture = models.CharField(max_length=200,default='', null=True)
    unit_texture = models.CharField(max_length=200,default='', null=True)
    date_texture=models.CharField(max_length=200,default='', null=True)
    vender_texture = models.CharField(max_length=200,default='',null=True)

    plate_texture1 = models.CharField(max_length=200,default='', null=True)
    quantity_texture1 = models.CharField(max_length=200,default='', null=True)
    unit_texture1 = models.CharField(max_length=200,default='', null=True)

    plate_texture2 = models.CharField(max_length=200,default='', null=True)
    quantity_texture2 = models.CharField(max_length=200,default='', null=True)
    unit_texture2 = models.CharField(max_length=200,default='', null=True)

    plate_texture3 = models.CharField(max_length=200,default='', null=True)
    quantity_texture3 = models.CharField(max_length=200,default='', null=True)
    unit_texture3 = models.CharField(max_length=200,default='', null=True)

    plate_texture4= models.CharField(max_length=200,default='', null=True)
    quantity_texture4 = models.CharField(max_length=200,default='', null=True)
    unit_texture4 = models.CharField(max_length=200,default='', null=True)

    plate_texture5 = models.CharField(max_length=200,default='', null=True)
    quantity_texture5 = models.CharField(max_length=200,default='', null=True)
    unit_texture5 = models.CharField(max_length=200,default='', null=True)


    plate_texture6 = models.CharField(max_length=200,default='', null=True)
    quantity_texture6 = models.CharField(max_length=200,default='', null=True)
    unit_texture6 = models.CharField(max_length=200,default='', null=True)
    

    plate_texture7 = models.CharField(max_length=200,default='', null=True)
    quantity_texture7 = models.CharField(max_length=200,default='', null=True)
    unit_texture7 = models.CharField(max_length=200,default='', null=True)

    plate_texture8 = models.CharField(max_length=200,default='', null=True)
    quantity_texture8 = models.CharField(max_length=200,default='', null=True)
    unit_texture8 = models.CharField(max_length=200,default='', null=True)

    plate_texture9 = models.CharField(max_length=200,default='', null=True)
    quantity_texture9 = models.CharField(max_length=200,default='', null=True)
    unit_texture9 = models.CharField(max_length=200,default='', null=True)

    plate_texture10 = models.CharField(max_length=200,default='', null=True)
    quantity_texture10 = models.CharField(max_length=200,default='', null=True)
    unit_texture10 = models.CharField(max_length=200,default='', null=True)
    

    
    def __str__(self):
        return self.plate_texture1




class Topi(models.Model):
    t_no_of_ups=models.CharField(max_length=200,default='', null=True,blank=True)
    t_printing_rate=models.CharField(max_length=200,default='', null=True,blank=True)
    t_plate_rate=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject1=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject2=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject3=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject4=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject5=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject6 = models.CharField(max_length=200, default='', null=True, blank=True)
    t_subject7 = models.CharField(max_length=200,default='',null=True)
    t_subject8=models.CharField(max_length=200,default='',null=True)
    t_subject9=models.CharField(max_length=200,default='',null=True)
    t_subject10=models.CharField(max_length=200,default='',null=True)
    t_subject11=models.CharField(max_length=200,default='',null=True)
    t_subject12=models.CharField(max_length=200,default='',null=True)
    t_subject13=models.CharField(max_length=200,default='',null=True)
    t_subject14=models.CharField(max_length=200,default='',null=True)
    t_subject15=models.CharField(max_length=200,default='',null=True)
    t_subject16=models.CharField(max_length=200,default='',null=True)
    t_subject17=models.CharField(max_length=200,default='',null=True)
    t_subject18=models.CharField(max_length=200,default='',null=True)
    t_subject19=models.CharField(max_length=200,default='',null=True)
    t_subject20=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject21=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject22=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject23=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject24=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject25=models.CharField(max_length=200,default='', null=True,blank=True)
    t_subject26 = models.CharField(max_length=200, default='', null=True, blank=True)
    t_subject27 = models.CharField(max_length=200,default='',null=True)
    t_subject28=models.CharField(max_length=200,default='',null=True)
    t_subject29=models.CharField(max_length=200,default='',null=True)
    t_subject30=models.CharField(max_length=200,default='',null=True)
    t_subject31=models.CharField(max_length=200,default='',null=True)
    t_subject32=models.CharField(max_length=200,default='',null=True)
    t_paper_to_be_used=models.CharField(max_length=200,default='',null=True)
    t_quantity=models.CharField(max_length=200,default='',null=True)
    t_plate_no=models.CharField(max_length=200,default='',null=True)


class Topi_order(models.Model):
    material_center = models.CharField(max_length=200,default='', null=True)
    ord_vendor=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_date=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_plate_no1=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity1=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit1=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate1=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount1=models.CharField(max_length=200,default='', null=True,blank=True)
    material_centre1=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate1=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate1=models.CharField(max_length=200,default='', null=True,blank=True)

    ord_plate_no2=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity2=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit2=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate2=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount2=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate2=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate2=models.CharField(max_length=200,default='', null=True,blank=True)

    ord_plate_no3=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity3=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit3=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate3=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount3=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate3=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate3=models.CharField(max_length=200,default='', null=True,blank=True)

    ord_plate_no4=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity4=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit4=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate4=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount4=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate4=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate4=models.CharField(max_length=200,default='', null=True,blank=True)


    ord_plate_no5=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity5=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit5=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate5=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount5=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate5=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate5=models.CharField(max_length=200,default='', null=True,blank=True)


    ord_plate_no6=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity6=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit6=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate6=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount6=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate6=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate6=models.CharField(max_length=200,default='', null=True,blank=True)

    ord_plate_no7=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity7=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit7=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate7=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount7=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate7=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate7=models.CharField(max_length=200,default='', null=True,blank=True)

    ord_plate_no8=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity8=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit8=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate8=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount8=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate8=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate8=models.CharField(max_length=200,default='', null=True,blank=True)

    ord_plate_no9=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity9=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit9=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate9=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount9=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate9=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate9=models.CharField(max_length=200,default='', null=True,blank=True)


    ord_plate_no10=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_quantity10=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_unit10=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_rate10=models.CharField(max_length=200,default='', null=True,blank=True)
    ord_amount10=models.CharField(max_length=200,default='', null=True,blank=True)
    printing_rate10=models.CharField(max_length=200,default='', null=True,blank=True)
    print_rate10=models.CharField(max_length=200,default='', null=True,blank=True)

    bill_sundries_1=models.CharField(max_length=200,default='', null=True)
    narration_1=models.CharField(max_length=200,default='', null=True)
    amount_1=models.CharField(max_length=200,default='', null=True)
    percent_1 =models.CharField(max_length=200,default='', null=True)

    bill_sundries_2=models.CharField(max_length=200,default='', null=True)
    narration_2=models.CharField(max_length=200,default='', null=True)
    amount_2=models.CharField(max_length=200,default='', null=True)
    percent_2 =models.CharField(max_length=200,default='', null=True)

    bill_sundries_3=models.CharField(max_length=200,default='', null=True)
    narration_3=models.CharField(max_length=200,default='', null=True)
    amount_3=models.CharField(max_length=200,default='', null=True)
    percent_3 =models.CharField(max_length=200,default='', null=True)

    bill_sundries_4=models.CharField(max_length=200,default='', null=True)
    narration_4=models.CharField(max_length=200,default='', null=True)
    amount_4=models.CharField(max_length=200,default='', null=True)
    percent_4 =models.CharField(max_length=200,default='', null=True)


    bill_sundries_5=models.CharField(max_length=200,default='', null=True)
    narration_5=models.CharField(max_length=200,default='', null=True)
    amount_5=models.CharField(max_length=200,default='', null=True)
    percent_5 =models.CharField(max_length=200,default='', null=True)
    totalAmount =models.CharField(max_length=200,default='', null=True)




class Cover_cutting(models.Model):
    cutting_plate_no = models.CharField(max_length=200,default='', null=True)
    cutting_date = models.CharField(max_length=200,default='', null=True)
    cutting_quantity = models.CharField(max_length=200,default='', null=True)
    cutting_sheet_quantity=models.CharField(max_length=200,default='', null=True)
    cutting_Gruce_quantity = models.CharField(max_length=200,default='',null=True)
    cutting_rim_quantity = models.CharField(max_length=200,default='', null=True)
    cutting_rate = models.CharField(max_length=200,default='', null=True)
    cutting_amount = models.CharField(max_length=200,default='', null=True)
    cutting_vendor=models.CharField(max_length=200,default='', null=True)
    cutting_voucher_no = models.CharField(max_length=200,default='',null=True)

class Sale_bill(models.Model):
    material_center =models.CharField(max_length=200,default='', null=True)
    company = models.CharField(max_length=200,default='', null=True)
    sale_date = models.CharField(max_length=200,default='', null=True)
    sale_vendor = models.CharField(max_length=200,default='', null=True)
    voucher_no=models.CharField(max_length=200,default='', null=True)
    plate_no1 = models.CharField(max_length=200,default='',null=True)
    sale_quantity1 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti1 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti1 = models.CharField(max_length=200,default='', null=True)
    rate1 = models.CharField(max_length=200,default='', null=True)
    sale_amount1= models.CharField(max_length=200,default='', null=True)
    sale_price1 = models.CharField(max_length=200,default='', null=True)
    discount1 = models.CharField(max_length=200,default='', null=True)
    extra_discount1= models.CharField(max_length=200,default='', null=True)

    plate_no2 = models.CharField(max_length=200,default='',null=True)
    sale_quantity2 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti2 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti2 = models.CharField(max_length=200,default='', null=True)
    rate2 = models.CharField(max_length=200,default='', null=True)
    sale_amount2 = models.CharField(max_length=200,default='', null=True)
    sale_price2 = models.CharField(max_length=200,default='', null=True)
    discount2 = models.CharField(max_length=200,default='', null=True)
    extra_discount2= models.CharField(max_length=200,default='', null=True)

    plate_no3 = models.CharField(max_length=200,default='',null=True)
    sale_quantity3 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti3 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti3 = models.CharField(max_length=200,default='', null=True)
    rate3 = models.CharField(max_length=200,default='', null=True)
    sale_amount3 = models.CharField(max_length=200,default='', null=True)
    sale_price3 = models.CharField(max_length=200,default='', null=True)
    discount3 = models.CharField(max_length=200,default='', null=True)
    extra_discount3= models.CharField(max_length=200,default='', null=True)
    
    plate_no4 = models.CharField(max_length=200,default='',null=True)
    sale_quantity4 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti4 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti4 = models.CharField(max_length=200,default='', null=True)
    rate4 = models.CharField(max_length=200,default='', null=True)
    sale_amount4 = models.CharField(max_length=200,default='', null=True)
    sale_price4 = models.CharField(max_length=200,default='', null=True)
    discount4 = models.CharField(max_length=200,default='', null=True)
    extra_discount4= models.CharField(max_length=200,default='', null=True)

    plate_no5 = models.CharField(max_length=200,default='',null=True)
    sale_quantity5 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti5 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti5 = models.CharField(max_length=200,default='', null=True)
    rate5 = models.CharField(max_length=200,default='', null=True)
    sale_amount5 = models.CharField(max_length=200,default='', null=True)
    sale_price5 = models.CharField(max_length=200,default='', null=True)
    discount5 = models.CharField(max_length=200,default='', null=True)
    extra_discount5= models.CharField(max_length=200,default='', null=True)

    plate_no6 = models.CharField(max_length=200,default='',null=True)
    sale_quantity6 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti6 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti6 = models.CharField(max_length=200,default='', null=True)
    rate6 = models.CharField(max_length=200,default='', null=True)
    sale_amount6 = models.CharField(max_length=200,default='', null=True)
    sale_price6 = models.CharField(max_length=200,default='', null=True)
    discount6 = models.CharField(max_length=200,default='', null=True)
    extra_discount6= models.CharField(max_length=200,default='', null=True)

    plate_no7 = models.CharField(max_length=200,default='',null=True)
    sale_quantity7 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti7 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti7 = models.CharField(max_length=200,default='', null=True)
    rate7 = models.CharField(max_length=200,default='', null=True)
    sale_amount7 = models.CharField(max_length=200,default='', null=True)
    sale_price7 = models.CharField(max_length=200,default='', null=True)
    discount7 = models.CharField(max_length=200,default='', null=True)
    extra_discount7= models.CharField(max_length=200,default='', null=True)

    plate_no8 = models.CharField(max_length=200,default='',null=True)
    sale_quantity8 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti8 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti8 = models.CharField(max_length=200,default='', null=True)
    rate8 = models.CharField(max_length=200,default='', null=True)
    sale_amount8 = models.CharField(max_length=200,default='', null=True)
    sale_price8 = models.CharField(max_length=200,default='', null=True)
    discount8 = models.CharField(max_length=200,default='', null=True)
    extra_discount8= models.CharField(max_length=200,default='', null=True)

    plate_no9 = models.CharField(max_length=200,default='',null=True)
    sale_quantity9 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti9 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti9 = models.CharField(max_length=200,default='', null=True)
    rate9 = models.CharField(max_length=200,default='', null=True)
    sale_amount9 = models.CharField(max_length=200,default='', null=True)
    sale_price9 = models.CharField(max_length=200,default='', null=True)
    discount9 = models.CharField(max_length=200,default='', null=True)
    extra_discount9= models.CharField(max_length=200,default='', null=True)

    plate_no10 = models.CharField(max_length=200,default='',null=True)
    sale_quantity10 = models.CharField(max_length=200,default='',null=True)
    qty_per_bitti10 = models.CharField(max_length=200,default='', null=True)
    no_of_bitti10 = models.CharField(max_length=200,default='', null=True)
    rate10 = models.CharField(max_length=200,default='', null=True)
    sale_amount10 = models.CharField(max_length=200,default='', null=True)
    sale_price10 = models.CharField(max_length=200,default='', null=True)
    discount10 = models.CharField(max_length=200,default='', null=True)
    extra_discount10= models.CharField(max_length=200,default='', null=True)

    total_sale_amount= models.CharField(max_length=200,default='', null=True)

    total_amount= models.CharField(max_length=200,default='', null=True)

    bill_sundries_1=models.CharField(max_length=200,default='', null=True)
    narration_1=models.CharField(max_length=200,default='', null=True)
    amount_1=models.CharField(max_length=200,default='', null=True)
    percent_1 =models.CharField(max_length=200,default='', null=True)

    bill_sundries_2=models.CharField(max_length=200,default='', null=True)
    narration_2=models.CharField(max_length=200,default='', null=True)
    amount_2=models.CharField(max_length=200,default='', null=True)
    percent_2 =models.CharField(max_length=200,default='', null=True)

    bill_sundries_3=models.CharField(max_length=200,default='', null=True)
    narration_3=models.CharField(max_length=200,default='', null=True)
    amount_3=models.CharField(max_length=200,default='', null=True)
    percent_3 =models.CharField(max_length=200,default='', null=True)

    bill_sundries_4=models.CharField(max_length=200,default='', null=True)
    narration_4=models.CharField(max_length=200,default='', null=True)
    amount_4=models.CharField(max_length=200,default='', null=True)
    percent_4 =models.CharField(max_length=200,default='', null=True)


    bill_sundries_5=models.CharField(max_length=200,default='', null=True)
    narration_5=models.CharField(max_length=200,default='', null=True)
    amount_5=models.CharField(max_length=200,default='', null=True)
    percent_5 =models.CharField(max_length=200,default='', null=True)
    vend_category=models.CharField(max_length=200,default='', null=True)
    category1=models.CharField(max_length=200,default='', null=True)
    category2=models.CharField(max_length=200,default='', null=True)
    category3=models.CharField(max_length=200,default='', null=True)
    category4=models.CharField(max_length=200,default='', null=True)
    category5=models.CharField(max_length=200,default='', null=True)
    category6=models.CharField(max_length=200,default='', null=True)
    category7=models.CharField(max_length=200,default='', null=True)
    category8=models.CharField(max_length=200,default='', null=True)
    category9=models.CharField(max_length=200,default='', null=True)
    category10=models.CharField(max_length=200,default='', null=True)
    subject1=models.CharField(max_length=200,default='', null=True)
    subject2=models.CharField(max_length=200,default='', null=True)
    subject3=models.CharField(max_length=200,default='', null=True)
    subject4=models.CharField(max_length=200,default='', null=True)
    subject5=models.CharField(max_length=200,default='', null=True)
    subject6=models.CharField(max_length=200,default='', null=True)
    subject7=models.CharField(max_length=200,default='', null=True)
    subject8=models.CharField(max_length=200,default='', null=True)
    subject9=models.CharField(max_length=200,default='', null=True)
    subject10=models.CharField(max_length=200,default='', null=True)

    brand_name1=models.CharField(max_length=200,default='', null=True)
    brand_name2=models.CharField(max_length=200,default='', null=True)
    brand_name3=models.CharField(max_length=200,default='', null=True)
    brand_name4=models.CharField(max_length=200,default='', null=True)
    brand_name5=models.CharField(max_length=200,default='', null=True)
    brand_name6=models.CharField(max_length=200,default='', null=True)
    brand_name7=models.CharField(max_length=200,default='', null=True)
    brand_name8=models.CharField(max_length=200,default='', null=True)
    brand_name9=models.CharField(max_length=200,default='', null=True)
    brand_name10=models.CharField(max_length=200,default='', null=True)





class Sale_return(models.Model):
    vend_category=models.CharField(max_length=200,default='', null=True)
    material_center =models.CharField(max_length=200,default='', null=True)
    r_company = models.CharField(max_length=200,default='', null=True)
    r_sale_date = models.CharField(max_length=200,default='', null=True)
    r_sale_vendor = models.CharField(max_length=200,default='', null=True)
    r_voucher_no=models.CharField(max_length=200,default='', null=True)

    r_plate_no1 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity1 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti1 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti1 = models.CharField(max_length=200,default='', null=True)
    r_rate1 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount1= models.CharField(max_length=200,default='', null=True)

    r_plate_no2 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity2 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti2 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti2 = models.CharField(max_length=200,default='', null=True)
    r_rate2 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount2 = models.CharField(max_length=200,default='', null=True)

    r_plate_no3 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity3 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti3 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti3 = models.CharField(max_length=200,default='', null=True)
    r_rate3 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount3 = models.CharField(max_length=200,default='', null=True)
    
    r_plate_no4 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity4 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti4 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti4 = models.CharField(max_length=200,default='', null=True)
    r_rate4 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount4 = models.CharField(max_length=200,default='', null=True)

    r_plate_no5 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity5 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti5 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti5 = models.CharField(max_length=200,default='', null=True)
    r_rate5 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount5 = models.CharField(max_length=200,default='', null=True)

    r_plate_no6 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity6 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti6 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti6 = models.CharField(max_length=200,default='', null=True)
    r_rate6 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount6 = models.CharField(max_length=200,default='', null=True)

    r_plate_no7 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity7 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti7 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti7 = models.CharField(max_length=200,default='', null=True)
    r_rate7 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount7 = models.CharField(max_length=200,default='', null=True)

    r_plate_no8 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity8 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti8 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti8 = models.CharField(max_length=200,default='', null=True)
    r_rate8 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount8 = models.CharField(max_length=200,default='', null=True)

    r_plate_no9 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity9 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti9 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti9 = models.CharField(max_length=200,default='', null=True)
    r_rate9 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount9 = models.CharField(max_length=200,default='', null=True)

    r_plate_no10 = models.CharField(max_length=200,default='',null=True)
    r_sale_quantity10 = models.CharField(max_length=200,default='',null=True)
    r_qty_per_bitti10 = models.CharField(max_length=200,default='', null=True)
    r_no_of_bitti10 = models.CharField(max_length=200,default='', null=True)
    r_rate10 = models.CharField(max_length=200,default='', null=True)
    r_sale_amount10 = models.CharField(max_length=200,default='', null=True)

    r_total_sale_amount= models.CharField(max_length=200,default='', null=True)
    
    sale_price1 = models.CharField(max_length=200,default='', null=True)
    discount1 = models.CharField(max_length=200,default='', null=True)
    extra_discount1= models.CharField(max_length=200,default='', null=True)
    
    sale_price2 = models.CharField(max_length=200,default='', null=True)
    discount2 = models.CharField(max_length=200,default='', null=True)
    extra_discount2= models.CharField(max_length=200,default='', null=True)
    

    sale_price3 = models.CharField(max_length=200,default='', null=True)
    discount3 = models.CharField(max_length=200,default='', null=True)
    extra_discount3= models.CharField(max_length=200,default='', null=True)
    
    
    sale_price4 = models.CharField(max_length=200,default='', null=True)
    discount4 = models.CharField(max_length=200,default='', null=True)
    extra_discount4= models.CharField(max_length=200,default='', null=True)

    
    sale_price5 = models.CharField(max_length=200,default='', null=True)
    discount5 = models.CharField(max_length=200,default='', null=True)
    extra_discount5= models.CharField(max_length=200,default='', null=True)

   
    sale_price6 = models.CharField(max_length=200,default='', null=True)
    discount6 = models.CharField(max_length=200,default='', null=True)
    extra_discount6= models.CharField(max_length=200,default='', null=True)

   
    sale_price7 = models.CharField(max_length=200,default='', null=True)
    discount7 = models.CharField(max_length=200,default='', null=True)
    extra_discount7= models.CharField(max_length=200,default='', null=True)

    
    sale_price8 = models.CharField(max_length=200,default='', null=True)
    discount8 = models.CharField(max_length=200,default='', null=True)
    extra_discount8= models.CharField(max_length=200,default='', null=True)

    
    sale_price9 = models.CharField(max_length=200,default='', null=True)
    discount9 = models.CharField(max_length=200,default='', null=True)
    extra_discount9= models.CharField(max_length=200,default='', null=True)

    
    sale_price10 = models.CharField(max_length=200,default='', null=True)
    discount10 = models.CharField(max_length=200,default='', null=True)
    extra_discount10= models.CharField(max_length=200,default='', null=True)

    category1=models.CharField(max_length=200,default='', null=True)
    category2=models.CharField(max_length=200,default='', null=True)
    category3=models.CharField(max_length=200,default='', null=True)
    category4=models.CharField(max_length=200,default='', null=True)
    category5=models.CharField(max_length=200,default='', null=True)
    category6=models.CharField(max_length=200,default='', null=True)
    category7=models.CharField(max_length=200,default='', null=True)
    category8=models.CharField(max_length=200,default='', null=True)
    category9=models.CharField(max_length=200,default='', null=True)
    category10=models.CharField(max_length=200,default='', null=True)

    subject1=models.CharField(max_length=200,default='', null=True)
    subject2=models.CharField(max_length=200,default='', null=True)
    subject3=models.CharField(max_length=200,default='', null=True)
    subject4=models.CharField(max_length=200,default='', null=True)
    subject5=models.CharField(max_length=200,default='', null=True)
    subject6=models.CharField(max_length=200,default='', null=True)
    subject7=models.CharField(max_length=200,default='', null=True)
    subject8=models.CharField(max_length=200,default='', null=True)
    subject9=models.CharField(max_length=200,default='', null=True)
    subject10=models.CharField(max_length=200,default='', null=True)

    brand_name1=models.CharField(max_length=200,default='', null=True)
    brand_name2=models.CharField(max_length=200,default='', null=True)
    brand_name3=models.CharField(max_length=200,default='', null=True)
    brand_name4=models.CharField(max_length=200,default='', null=True)
    brand_name5=models.CharField(max_length=200,default='', null=True)
    brand_name6=models.CharField(max_length=200,default='', null=True)
    brand_name7=models.CharField(max_length=200,default='', null=True)
    brand_name8=models.CharField(max_length=200,default='', null=True)
    brand_name9=models.CharField(max_length=200,default='', null=True)
    brand_name10=models.CharField(max_length=200,default='', null=True)


class Cost_production(models.Model):

    sale = models.CharField(max_length=200,default='', null=True)
    closing_stock = models.CharField(max_length=200,default='', null=True)
    total = models.CharField(max_length=200,default='', null=True)
    opening_stock=models.CharField(max_length=200,default='', null=True)
    production_date=models.CharField(max_length=200,default='', null=True)
    total_production=models.CharField(max_length=200,default='', null=True)



class Sale_type(models.Model):
    
    t_sale_date = models.CharField(max_length=200,default='', null=True)
    sale_type= models.CharField(max_length=200,default='', null=True)
    sale_account=models.CharField(max_length=200,default='', null=True)
    taxation_type=models.CharField(max_length=200,default='', null=True)
    tax_invoice=models.CharField(max_length=200,default='', null=True)

    specify_here=  models.CharField(max_length=200,default='', null=True)
    specify_voucher= models.CharField(max_length=200,default='', null=True)
    taxable_voucher=models.CharField(max_length=200,default='', null=True)
    t_exempt=models.CharField(max_length=200,default='', null=True)
    taxable_item=models.CharField(max_length=200,default='', null=True)
    reverse_charge=models.CharField(max_length=200,default='', null=True)
    non_gst=models.CharField(max_length=200,default='', null=True)
    zero_rated=models.CharField(max_length=200,default='', null=True)
    nil_rated=models.CharField(max_length=200,default='', null=True)
    local=models.CharField(max_length=200,default='', null=True)
    central=models.CharField(max_length=200,default='', null=True)
    stock_transfer=models.CharField(max_length=200,default='', null=True)
    others=models.CharField(max_length=200,default='', null=True)
    deemed_export=models.CharField(max_length=200,default='', null=True)
    multi_rate=models.CharField(max_length=200,default='', null=True)
    single_tax=models.CharField(max_length=200,default='', null=True)

    
class Purchase_type(models.Model):
    

    material_center =models.CharField(max_length=200,default='', null=True)
    name= models.CharField(max_length=200,default='', null=True)
    alias=models.CharField(max_length=200,default='', null=True)
    print_name=models.CharField(max_length=200,default='', null=True)
    default_value=models.CharField(max_length=200,default='', null=True)

    sub_total_heading=  models.CharField(max_length=200,default='', null=True)
    bill_sundry_nature= models.CharField(max_length=200,default='', null=True)
    affected_good=models.CharField(max_length=200,default='', null=True)
    adjust_amount=models.CharField(max_length=200,default='', null=True)
    account_past=models.CharField(max_length=200,default='', null=True)
    affected_good_purchase=models.CharField(max_length=200,default='', null=True)
    adjust_purchase_account=models.CharField(max_length=200,default='', null=True)
    account_heat=models.CharField(max_length=200,default='', null=True)
    affected_material_issue=models.CharField(max_length=200,default='', null=True)
    affected_material_receipt=models.CharField(max_length=200,default='', null=True)
    affected_stock_transfer=models.CharField(max_length=200,default='', null=True)
    p_specify_here=models.CharField(max_length=200,default='', null=True)
    p_taxable_voucher=models.CharField(max_length=200,default='', null=True)
    p_local=models.CharField(max_length=200,default='', null=True)
    p_stock_transfer=models.CharField(max_length=200,default='', null=True)
    p_single_tax=models.CharField(max_length=200,default='', null=True)
    p_sale_date=models.CharField(max_length=200,default='', null=True)
   



class Cover_available(models.Model):
    particular = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster = models.CharField(max_length=200,default='', null=True)
    cover_balance = models.CharField(max_length=200,default='', null=True)

    particular_1 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_1= models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_1 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_1 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_1 = models.CharField(max_length=200,default='', null=True)
    cover_balance_1 = models.CharField(max_length=200,default='', null=True)

    particular_2 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_2 = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_2 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_2 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_2 = models.CharField(max_length=200,default='', null=True)
    cover_balance_2 = models.CharField(max_length=200,default='', null=True)


    particular_3 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_3 = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_3 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_3 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_3 = models.CharField(max_length=200,default='', null=True)
    cover_balance_3 = models.CharField(max_length=200,default='', null=True)

    particular_4 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_4 = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_4 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_4 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_4 = models.CharField(max_length=200,default='', null=True)
    cover_balance_4 = models.CharField(max_length=200,default='', null=True)

    particular_5 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_5 = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_5 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_5 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_5 = models.CharField(max_length=200,default='', null=True)
    cover_balance_5 = models.CharField(max_length=200,default='', null=True)

    particular_6 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_6 = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_6 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_6 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_6 = models.CharField(max_length=200,default='', null=True)
    cover_balance_6 = models.CharField(max_length=200,default='', null=True)

    particular_7 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_7 = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_7 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_7 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_7 = models.CharField(max_length=200,default='', null=True)
    cover_balance_7 = models.CharField(max_length=200,default='', null=True)

    particular_8 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_8 = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_8 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_8 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_8 = models.CharField(max_length=200,default='', null=True)
    cover_balance_8 = models.CharField(max_length=200,default='', null=True)

    particular_9 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_cover_9 = models.CharField(max_length=200,default='', null=True)
    cover_recived_after_cutting_9 = models.CharField(max_length=200,default='', null=True)
    cover_issued_for_pasting_9 = models.CharField(max_length=200,default='', null=True)
    cover_returned_by_paster_9 = models.CharField(max_length=200,default='', null=True)
    cover_balance_9 = models.CharField(max_length=200,default='', null=True)



class Topi_available(models.Model):
    particular_1 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_1 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_1 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_1 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_1 = models.CharField(max_length=200,default='', null=True)
    topi_balance_1 = models.CharField(max_length=200,default='', null=True)   
    
    particular_2 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_2 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_2 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_2 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_2 = models.CharField(max_length=200,default='', null=True)
    topi_balance_2 = models.CharField(max_length=200,default='', null=True) 

    particular_3 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_3 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_3 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_3 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_3 = models.CharField(max_length=200,default='', null=True)
    topi_balance_3 = models.CharField(max_length=200,default='', null=True)

    particular_4 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_4 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_4 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_4 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_4 = models.CharField(max_length=200,default='', null=True)
    topi_balance_4 = models.CharField(max_length=200,default='', null=True)

    particular_5 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_5 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_5 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_5 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_5 = models.CharField(max_length=200,default='', null=True)
    topi_balance_5 = models.CharField(max_length=200,default='', null=True)  

    particular_6 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_6 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_6 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_6 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_6 = models.CharField(max_length=200,default='', null=True)
    topi_balance_6 = models.CharField(max_length=200,default='', null=True)   

    particular_7 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_7 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_7 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_7 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_7 = models.CharField(max_length=200,default='', null=True)
    topi_balance_7 = models.CharField(max_length=200,default='', null=True)  

    particular_8 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_8 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_8 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_8 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_8 = models.CharField(max_length=200,default='', null=True)
    topi_balance_8 = models.CharField(max_length=200,default='', null=True)  

    particular_9 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_9 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_9 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_9 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_9 = models.CharField(max_length=200,default='', null=True)
    topi_balance_9 = models.CharField(max_length=200,default='', null=True)  

    particular_10 = models.CharField(max_length=200,default='', null=True)
    opening_stock_of_topi_10 = models.CharField(max_length=200,default='', null=True)
    topi_recived_after_cutting_10 = models.CharField(max_length=200,default='', null=True)
    topi_issued_for_pasting_10 = models.CharField(max_length=200,default='', null=True)
    topi_returned_by_paster_10 = models.CharField(max_length=200,default='', null=True)
    topi_balance_10 = models.CharField(max_length=200,default='', null=True)   
