from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('setting-brands/',brand_setting,name="setting-brands"),
    path('edit-brands/<int:id>/',edit_brands,name="edit-brands"),
    path('delete-brands/<int:id>/',delete_brand, name="delete-brands"),
    path('setting-classes/',class_setting,name="setting-classes"),
    path('edit-classes/<int:id>/',edit_classes,name="edit-classes"),
    path('delete-classes/<int:id>/',delete_class, name="delete-classes"),

    path('excel_export_view/',excel_export_view,name='excel_export_view'),
    path('setting-books/',books_setting,name="setting-books"), 
    path('delete-books/<int:id>/',delete_books, name="delete-books"),
    path('edit-books/<int:id>/',edit_books,name="edit-books"),
    path('forms-setting/',form_setting,name="forms-setting"),
    path('edit-form/<int:id>/',edit_form,name="edit-form"),
    path('delete-form/<int:id>/',delete_form, name="delete-form"),
    path('medium-setting/',medium_setting,name="medium-setting"),
    path('edit-medium/<int:id>/',edit_medium,name="edit-medium"),
    path('delete-medium/<int:id>/',delete_medium, name="delete-medium"),
    path('cover_rawmaterial/',cover_rawmaterial,name="cover_rawmaterial"),
    path('edit_cover_rawmaterial/<int:id>/',edit_cover_rawmaterial,name="edit_cover_rawmaterial"),
    path('delete_cover_rawmaterial/<int:id>/',delete_cover_rawmaterial, name="delete_cover_rawmaterial"),


    path('company/',company,name="company"), 
    path('edit_company/<int:id>/', edit_company, name="edit_company"),

    path('delete_company/<int:id>/',delete_company,name="delete_company"),



    path('binding_vender/',binding_vender,name="binding_vender"), 
    path('edit_bindingvender/<int:id>/', edit_bindingvender, name="edit_bindingvender"),

    path('gathering_vender/',gathering_vender,name="gathering_vender"),
    path('edit_gatheringvenders/<int:id>/', edit_gatheringvenders, name="edit_gatheringvenders"),
    path('delete_gatheringvenders/<int:id>/', delete_gatheringvenders, name="delete_gatheringvenders"),


    path('cutting_vender/',cutting_vender,name="cutting_vender"),
    path('delete_cuttingvenders/<int:id>/', delete_cuttingvenders, name="delete_cuttingvenders"),
    path('edit_cuttingvenders/<int:id>/', edit_cuttingvenders, name="edit_cuttingvenders"),



    path('packing_vender/',packing_vender,name="packing_vender"),
    path('delete_packingvenders/<int:id>/', delete_packingvenders, name="delete_packingvenders"),
    path('edit_packingvenders/<int:id>/', edit_packingvenders, name="edit_packingvenders"),




    path('delete_bindingvender/<int:id>/',delete_bindingvender,name="delete_bindingvender"),  
    path('cover_vender/',cover_vender,name="cover_vender"), 
    path('edit_cover_vender/<int:id>/', edit_cover_vender, name="edit_cover_vender"),

    path('delete_cover_vender/<int:id>/',delete_cover_vender,name="delete_cover_vender"), 
    path('venders-setting/',vender_setting,name="venders-setting"),
    path('edit-venders/<int:id>/',edit_venders,name="edit-venders"),
    path('delete-venders/<int:id>/',delete_venders, name="delete-venders"),
    path('centre-setting/',centre_setting,name="centre-setting"),
    path('delete-centre/<int:id>/',delete_centre, name="delete-centre"),
    path('edit-centre/<int:id>/',edit_centre,name="edit-centre"),
    path('distributor/',distributor,name="distributor"),
    path('group/', group, name="group"),
    path('delete_group/<int:id>/', delete_group, name="delete_group"),
    path('edit_group/<int:id>/', edit_group, name="edit_group"),
    path('delete_distributor/<int:id>/', delete_distributor, name="delete_distributor"),
    path('edit_distributor/<int:id>/', edit_distributor, name="edit_distributor"),


    path('printing-data/',printing_bookwise,name="printing-data"),
    path('edit_printing_form/<int:id>/', edit_printing_data, name="edit_printing_data"),
    path('delete_printing/<int:id>/',delete_printing,name="delete_printing"), 
    path('print_view/<int:id>/',print_view,name="print_view"),
    path('print_transfer/',print_transfer,name="print_transfer"),


    path('gathering/', gathering, name="gathering"),
    path('delete_gather/<int:id>/',delete_gather, name="delete_gather"),
    path('edit_gather/<int:id>/',edit_gather, name="edit_gather"),
    path('gather_view/<int:id>/',gather_view, name="gather_view"),
     path('gather_transfer/',gather_transfer,name="gather_transfer"),



    path('cutting_info/', Cutting_info, name="cutting_info"),
    path('delete_cutting/<int:id>/',delete_cutting, name="delete_cutting"),
    path('edit_cutting/<int:id>/',edit_cutting, name="edit_cutting"),



    path('machine_binding/', machine_binding, name="machine_binding"),
    path('delete_machine/<int:id>/',delete_machine, name="delete_machine"),
    path('edit_machine/<int:id>/',edit_machine, name="edit_machine"),
    path('machine_transfer/',machine_transfer,name="machine_transfer"),
    path('cutting_machine_transfer_packing/',cutting_machine_transfer_packing,name="cutting_machine_transfer_packing"),


    path('manual-info/',Manual_info,name="manual-info"),
    path('edit_manual/<int:id>/', edit_manual, name="edit_manual"),
    path('delete_manual/<int:id>/', delete_manual, name="delete_manual"),
    path('gather_transfer_manual/',gather_transfer_manual,name="gather_transfer_manual"), 
    path('vouchers/',vouchers_1,name="vouchers"),
    path('delete-vouchers/<int:id>/',delete_voucher, name="delete-voucher"),
    path('view_voucher/<int:id>/',view_voucher, name="view_voucher"),
    path('edit-voucher/<int:id>/',edit_voucher,name="edit-voucher"),


    path('pasting/',pasting,name="pasting"), 
    path('edit_pasting/<int:id>/', edit_pasting, name="edit_pasting"),

    path('delete_pasting/<int:id>/',delete_pasting,name="delete_pasting"),
    path('stiching_transfer_pasting/',stiching_transfer_pasting,name="stiching_transfer_pasting"), 
    path('pasting_transfer_cutting/',pasting_transfer_cutting,name="pasting_transfer_cutting"),
    path('cutting_manual_transfer_packing/',cutting_manual_transfer_packing,name="cutting_manual_transfer_packing"),
    path('subbrand_name/',subbrand_name,name="subbrand_name"),
    path('delete_subbrand/<int:id>/',delete_subbrand,name="delete_subbrand"),
    path('edit_subbrand/<int:id>/',edit_subbrand,name="edit_subbrand"),
    path('view_subbrand/<int:id>/',view_subbrand,name="view_subbrand"),

    path('cover_order/',cover_order,name="cover_order"),
    path('cover_order/<int:id>/',cover_order_bill_view,name="cover_order_bill_view"), 
    path('cover_transfer/',cover_transfer,name="cover_transfer"),  
    path('cover_printing/',cover_printing,name="cover_printing"), 
    path('edit_cover/<int:id>/',edit_cover,name="edit_cover"), 

    # path('edit_cover_order/<int:id>/', edit_cover_order, name="edit_cover_order"),

    path('delete_cover/<int:id>/',delete_cover,name="delete_cover"),
    path('delete_cover_order/<int:id>/',delete_cover_order,name="delete_cover_order"),
    # path('edit_cover_order/<int:id>/', edit_cover_order, name="edit_cover_order"),

    path('main_group/', main_group, name="main_group"),
    path('delete_main_group/<int:id>/', delete_main_group, name="delete_main_group"),
    path('item_creation/', item_creation, name="item_creation"),
    path('delete_item_creation/<int:id>/', delete_item_creation, name="delete_item_creation"),
    path('edit_item_creation/<int:id>/', edit_item_creation, name="edit_item_creation"),

    path('database/', database_creation, name="database"),
    path('delete_database_creation/<int:id>/', delete_database_creation, name="delete_database_creation"),
    path('edit_database/<int:id>/', edit_database, name="edit_database"),

    path('transactions_operation/', transactions_operation, name="transactions_operation"),
    path('transaction_view/<int:id>/', transaction_view, name="transaction_view"),
    path('delete_transaction/<int:id>/', delete_transaction, name="delete_transaction"),
    path('edit_transaction/<int:id>/', edit_transaction, name="edit_transaction"),

    path('binder_ledger/',binder_ledger,name="binder_ledger"), 
    path('edit_binder/<int:id>/', edit_binder, name="edit_binder"),
    path('delete_binder/<int:id>/',delete_binder,name="delete_binder"),

    path('gather_ledger/',gather_ledger,name="gather_ledger"), 
    path('edit_gather_ledger/<int:id>/', edit_gather_ledger, name="edit_gather_ledger"),
    path('delete_gather_ledger/<int:id>/',delete_gather_ledger,name="delete_gather_ledger"),

    path('stitcher_ledger/',stitcher_ledger,name="stitcher_ledger"), 
    path('edit_stitcher_ledger/<int:id>/', edit_stitcher_ledger, name="edit_stitcher_ledger"),
    path('delete_stitcher_ledger/<int:id>/',delete_stitcher_ledger,name="delete_stitcher_ledger"),

    path('paster_ledger/',paster_ledger,name="paster_ledger"), 
    path('edit_paster_ledger/<int:id>/', edit_paster_ledger, name="edit_paster_ledger"),
    path('delete_paster_ledger/<int:id>/',delete_paster_ledger,name="delete_paster_ledger"),

    path('machine_ledger/',machine_ledger,name="machine_ledger"), 
    path('edit_machine_ledger/<int:id>/', edit_machine_ledger, name="edit_machine_ledger"),
    path('delete_machine_ledger/<int:id>/',delete_machine_ledger,name="delete_machine_ledger"),

    path('cutter_ledger/',cutter_ledger,name="cutter_ledger"), 
    path('edit_cutter_ledger/<int:id>/', edit_cutter_ledger, name="edit_cutter_ledger"),
    path('delete_cutter_ledger/<int:id>/',delete_cutter_ledger,name="delete_cutter_ledger"),

    path('packer_ledger/',packer_ledger,name="packer_ledger"), 
    path('edit_packer_ledger/<int:id>/', edit_packer_ledger, name="edit_packer_ledger"),
    path('delete_packer_ledger/<int:id>/',delete_packer_ledger,name="delete_packer_ledger"),

    path('general_ledger/',general_ledger,name="general_ledger"), 
    path('edit_general_ledger/<int:id>/', edit_general_ledger, name="edit_general_ledger"),
    path('delete_general_ledger/<int:id>/',delete_general_ledger,name="delete_general_ledger"),

    path('customer_ledger/',customer_ledger,name="customer_ledger"), 
    path('edit_customer_ledger/<int:id>/', edit_customer_ledger, name="edit_customer_ledger"),
    path('delete_customer_ledger/<int:id>/',delete_customer_ledger,name="delete_customer_ledger"),

    path('cover_scrap/',cover_scrap,name="cover_scrap"), 
    path('delete_cover_scrap_voucher/<int:id>/',delete_cover_scrap_voucher,name="delete_cover_scrap_voucher"),
    path('edit_cover_scrap_voucher/<int:id>/', edit_cover_scrap_voucher, name="edit_cover_scrap_voucher"),



    path('other_voucher/',other_voucher,name="other_voucher"), 
    path('edit_other_voucher/<int:id>/',edit_other_voucher,name="edit_other_voucher"),
    path('delete_other_voucher/<int:id>/', delete_other_voucher, name="delete_other_voucher"),
    # path('unit_conversion/', unit_conversion, name="unit_conversion"),





    path('product_group/',product_group,name="product_group"), 
    path('edit_product_group/<int:id>/', edit_product_group, name="edit_product_group"),
    path('delete_product_group/<int:id>/',delete_product_group,name="delete_product_group"),

    
    path('district/', district, name="district"),
    # path('edit_district/<int:id>/',edit_district,name="edit_district"),
    path('delete_district/<int:id>/', delete_district, name="delete_district"),

    path('by_product/', by_product, name="by_product"),
    path('delete_by_product/<int:id>/', delete_by_product, name="delete_by_product"),
    path('edit_by_product/<int:id>/', edit_by_product, name="edit_by_product"),

    path('categories/', categories, name="categories"),
    # path('edit_district/<int:id>/',edit_district,name="edit_district"),
    path('delete_categories/<int:id>/', delete_categories, name="delete_categories"),


    path('delete_form/<int:id>/',delete_form,name="delete_form"),
    path('form_printing/',form_printing,name="form_printing"), 
    path('edit_form_printing/<int:id>/', edit_form_printing, name="edit_form_printing"),

    path('unit_master/',unit_master,name="unit_master"),
    path('edit_unit_master/<int:id>/', edit_unit_master, name="edit_unit_master"),
    path('delete-unit_master/<int:id>/',delete_unit_master,name='delete_unit_master'),

    path('unit_conversion/',unit_conversion,name="unit_conversion"),
    path('edit-unit_conversion/<int:id>/', edit_unit_conversion, name="edit_unit_conversion"),
    path('delete-unit_conversion/<int:id>/',delete_unit_conversion,name='delete_unit_conversionr'),


    path('item_masters/',item_masters,name="item_masters"),
    path('delete_tehsil/<int:id>/', delete_tehsil, name="delete_tehsil"),

    path('Tehsil/', Tehsil, name="Tehsil"),
    path('tour_group/', tour_group, name="tour_group"),
    path('delete_tour_group/<int:id>/', delete_tour_group, name="delete_tour_group"),



    path('pending_printing/<int:id>/',pending_printing,name="pending_printing"),

    path('pending_gathering/<int:id>/',pending_gathering,name="pending_gathering"),

    path('pending_machine/<int:id>/',pending_machine,name="pending_machine"),

    path('pending_manual/<int:id>/',pending_manual,name="pending_manual"),

    path('pending_pasting/<int:id>/',pending_pasting,name="pending_pasting"),

    path('pending_cutting/<int:id>/',pending_cutting,name="pending_cutting"),
    
 

]