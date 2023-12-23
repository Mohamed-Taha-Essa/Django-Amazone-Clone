#form 
from rest_framework import serializers
from .models import Product,Brand,Review ,ProductImages

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =Review 
        fields = ['user' , 'content' ,'rate' ,'created_at']

class ProductImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model =ProductImages 
        fields = ['image']

class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count =serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields ='__all__'

    def get_review_count(self,object ):
        reviews= object.review_product.all().count()
        return reviews


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ='__all__'

class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ='__all__'



class ProductDetailSerializer(serializers.ModelSerializer):
    brand = BrandDetailSerializer()
    review = ReviewSerializers(source ='review_product' ,many =True)
    images = ProductImagesSerializers(source ='product_image' ,many = True)
    class Meta:
        model = Product
        fields ='__all__'