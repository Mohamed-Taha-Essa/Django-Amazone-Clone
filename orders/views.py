from django.shortcuts import render
from .models import Order ,OrderDetail,Cart,CartDetail
# Create your views here.

def order_list(request):
    data=Order.objects.filter(user=request.user)
    return render(request ,'orders/orderlist.html',{'orders':data})


def checkout(request):
    
    return render(request ,'orders/checkout.html',{})