from django.shortcuts import render,redirect
from AdminAPP.models import CategoryDb,ProductDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDb

# Create your views here.
def index_page(request):
    return render(request,"index.html")

def category_page(request):
    return render(request,"AddCategory.html")

def save_category(request):
    if request.method=="POST":
        category_name=request.POST.get('name')
        category_des= request.POST.get('description')
        pr=request.FILES['profile']
        obj=CategoryDb(Name=category_name,Description=category_des,Category_Image=pr)
        obj.save()
        return redirect(category_page)

def display_category(request):
    category=CategoryDb.objects.all()
    return render(request,"DisplayCategory.html",{'category':category})

def edit_category(request,cat_id):
    category=CategoryDb.objects.get(id=cat_id)
    return render(request,"EditCategory.html",{'category':category})

def delete_category(request,cat_id):
    category=CategoryDb.objects.filter(id=cat_id)
    category.delete()
    return redirect(display_category)
def update_category(request,cats_id):
    if request.method == "POST":
        cat_name= request.POST.get('name')
        cat_des= request.POST.get('description')
        try:
            img=request.FILES['profile']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=cats_id).Category_Image

        CategoryDb.objects.filter(id=cats_id).update(Name=cat_name,Description=cat_des,Category_Image=file)
        return redirect(display_category)

def product_page(request):
    cat=CategoryDb.objects.all()
    return render(request,"AddProduct.html",{'categories':cat})

def save_product(request):
    if request.method=="POST":
        category_name=request.POST.get('categoryname')
        product_name=request.POST.get('productname')
        description=request.POST.get('description')
        price=request.POST.get('price')
        product_image= request.FILES['pimage']
        obj = ProductDb(Category_Name=category_name,Product_Name=product_name,Description=description,
                        Price=price,Product_Image=product_image)
        obj.save()
        return redirect(product_page)



def display_product(request):
    pro = ProductDb.objects.all()
    return render(request, "DisplayProduct.html", {'pro': pro})

def delete_product(request,pr_id):
    categories=ProductDb.objects.filter(id=pr_id)
    categories.delete()
    return redirect(display_product)

def edit_product(request,pro_id):
    cat=CategoryDb.objects.all()
    pro=ProductDb.objects.get(id=pro_id)
    return render(request,"EditProduct.html",{'pro':pro,'cat':cat})

def update_product(request,pro_id):
    if request.method=="POST":
        cat=request.POST.get('categoryname')
        pro=request.POST.get('productname')
        des=request.POST.get('description')
        pr=request.POST.get('price')
        try:
            img=request.FILES['pimage']
            fs=FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=pro_id).Product_Image
        ProductDb.objects.filter(id=pro_id).update(Category_Name=cat,Product_Name=pro,Description=des,Price=pr,Product_Image=file)
        return redirect(display_product)

def admin_login_page(request):
    return render(request,"Admin_login_page.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                request.session['username']=un
                request.session['password']=pswd
                login(request,user)
                return redirect(index_page)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

def contact_data(request):
    data=ContactDb.objects.all()
    return render(request,"Contact_Data.html",{'data':data})

def delete_contact(request,c_id):
    datas=ContactDb.objects.filter(id=c_id)
    datas.delete()
    return redirect(contact_data)