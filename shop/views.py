from django.shortcuts import render,redirect
from shop.forms import BrandCreateForm,MobileCreationForm
from .models import Brands,Mobile,Order,Cart
from django.contrib.auth.models import User
from .forms import UserRegForm,OrderForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

# Create your views here.
def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect('errorpage')
        else:
            return func(request)
    return wrapper
def admin_permission_required_id(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect('errorpage')
        else:
            return func(request,id)
    return wrapper
def errorpage(request):
    return render(request,'shop/errorpage.html')

def brand_view(request):
    form=BrandCreateForm()
    context={}
    context['form']=form
    brands=Brands.objects.all()
    context['brands']=brands
    if request.method=='POST':
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('brandview')
    return render(request,'shop/brandcreate.html',context)

@admin_permission_required_id
def brand_edit(request,id):
    brand=Brands.objects.get(id=id)
    form=BrandCreateForm(instance=brand)
    context={}
    context['form']=form
    if request.method=='POST':
        form=BrandCreateForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brandview')
    return render(request, 'shop/brandedit.html', context)

@admin_permission_required_id
def brand_delete(request,id):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect('brandview')
@admin_permission_required
def create_mobile(request):
    form=MobileCreationForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=MobileCreationForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print('save')
            return redirect('createmobile')

    return render(request,'shop/mobilecreate.html',context)

def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context['mobiles']=mobiles

    return render(request,'shop/listmobiles.html',context)

def mobile_details(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context['mobile']=mobile
    return render(request,'shop/mobiledtail.html',context)

def user_registration(request):
    form=UserRegForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
        else:
            form=UserRegForm(request.POST)
            context['form']=form
            return render(request, 'shop/userreg.html', context)

    return render(request,'shop/userreg.html',context)

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('listmobiles')
        else:
            return render(request, 'shop/login.html')


    return render(request,'shop/login.html')

def user_logout(request):
    logout(request)
    return redirect('userlogin')

def order(request,id):
    product=Mobile.objects.get(id=id)
    form=OrderForm(initial={'user':request.user,'product':product})
    context={}
    context['form']=form
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('orderview')
        else:
            form=OrderForm(request.POST)
            context['form']=form
            return render(request, 'shop/order.html', context)
    return render(request,'shop/order.html',context)

def order_view(request):
    username=request.user
    products=Order.objects.all().filter(user=username)
    context={}
    context['products']=products
    return render(request,'shop/orderlist.html',context)
def add_to_order(request,id):
    user=request.user
    mobile=Mobile.objects.get(id=id).filter(user=request.user)
    context={}
    context['mobile']=mobile
    return render(request,'shop/success.html',context)

def order_delete(request,id):
    order=Order.objects.get(id=id)
    order.delete()
    return redirect('orderview')

def add_to_cart(request,id):
    user=request.user
    mobile=Mobile.objects.get(id=id)
    print(type(mobile))
    print(mobile.mobile_name)
    cart=Cart(user=user,product=mobile,price=mobile.price)
    cart.save()
    return redirect('cartview')

def cart_view(request):
    username=request.user
    carts=Cart.objects.all().filter(user=username)
    context={}
    context['carts']=carts
    return render(request,'shop/cart.html',context)

def cart_delete(request,id):
    cart=Cart.objects.get(id=id)
    cart.delete()
    return redirect('cartview')

def product_details(request,id):
    item=Order.objects.get(id=id)
    context={}
    context['item']=item
    return render(request,'shop/productdetail.html',context)


