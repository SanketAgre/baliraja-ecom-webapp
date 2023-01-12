
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from app.models import cart, Order, OrderItem,product,Profile
from django.contrib.auth.models import User
import random

@login_required(login_url="loginpage")
def index(request):
    rawcart=cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.Product.quantity:
            # return JsonResponse({'status': "Only "+ str(item.Product.quantity) + " quantity available"})
            return redirect("/cart")
    cartitems= cart.objects.filter(user=request.user)
    total_price= 0
    for item in cartitems:
        total_price= total_price + item.Product.selling_price * item.product_qty

    userprofile=Profile.objects.filter(user=request.user).first()

    context={'cartitems':cartitems, 'total_price':total_price, 'userprofile':userprofile }
    return render(request, 'products/checkout.html',context)


@login_required(login_url="loginpage")
def placeorder(request):
    if request.method == "POST":

        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name :
            currentuser.first_name =request.POST.get('fname')
            currentuser.last_name =request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile =Profile()
            userprofile.user=request.user
            userprofile.phone=request.POST.get('phone')
            userprofile.address=request.POST.get('address')
            userprofile.city=request.POST.get('city')
            userprofile.state=request.POST.get('state')
            userprofile.country=request.POST.get('country')
            userprofile.pincode=request.POST.get('pincode')    
            userprofile.save()


        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pincode=request.POST.get('pincode')

        neworder.payment_mode=request.POST.get('payment_mode')
        neworder.payment_id=request.POST.get('payment_id')

        Cart=cart.objects.filter(user=request.user)
        cart_total_price= 0
        for item in Cart:
            cart_total_price=cart_total_price + item.Product.selling_price * item.product_qty

        neworder.total_price = cart_total_price
        trackno= 'sharma'+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno)is None:
            trackno= 'sharma'+str(random.randint(1111111,9999999))
        
        neworder.tracking_no=trackno
        neworder.save()

        neworderitems=cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                Product=item.Product,
                price=item.Product.selling_price,
                quantity=item.product_qty

            )

            # to decrease the product quantity from available stock
            orderproduct= product.objects.filter(id=item.Product_id).first()
            orderproduct.quantity=orderproduct.quantity- item.product_qty
            orderproduct.save()

        #to clear user'cart
        cart.objects.filter(user=request.user).delete()

        payMode=request.POST.get('payment_mode')
        if (payMode== 'Paid by Razorpay'):
            return JsonResponse({'status':"Your Order has Been placed successfully"})
        else:
            messages.success(request, "Your Order has Been placed successfully")

    return redirect("/")



@login_required(login_url="loginpage")
def razorpaycheck(request):
    Cart=cart.objects.filter(user=request.user)
    total_price=0
    for item in Cart:
        total_price = total_price + item.Product.selling_price * item.product_qty
        return JsonResponse({
            'total_price':total_price
        })


def orders(request):
    return HttpResponse("my order page")