from django.urls import path
from .views import ProductList ,ProductDetail ,BrandDetail,BrandList ,mydebug
from . import api

urlpatterns = [
    path('debug' ,mydebug),
    path("brands", BrandList.as_view()),
    path("brands/<slug:slug>", BrandDetail.as_view()),
    path('' ,ProductList.as_view() ),
    path('<slug:slug>' ,ProductDetail.as_view() ),


    #api 
    path('api/list' ,api.ProductListAPI.as_view() ),
    path('api/list/<int:pk>' ,api.ProductDetailAPI.as_view() ),
   
    path('api/brand' ,api.BrandListAPI.as_view() ),
    path('api/brand/<int:pk>' ,api.BrandDetailAPI.as_view() ),
   
]
