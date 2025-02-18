from django.shortcuts import render,redirect
from AdminAPP.models import CategoryDb, ProductDb
from WebApp.models import ContactDb, SignUpDb, CartDb,CheckoutDb
from django.contrib import messages
import razorpay


# Create your views here.
def home_page(request):
    categories=CategoryDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['Username'])
    x = cart_count.count()
    return render(request,"Home.html",{'categories':categories,'x':x})

def products(request):
    products=ProductDb.objects.all()
    categories = CategoryDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['Username'])
    x = cart_count.count()
    return render(request,"Products.html",{'products':products,'categories':categories,'x':x})

def shop_detail(request):
    categories = CategoryDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['Username'])
    x = cart_count.count()
    return render(request,"Shop_Detail.html",{'categories':categories,'x':x})

def filtered_items(request,cat_name):
    data=ProductDb.objects.filter(Category_Name=cat_name)
    categories = CategoryDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['Username'])
    x = cart_count.count()
    return render(request,"Filtered_Items.html",{'data':data,'categories':categories,'x':x})

def single_item(request,item_id):
    product=ProductDb.objects.get(id=item_id)
    categories = CategoryDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['Username'])
    x = cart_count.count()
    return render(request,"Single_Item.html",{'product':product,'categories':categories,'x':x})

def contact_page(request):
    categories = CategoryDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['Username'])
    x = cart_count.count()
    return render(request,"Contact.html",{'categories':categories,'x':x})

def save_contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        obj=ContactDb(Name=name,Email=email,Subject=sub,Message=msg)
        obj.save()
        messages.success(request, "Contact saved Successfully")
        return redirect(contact_page)

def sign_in(request):
    return render(request,"Sign_in.html")

def sign_up(request):
    return render(request,"Sign_up.html")

def save_signup(request):
    if request.method=="POST":
        user=request.POST.get('username')
        psd=request.POST.get('pass1')
        con_psd=request.POST.get('pass2')
        em=request.POST.get('email')
        obj=SignUpDb(Username=user,Password=psd,Confirm_Password=con_psd,Email_Id=em)
        obj.save()
        messages.success(request, "Registered Successfully")
    return redirect(sign_in)

def user_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('pass1')
        if SignUpDb.objects.filter(Username=un,Password=pswd).exists():
            request.session['Username']=un
            request.session['Password']=pswd
            messages.success(request, "Welcome to EShopper")
            return redirect(home_page)
        else:
            messages.warning(request, "Failed To Login")
            return redirect(sign_in)
    else:
        return redirect(sign_in)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(user_login)



def save_cart(request):
    if request.method=="POST":
        user_name=request.POST.get('username')
        productname=request.POST.get('prod_name')
        quan=request.POST.get('quantity')
        pr=request.POST.get('price')
        to=request.POST.get('total')
        try:
            x = ProductDb.objects.filter(Product_Name=productname).first()
            img=x.Product_Image
        except ProductDb.DoesNotExist:
            img=None
        obj=CartDb(Username=user_name,Product_Name=productname,Quantity=quan,Price=pr,Total_Price=to,Product_Image=img)
        obj.save()
        return redirect(home_page)

def cart_page(request):
    sub_total=0
    shipping_amount=0
    total_amount=0
    categories = CategoryDb.objects.all()
    cart=CartDb.objects.filter(Username=request.session['Username'])
    for i in cart:
        sub_total+=i.Total_Price
        if sub_total>500:
            shipping_amount=50
        else:
            shipping_amount=100
        total_amount=sub_total+shipping_amount
        cart_count = CartDb.objects.filter(Username=request.session['Username'])
        x = cart_count.count()
    return render(request,"Cart.html",{'categories':categories,'cart':cart,'sub_total':sub_total,
                                       'shipping_amount':shipping_amount,'total_amount':total_amount,'x':x})

def checkout(request):
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    categories = CategoryDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['Username'])
    x = cart_count.count()
    cart = CartDb.objects.filter(Username=request.session['Username'])
    for i in cart:
        sub_total += i.Total_Price
        if sub_total > 500:
            shipping_amount = 50
        else:
            shipping_amount = 100
        total_amount = sub_total + shipping_amount
    return render(request,"checkout.html",{'categories':categories,'cart':cart,'sub_total':sub_total,
                                       'shipping_amount':shipping_amount,'total_amount':total_amount,'x':x})

def save_checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        place=request.POST.get('place')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        total=request.POST.get('total')
        message=request.POST.get('message')
        obj=CheckoutDb(Name=name,Email=email,Place=place,Address=address,State=state,
                       Mobile_Number=mobile,Pincode=pincode,Total_Price=total,Message=message)
        obj.save()
        return redirect(payment)

def payment(request):
    categories = CategoryDb.objects.all()
    username = request.session.get('Username')
    customer=CartDb.objects.order_by('-id').first()
    pay=customer.Total_Price
    amount=int(pay*100)
    pay_str=str(amount)
    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_OeaKOOhKcsCdcn','NySeZajvZmcgsBhkRX5UrRF4'))
        payment=client.order.create({'amount':amount,'order_currency':order_currency})
    return render(request,"Payment.html",{'username':username,'customer':customer,'pay_str':pay_str,'categories':categories})