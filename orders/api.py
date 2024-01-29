from rest_framework import generics 
from django.contrib.auth.models import User

from .serializers import OrderDetailSerializers ,OrderSerializers , CartDetailSerializers , CartSerializers
from .models import Order ,OrderDetail ,Cart ,CartDetail


class OrderListAPI(generics.ListAPIView):
    queryset =Order.objects.all()
    serializer_class = OrderSerializers

    def get_queryset(self):
        queryset = super(OrderListAPI,self).get_queryset()
        user = User.objects.get( username = self.kwargs['username'])
        queryset = queryset.filter(user = user)  
        return queryset
        