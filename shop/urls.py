"""MobileApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import render
from .views import brand_view,brand_edit,brand_delete,create_mobile,\
    list_mobiles,mobile_details,user_registration,user_login,user_logout,\
    order,errorpage,order_view,add_to_order,order_delete,add_to_cart,cart_view,cart_delete,product_details

urlpatterns = [
    path('',lambda request:render(request,'shop/index.html')),
    path('brands',brand_view,name='brandview'),
    path('brands/edit/<int:id>',brand_edit,name='brandedit'),
    path('brands/delete/<int:id>',brand_delete,name='branddelete'),
    path('mobiles',create_mobile,name='createmobile'),
    path('mobiles/list',list_mobiles,name='listmobiles'),
    path('mobiles/detail/<int:id>',mobile_details,name='detail'),
    path('mobiles/userRegistration',user_registration,name='register'),
    path('mobile/userlogin',user_login,name='userlogin'),
    path('mobile/userlogout',user_logout,name='userlogout'),
    path('mobile/order/<int:id>',order,name='order'),
    path('errorpage',errorpage,name='errorpage'),
    path('orderview',order_view,name='orderview'),
    path('addtoorder/<int:id>',add_to_order,name='addtoorder'),
    path('deleteorder/<int:id>',order_delete,name='orderdelete'),
    path('addtocart/<int:id>',add_to_cart,name='addtocart'),
    path('cartview',cart_view,name='cartview'),
    path('cartdelete/<int:id>',cart_delete,name='cartdelete'),
    path('productdetails/<int:id>',product_details,name='productdetails')
]
