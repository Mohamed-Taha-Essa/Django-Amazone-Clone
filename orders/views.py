from django.shortcuts import render,redirect ,get_object_or_404
from .models import Order ,OrderDetail,Cart,CartDetail,Coupon
import datetime
from products.models import Product
from settings.models import DeliveryFee
# Create your views here.

def order_list(request):
    data=Order.objects.filter(user=request.user)
    return render(request ,'orders/orderlist.html',{'orders':data})


def checkout(request):
    cart = Cart.objects.get(user = request.user ,status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart = cart)
    delivery_fee = DeliveryFee.objects.last().fee


    if request.method =='POST':
        code = request.POST['coupon_code']
        # coupon = Coupon.objects.get(code = code) #server stop if not have acorrect code
        coupon = get_object_or_404(Coupon ,code =code)
        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()

            if coupon.start_date <= today_date and coupon.end_date >= today_date :
               
                coupon_value = round(cart.cart_total / 100 * coupon.discount ,2)
                sub_total = cart.cart_total - coupon_value
                total = sub_total + delivery_fee

                cart.coupon = coupon
                cart.total_with_coupon =sub_total
                cart.save()

                return render(request ,'orders/checkout.html',{
                    'cart_detail':cart_detail,
                    'total':total,
                    'delivery_fee':delivery_fee,
                    'discount':coupon_value,
                    'sub_total':sub_total,
                })
   
    sub_total = cart.cart_total
    discount = 0  
    total = sub_total + delivery_fee
    return render(request ,'orders/checkout.html',{
        'cart_detail':cart_detail,
        'total':total,
        'delivery_fee':delivery_fee,
        'discount':discount,
        'sub_total':sub_total,
    })



def add_to_cart(request):
    product=Product.objects.get(id = request.POST['product_id'])
    quantity = int(request.POST['quantity'])

    cart = Cart.objects.get(user = request.user ,status = 'Inprogress')
    cart_detail ,created = CartDetail.objects.get_or_create(cart = cart , product =product)
    
    # if created :
    #     cart_detail.quantity +=quantity
    cart_detail.quantity = quantity
    cart_detail.total = round(product.price * cart_detail.quantity,2)
    cart_detail.save()

    return redirect(f'/products/{product.slug}')