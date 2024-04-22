from django.urls import path
from .views import order_list,checkout,add_to_cart,payment_failed,payment_proces,payment_success
from .api  import OrderListAPI,OrderDetailAPI,ApplyCouponAPI,CreateOrderAPI,CartCreateUpdateDelete

urlpatterns = [
    path("", order_list),
    path("checkout/", checkout),
    path("add-to-cart", add_to_cart),

    path("checkout/payment-process", payment_proces),
    path("checkout/payment/success", payment_success),
    path("checkout/payment/failed", payment_failed),



    # api 
    path('api/<str:username>/orders' ,OrderListAPI.as_view()),
    path('api/<str:username>/orders/<int:pk>' ,OrderDetailAPI.as_view()),
    path('api/<str:username>/apply-coupon' ,ApplyCouponAPI.as_view()),
    path('api/<str:username>/cart' ,CartCreateUpdateDelete.as_view()),
    path('api/<str:username>/order/create' ,CreateOrderAPI.as_view()),

    
]
