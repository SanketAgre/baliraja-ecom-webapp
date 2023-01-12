from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Wishlist,product

@login_required(login_url="loginpage")
def index(request):
    wishlist=Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlist}
    return render(request,"products/wishlist.html", context)


def addtowishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("Product_id"))
            product_check =product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, Product_id=prod_id)):
                    return JsonResponse({'status': "Product Already In Wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, Product_id=prod_id)
                    return JsonResponse({'status': "Product Add In Wishlist"})
            else:
                return JsonResponse({'status': " No Such Product Found"})
        else:
                return JsonResponse({'status': " Login To Continue"})
    return redirect("/")

def deletewishlistitem(request):
        if request.method == "POST":
            if request.user.is_authenticated:
                prod_id = int(request.POST.get("Product_id"))
               
                if(Wishlist.objects.filter(user=request.user, Product_id=prod_id)):
                    wishlistitem=Wishlist.objects.get(Product_id=prod_id)
                    wishlistitem.delete()
                    return JsonResponse({'status': "Product Removed from Wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, Product_id=prod_id)
                    return JsonResponse({'status': "Product not found in Wishlist"})
            else:
                return JsonResponse({'status': " Login To Continue"})
        return redirect("/")



