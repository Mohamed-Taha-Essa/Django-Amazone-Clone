#form 
from rest_framework import serializers
from .models import Product,Brand,Review ,ProductImages

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =Review 
        fields = ['user' , 'content' ,'rate' ,'created_at']

class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        fields ='__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review = ReviewSerializers(source ='review_product' ,many =True)
    class Meta:
        model = Product
        fields ='__all__'

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ='__all__'

class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ='__all__'