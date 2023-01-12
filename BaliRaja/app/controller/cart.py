from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from app.models import product, cart

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('Product_id'))
            product_check= product.objects.get(id=prod_id)
            if(product_check):
                if(cart.objects.filter(user=request.user.id, Product_id=prod_id)):
                    return JsonResponse({'status':"Product Already in cart"})
                else:
                    prod_qty =int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        cart.objects.create(user=request.user,Product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product Added Successfully"})
                    else:
                        return JsonResponse({'status': "Only "+ str(product_check.quantity) + " quantity available"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect("/")

@login_required(login_url="loginpage")
def viewcart(request):
    Cart= cart.objects.filter(user=request.user)
    context={'Cart':Cart}
    return render(request, "products/cart.html", context)

def updatecart(request):
    if request.method == "POST":
        prod_id=int(request.POST.get('Product_id'))
        if(cart.objects.filter(user=request.user, Product_id=prod_id)):
            prod_qty=int(request.POST.get("product_qty"))
            Cart = cart.objects.get(Product_id=prod_id, user=request.user)
            Cart.product_qty=prod_qty
            Cart.save()
            return JsonResponse({'status':"Update Successfully"})
    return redirect("/")



def deletecartitem(request):
    if request.method == "POST":
        prod_id=int(request.POST.get('Product_id'))
        if(cart.objects.filter(user=request.user, Product_id=prod_id)):
            cartitem=cart.objects.filter(Product_id=prod_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status':"Deleted Successfully"})
    return redirect("/")
