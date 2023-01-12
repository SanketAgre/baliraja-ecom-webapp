

from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponse
from app.models import product,category
from .models import *

# Create your views here.
def aboutbaliraja(request):
    return render(request, 'abouts/aboutbaliraja.html')

def index(request):
    trendin_product = product.objects.filter(trending=1)
    trending_category=category.objects.filter(trending=1)
    best_deal=product.objects.filter(best_deal=1)
    vegitables=product.objects.filter(vegitables=1)
    fruits=product.objects.filter(fruits=1)
    harbs=product.objects.filter(harbs=1)
    dry_fruits=product.objects.filter(dry_fruits=1)
    dal=product.objects.filter(dal=1)
    masale=product.objects.filter(masale=1)
    farming_Tools=product.objects.filter(farming_Tools=1)
    fertilizer=product.objects.filter(fertilizer=1)
    insecticides=product.objects.filter(insecticides=1)
    other_farming_Tools=product.objects.filter(other_farming_Tools=1)
    
    context={'trendin_product':trendin_product, 'trending_category':trending_category, 'best_deal':best_deal,'vegitables':vegitables,'fruits':fruits,'harbs':harbs, 'dry_fruits':dry_fruits, 'dal':dal, 'masale':masale, 'farming_Tools':farming_Tools, 'fertilizer':fertilizer, 'insecticides':insecticides,'other_farming_Tools':other_farming_Tools}
    return render(request, 'index.html', context)

def collection(request):
    Category=category.objects.filter(status=0)
    context={'Category':Category}
    return render(request,'products/collection.html', context)
    # return render(request,'product/collection.html')

def collectionview(request, slug):
    if(category.objects.filter(slug=slug, status=0)):
        products=product.objects.filter(category__slug=slug)
        catagory=category.objects.filter(slug=slug).first()
        context={'products':products, 'catagory':catagory}
        return render(request, "products/product.html", context)
    else:
        messages.warning(request,'no such catagory found')
        return redirect('collection')

def productview(request, cata_slug, prod_slug):
    if(category.objects.filter(slug=cata_slug, status=0)):
        if(product.objects.filter(slug=prod_slug, status=0)):
                products=product.objects.filter(slug=prod_slug, status=0).first()
                context={'products':products}
        else:
            messages.error("no such products found")
            return redirect('collection')
    else:
        messages.error("no such category found")
        return redirect('collection')
    return render(request, "products/view.html", context)





