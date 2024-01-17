from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utils.generate_code import generate_code
from products.models import Product,Brand
from accounts.models import Address
import datetime
# Create your models here.
ORDER_STATUS=(
    ('Recieved','Recieved'),
    ('Processed' ,'Processed') ,
    ('Shipped' ,'Shipped') ,
   ('Delivered' ,'Delivered'),
)

class Order(models.Model):
    user =models.ForeignKey(User, related_name='order_user' , on_delete=models.SET_NULL ,null=True,blank=True)
    status = models.CharField(choices =ORDER_STATUS ,max_length =12)
    code =models.CharField(default =generate_code,max_length=50) #call function
    order_time = models.DateField(default=timezone.now)
    delivery_time =models.DateField(null=True ,blank =True)
    delivery_address =models.ForeignKey(Address, related_name='orderdelivery_address', on_delete=models.SET_NULL ,null=True,blank=True)
    coupon = models.ForeignKey("Coupon", related_name='order_coupon', on_delete=models.SET_NULL ,null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    total_with_coupon = models.FloatField(null=True,blank=True)
    def save(self , *args, **kwargs):
        week = datetime.timedelta(days=7)
        self.delivery_time = self.order_time + week
        super(Order , self).save(*args, **kwargs )
    

    def __str__(self):
       
        return (self.order_detail.all()[0].product.name)
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product =models.ForeignKey(Product,related_name='orderdetail_product', on_delete=models.SET_NULL ,null=True,blank=True)
    price =models.FloatField()
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True,blank=True)

CART_STATUS=(
    ('Inprogress','Inprogress'),
    ('Completed' ,'Completed') ,
   
)
class Cart(models.Model):
    user =models.ForeignKey(User, related_name='cart_user' , on_delete=models.SET_NULL ,null=True,blank=True)
    status = models.CharField(choices =CART_STATUS ,max_length =12)
    total = models.FloatField(null=True,blank=True)
    coupon = models.ForeignKey("Coupon", related_name='cart_coupon', on_delete=models.SET_NULL ,null=True,blank=True)
    total_with_coupon = models.FloatField(null=True,blank=True)


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    product =models.ForeignKey(Product,related_name='cartdetail_product', on_delete=models.SET_NULL ,null=True,blank=True)
    quantity = models.IntegerField(default =1)
    total = models.FloatField(null=True,blank=True)

class Coupon(models.Model):
    code = models.CharField( max_length=20)
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField()
    quantity =models.IntegerField()
    discount = models.FloatField()

#add a week on start date in save fun
    def save(self , *args, **kwargs):
        week = datetime.timedelta(days=7)
        self.end_date = self.start_date + week
        super(Coupon , self).save(*args, **kwargs )
    

    