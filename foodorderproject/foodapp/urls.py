"""foodorderproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.Customer_index,name="Customer_index"),
    path('restaurant_index',views.restaurant_index,name="restaurant_index"),
    path('Customer_layout',views.layout,name="layout"),
    path('cregister/',views.cregister,name="cregister"),
    path('Customer_home',views.Customer_home,name="Customer_home"),
    path('rregister',views.rregister,name="rregister"),
    path('clogin/',views.clogin,name="clogin"),
    path('Customer_list',views.Customer_list,name="Customer_list"),
    path('Customer_delete/<int:id>',views.Customer_delete,name="Customer_delete"),
    path('Customer_deleteByName/',views.Customer_deleteByName,name="Customer_deleteByName"),
    path('Customer_complaint/',views.Customer_complaint,name="Customer_complaint"),
    path('Customer_complaint_submit/',views.Customer_complaint_submit,name="Customer_complaint_submit"),
    path('Customer_orders',views.Customer_orders,name="Customer_orders"),
    path('Customer_logout',views.Customer_logout,name="Customer_logout"),
    path('Customer_cart',views.Customer_cart,name="Customer_cart"),
    path('Customer_addcart/',views.Customer_addcart,name="Customer_addcart"),
    path('addcart_form/<int:id>/',views.addcart_form,name="addcart_form"),
    path('Customer_cartdelete/<int:id>/',views.Customer_cartdelete,name="Customer_cartdelete"),
    path('Customer_about',views.Customer_about,name="Customer_about"),
    #path('listdata/',views.listdata,name='listdata'),
    path('profile/',views.profile,name='profile'),
    path('profileupdate/',views.profileupdate,name='profileupdate'),
    path('admin_index',views.admin_index,name="admin_index"),
    path('adminreg/',views.adminreg,name="adminreg"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('admin_complaintView',views.admin_complaintView,name="admin_complaintView"),
    path('admin_staff_manage',views.admin_staff_manage,name="admin_staff_manage"),
    path('admin_customer_manage',views.admin_customer_manage,name="admin_customer_manage"),
    path('admin_fooditem_manage',views.admin_fooditem_manage,name="admin_fooditem_manage"),
    path('admin_order_manage',views.admin_order_manage,name="admin_order_manage"),
    path('adminprofile',views.adminprofile,name="adminprofile"),
    path('adminprofileupdate/',views.adminprofileupdate,name="adminprofileupdate"),
    path('adminstaff_delete/<int:id>',views.adminstaff_delete,name="adminstaff_delete"),
    path('adminfood_delete/<int:id>',views.adminfood_delete,name="adminfood_delete"),
    path('admin_foodadd',views.admin_foodadd,name="admin_foodadd"),
    path('addproducts/',views.addproducts,name="addproducts"),
    path('adminfood_edit/<int:id>',views.adminfood_edit,name="adminfood_edit"),
    path('editproducts/<int:id>',views.editproducts,name="editproducts"),

    path('Restaurantlogin/',views.Restaurantlogin,name="Restaurantlogin"),
    path('Restaurantreg/',views.Restaurantreg,name="Restaurantreg"),
    path('Restaurant_index/',views.Restaurant_index,name="Restaurant_index"),
    path('Restaurant_home',views.Restaurant_home,name="Restaurant_home"),
    path('res_fooditem_manage',views.res_fooditem_manage,name="res_fooditem_manage"),
    path('res_profileupdate/',views.res_profileupdate,name="res_profileupdate"),
    path('res_profile',views.res_profile,name="res_profile"),
    path('resfood_edit/<int:id>',views.resfood_edit,name="resfood_edit"),
    path('reseditproducts/<int:id>',views.reseditproducts,name="reseditproducts"),
    path('res_complete/<int:id>',views.res_complete,name="res_complete"),
    path('payment/',views.payment,name="payment"),
    path('paymenthandler/',views.paymenthandler,name="paymenthandler"),

    
    



    

]

