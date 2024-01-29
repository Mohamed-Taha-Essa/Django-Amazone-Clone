import datetime
from rest_framework import generics 
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from settings.models import DeliveryFee

from .serializers import OrderDetailSerializers ,OrderSerializers , CartDetailSerializers , CartSerializers
from .models import Order ,OrderDetail ,Cart ,CartDetail ,Coupon


class OrderListAPI(generics.ListAPIView):
    queryset =Order.objects.all()
    serializer_class = OrderSerializers

    # def get_queryset(self):
    #     queryset = super(OrderListAPI,self).get_queryset()
    #     user = User.objects.get( username = self.kwargs['username'])
    #     queryset = queryset.filter(user = user)  
    #     return queryset

    def list(self ,request ,*args, **kwargs):
        queryset = super(OrderListAPI,self).get_queryset()
        user = User.objects.get( username = self.kwargs['username'])
        queryset = queryset.filter(user = user)  
        data = OrderSerializers(queryset,many =True).data
        return Response({'orders':data})
        

class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderSerializers
    queryset =Order.objects.all()


class ApplyCouponAPI(generics.GenericAPIView):
    #i need method post to apply coupon
    def post(self , request ,*args, **kwargs):
        user = User.objects.get( username = self.kwargs['username']) #url
        coupon = get_object_or_404(Coupon ,code = request.data['coupon_code']) #request.body
        delivery_fee = DeliveryFee.objects.last().fee
        cart = Cart.objects.get(user = user ,status='Inprogress')
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
                return Response({'message':'coupon was applied successfully'})
            #what will happen after return this message for android app how he arrive to new value and show it for user

            else:
                return Response({'message':'copon is invalid'})
        else :
            return Response({'message':'coupon not found'})
