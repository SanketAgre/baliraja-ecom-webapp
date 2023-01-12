from unicodedata import name
from django.contrib import admin
from django.urls import path
from app import views
from app.controller import authview, cart, wishlist,checkout, order
from app.models import Wishlist

urlpatterns = [
    path("",views.index, name="home"),

    path('aboutbaliraja', views.aboutbaliraja, name='aboutbaliraja'),

    path("collection",views.collection, name="collection"),
    path("collection/<str:slug>",views.collectionview, name="collectionview"),
    path("collectionview/<str:cata_slug>/<str:prod_slug>",views.productview, name="productview"),
    

    path("register", authview.register, name='register'),
    path("login", authview.loginpage, name="loginpage"),
    path("logout", authview.logoutpage, name="logout"),

    path("add-to-cart",cart.addtocart, name="addtocart"),
    path("cart", cart.viewcart, name='cart'),
    path("update-cart", cart.updatecart, name="updatecart"),
    path("delete-cart-item", cart.deletecartitem, name="deletecartitem"),

    path("wishlist", wishlist.index, name="wishlist"),
    path("add-to-wishlist", wishlist.addtowishlist, name="addtowishlist"),
    path("delete-wishlist-item", wishlist.deletewishlistitem, name="deletewishlistitem"),

    path("checkoutitem", checkout.index, name="checkout"),
    path("place-order",checkout.placeorder, name="placeorder"),
    path("proced-to-pay", checkout.razorpaycheck),

    path("my-orders", order.index, name="myorder"),
    path("view-order/<str:t_no>", order.orderview, name="orderview"),

]
