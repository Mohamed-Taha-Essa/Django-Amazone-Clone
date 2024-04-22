from django.shortcuts import render,redirect ,get_object_or_404
from .models import Order ,OrderDetail,Cart,CartDetail,Coupon
import datetime
from django.conf import settings
import stripe
from utils.generate_code import generate_code
from django.http import JsonResponse
from django.template.loader import render_to_string

from accounts.models import Address
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
    pub_key =settings.STRIPE_API_KEY_PUBLISHABLE

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
                
                coupon.quantity -=1 
                coupon.save()
                page = render_to_string('includes/checkout.html',{'cart_detail':cart_detail ,
                                                                 'total':total,
                                                                 'delivery_fee':delivery_fee,
                                                                 'discount':coupon_value ,
                                                                 'sub_total':sub_total,
                                                                 'pub_key':pub_key
                                                                 })
                return JsonResponse({'result':page})


                # return render(request ,'orders/checkout.html',{
                #     'cart_detail':cart_detail,
                #     'total':total,
                #     'delivery_fee':delivery_fee,
                #     'discount':coupon_value,
                #     'sub_total':sub_total,
                # })
   
    sub_total = cart.cart_total
    discount = 0  
    total = sub_total + delivery_fee
    return render(request ,'orders/checkout.html',{
        'cart_detail':cart_detail,
        'total':total,
        'delivery_fee':delivery_fee,
        'discount':discount,
        'sub_total':sub_total,
        'pub_key':pub_key
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

    cart = Cart.objects.get(user = request.user ,status = 'Inprogress')
    cart_detail  = CartDetail.objects.filter(cart = cart)

    total = cart.cart_total
    count = len(cart_detail)
    page = render_to_string('cart_include.html',{'cart_detail_data':cart_detail ,'cart_data':cart})
    return JsonResponse({'result':page,
                         'total':total,
                         'count':count})



def payment_proces(request): #create invoice
    cart = Cart.objects.get(user = request.user ,status ='Inprogress')
    delivery_fee = DeliveryFee.objects.last().fee

    if cart.total_with_coupon :
        total = cart.total_with_coupon + delivery_fee
 
    else :
        total =cart.total + delivery_fee
    code = generate_code()
    
    #django sessions  to save small data in browser of user
    request.session['order_code'] =code 
    request.session.save()

    # create invoice in stripe 
    stripe.api_key =settings.STRIPE_API_KEY_SECRETE

    checkout_session = stripe.checkout.Session.create(
        line_items = [
            {
                'price_data':{
                    'currency':'usd',
                    'product_data':{'name':code},
                    'unit_amount':int(total*100)
                },
                'quantity':1
            },
        ],
        mode ='payment',
        success_url ='http://127.0.0.1:8000/orders/checkout/payment/success',
        cancel_url ='http://127.0.0.1:8000/orders/checkout/payment/failed',
     )
    return JsonResponse({'session':checkout_session})


def payment_success(request):
    cart = Cart.objects.get(user=request.user ,status ='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_address = Address.objects.last()
    code =request.session.get('order_code')
    new_order = Order.objects.create(
            user = request.user ,
            status = 'Inprogress',#it's best if it have adefault
            code = code, #request.body
            delivery_address = delivery_address ,
            coupon = cart.coupon,
            total_with_coupon =cart.total_with_coupon,
            total = cart.cart_total
        )

    for item in cart_detail :
        product = Product.objects.get(id = item.product.id)
        OrderDetail.objects.create(
            order = new_order ,
            product = item.product ,
            price = product.price ,
            quantity = item.quantity,
            total = round(product.price * item.quantity,2)
        )

        product.quantity -= item.quantity
        product.save() 

    cart.status = 'Completed'
    cart.save() 

    return render(request , 'orders/sucess.html',{'code':code})


def payment_failed(request):
    return render(request , 'orders/failed.html',{})
