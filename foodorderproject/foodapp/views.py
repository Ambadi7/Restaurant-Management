from django.shortcuts import render
from django.shortcuts import redirect,HttpResponse
from.models import Customer
from.models import Resturant_staff
from.models import Customers_complaint
from.models import fooditem 
from.models import admin_data
from.models import cart
from.models import CompletedOrder 
from.models import OngoingOrder 
from.models import Order 
from.models import Order 
from.models import pay 

import razorpay
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


# Create your views here.

#Customer_index page
def Customer_index(request):
    return render(request,'Customer_index.html')
#restaurant_index page
def restaurant_index(request):
    return render(request,'Restaurant_index.html')
def layout(request):
    return render(request,'Customer_layout.html')

#Customer_home page
def Customer_home(request):
    return render(request,'Customer_home.html')
    
#Customer registration
def cregister(request):
    if request.method=="POST" :
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        mobileNumber = request.POST.get('mobileNumber') 
        username = request.POST.get('username')
        password = request.POST.get('password')
        Customer(c_name=name,c_age=age,c_email=email,c_mobileNumber=mobileNumber,c_username=username,c_password=password).save()
        return redirect('Customer_index')
    else:
        return render(request,'Cregister.html')


# Resturant registration
def rregister(request):
    return render(request,'Rregister.html')


#Customer login
def clogin(request):
    if request.method=='POST':

        uname = request.POST.get('username')
        pswd = request.POST.get('password')

        key = Customer.objects.filter(c_username=uname,c_password=pswd)
        if key:
            userd = Customer.objects.get(c_username=uname,c_password=pswd)
            id=userd.id
            name=userd.c_username
            pswd=userd.c_password
            request.session['id']=id
            request.session['uname']=uname
            request.session['pswd']=pswd

            return redirect('Customer_home')

        else:
            return render(request,'Customer_index.html')

    else:
        return render(request,'Customer_index.html')



#printing data from models
def Customer_list(request):
    Customers = Customer.objects.all()
    return render(request, 'Customers_list.html',{'Customers': Customers})

#deleting data from models
def Customer_delete(request,id):
    Customers = Customer.objects.get(id=id)
    Customers.delete()
    return render(request,'Customers_list.html')

#deleting data from models by name
def Customer_deleteByName(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        Customers = Customer.objects.get(c_username=uname)
        Customers.delete()
        return render(request,'Customers_list.html')
    else:
        return render(request,'Customer_deleteByName.html')

# compliant registrations
# def Customer_complaint(request):
#     if request.method=="POST" :
#         name = request.POST.get('name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         complaint = request.POST.get('complaint')
#         Customers_complaint(c_name=name,c_username=username,c_email=email,c_complaint=complaint).save()
#         return redirect('Customer_home')
#     else:
#         return render(request,'Customer_home')


#list image
def Customer_home(request):
    cr=fooditem.objects.all()
    return render(request,'Customer_home.html',{'fooditems':cr})

#profile
def profile(request):
    uname=request.session['uname']
    data=Customer.objects.get(c_username=uname)
    c_name=data.c_name
    c_age=data.c_age
    c_email=data.c_email
    c_mobileNumber=data.c_mobileNumber
    c_username=data.c_username
    c_password=data.c_password




    return render(request,'Customer_profile.html',{'c_name':c_name,'uname':uname,'c_age':c_age,'c_email':c_email,'c_mobileNumber':c_mobileNumber,'c_username':c_username,'c_password':c_password})

#profileupdate
def profileupdate(request):
    if request.method=="POST":
        uname=request.session['uname']
        c_name = request.POST.get('name')
        c_age = request.POST.get('age')
        c_mobileNumber = request.POST.get('mobileNumber') 
        c_password = request.POST.get('password')
        c_email = request.POST.get('email')
        data=Customer.objects.get(c_username=uname)
        data.c_name=c_name
        data.c_age=c_age
        data.c_email=c_email
        data.c_mobileNumber=c_mobileNumber
        data.c_password=c_password
        data.save()
        return render(request,'Customer_profile.html',{'c_name':c_name,'c_email':c_email,'c_age':c_age,'c_mobileNumber':c_mobileNumber,'uname':uname,'c_password':c_password})
    else:
        return render(request,'Customer_profile.html')



def admin_index(request):
    return render(request,'admin_index.html')

#admin regstration
def adminreg(request):
    if request.method=="POST" :
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin_data(a_username=username,a_name=name,a_email=email,a_password=password).save()
        return redirect('admin_index')
    else:
        return render(request,'Cregister.html')


#admin login
def adminlogin(request):
    if request.method=='POST':

        uname = request.POST.get('username')
        pswd = request.POST.get('password')

        key = admin_data.objects.filter(a_username=uname,a_password=pswd)
        if key:
            userd = admin_data.objects.get(a_username=uname,a_password=pswd)
            id=userd.id
            name=userd.a_username
            pswd=userd.a_password
            request.session['id']=id
            request.session['uname']=uname
            request.session['pswd']=pswd

            return redirect('admin_order_manage')

        else:
            return render(request,'admin_index.html')

    else:
        return render(request,'admin_index.html')
    
def admin_home(request):
    return render(request,'admin_home.html')

def Restaurant_index(request):
    return render(request,'Restaurant_index.html')

def Restaurant_home(request):
    return render(request,'Restaurant_home.html')

#Restaurant regstration
def Restaurantreg(request):
    if request.method=='POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        mobileNumber = request.POST.get('mobileNumber') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        Resturant_staff(rs_username=username,rs_name=name,rs_mobileNumber=mobileNumber,rs_email=email,rs_password=password).save()
        return redirect('Restaurant_index')
    else:
        return redirect('Restaurant_index')

#Restarunt login
def Restaurantlogin(request):
    if request.method=='POST':

        uname = request.POST.get('username')
        pswd = request.POST.get('password')

        key = Resturant_staff.objects.filter(rs_username=uname,rs_password=pswd)
        if key:
            userd = Resturant_staff.objects.get(rs_username=uname,rs_password=pswd)
            id=userd.id
            name=userd.rs_username
            pswd=userd.rs_password
            request.session['id']=id
            request.session['uname']=uname
            request.session['pswd']=pswd

            return redirect('Restaurant_home')

        else:
             return redirect('Restaurant_index')

    else:
         return redirect('Restaurant_index')


#customer complaint
def Customer_complaint(request):
    uname=request.session['uname']
    data=Customer.objects.get(c_username=uname)
    c_name=data.c_name
    c_email=data.c_email
    c_username=data.c_username
    
    return render(request,'Customer_complaint.html',{'c_name':c_name,'uname':uname,'c_email':c_email,})
    
#customer complaint send
def Customer_complaint_submit(request):
    if request.method=="POST" :
        uname=request.session['uname']
        complaint = request.POST.get('complaint')

        data=Customer.objects.get(c_username=uname)
        name = data.c_name
        email = data.c_email
        Customers_complaint(c_username=uname,c_name=name,c_email=email,c_complaint=complaint).save()
        print("complaint send")
        return redirect('Customer_complaint')
    else:
        return redirect('Customer_orders')

#customer orders
def Customer_orders(request):
    
    return render(request,'Customer_orders.html')

#customer logout
def Customer_logout(request):
    return redirect('Customer_index')


#Add to cart
# def addcart(request):
#     if request.method=="POST" :
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         quantity = request.POST.get('quantity')
#         image = request.POST.get('image')
#         uname = request.session['uname']
#         data = Customer.objects.get(c_username=uname)

#         username = data.c_username
#         email = data.c_email
#         Cart().save
#         return redirect('Customer_home')
#     else:
#         return render(request,'Customer_addcart.html')

#Add to cart
def Customer_addcart(request):
    if request.method =='POST':
        product = request.POST.get('name')
        quantity = int(request.POST.get('quantity'))
        try:
            data = fooditem.objects.get(food_name=product)
            a = data.quantity
            image = data.image
            price = data.price
            b = int(a)
            newquantity = b - quantity
            total_price = price * quantity

            if newquantity < 0:
                return render(request, 'Rregister.html')
            
            c = request.session['uname']
            cr = Customer.objects.get(c_username=c)
            name = cr.c_name
            email = cr.c_email
            phno = cr.c_mobileNumber
            username= cr.c_username
           

            data.quantity = newquantity
            data.save()

            cart(product=product, image=image,  total_price=total_price, quantity=quantity, username=username, userEmail=email,).save()

            return render(request, 'Customer_home.html')
        except fooditem.DoesNotExist:
            return render(request, 'Rregister.html')
    else:
        return render(request, 'Customer_cartForm.html')
    # if request.method == 'POST':
    #     product = get_object_or_404(fooditem,id=product_id)
    #     print(product)
    #     quantity = int(request.POST.get('quantity',1))
    #     total_price = product.price * quantity

    #     cart_item, created = Cart.objects.get_or_create(product=product)

    #     if not created:
    #         cart_item.quantity = quantity
    #         cart_item.total_price = total_price
    #         cart_item.save()
    #     else:
    #         cart_item.quantity = quantity
    #         cart_item.total_price = total_price
    #         cart_item.save()
    #         return redirect('Customer_home')
    # return redirect('Customer_home')


#Customer addform
def addcart_form(request,id):
    uname=request.session['uname']
    dt=fooditem.objects.get(id=id)
    a = dt.image
    b = dt.food_name
    c = dt.description
    e = dt.price
    f = dt.quantity
    return render(request,"Customer_cartForm.html",{ 'a':a,'b': b, 'c':c, 'e': e, 'f': f, 'g': uname})

    
#customer cartlist
from django.contrib.auth.decorators import login_required

@login_required
def Customer_cart(request):
    uname = request.session.get('uname')
    if uname:
        # Assuming your cart model has a field named 'username' to store the username of the user who added the item to the cart
        cr = cart.objects.filter(username=uname)
        return render(request, 'Customer_cart.html', {'carts': cr})
    else:
        # Handle the case when the user is not logged in
        # You might want to redirect the user to the login page or show an error message
        return HttpResponse("You need to be logged in to view your cart.")


def Customer_cartdelete(request,id):
    data=cart.objects.get(id=id)
    a=data.quantity
    c=data.product
    b=int(a)
    data1=fooditem.objects.get(food_name=c)
    d=int(data1.quantity)
    e=int(d+b)
    data1.quantity=e
    data1.save()
    data.delete()
    return redirect('Customer_cart')

    
#customer about
def Customer_about(request):
    return render(request,'Customer_about.html')
    
#admin_complaints View
def admin_complaintView(request):
    cr=Customers_complaint.objects.all()
    return render(request,'admin_complaintView.html',{'complaints':cr})

#admin restaurant staff manageing
def admin_staff_manage(request):
    cr=Resturant_staff.objects.all()
    return render(request,'admin_Staff.html',{'r_staff':cr})

#admin restaurant staff manageing
def admin_customer_manage(request):
    cr=Customer.objects.all()
    return render(request,'admin_customer.html',{'cstmr':cr})

#admin fooditems manageing
def admin_fooditem_manage(request):
    cr=fooditem.objects.all()
    return render(request,'admin_fooditems.html',{'fooditems':cr})

#admin orders manageing
def admin_order_manage(request):
    data_completed=CompletedOrder.objects.all()
    data_pending=OngoingOrder.objects.all()
    return render(request,'admin_orders.html',{'o_orders':data_pending ,'c_orders':data_completed})

#admin profile view
def adminprofile(request):
    uname=request.session['uname']
    data=admin_data.objects.get(a_username=uname)
    a_name=data.a_name
    a_email=data.a_email
    a_username=data.a_username
    a_password=data.a_password




    return render(request,'admin_profile.html',{'a_name':a_name,'uname':uname,'a_email':a_email,'a_username':a_username,'a_password':a_password})

#admin profile update
def adminprofileupdate(request):
    if request.method=="POST":
        uname=request.session['uname']
        a_name = request.POST.get('name') 
        a_password = request.POST.get('password')
        a_email = request.POST.get('email')
        data=admin_data.objects.get(a_username=uname)
        data.a_name=a_name
        data.a_email=a_email
        data.a_password=a_password
        data.save()
        return render(request,'admin_profile.html',{'a_name':a_name,'a_email':a_email,'uname':uname,'a_password':a_password})
    else:
        return render(request,'admin_profile.html')

#admin delete staff
def adminstaff_delete(request,id):
    data=Resturant_staff.objects.get(id=id)
    data.delete()
    return redirect('admin_staff_manage')

def adminfood_delete(request,id):
    data=fooditem.objects.get(id=id)
    data.delete()
    return redirect('admin_fooditem_manage')

#admin food add view
def admin_foodadd(request):
    return render(request,'admin_foodadd.html')

def addproducts(request):
    if request.method=='POST':
        
         name=request.POST.get('name')
         description=request.POST.get('description')
         price=request.POST.get('price')
         quantity=request.POST.get('quantity')
         image=request.FILES['image']
         category=request.POST.get('category')
         fooditem(food_name=name,description=description,category=category,price=price,quantity=quantity,image=image).save()
         return redirect('admin_fooditem_manage')
    else:
        return render(request,'admin_foodadd.html')

def adminfood_edit(request,id):
    uname=request.session['uname']
    dt=fooditem.objects.get(id=id)
    a = dt.image
    b = dt.food_name
    c = dt.description
    e = dt.price
    f = dt.quantity
    h = dt.category
    return render(request,"admin_foodedit.html",{ 'a':a,'b': b, 'c':c, 'e': e, 'f': f,'h':h,'id':id , 'g': uname})

def editproducts(request,id):
    if request.method=="POST":
        uname=request.session['uname']
        b = request.POST.get('name') 
        c = request.POST.get('description')
        e = request.POST.get('price')
        h = request.POST.get('category')
        f = request.POST.get('quantity')
        data=fooditem.objects.get(id=id)
        data.food_name=b
        data.description= c
        data.category=h
        data.quantity=f
        data.price=e
        data.save()
        return render(request,'admin_foodedit.html',{'b': b, 'c':c, 'e': e, 'f': f,'h':h})
    else:
        return render(request,'admin_foodedit.html')




#home restaurant
def Restaurant_home(request):
    data_completed=CompletedOrder.objects.all()
    data_pending=OngoingOrder.objects.all()
    return render(request,'Restaurant_home.html',{'o_orders':data_pending ,'c_orders':data_completed})
    
def res_fooditem_manage(request):
    cr=fooditem.objects.all()
    return render(request,'Restaurant_fooditem.html',{'fooditems':cr})

def res_profile(request):
    uname=request.session['uname']
    data=Resturant_staff.objects.get(rs_username=uname)
    rs_name=data.rs_name
    rs_email=data.rs_email
    rs_username=data.rs_username
    rs_password=data.rs_password
    rs_mobileNumber=data.rs_mobileNumber




    return render(request,'Restaurant_profile.html',{'rs_name':rs_name,'uname':uname,'rs_email':rs_email,'rs_username':rs_username,'rs_password':rs_password ,'rs_mobileNumber':rs_mobileNumber})

def res_profileupdate(request):
    if request.method=="POST":
        uname=request.session['uname']
        rs_name = request.POST.get('name') 
        rs_password = request.POST.get('password')
        rs_email = request.POST.get('email')
        rs_mobileNumber = request.POST.get('mobileNumber')
        data=Resturant_staff.objects.get(rs_username=uname)
        data.rs_name=rs_name
        data.rs_email=rs_email
        data.rs_password=rs_password
        data.rs_mobileNumber=rs_mobileNumber
        data.save()
        return render(request,'Restaurant_profile.html',{'rs_name':rs_name,'rs_email':rs_email,'uname':uname,'rs_password':rs_password,'rs_mobileNumber':rs_mobileNumber})
    else:
        return render(request,'Restaurant_profile.html')

def resfood_edit(request,id):
    uname=request.session['uname']
    dt=fooditem.objects.get(id=id)
    a = dt.image
    b = dt.food_name
    c = dt.description
    e = dt.price
    f = dt.quantity
    h = dt.category
    return render(request,"Restaurant_foodedit.html",{ 'a':a,'b': b, 'c':c, 'e': e, 'f': f,'h':h,'id':id , 'g': uname})

def reseditproducts(request,id):
    if request.method=="POST":
        uname=request.session['uname']
        b = request.POST.get('name') 
        c = request.POST.get('description')
        e = request.POST.get('price')
        h = request.POST.get('category')
        f = request.POST.get('quantity')
        data=fooditem.objects.get(id=id)
        data.food_name=b
        data.description= c
        data.category=h
        data.quantity=f
        data.price=e
        data.save()
        return render(request,'Restaurant_foodedit.html',{'b': b, 'c':c, 'e': e, 'f': f,'h':h})
    else:
        return render(request,'Restaurant_foodedit.html')

def res_complete(request,id):
    data_delete = OngoingOrder.objects.get(id=id)
    username = data_delete.username
    food_name = data_delete.food_name
    status = data_delete.status
    category = data_delete.category
    quantity = data_delete.quantity
    price = data_delete.price
    CompletedOrder(username=username,food_name=food_name,status=status,category=category,price=price,quantity=quantity).save()
    data_delete.delete()
    return redirect('Restaurant_home')









def payment(request):
    username = request.session.get('uname')
    if username:
        cr = cart.objects.filter(username=username)
        total_price = sum(int(item.total_price) for item in cr)
        total_price *= 100  # Converting to paisa (assuming the price is in INR)

        amount = total_price
        currency = 'INR'
        razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
        razorpay_order_id = razorpay_order['id']
        callback_url = '/paymenthandler/'

        context = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_merchant_key': settings.RAZOR_KEY_ID,
            'razorpay_amount': amount,
            'currency': currency,
            'callback_url': callback_url
        }
        return render(request, 'payment.html', context=context)
    else:
        return HttpResponseBadRequest("User email not found in session")

@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result:
                # Capture the payment amount
                amount = result.get('amount')
                try:
                    razorpay_client.payment.capture(payment_id, amount)
                    return render(request, 'pay_success.html')
                except Exception as e:
                    print(e)  # Log the error
                    return render(request, 'pay_failed.html')
            else:
                return render(request, 'pay_failed.html')
        except Exception as e:
            print(e)  # Log the error
            return HttpResponseBadRequest("Invalid request")
    else:
        return HttpResponseBadRequest("Invalid request")
    