from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)

class SignUpDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password=models.CharField(max_length=100,null=True,blank=True)
    Email_Id=models.EmailField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Total_Price=models.IntegerField(null=True,blank=True)
    Product_Image=models.ImageField(upload_to="Cart_Images",null=True,blank=True)

class CheckoutDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)