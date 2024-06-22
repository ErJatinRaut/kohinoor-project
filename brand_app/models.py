from django.db import models

# Create your models here.
class brands(models.Model):
    brand_code = models.CharField(unique=True,max_length=200,default='')
    brand_name = models.CharField(max_length=200,default='', null=True)
    sub_brand = models.CharField(max_length=200,default='', null=True)
    brand_size = models.CharField(max_length=200,default='', null=True)
    brands_added_on_1 = models.DateTimeField(null="True")
    brands_added_on = models.CharField(max_length=200,default='',null=True)
    pages_per_form=models.CharField(max_length=200,default='',null=True)
    binding_form_size = models.CharField(max_length=200,default='',null=True)

    
    def __str__(self):
        return self.brand_name

class Subbrand(models.Model):
    subbrand = models.CharField(max_length=200,default='',null=True)
    brand = models.CharField(max_length=200,default='',null=True)
    brand_size = models.CharField(max_length=200,default='', null=True)
    pages_per_form=models.CharField(max_length=200,default='',null=True)
    subtitle=models.CharField(max_length=200,default='', null=True)
    brand_combine=models.CharField(max_length=200,default='', null=True)
    
    binding_form_size=models.CharField(max_length=200,default='', null=True)
    printing_form_size=models.CharField(max_length=200,default='', null=True)


    category_1 = models.CharField(max_length=200,default='',null=True)
    mainDiscount_1 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_1 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_1 = models.CharField(max_length=100,default='0',null=True)

    category_2 = models.CharField(max_length=200,default='0',null=True)
    mainDiscount_2 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_2 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_2 = models.CharField(max_length=100,default='0',null=True)

    category_3 = models.CharField(max_length=200,default='0',null=True)
    mainDiscount_3 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_3 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_3 = models.CharField(max_length=100,default='0',null=True)

    category_4 = models.CharField(max_length=200,default='0',null=True)
    mainDiscount_4 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_4 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_4 = models.CharField(max_length=100,default='0',null=True)


    category_5 = models.CharField(max_length=200,default='0',null=True)
    mainDiscount_5 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_5 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_5 = models.CharField(max_length=100,default='0',null=True)

    category_6 = models.CharField(max_length=200,default='0',null=True)
    mainDiscount_6 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_6 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_6 = models.CharField(max_length=100,default='0',null=True)

    category_7 = models.CharField(max_length=200,default='0',null=True)
    mainDiscount_7 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_7 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_7 = models.CharField(max_length=100,default='0',null=True)

    category_8 = models.CharField(max_length=200,default='0',null=True)
    mainDiscount_8 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_8 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_8 = models.CharField(max_length=100,default='0',null=True)

    category_9 = models.CharField(max_length=200,default='0',null=True)
    mainDiscount_9 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_9 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_9 = models.CharField(max_length=100,default='0',null=True)

    category_10 =models.CharField(max_length=200,default='0',null=True)
    mainDiscount_10 = models.CharField(max_length=100,default='0',null=True)
    extraDiscount_10 = models.CharField(max_length=100,default='0',null=True)
    additionalDiscount_10 = models.CharField(max_length=100,default='0',null=True)

    def __str__(self):
        return self.subbrand
    
    
class classes(models.Model):
    class_name =models.CharField(max_length=200,default='', null=True)
    class_book =models.CharField(max_length=200,default='', null=True)
    classes_added_on_1 =models.DateTimeField(null="True")
    classes_added_on = models.CharField(max_length=200,default='',null=True)
    subject =models.CharField(max_length=200,default='',null=True)
    
    def __str__(self):
        return self.class_name
    
class mediums(models.Model):
    medium =models.CharField(max_length=200,default='', null=True)
    medium_added_on_1 =models.DateTimeField(null="True")
    medium_added_on = models.CharField(max_length=200,default='',null=True)
    
    def __str__(self): 
        return self.medium
    
    
class books(models.Model):
    color =models.CharField(max_length=200,default='', null=True)
    books_name =models.CharField(max_length=200,default='', null=True)
    books_pages =models.CharField(max_length=200,default='', null=True)
    books_class =models.CharField(max_length=200,default='', null=True)
    books_added_on_1 =models.DateTimeField(null="True")
    books_added_on = models.CharField(max_length=200,default='',null=True)
    code = models.CharField(max_length=200,default='', null=True)
    subject =models.CharField(max_length=200,default='',null=True)
    no_of_pages =models.CharField(max_length=200,default='',null=True)
    book_size =models.CharField(max_length=200,default='',null=True)
    per_book_forms =models.CharField(max_length=200,default='',null=True)
    medium=models.CharField(max_length=200,default='',null=True)
    pages_per_form=models.CharField(max_length=200,default='',null=True)
    binding_form_size = models.CharField(max_length=200,default='',null=True)
    stock=models.CharField(max_length=200,default='',null=True)
    shrink_pack_size=models.CharField(max_length=200,default='',null=True)
    bitti_pack_size=models.CharField(max_length=200,default='',null=True)
    cover=models.CharField(max_length=200,default='',null=True)
    topi=models.CharField(max_length=200,default='',null=True)
    form1=models.CharField(max_length=200,default='',null=True)
    form2=models.CharField(max_length=200,default='',null=True)
    form3=models.CharField(max_length=200,default='',null=True)
    form4=models.CharField(max_length=200,default='',null=True)
    form5=models.CharField(max_length=200,default='',null=True)
    form6=models.CharField(max_length=200,default='',null=True)
    form7=models.CharField(max_length=200,default='',null=True)
    form8=models.CharField(max_length=200,default='',null=True)
    form9=models.CharField(max_length=200,default='',null=True)
    form10=models.CharField(max_length=200,default='',null=True)
    form11=models.CharField(max_length=200,default='',null=True)
    form12=models.CharField(max_length=200,default='',null=True)
    binding_rate =models.CharField(max_length=200,default='',null=True)
    onec_rate=models.CharField(max_length=200,default='',null=True)
    twoc_rate=models.CharField(max_length=200,default='',null=True)
    fourc_rate=models.CharField(max_length=200,default='',null=True)
    printing_rate1 =models.CharField(max_length=200,default='',null=True)
    printing_form_size =models.CharField(max_length=200,default='',null=True)
    subbrand_printing_form_size =models.CharField(max_length=200,default='',null=True)
    subbrand_binding_form_size =models.CharField(max_length=200,default='',null=True)
    selling_price=models.CharField(max_length=200,default='',null=True)
    main_discount=models.CharField(max_length=200,default='',null=True)
    extra_discount=models.CharField(max_length=200,default='',null=True)

    
    def __str__(self):
        return self.books_name



class Company(models.Model):
    company_type =models.CharField(max_length=200,default='', null=True)
    company_name =models.CharField(max_length=200,default='', null=True)
    company_contact =models.CharField(max_length=200,default='', null=True)
    company_email =models.CharField(max_length=200,default='', null=True)
    gstin_no =models.CharField(max_length=200,default='', null=True)
    company_address =models.CharField(max_length=200,default='', null=True)
    company_created_by =models.CharField(max_length=200,default='', null=True)
    pincode =models.CharField(max_length=200,default='', null=True)
    country =models.CharField(max_length=200,default='', null=True)
    state =models.CharField(max_length=200,default='', null=True)
    website =models.CharField(max_length=200,default='', null=True)
    
    def __str__(self):
        return self.company_name

    
class forms(models.Model):
    rmname=models.CharField(max_length=200,default='', null=True)
    rmalias=models.CharField(max_length=200,default='', null=True)
    print_name=models.CharField(max_length=200,default='', null=True)
    qunit=models.CharField(max_length=200,default='', null=True)
    opening_stock_value=models.CharField(max_length=200,default='', null=True)
    gsm=models.CharField(max_length=200,default='', null=True)
    p_width=models.CharField(max_length=200,default='', null=True)
    p_length=models.CharField(max_length=200,default='', null=True)
    unit1=models.CharField(max_length=200,default='', null=True)
    qunit1=models.CharField(max_length=200,default='', null=True)
    unit2=models.CharField(max_length=200,default='', null=True)
    qunit2=models.CharField(max_length=200,default='', null=True)
    unit3=models.CharField(max_length=200,default='', null=True)
    qunit3=models.CharField(max_length=200,default='', null=True)
    unit1_conversion=models.CharField(max_length=200,default='', null=True)
    cunit1=models.CharField(max_length=200,default='', null=True)
    unit2_conversion=models.CharField(max_length=200,default='', null=True)
    cunit2=models.CharField(max_length=200,default='', null=True)
    opening_stock_rm = models.CharField(max_length=200,default='', null=True)
    Waste = models.CharField(max_length=200,default='', null=True)
    waste_percent = models.CharField(max_length=200,default='', null=True)






    no_of_forms =models.CharField(max_length=200,default='', null=True)
    form_length =models.CharField(max_length=200,default='', null=True)
    form_width =models.CharField(max_length=200,default='', null=True)
    form_gsm =models.CharField(max_length=200,default='', null=True)
    no_of_pages =models.CharField(max_length=200,default='', null=True)
    forms_added_on_1 =models.DateTimeField(null="True")
    forms_added_on = models.CharField(max_length=200,default='',null=True)
    per_kg_weight = models.CharField(max_length=200,default='', null=True)
    p_date_1 = models.DateTimeField(null="True")
    p_date = models.CharField(max_length=200,default='',null=True)
    p_raw_material = models.CharField(max_length=200,default='', null=True)
    material_center = models.CharField(max_length=200,default='', null=True)
    form_received_by = models.CharField(max_length=200,default='', null=True)
    purchase_quantity = models.CharField(max_length=200,default='', null=True)
    wastage_percent = models.CharField(max_length=200,default='', null=True)
    gross = models.CharField(max_length=200,default='', null=True)
    single_rate = models.CharField(max_length=200,default='', null=True)
    double_rate = models.CharField(max_length=200,default='', null=True)
    four_rate = models.CharField(max_length=200,default='', null=True)
    gsm_paper = models.CharField(max_length=200,default='', null=True)
    raw_material_center = models.CharField(max_length=200,default='', null=True)
    unit3_conversion=models.CharField(max_length=200,default='', null=True)
    cunit3=models.CharField(max_length=200,default='', null=True)
    cunit4=models.CharField(max_length=200,default='', null=True)
    unit4=models.CharField(max_length=200,default='', null=True)
    conversion_factor1=models.CharField(max_length=200,default='', null=True)
    opening_stock1=models.CharField(max_length=200,default='', null=True)




class Bindingvender(models.Model):
    organization_name1 =models.CharField(max_length=200,default='', null=True)
    vender_contact1 =models.CharField(max_length=200,default='', null=True)
    vender_email1 =models.CharField(max_length=200,default='', null=True)
    vender_gstin_no1 =models.CharField(max_length=200,default='', null=True)
    vender_address1 =models.CharField(max_length=200,default='', null=True)
    vender_created_by1 =models.CharField(max_length=200,default='', null=True)
    vender_group1 =models.CharField(max_length=200,default='', null=True)
    
    def __str__(self):
        return self.organization_name1

class Cuttingvender(models.Model):
    corganization_name1 =models.CharField(max_length=200,default='', null=True)
    cvender_contact1 =models.CharField(max_length=200,default='', null=True)
    cvender_email1 =models.CharField(max_length=200,default='', null=True)
    cvender_gstin_no1 =models.CharField(max_length=200,default='', null=True)
    cvender_address1 =models.CharField(max_length=200,default='', null=True)
    cvender_created_by1 =models.CharField(max_length=200,default='', null=True)
    cvender_group1 =models.CharField(max_length=200,default='', null=True)
    
    def __str__(self):
        return self.corganization_name1

class Packingvender(models.Model):
    porganization_name1 =models.CharField(max_length=200,default='', null=True)
    pvender_contact1 =models.CharField(max_length=200,default='', null=True)
    pvender_email1 =models.CharField(max_length=200,default='', null=True)
    pvender_gstin_no1 =models.CharField(max_length=200,default='', null=True)
    pvender_address1 =models.CharField(max_length=200,default='', null=True)
    pvender_created_by1 =models.CharField(max_length=200,default='', null=True)
    pvender_group1 =models.CharField(max_length=200,default='', null=True)
    
    def __str__(self):
        return self.porganization_name1

class Gatheringvender(models.Model):
    gorganization_name1 =models.CharField(max_length=200,default='', null=True)
    gvender_contact1 =models.CharField(max_length=200,default='', null=True)
    gvender_email1 =models.CharField(max_length=200,default='', null=True)
    gvender_gstin_no1 =models.CharField(max_length=200,default='', null=True)
    gvender_address1 =models.CharField(max_length=200,default='', null=True)
    gvender_created_by1 =models.CharField(max_length=200,default='', null=True)
    gvender_group1 =models.CharField(max_length=200,default='', null=True)
    
    def __str__(self):
        return self.gorganization_name1

class Covervender(models.Model):
    c_organization_name =models.CharField(max_length=200,default='', null=True)
    c_vender_contact =models.CharField(max_length=200,default='', null=True)
    c_vender_email =models.CharField(max_length=200,default='', null=True)
    c_vender_gstin_no =models.CharField(max_length=200,default='', null=True)
    c_vender_address =models.CharField(max_length=200,default='', null=True)
    c_vender_created_by =models.CharField(max_length=200,default='', null=True)
    c_vender_group =models.CharField(max_length=200,default='', null=True)
    
    def __str__(self):
        return self.c_organization_name            
    
class venders(models.Model):
    organization_name =models.CharField(max_length=200,default='', null=True)
    vender_contact =models.CharField(max_length=200,default='', null=True)
    vender_email =models.CharField(max_length=200,default='', null=True)
    vender_gstin_no =models.CharField(max_length=200,default='', null=True)
    vender_address =models.CharField(max_length=200,default='', null=True)
    vender_created_by_1 =models.DateTimeField(null="True")
    vender_created_by = models.CharField(max_length=200,default='',null=True)
    vender_group =models.CharField(max_length=200,default='', null=True)
    
    def __str__(self):
        return self.organization_name
    


class Distributors(models.Model):
    distributor_name =models.CharField(max_length=200,default='', null=True)
    distributor_contact =models.CharField(max_length=200,default='', null=True)
    distributor_email =models.CharField(max_length=200,default='', null=True)
    distributor_gstin_no =models.CharField(max_length=200,default='', null=True)
    distributor_address =models.CharField(max_length=200,default='', null=True)
    distributor_created_by_1 =models.DateTimeField(null="True")
    distributor_created_by = models.CharField(max_length=200,default='',null=True)
    distributor_group =models.CharField(max_length=200,default='', null=True)
    
    def __str__(self):
        return self.distributor_name    



class material_centre(models.Model):
    # brand_code = models.CharField(unique=True,max_length=200,default='')
    centre_name = models.CharField(max_length=200,default='', null=True)
    stock_of_book_paper = models.CharField(max_length=200,default='', null=True)
    stock_of_cover_paper = models.CharField(max_length=200,default='', null=True)
    topi=models.CharField(max_length=200,default='',null=True)
    alias = models.CharField(max_length=200,default='',null=True)
    print_name = models.CharField(max_length=200,default='',null=True)
    group = models.CharField(max_length=200,default='',null=True)
    # binding_form_size = models.CharField(max_length=200,default='',null=True)

    
    def __str__(self):
        return self.centre_name   




class Group(models.Model):
    group_name = models.CharField(max_length=200,default='', null=True)
    group_type = models.CharField(max_length=200,default='', null=True)
    main_discount= models.CharField(max_length=200,default='', null=True)
    extra_discount= models.CharField(max_length=200,default='', null=True)



    def __str__(self):
        return self.group_type  




class Gathering(models.Model):
    code_g=models.CharField(max_length=200,default='',null=True)
    brand_name=models.CharField(max_length=200,default='',null=True)
    class_name=models.CharField(max_length=200,default='',null=True)
    medium=models.CharField(max_length=200,default='',null=True)
    subject=models.CharField(max_length=200,default='',null=True)
    g_quantity=models.CharField(max_length=200,default='',null=True)
    gather1=models.CharField(max_length=200,default='',null=True)
    gather2=models.CharField(max_length=200,default='',null=True)
    gather3=models.CharField(max_length=200,default='',null=True)
    gather4=models.CharField(max_length=200,default='',null=True)
    gather5=models.CharField(max_length=200,default='',null=True)
    gather6=models.CharField(max_length=200,default='',null=True)
    gather7=models.CharField(max_length=200,default='',null=True)
    gather8=models.CharField(max_length=200,default='',null=True)
    gather9=models.CharField(max_length=200,default='',null=True)
    gather10=models.CharField(max_length=200,default='',null=True)
    date=models.CharField(max_length=200,default='',null=True)

    v1_name=models.CharField(max_length=200,default='',null=True)
    m1_no=models.CharField(max_length=200,default='',null=True)
    a1_name=models.CharField(max_length=200,default='',null=True)
    total_gather=models.CharField(max_length=200,default='',null=True)
    page=models.CharField(max_length=200,default='',null=True)


    gather_approved_1 = models.BooleanField(default=False)
    tra_from_2=models.CharField(max_length=200,default='', null=True)
    to_2=models.CharField(max_length=200,default='', null=True)
    voucher_2 =models.CharField(max_length=200,default='', null=True)
    transfer=models.CharField(max_length=200,default='0',null=True)
    transfer_pending=models.CharField(max_length=200,default='0',null=True)
    Material_center = models.CharField(max_length=200,default='', null=True)

    transfer1=models.CharField(max_length=200,default='0',null=True)
    total_remaining = models.CharField(max_length=200, default='0', null=True, blank=True)
    total_transfer_form = models.CharField(max_length=200, default='0', null=True, blank=True)


    def __str__(self):
            return f"{self.v1_name}  {self.date}"
    

class Binding(models.Model):
    b_code=models.CharField(max_length=200,default='',null=True)
    b_brand_name=models.CharField(max_length=200,default='',null=True)
    b_class_name=models.CharField(max_length=200,default='',null=True)
    b_medium=models.CharField(max_length=200,default='',null=True)
    b_subject=models.CharField(max_length=200,default='',null=True)
    
    b_date=models.CharField(max_length=200,default='',null=True)

    b_v1_name=models.CharField(max_length=200,default='',null=True)
    b_m1_no=models.CharField(max_length=200,default='',null=True)
    b_a1_name=models.CharField(max_length=200,default='',null=True)
    total_binding=models.CharField(max_length=200,default='',null=True)

    tra_from_b=models.CharField(max_length=200,default='', null=True)
    to_b=models.CharField(max_length=200,default='', null=True)
    voucher_b =models.CharField(max_length=200,default='', null=True)

   
    binding_approved_1 = models.BooleanField(default=False)
    transfer=models.CharField(max_length=200,default='0',null=True)
    transfer_pending=models.CharField(max_length=200,default='0',null=True)
    Material_center = models.CharField(max_length=200,default='', null=True)

    transfer1=models.CharField(max_length=200,default='0',null=True)
    total_remaining = models.CharField(max_length=200, default='0', null=True, blank=True)
    total_transfer_form = models.CharField(max_length=200, default='0', null=True, blank=True)


    def __str__(self):
            return f"{self.b_v1_name}  {self.b_date}"


class Cuttting(models.Model):
    c_code=models.CharField(max_length=200,default='',null=True)
    c_brand_name=models.CharField(max_length=200,default='',null=True)
    c_class_name=models.CharField(max_length=200,default='',null=True)
    c_medium=models.CharField(max_length=200,default='',null=True)
    c_subject=models.CharField(max_length=200,default='',null=True)
    c_date=models.CharField(max_length=200,default='',null=True)
    c_quantity_5=models.CharField(max_length=200,default='',null=True)

    c_v1_name=models.CharField(max_length=200,default='',null=True)
    c_m1_no=models.CharField(max_length=200,default='',null=True)
    c_a1_name=models.CharField(max_length=200,default='',null=True)


    transfer=models.CharField(max_length=200,default='0',null=True)
    transfer_pending=models.CharField(max_length=200,default='0',null=True)
    machine_cutting_approved_1 = models.BooleanField(default=False)
    tra_from_c=models.CharField(max_length=200,default='', null=True)
    to_c=models.CharField(max_length=200,default='', null=True)
    voucher_c =models.CharField(max_length=200,default='', null=True)
    complete_book =models.CharField(max_length=200,default='', null=True)
    Material_center = models.CharField(max_length=200,default='', null=True)

    transfer1=models.CharField(max_length=200,default='0',null=True)
    total_remaining = models.CharField(max_length=200, default='0', null=True, blank=True)
    total_transfer_form = models.CharField(max_length=200, default='0', null=True, blank=True)

    def __str__(self):
            return f"{self.c_v1_name}  {self.c_date}"

class Manual(models.Model):
    m_code=models.CharField(max_length=200,default='',null=True)   
    m_brand_name1=models.CharField(max_length=200,default='', null=True, blank=True)
    m_class_name1=models.CharField(max_length=200,default='', null=True,blank=True)
    m_medium1=models.CharField(max_length=200,default='', null=True,blank=True)
    m_subject1=models.CharField(max_length=200,default='', null=True,blank=True)
    
    m_striching1=models.CharField(max_length=200,default='', null=True,blank=True)
    m_pasting1=models.CharField(max_length=200,default='', null=True,blank=True)
    m_cutting1=models.CharField(max_length=200,default='', null=True,blank=True)
    
    b_vender_name=models.CharField(max_length=200,default='', null=True,blank=True)
    b_mobile_no=models.CharField(max_length=200,default='', null=True,blank=True)
    b_adress_name = models.CharField(max_length=200, default='', null=True, blank=True)
    b_print_date = models.CharField(max_length=200,default='',null=True)


    stiching_approved_1 = models.BooleanField(default=False)
    tra_from_m=models.CharField(max_length=200,default='', null=True)
    to_m=models.CharField(max_length=200,default='', null=True)
    voucher_m =models.CharField(max_length=200,default='', null=True)
  
    transfer=models.CharField(max_length=200,default='0',null=True)
    transfer_pending=models.CharField(max_length=200,default='0',null=True)
    Material_center = models.CharField(max_length=200,default='', null=True)

    transfer1=models.CharField(max_length=200,default='0',null=True)
    total_remaining = models.CharField(max_length=200, default='0', null=True, blank=True)
    total_transfer_form = models.CharField(max_length=200, default='0', null=True, blank=True)



    def __str__(self):
            return f"{self.b_vender_name}  {self.b_print_date}"            



class printing(models.Model):

    p_vender_name = models.CharField(max_length=200,default='', null=True)
    p_vender_address = models.CharField(max_length=200,default='', null=True)
    p_vender_email = models.CharField(max_length=200,default='', null=True)
    p_vender_mob = models.CharField(max_length=200,default='', null=True)
    p_code=models.CharField(max_length=200,default='',null=True)

    #all items in detail
    p_brand_name_1=models.CharField(max_length=200,default='',null=True)
    p_class_name_1=models.CharField(max_length=200,default='',null=True)
    p_medium_1=models.CharField(max_length=200,default='',null=True)
    p_subject_1=models.CharField(max_length=200,default='',null=True)
    p_quantity_1=models.CharField(max_length=200,default='',null=True)
    p_rim_1=models.CharField(max_length=200,default='',null=True)
    p_pages_1=models.CharField(max_length=200,default='',null=True)


    p_printing_received_form_1 = models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_1 = models.CharField(max_length=200,default='', null=True)


    p_printing_received_form_2=models.CharField(max_length=200,default='', null=True)
    p_printing_received_form_3=models.CharField(max_length=200,default='', null=True)
    p_printing_received_form_4=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_2=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_3=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_4=models.CharField(max_length=200,default='', null=True)
    p_printing_received_form_5=models.CharField(max_length=200,default='', null=True)
    p_printing_received_form_6=models.CharField(max_length=200,default='', null=True)
    p_printing_received_form_7=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_5=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_6=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_7=models.CharField(max_length=200,default='', null=True)
    p_printing_received_form_8=models.CharField(max_length=200,default='', null=True)
    p_printing_received_form_9=models.CharField(max_length=200,default='', null=True)
    p_printing_received_form_10=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_8=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_9=models.CharField(max_length=200,default='', null=True)
    p_print_wastage_form_10=models.CharField(max_length=200,default='', null=True)
    p_single_1=models.CharField(max_length=200,default='', null=True)
    p_double_1=models.CharField(max_length=200,default='', null=True)
    p_four_1=models.CharField(max_length=200,default='', null=True)
    p_print_date =models.CharField(max_length=200,default='')

    total_received_forms = models.CharField(max_length=200,default='', null=True)
    total_wastage_forms = models.CharField(max_length=200,default='', null=True)

    transfer1=models.CharField(max_length=200,default='',null=True)
    transfer2=models.CharField(max_length=200,default='',null=True)
    transfer3=models.CharField(max_length=200,default='',null=True)
    transfer4=models.CharField(max_length=200,default='',null=True)
    transfer5=models.CharField(max_length=200,default='',null=True)
    transfer6=models.CharField(max_length=200,default='',null=True)
    transfer7=models.CharField(max_length=200,default='',null=True)
    transfer8=models.CharField(max_length=200,default='',null=True)
    transfer9=models.CharField(max_length=200,default='',null=True)
    transfer10=models.CharField(max_length=200,default='',null=True)
    
    transfer_pending1=models.CharField(max_length=200,default='',null=True)
    transfer_pending2=models.CharField(max_length=200,default='',null=True)
    transfer_pending3=models.CharField(max_length=200,default='',null=True)
    transfer_pending4=models.CharField(max_length=200,default='',null=True)
    transfer_pending5=models.CharField(max_length=200,default='',null=True)
    transfer_pending6=models.CharField(max_length=200,default='',null=True)
    transfer_pending7=models.CharField(max_length=200,default='',null=True)
    transfer_pending8=models.CharField(max_length=200,default='',null=True)
    transfer_pending9=models.CharField(max_length=200,default='',null=True)
    transfer_pending10=models.CharField(max_length=200,default='',null=True)
    Material_center = models.CharField(max_length=200,default='', null=True)

    transfer=models.CharField(max_length=200,default='',null=True)
    transfer_pending=models.CharField(max_length=200,default='',null=True)


    tra_from_1=models.CharField(max_length=200,default='', null=True)
    to_1=models.CharField(max_length=200,default='', null=True)
    voucher_1 =models.CharField(max_length=200,default='', null=True)
    
   
    
    print_approved_1= models.BooleanField(default=False)

    total_received_form_data = models.CharField(max_length=200, default='0', null=True, blank=True)
    total_transfer_form = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form1 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form2 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form3 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form4 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form5 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form6 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form7 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form8 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form9 = models.CharField(max_length=200, default='0', null=True, blank=True)
    transfer_total_form10 = models.CharField(max_length=200, default='0', null=True, blank=True)
    


    def __str__(self):
            return f"{self.p_vender_name}  {self.p_print_date}"
            

class vouchers(models.Model):
    series =models.CharField(max_length=200,default='', null=True)
    date =models.CharField(max_length=200,default='', null=True)
    voucher_no =models.CharField(max_length=200,default='', null=True)
    tax_type =models.CharField(max_length=200,default='', null=True)
    party =models.CharField(max_length=200,default='', null=True)
    material_centre =models.CharField(max_length=200,default='', null=True)
    voucher_type =models.CharField(max_length=200,default='', null=True)

    debit =models.CharField(max_length=200,default='', null=True)
    credit =models.CharField(max_length=200,default='', null=True)
    short_narration =models.CharField(max_length=200,default='', null=True)
    account=models.CharField(max_length=200,default='', null=True)
    dc=models.CharField(max_length=200,default='', null=True)

    debit1 =models.CharField(max_length=200,default='', null=True)
    credit1 =models.CharField(max_length=200,default='', null=True)
    short_narration1 =models.CharField(max_length=200,default='', null=True)
    account1=models.CharField(max_length=200,default='', null=True)
    dc1=models.CharField(max_length=200,default='', null=True)

    debit2 =models.CharField(max_length=200,default='', null=True)
    credit2 =models.CharField(max_length=200,default='', null=True)
    short_narration2 =models.CharField(max_length=200,default='', null=True)
    account2=models.CharField(max_length=200,default='', null=True)
    dc2=models.CharField(max_length=200,default='', null=True)

    debit3=models.CharField(max_length=200,default='', null=True)
    credit3 =models.CharField(max_length=200,default='', null=True)
    short_narration3 =models.CharField(max_length=200,default='', null=True)
    account3=models.CharField(max_length=200,default='', null=True)
    dc3=models.CharField(max_length=200,default='', null=True)
    
    debit4 =models.CharField(max_length=200,default='', null=True)
    credit4 =models.CharField(max_length=200,default='', null=True)
    short_narration4 =models.CharField(max_length=200,default='', null=True)
    account4=models.CharField(max_length=200,default='', null=True)
    dc4=models.CharField(max_length=200,default='', null=True)

    debit5 =models.CharField(max_length=200,default='', null=True)
    credit5 =models.CharField(max_length=200,default='', null=True)
    short_narration5 =models.CharField(max_length=200,default='', null=True)
    account5=models.CharField(max_length=200,default='', null=True)
    dc5=models.CharField(max_length=200,default='', null=True)

    debit6 =models.CharField(max_length=200,default='', null=True)
    credit6 =models.CharField(max_length=200,default='', null=True)
    short_narration6 =models.CharField(max_length=200,default='', null=True)
    account6=models.CharField(max_length=200,default='', null=True)
    dc6=models.CharField(max_length=200,default='', null=True)

    debit7 =models.CharField(max_length=200,default='', null=True)
    credit7 =models.CharField(max_length=200,default='', null=True)
    short_narration7 =models.CharField(max_length=200,default='', null=True)
    account7=models.CharField(max_length=200,default='', null=True)
    dc7=models.CharField(max_length=200,default='', null=True)

    debit8 =models.CharField(max_length=200,default='', null=True)
    credit8 =models.CharField(max_length=200,default='', null=True)
    short_narration8 =models.CharField(max_length=200,default='', null=True)
    account8=models.CharField(max_length=200,default='', null=True)
    dc8=models.CharField(max_length=200,default='', null=True)

    debit9 =models.CharField(max_length=200,default='', null=True)
    credit9 =models.CharField(max_length=200,default='', null=True)
    short_narration9 =models.CharField(max_length=200,default='', null=True)
    account9=models.CharField(max_length=200,default='', null=True)
    dc9=models.CharField(max_length=200,default='', null=True)

    debit10 =models.CharField(max_length=200,default='', null=True)
    credit10 =models.CharField(max_length=200,default='', null=True)
    short_narration10 =models.CharField(max_length=200,default='', null=True)
    account10=models.CharField(max_length=200,default='', null=True)
    dc10=models.CharField(max_length=200,default='', null=True)

    debit11 =models.CharField(max_length=200,default='', null=True)
    credit11 =models.CharField(max_length=200,default='', null=True)
    short_narration11 =models.CharField(max_length=200,default='', null=True)
    account11=models.CharField(max_length=200,default='', null=True)
    dc11=models.CharField(max_length=200,default='', null=True)

    debit12 =models.CharField(max_length=200,default='', null=True)
    credit12 =models.CharField(max_length=200,default='', null=True)
    short_narration12 =models.CharField(max_length=200,default='', null=True)
    account12=models.CharField(max_length=200,default='', null=True)
    dc12=models.CharField(max_length=200,default='', null=True)

    debit13 =models.CharField(max_length=200,default='', null=True)
    credit13 =models.CharField(max_length=200,default='', null=True)
    short_narration13 =models.CharField(max_length=200,default='', null=True)
    account13=models.CharField(max_length=200,default='', null=True)
    dc13=models.CharField(max_length=200,default='', null=True)

    debit14 =models.CharField(max_length=200,default='', null=True)
    credit14 =models.CharField(max_length=200,default='', null=True)
    short_narration14 =models.CharField(max_length=200,default='', null=True)
    account14=models.CharField(max_length=200,default='', null=True)
    dc14=models.CharField(max_length=200,default='', null=True)

    debit15 =models.CharField(max_length=200,default='', null=True)
    credit15 =models.CharField(max_length=200,default='', null=True)
    short_narration15 =models.CharField(max_length=200,default='', null=True)
    account15=models.CharField(max_length=200,default='', null=True)
    dc15=models.CharField(max_length=200,default='', null=True)




    def __str__(self):
        return self.voucher_no


class Pasting(models.Model):
    pasting_approved_1 = models.BooleanField(default=False)
    tra_from_pasting=models.CharField(max_length=200,default='', null=True)
    to_pasting=models.CharField(max_length=200,default='', null=True)
    voucher_pasting =models.CharField(max_length=200,default='', null=True)
    pasting_brand_name1=models.CharField(max_length=200,default='', null=True, blank=True)
    pasting_class_name1=models.CharField(max_length=200,default='', null=True,blank=True)
    pasting_medium1=models.CharField(max_length=200,default='', null=True,blank=True)
    pasting_subject1=models.CharField(max_length=200,default='', null=True,blank=True)
    pasting_pasting1=models.CharField(max_length=200,default='', null=True,blank=True)
    pasting_code=models.CharField(max_length=200,default='', null=True,blank=True)
    pasting_vender_name=models.CharField(max_length=200,default='', null=True,blank=True)
    pasting_mobile_no=models.CharField(max_length=200,default='', null=True,blank=True)
    pasting_adress_name = models.CharField(max_length=200, default='', null=True, blank=True)
    pasting_print_date = models.CharField(max_length=200,default='',null=True)
    transfer=models.CharField(max_length=200,default='0',null=True)
    transfer_pending=models.CharField(max_length=200,default='0',null=True)  
    Material_center = models.CharField(max_length=200,default='', null=True)

    transfer1=models.CharField(max_length=200,default='0',null=True)
    total_remaining = models.CharField(max_length=200, default='0', null=True, blank=True)
    total_transfer_form = models.CharField(max_length=200, default='0', null=True, blank=True)



    def __str__(self):
        return self.pasting_vender_name





class Manual_cutting(models.Model):
    cutting_approved_1 = models.BooleanField(default=False)
    tra_from_cutting=models.CharField(max_length=200,default='', null=True)
    to_cutting=models.CharField(max_length=200,default='', null=True)
    voucher_cutting =models.CharField(max_length=200,default='', null=True)
    cutting_brand_name1=models.CharField(max_length=200,default='', null=True, blank=True)
    cutting_class_name1=models.CharField(max_length=200,default='', null=True,blank=True)
    cutting_medium1=models.CharField(max_length=200,default='', null=True,blank=True)
    cutting_subject1=models.CharField(max_length=200,default='', null=True,blank=True)
    cutting_cutting1=models.CharField(max_length=200,default='', null=True,blank=True)
    cutting_code=models.CharField(max_length=200,default='', null=True,blank=True)
    cutting_vender_name=models.CharField(max_length=200,default='', null=True,blank=True)
    cutting_mobile_no=models.CharField(max_length=200,default='', null=True,blank=True)
    cutting_adress_name = models.CharField(max_length=200, default='', null=True, blank=True)
    cutting_print_date = models.CharField(max_length=200,default='',null=True)
    transfer=models.CharField(max_length=200,default='',null=True)
    transfer_pending=models.CharField(max_length=200,default='',null=True)



    def __str__(self):
        return self.cutting_vender_name



class Cover_Printing(models.Model):
    cover_transfer= models.BooleanField(default=False)
    plate_no=models.CharField(max_length=200,default='', null=True)
    paper_to_be_used=models.CharField(max_length=200,default='', null=True)
    width =models.CharField(max_length=200,default='', null=True)
    length=models.CharField(max_length=200,default='', null=True, blank=True)
    unit=models.CharField(max_length=200,default='', null=True,blank=True)
    no_of_ups=models.CharField(max_length=200,default='', null=True,blank=True)
    subject1=models.CharField(max_length=200,default='', null=True,blank=True)
    subject2=models.CharField(max_length=200,default='', null=True,blank=True)
    subject3=models.CharField(max_length=200,default='', null=True,blank=True)
    subject4=models.CharField(max_length=200,default='', null=True,blank=True)
    subject5=models.CharField(max_length=200,default='', null=True,blank=True)
    subject6 = models.CharField(max_length=200, default='', null=True, blank=True)
    subject7 = models.CharField(max_length=200,default='',null=True)
    subject8=models.CharField(max_length=200,default='',null=True)
    subject9=models.CharField(max_length=200,default='',null=True)
    subject10=models.CharField(max_length=200,default='',null=True)
    subject11=models.CharField(max_length=200,default='',null=True)
    subject12=models.CharField(max_length=200,default='',null=True)
    subject13=models.CharField(max_length=200,default='',null=True)
    subject14=models.CharField(max_length=200,default='',null=True)
    subject15=models.CharField(max_length=200,default='',null=True)
    subject16=models.CharField(max_length=200,default='',null=True)
    plate_rate=models.CharField(max_length=200,default='', null=True)
    printing_rate=models.CharField(max_length=200,default='', null=True)
    tax=models.CharField(max_length=200,default='', null=True)
    lamination=models.CharField(max_length=200,default='', null=True)
    rate1=models.CharField(max_length=200,default='', null=True)
    rate2=models.CharField(max_length=200,default='', null=True)
    bill_company=models.CharField(max_length=200,default='', null=True)
    texture=models.CharField(max_length=200,default='', null=True)
    from_vend=models.CharField(max_length=200,default='', null=True)
    to_vend=models.CharField(max_length=200,default='', null=True)
    transfer=models.CharField(max_length=200,default='',null=True)
    transfer_pending=models.CharField(max_length=200,default='',null=True)
    quantity_cover=models.CharField(max_length=200,default='',null=True)


    def __str__(self):
        return self.plate_no

class Subject(models.Model):
    
    subject=models.CharField(max_length=200,default='', null=True)
    subject_added_on=models.CharField(max_length=200,default='')
    def __str__(self):
        return self.subject


    
class Cover_order(models.Model):
    material_center =models.CharField(max_length=200,default='', null=True)
    palte_order=models.CharField(max_length=200,default='', null=True)
    subject_order=models.CharField(max_length=200,default='', null=True)
    self_company=models.CharField(max_length=200,default='', null=True)
    vendor_order=models.CharField(max_length=200,default='', null=True)
    date_order=models.CharField(max_length=200,default='', null=True)
    quantity_order=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order1=models.CharField(max_length=200,default='', null=True)
    quantity_order1=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order1=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount1=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order2=models.CharField(max_length=200,default='', null=True)
    quantity_order2=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order2=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount2=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order3=models.CharField(max_length=200,default='', null=True)
    quantity_order3=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order3=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount3=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order4=models.CharField(max_length=200,default='', null=True)
    quantity_order4=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order4=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount4=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order5=models.CharField(max_length=200,default='', null=True)
    quantity_order5=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order5=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount5=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order6=models.CharField(max_length=200,default='', null=True)
    quantity_order6=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order6=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount6=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order7=models.CharField(max_length=200,default='', null=True)
    quantity_order7=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order7=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount7=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order8=models.CharField(max_length=200,default='', null=True)
    quantity_order8=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order8=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount8=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order9=models.CharField(max_length=200,default='', null=True)
    quantity_order9=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order9=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount9=models.CharField(max_length=200,default='', null=True, blank=True)

    plate_order10=models.CharField(max_length=200,default='', null=True)
    quantity_order10=models.CharField(max_length=200,default='', null=True, blank=True)
    rate_order10=models.CharField(max_length=200,default='', null=True, blank=True)  
    amount10=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet=models.CharField(max_length=200,default='', null=True, blank=True)


    printing_sheet1=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet1=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet1=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet2=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet2=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet2=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet3=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet3=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet3=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet4=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet4=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet4=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet5=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet5=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet5=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet6=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet6=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet6=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet7=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet7=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet7=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet8=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet8=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet8=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet9=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet9=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet9=models.CharField(max_length=200,default='', null=True, blank=True)

    printing_sheet10=models.CharField(max_length=200,default='', null=True, blank=True)
    lamination_sheet10=models.CharField(max_length=200,default='', null=True, blank=True)  
    texture_sheet10=models.CharField(max_length=200,default='', null=True, blank=True)

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


class Main_group(models.Model):
    group_name = models.CharField(max_length=200,default='', null=True)
    alias = models.CharField(max_length=200,default='', null=True)
    primary_input= models.CharField(max_length=200,default='', null=True)
    type= models.CharField(max_length=200,default='', null=True)

    def __str__(self):
        return self.group_name
    
class Item_creation(models.Model):
    brand_trade_name=models.CharField(max_length=200,default='', null=True)
    brand_subtitle=models.CharField(max_length=200,default='', null=True)
    class1=models.CharField(max_length=200,default='', null=True)
    size=models.CharField(max_length=200,default='', null=True)
    subject_name_author=models.CharField(max_length=200,default='', null=True)
    code=models.CharField(max_length=200,default='', null=True)
    from_size=models.CharField(max_length=200,default='', null=True)
    no_of_pages=models.CharField(max_length=200,default='', null=True)
    unit=models.CharField(max_length=200,default='', null=True)
    no_of_forms=models.CharField(max_length=200,default='', null=True)
    binding_rate=models.CharField(max_length=200,default='', null=True)
    opening_stock_qty=models.CharField(max_length=200,default='', null=True)
    opening_stock_value=models.CharField(max_length=200,default='', null=True)
    bundle_pack=models.CharField(max_length=200,default='', null=True)
    tax_information_rate=models.CharField(max_length=200,default='', null=True)
    tax_information_rate_central=models.CharField(max_length=200,default='', null=True)
    item_binding_form_size=models.CharField(max_length=200,default='', null=True)
    binding_no_of_form=models.CharField(max_length=200,default='', null=True)
    item_material_center = models.CharField(max_length=200,default='', null=True)



    def __str__(self):
        return self.brand_trade_name
    

class database(models.Model):
    district_d=models.CharField(max_length=200,default='', null=True)
    tehsil=models.CharField(max_length=200,default='', null=True)
    town=models.CharField(max_length=200,default='', null=True)
    pincode=models.CharField(max_length=200,default='', null=True)
    zone=models.CharField(max_length=200,default='', null=True)
    tour_group=models.CharField(max_length=200,default='', null=True)
    currency=models.CharField(max_length=200,default='', null=True)


    def __str__(self):
        return self.district_d

class transaction_operation(models.Model):
    company_type=models.CharField(max_length=200,default='', null=True)
    t_series=models.CharField(max_length=200,default='', null=True)
    party=models.CharField(max_length=200,default='', null=True)
    vehno=models.CharField(max_length=200,default='', null=True)
    delivered_at=models.CharField(max_length=200,default='', null=True)
    narration=models.CharField(max_length=200,default='', null=True)
    roll_quantity=models.CharField(max_length=200,default='', null=True)
    roll_unit=models.CharField(max_length=200,default='', null=True)
    roll_rate=models.CharField(max_length=200,default='', null=True)
    roll_amount=models.CharField(max_length=200,default='', null=True)
    
    

    Particular_1=models.CharField(max_length=200,default='', null=True)
    roll_quantity_1=models.CharField(max_length=200,default='', null=True)
    roll_unit_1=models.CharField(max_length=200,default='', null=True)
    roll_rate_1=models.CharField(max_length=200,default='', null=True)
    roll_amount_1=models.CharField(max_length=200,default='', null=True)
    ex_no_1=models.CharField(max_length=200,default='', null=True)
    weight_1=models.CharField(max_length=200,default='', null=True)
    p_weight_1=models.CharField(max_length=200,default='', null=True)
    rim_1=models.CharField(max_length=200,default='', null=True)
    sheet_1=models.CharField(max_length=200,default='', null=True)

    Particular2=models.CharField(max_length=200,default='', null=True)
    paper_rim_qty=models.CharField(max_length=200,default='', null=True)
    rim_unit=models.CharField(max_length=200,default='', null=True)
    rim_rate=models.CharField(max_length=200,default='', null=True)
    rim_amount=models.CharField(max_length=200,default='', null=True)

    Particular3=models.CharField(max_length=200,default='', null=True)
    cover_paper_qty=models.CharField(max_length=200,default='', null=True)
    cover_paper_unit=models.CharField(max_length=200,default='', null=True)
    cover_paper_rate=models.CharField(max_length=200,default='', null=True)
    cover_paper_amount=models.CharField(max_length=200,default='', null=True)

    Particular=models.CharField(max_length=200,default='', null=True)
    roll_quantity=models.CharField(max_length=200,default='', null=True)
    roll_unit=models.CharField(max_length=200,default='', null=True)
    roll_rate=models.CharField(max_length=200,default='', null=True)
    roll_amount=models.CharField(max_length=200,default='', null=True)
    ex_no=models.CharField(max_length=200,default='', null=True)
    weight=models.CharField(max_length=200,default='', null=True)
    p_weight=models.CharField(max_length=200,default='', null=True)
    rim=models.CharField(max_length=200,default='', null=True)
    sheet=models.CharField(max_length=200,default='', null=True)

    dynamic_data = models.JSONField(null=True, blank=True)
    

    def __str__(self):
        return self.t_series
    


class Binder_ledger(models.Model):
    name=models.CharField(max_length=200,default='', null=True)
    prefix=models.CharField(max_length=200,default='', null=True)
    alias=models.CharField(max_length=200,default='', null=True)
    adress=models.CharField(max_length=200,default='', null=True)
    contact_no=models.CharField(max_length=200,default='', null=True)
    whatsapp=models.CharField(max_length=200,default='', null=True)
    opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_binder=models.CharField(max_length=200,default='', null=True, blank=True)
    email=models.CharField(max_length=200,default='', null=True, blank=True)
    vender_group=models.CharField(max_length=200,default='', null=True, blank=True)
    vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.name

class Gather_ledger(models.Model):
    g_name=models.CharField(max_length=200,default='', null=True)
    g_prefix=models.CharField(max_length=200,default='', null=True)
    g_alias=models.CharField(max_length=200,default='', null=True)
    g_adress=models.CharField(max_length=200,default='', null=True)
    g_contact_no=models.CharField(max_length=200,default='', null=True)
    g_whatsapp=models.CharField(max_length=200,default='', null=True)
    g_opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    gathering_rate=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_gather=models.CharField(max_length=200,default='', null=True, blank=True)
    g_email=models.CharField(max_length=200,default='', null=True, blank=True)
    g_vender_group=models.CharField(max_length=200,default='', null=True, blank=True)
    g_vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.g_name
      
class Stitcher_ledger(models.Model):
    s_name=models.CharField(max_length=200,default='', null=True)
    s_prefix=models.CharField(max_length=200,default='', null=True)
    s_alias=models.CharField(max_length=200,default='', null=True)
    s_adress=models.CharField(max_length=200,default='', null=True)
    s_contact_no=models.CharField(max_length=200,default='', null=True)
    s_whatsapp=models.CharField(max_length=200,default='', null=True)
    s_opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    stitching_rate=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_stitcher=models.CharField(max_length=200,default='', null=True, blank=True)
    s_email=models.CharField(max_length=200,default='', null=True, blank=True)
    s_vender_group=models.CharField(max_length=200,default='', null=True, blank=True)
    s_vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.s_name
      


class Paster_ledger(models.Model):
    p_name=models.CharField(max_length=200,default='', null=True)
    p_prefix=models.CharField(max_length=200,default='', null=True)
    p_alias=models.CharField(max_length=200,default='', null=True)
    p_adress=models.CharField(max_length=200,default='', null=True)
    p_contact_no=models.CharField(max_length=200,default='', null=True)
    p_whatsapp=models.CharField(max_length=200,default='', null=True)
    p_opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    pasting_rate=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_paster=models.CharField(max_length=200,default='', null=True, blank=True)
    p_email=models.CharField(max_length=200,default='', null=True, blank=True)
    p_vender_group=models.CharField(max_length=200,default='', null=True, blank=True)
    p_vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.p_name


class Machine_ledger(models.Model):
    m_name=models.CharField(max_length=200,default='', null=True)
    m_prefix=models.CharField(max_length=200,default='', null=True)
    m_alias=models.CharField(max_length=200,default='', null=True)
    m_adress=models.CharField(max_length=200,default='', null=True)
    m_contact_no=models.CharField(max_length=200,default='', null=True)
    m_whatsapp=models.CharField(max_length=200,default='', null=True)
    m_opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    machine_rate=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_machine=models.CharField(max_length=200,default='', null=True, blank=True)
    m_email=models.CharField(max_length=200,default='', null=True, blank=True)
    m_vender_group=models.CharField(max_length=200,default='', null=True, blank=True)
    m_vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.m_name


class Cutter_ledger(models.Model):
    c_name=models.CharField(max_length=200,default='', null=True)
    c_prefix=models.CharField(max_length=200,default='', null=True)
    c_alias=models.CharField(max_length=200,default='', null=True)
    c_adress=models.CharField(max_length=200,default='', null=True)
    c_contact_no=models.CharField(max_length=200,default='', null=True)
    c_whatsapp=models.CharField(max_length=200,default='', null=True)
    c_opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    cutting_rate=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_cutter=models.CharField(max_length=200,default='', null=True, blank=True)
    cutting_rate_sheet=models.CharField(max_length=200,default='', null=True, blank=True)
    c_email=models.CharField(max_length=200,default='', null=True, blank=True)
    c_vender_group=models.CharField(max_length=200,default='', null=True, blank=True)
    c_vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.c_name


class Packer_ledger(models.Model):
    pack_name=models.CharField(max_length=200,default='', null=True)
    pack_prefix=models.CharField(max_length=200,default='', null=True)
    pack_alias=models.CharField(max_length=200,default='', null=True)
    pack_adress=models.CharField(max_length=200,default='', null=True)
    pack_contact_no=models.CharField(max_length=200,default='', null=True)
    pack_whatsapp=models.CharField(max_length=200,default='', null=True)
    pack_opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    packing_rate=models.CharField(max_length=200,default='', null=True, blank=True)
    bitti_rate=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_packer=models.CharField(max_length=200,default='', null=True, blank=True)
    pack_email=models.CharField(max_length=200,default='', null=True, blank=True)
    pack_vender_group=models.CharField(max_length=200,default='', null=True, blank=True)
    pack_vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.pack_name

class General_ledger(models.Model):
    g_name=models.CharField(max_length=200,default='', null=True)
    g_prefix=models.CharField(max_length=200,default='', null=True)
    g_alias=models.CharField(max_length=200,default='', null=True)
    g_adress=models.CharField(max_length=200,default='', null=True)
    g_contact_no=models.CharField(max_length=200,default='', null=True)
    g_whatsapp=models.CharField(max_length=200,default='', null=True)
    g_opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    previous_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    act_material_center=models.CharField(max_length=200,default='', null=True, blank=True)
    fax=models.CharField(max_length=200,default='', null=True, blank=True)
    eamil=models.CharField(max_length=200,default='', null=True, blank=True)
    tel_no=models.CharField(max_length=200,default='', null=True, blank=True)
    print_name=models.CharField(max_length=200,default='', null=True, blank=True)
    group=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_general=models.CharField(max_length=200,default='', null=True, blank=True)

   
    g_vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.g_name


class Customer_ledger(models.Model):
    cust_name=models.CharField(max_length=200,default='', null=True)
    cust_prefix=models.CharField(max_length=200,default='', null=True)
    cust_alias=models.CharField(max_length=200,default='', null=True)
    cust_adress=models.CharField(max_length=200,default='', null=True)
    cust_contact_no=models.CharField(max_length=200,default='', null=True)
    cust_whatsapp=models.CharField(max_length=200,default='', null=True)
    cust_opening_balence=models.CharField(max_length=200,default='', null=True, blank=True)
    district=models.CharField(max_length=200,default='', null=True, blank=True)
    zone=models.CharField(max_length=200,default='', null=True, blank=True)
    tour_group=models.CharField(max_length=200,default='', null=True, blank=True)
    cust_eamil=models.CharField(max_length=200,default='', null=True, blank=True)
    tahsil=models.CharField(max_length=200,default='', null=True, blank=True)
    pin=models.CharField(max_length=200,default='', null=True, blank=True)
    group=models.CharField(max_length=200,default='', null=True, blank=True)
    area=models.CharField(max_length=200,default='', null=True, blank=True)
    price_category=models.CharField(max_length=200,default='', null=True, blank=True)
    code=models.CharField(max_length=200,default='', null=True, blank=True)
    debit_customer=models.CharField(max_length=200,default='', null=True, blank=True)

    c_vender_gst=models.CharField(max_length=200,default='', null=True, blank=True)

    def __str__(self):
        return self.cust_name

class cover_scrap_voucher(models.Model):
    cover_date=models.CharField(max_length=200,default='', null=True)
    cover_voucher_no=models.CharField(max_length=200,default='', null=True)
    cover_subject=models.CharField(max_length=200,default='', null=True)
    cover_qty=models.CharField(max_length=200,default='', null=True)
    cover_unit=models.CharField(max_length=200,default='', null=True)
    cover_rate=models.CharField(max_length=200,default='', null=True)
    cover_bill_material=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_bill_material_name=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_alias=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_item_produce=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_quantity=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_unit1=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_expenses=models.CharField(max_length=200,default='', null=True, blank=True)
    item_generated=models.CharField(max_length=200,default='', null=True, blank=True)
    item_consumed=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular1=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty1=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit1=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate1=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular2=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty2=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit2=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate2=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular3=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty3=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit3=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate3=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular4=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty4=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit4=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate4=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular5=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty5=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit5=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate5=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular6=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty6=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit6=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate6=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular7=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty7=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit7=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate7=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular8=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty8=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit8=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate8=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular9=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty9=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit9=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate9=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_particular10=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_qty10=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_unit10=models.CharField(max_length=200,default='', null=True, blank=True)
    cover_scrap_rate10=models.CharField(max_length=200,default='', null=True, blank=True)

    cover_scrap_total_quantity=models.CharField(max_length=200,default='', null=True, blank=True)

    remaning_cover=models.CharField(max_length=200,default='',null=True)
    remaning_cover1=models.CharField(max_length=200,default='',null=True)
    remaning_cover2=models.CharField(max_length=200,default='',null=True)
    remaning_cover3=models.CharField(max_length=200,default='',null=True)
    remaning_cover4=models.CharField(max_length=200,default='',null=True)
    remaning_cover5=models.CharField(max_length=200,default='',null=True)
    remaning_cover6=models.CharField(max_length=200,default='',null=True)
    remaning_cover7=models.CharField(max_length=200,default='',null=True)
    remaning_cover8=models.CharField(max_length=200,default='',null=True)
    remaning_cover9=models.CharField(max_length=200,default='',null=True)
    remaning_cover10=models.CharField(max_length=200,default='',null=True)



class other_vouchers(models.Model):
    contes=models.CharField(max_length=200,default='', null=True)
    account_dr=models.CharField(max_length=200,default='', null=True)
    account_cr=models.CharField(max_length=200,default='', null=True)
    Debit_credit=models.CharField(max_length=200,default='', null=True)
    account=models.CharField(max_length=200,default='', null=True)
    debit=models.CharField(max_length=200,default='', null=True)
    credit=models.CharField(max_length=200,default='', null=True)
    inst_type=models.CharField(max_length=200,default='', null=True)
    inst_no=models.CharField(max_length=200,default='', null=True)


class District(models.Model):
    district_master=models.CharField(max_length=200,default='', null=True)
    tehsil_master=models.CharField(max_length=200,default='', null=True)


class District1(models.Model):
    district_master=models.CharField(max_length=200,default='', null=True)
    tehsil_master=models.CharField(max_length=200,default='', null=True)

class Product_group(models.Model):
    brand_name=models.CharField(max_length=200,default='', null=True)
    sub_brand_name=models.CharField(max_length=200,default='', null=True)
    brand_subtitle=models.CharField(max_length=200,default='', null=True)
    categories=models.CharField(max_length=200,default='', null=True)
    main_discount=models.CharField(max_length=200,default='', null=True)
    extra_discount=models.CharField(max_length=200,default='', null=True)
    size=models.CharField(max_length=200,default='', null=True)

class Category(models.Model):
    category=models.CharField(max_length=200,default='', null=True)

class product_by(models.Model):
     pname=models.CharField(max_length=200,default='', null=True)
     palias=models.CharField(max_length=200,default='', null=True)
     p_print_name=models.CharField(max_length=200,default='', null=True)
     opening_stock_p=models.CharField(max_length=200,default='', null=True)
     punit=models.CharField(max_length=200,default='', null=True)
     p_opening_stock_value=models.CharField(max_length=200,default='', null=True)
     p_gsm=models.CharField(max_length=200,default='', null=True)
     p_p_width=models.CharField(max_length=200,default='', null=True)
     p_p_length=models.CharField(max_length=200,default='', null=True)
     punit1=models.CharField(max_length=200,default='', null=True)
     punit2=models.CharField(max_length=200,default='', null=True)
     punit3=models.CharField(max_length=200,default='', null=True)
     punit1_conversion=models.CharField(max_length=200,default='', null=True)
     pcunit1=models.CharField(max_length=200,default='', null=True)
     punit2_conversion=models.CharField(max_length=200,default='', null=True)
     pcunit2=models.CharField(max_length=200,default='', null=True)
     sale_price=models.CharField(max_length=200,default='', null=True)
     purchase_price=models.CharField(max_length=200,default='', null=True)
     mrp=models.CharField(max_length=200,default='', null=True)
     min_sale_price=models.CharField(max_length=200,default='', null=True)
     sale_value_price=models.CharField(max_length=200,default='', null=True)
     product_tax_local=models.CharField(max_length=200,default='', null=True)
     product_tax_central=models.CharField(max_length=200,default='', null=True)
     product_gst=models.CharField(max_length=200,default='', null=True)
     product_item_description=models.CharField(max_length=200,default='', null=True)
     punit33=models.CharField(max_length=200,default='', null=True)
     punit22=models.CharField(max_length=200,default='', null=True)
     by_material_center=models.CharField(max_length=200,default='', null=True)



class Form_Printing(models.Model):
    form_pages=models.CharField(max_length=200,default='', null=True)
    form_vender=models.CharField(max_length=200,default='', null=True)
    form_code=models.CharField(max_length=200,default='', null=True)
    form_brand=models.CharField(max_length=200,default='', null=True)
    form_class=models.CharField(max_length=200,default='', null=True)
    form_medium=models.CharField(max_length=200,default='', null=True)
    form_subject=models.CharField(max_length=200,default='', null=True)
    form_quantity=models.CharField(max_length=200,default='', null=True, blank=True)
    form1=models.CharField(max_length=200,default='', null=True)
    form2=models.CharField(max_length=200,default='', null=True, blank=True)  
    form3=models.CharField(max_length=200,default='', null=True, blank=True)  
    form4=models.CharField(max_length=200,default='', null=True)
    form5=models.CharField(max_length=200,default='', null=True, blank=True)  
    form6=models.CharField(max_length=200,default='', null=True, blank=True)  
    form7=models.CharField(max_length=200,default='', null=True)
    form8=models.CharField(max_length=200,default='', null=True, blank=True)  
    form9=models.CharField(max_length=200,default='', null=True, blank=True)  
    form10=models.CharField(max_length=200,default='', null=True, blank=True)  
    transfer_1=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer_2=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer_3=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer_4=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer_5=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer_6=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer_7=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer_8=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer9=models.CharField(max_length=200,default='', null=True, blank=True)
    transfer10=models.CharField(max_length=200,default='', null=True, blank=True)
    form_date=models.CharField(max_length=200,default='', null=True, blank=True)
    total_forms = models.CharField(max_length=200,default='', null=True)
    transfer= models.CharField(max_length=200,default='', null=True)
    transfer_pending=models.CharField(max_length=200,default='', null=True)
    transfer_pending1=models.CharField(max_length=200,default='', null=True)
    transfer_pending2=models.CharField(max_length=200,default='', null=True)
    transfer_pending3=models.CharField(max_length=200,default='', null=True)
    transfer_pending4=models.CharField(max_length=200,default='', null=True)
    transfer_pending5=models.CharField(max_length=200,default='', null=True)
    transfer_pending6=models.CharField(max_length=200,default='', null=True)
    transfer_pending7=models.CharField(max_length=200,default='', null=True)
    transfer_pending8=models.CharField(max_length=200,default='', null=True)
    transfer_pending9=models.CharField(max_length=200,default='', null=True)
    transfer_pending10=models.CharField(max_length=200,default='', null=True)
    to=models.CharField(max_length=200,default='', null=True)


class Cover_rawmaterial(models.Model):
    cmname=models.CharField(max_length=200,default='', null=True)
    cmalias=models.CharField(max_length=200,default='', null=True)
    cprint_name=models.CharField(max_length=200,default='', null=True)
    cqunit=models.CharField(max_length=200,default='', null=True)
    copening_stock_value=models.CharField(max_length=200,default='', null=True)
    cgsm=models.CharField(max_length=200,default='', null=True)
    cp_width=models.CharField(max_length=200,default='', null=True)
    cp_length=models.CharField(max_length=200,default='', null=True)
    cunit1=models.CharField(max_length=200,default='', null=True)
    cqunit1=models.CharField(max_length=200,default='', null=True)
    cunit2=models.CharField(max_length=200,default='', null=True)
    cqunit2=models.CharField(max_length=200,default='', null=True)
    cunit3=models.CharField(max_length=200,default='', null=True)
    cqunit3=models.CharField(max_length=200,default='', null=True)
    cunit1_conversion=models.CharField(max_length=200,default='', null=True)
    cmunit1=models.CharField(max_length=200,default='', null=True)
    cunit2_conversion=models.CharField(max_length=200,default='', null=True)

    cmunit2=models.CharField(max_length=200,default='', null=True)
    opening_stock_rm = models.CharField(max_length=200,default='', null=True)
    gross = models.CharField(max_length=200,default='', null=True)
    p_date = models.CharField(max_length=200,default='',null=True)
    cwaste_percent= models.CharField(max_length=200,default='',null=True)
    cWaste= models.CharField(max_length=200,default='',null=True)
    opening_stock1= models.CharField(max_length=200,default='', null=True)
    opening_unit1 =models.CharField(max_length=200,default='', null=True)
    opening_unit2 =models.CharField(max_length=200,default='', null=True)
    opening_stock2 = models.CharField(max_length=200,default='',null=True)
    conversion_factor1= models.CharField(max_length=200,default='',null=True)
    conversion_unit1= models.CharField(max_length=200,default='', null=True)
    conversion_unit2= models.CharField(max_length=200,default='', null=True)

    conversion_factor2= models.CharField(max_length=200,default='',null=True)
    unit4=models.CharField(max_length=200,default='',null=True)
    Cover_material_centre=models.CharField(max_length=200,default='', null=True)
    cover_material=models.CharField(max_length=200,default='',null=True)


class master_unit(models.Model):
    unit_name_master=models.CharField(max_length=200,default='',null=True)
    unit_Alias=models.CharField(max_length=200,default='',null=True)
    unit_print_name=models.CharField(max_length=200,default='',null=True)

class conversion_unit(models.Model):
    main_unit=models.CharField(max_length=200,default='',null=True)
    sub_unit=models.CharField(max_length=200,default='',null=True)
    Con_factor=models.CharField(max_length=200,default='',null=True)

class item_master(models.Model):
    item_name=models.CharField(max_length=200,default='',null=True)
    item_alias=models.CharField(max_length=200,default='',null=True)
    item_print_name=models.CharField(max_length=200,default='',null=True)
    item_group=models.CharField(max_length=200,default='',null=True)
    
class Tour_group(models.Model):
    zone=models.CharField(max_length=200,default='',null=True)
    tour_group=models.CharField(max_length=200,default='',null=True)