"""UserEmailLogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from testapp import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home_view),
    path('signup/', views.signup_view),
    path('', views.login_view, name="login"),
    path('dashboard/', views.student_view ,name='dashboard'),
    path('logout/', views.logout_view,name="logout"),
    path('forgotpass/', views.forgot_pass_view,name="forgot-password"),
    path('forgotsuccess/', views.forgotsuccess,name="forgot-success"),
    path('changepass/', views.PasswordsChangeView.as_view(template_name = 'testapp/changepass.html'),name="change-success"),

    path('profile/', views.UserEditView.as_view(),name="profile"),
    path('create_user/<str:user_roles>/',views.create_user,name="create_user"),
    path('role/',views.role,name="role"),

    path('generate_random_password',views.generate_random_password),
    path('dash_printing/',views.dash_printing,name="dash_printing"),
    path('user_resetpassword/',views.user_resetpassword,name="user_resetpassword"),
    path('user_pass/<int:id>/',views.user_pass,name="user_pass"),
    path('edit_user/<int:id>/',views.edit_user,name="edit_user"),
    path('delete_user/<int:id>/',views.delete_user,name="delete_user"),
    path('role_permission/',views.role_permission,name="role_permission"),
    path('role_permission_show/',views.role_permission_show,name="role_permission_show"),
    path('master_permission/<str:user_roles>/',views.master_permission,name="master_permission"),
    path('master_permission_show/',views.master_permission_show,name="master_permission_show"),
    path('',include('brand_app.urls')),
    path('',include('order_app.urls')),
    path('',include('processing.urls')),
    path('',include('report.urls')),
    path('',include('packing_app.urls')),
    path('',include('cover_app.urls')),
    
]
