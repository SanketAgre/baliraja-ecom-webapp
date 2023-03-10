from distutils import text_file
from email import message
from django.db import models
import datetime
import os
from django.contrib.auth.models import User
from django.forms import CharField


from requests import request

# Create your models here.

def get_file_path(request,filename):
    original_filename=filename
    nowtime=datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename="%s%s"%(nowtime, original_filename)
    return os.path.join('uploads/',filename)


class category(models.Model):
    slug= models.CharField(max_length=191, null=False, blank=False)
    name= models.CharField(max_length=191, null=False, blank=False)
    image=models.ImageField(upload_to=get_file_path,null=False, blank=False )
    desc= models.TextField(max_length=500, null=False, blank=False )
    status=models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title=models.CharField(max_length=191, null=False, blank=False)
    meta_keywords=models.CharField(max_length=191, null=False, blank=False)
    meta_desc= models.TextField(max_length=500, null=False, blank=False )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class product(models.Model):
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    slug= models.CharField(max_length=191, null=False, blank=False)
    name= models.CharField(max_length=191, null=False, blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=False, blank=False )
    small_desc= models.TextField(max_length=250, null=True, blank=False )
    quantity=models.IntegerField(null=False, blank=False)
    qty_prod= models.CharField(max_length=191, null=True, blank=True)
    title_qty= models.CharField(max_length=191, null=True, blank=True)
    product_desc= models.TextField(max_length=500, null=False, blank=False )
    original_price=models.FloatField(null=False, blank=False)
    selling_price=models.FloatField(null=False, blank=False)

    status=models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False, help_text="0=default, 1=Trending")
    best_deal=models.BooleanField(default=False, help_text="0=default, 1=Best_deal")
    vegitables=models.BooleanField(default=False, help_text="0=default, 1=Vegitables")
    fruits=models.BooleanField(default=False, help_text="0=default, 1=Fruits")
    harbs=models.BooleanField(default=False, help_text="0=default, 1=Harbs")
    dry_fruits=models.BooleanField(default=False, help_text="0=default, 1=Dry_fruits")
    dal=models.BooleanField(default=False, help_text="0=default, 1=Dal")
    masale=models.BooleanField(default=False, help_text="0=default, 1=Masale")
    farming_Tools=models.BooleanField(default=False, help_text="0=default, 1=Farming_Tools")
    fertilizer=models.BooleanField(default=False, help_text="0=default, 1=Fertilizer")
    insecticides=models.BooleanField(default=False, help_text="0=default, 1=Insecticides")
    other_farming_Tools=models.BooleanField(default=False, help_text="0=default, 1=Other_farming_Tools")


    tag=models.CharField(max_length=150, null=True, blank=False )
    meta_title=models.CharField(max_length=191, null=False, blank=False)
    meta_keywords=models.CharField(max_length=191, null=False, blank=False)
    meta_desc= models.TextField(max_length=500, null=False, blank=False )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class sliderimg(models.Model):
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    slug= models.CharField(max_length=191, null=False, blank=False)
    name= models.CharField(max_length=191, null=False, blank=False)
    image=models.ImageField(upload_to=get_file_path,null=False, blank=False )
    desc=models.TextField(max_length=500, null=False, blank=False )
    small_desc= models.TextField(max_length=250, null=True, blank=False )
    status=models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False, help_text="0=default, 1=Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Product=models.ForeignKey(product, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product.name


class Wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Product=models.ForeignKey(product, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    fname= models.CharField(max_length=150, null=False)
    lname= models.CharField(max_length=150, null=False)
    email= models.CharField(max_length=150, null=False)
    phone= models.CharField(max_length=150, null=False)
    address= models.TextField(null=False)
    city= models.CharField(max_length=150, null=False)
    state= models.CharField(max_length=150, null=False)
    country= models.CharField(max_length=150, null=False)
    pincode= models.CharField(max_length=150, null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150, null=False)
    payment_id=models.CharField(max_length=250, null=True, blank=True)
    orderstatus=(
        ('pending','pending'),
        ('out for shipping','out for shipping' ),
        ('completed','completed')
    )
    status= models.CharField(max_length=150, choices=orderstatus, default='pending')
    message= models.TextField(null=True, blank=True)
    tracking_no=models.CharField(max_length=150, null=True)
    created_at=models.DateTimeField( auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True) 

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    Product=models.ForeignKey(product, on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)  
    phone= models.CharField(max_length=150, null=False)
    address= models.TextField(null=False)
    city= models.CharField(max_length=150, null=False)
    state= models.CharField(max_length=150, null=False)
    country= models.CharField(max_length=150, null=False)
    pincode= models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.user.username


