from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('reports-data/',reports_data,name="reports-data"),
    path('reports-view/<int:id>/',reports_view,name="reports-view"),
    path('forms_report/',forms_report,name="forms_report"),
    path('extra_form/',extra_form,name="extra_form"),
    
]