from rest_framework import serializers
from .models import Order ,OrderDetail ,Cart ,CartDetail


class OrderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields='__all__'

class OrderSerializers(serializers.ModelSerializer):
    order_detail = OrderDetailSerializers
    class Meta:
        model = Order
        fields = '__all__'


class CartDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields='__all__'

class CartSerializers(serializers.ModelSerializer):
    cart_detail = CartDetailSerializers
    class Meta:
        model = Cart
        fields = '__all__'

