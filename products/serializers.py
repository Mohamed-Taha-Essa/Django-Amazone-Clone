#form 
from rest_framework import serializers
from .models import Product,Brand,Review ,ProductImages

class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model =Review 
        fields = ['user' , 'content' ,'rate' ,'created_at']

class ProductImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model =ProductImages 
        fields = ['image']

class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        # fields ='__all__'
        fields =['name','brand','price','review_count', 'avg_rate']
            

    
class BrandDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields ='__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    brand = BrandDetailSerializer()
    images = ProductImagesSerializers(source ='product_image' ,many = True)

    class Meta:
        model = Product
        fields=['name','price','review_count', 'avg_rate',
          'flag' , 'subtitle' ,'description', 'quantity','brand','images']


   

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ='__all__'





