from django.urls import path
from WebApp import views

urlpatterns=[
    path('Home/',views.home_page,name="home_page"),
    path('Our_Products/',views.products,name="products"),
    path('shop_detail/',views.shop_detail,name="shop_detail"),
    path('filtered_items/<cat_name>',views.filtered_items,name="filtered_items"),
    path('single_item/<int:item_id>',views.single_item,name="single_item"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('',views.sign_in,name="sign_in"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('checkout/',views.checkout,name="checkout"),
    path('save_checkout/',views.save_checkout,name="save_checkout"),
    path('payment/',views.payment,name="payment"),

]