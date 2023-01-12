
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from app.models import Order, OrderItem
from django.contrib.auth.models import User

@login_required(login_url="loginpage")
def index(request):
    orders= Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request, "products/orders.html", context)

@login_required(login_url="loginpage")
def orderview(request, t_no):
    order= Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems=OrderItem.objects.filter(order=order)
    context={'order':order,'orderitems':orderitems}
    return render(request, 'products/order/view.html', context)
