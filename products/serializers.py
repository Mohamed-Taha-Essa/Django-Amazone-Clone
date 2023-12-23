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
    review_count =serializers.SerializerMethodField()
    avg_rate  =serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields ='__all__'

    def get_review_count(self,object ):
        reviews= object.review_product.all().count()
        return reviews
    
    def get_avg_rate(self ,object):
        reviews = object.review_product.all()
        temp =0 
        if len(reviews)>0:
            for obj in reviews:
                temp +=obj.rate
            avg_rate = temp /len(reviews)
        else :
            avg_rate =0 
        return avg_rate


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
    avg_rate  =serializers.SerializerMethodField()
    review_count =serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields ='__all__'

    def get_review_count(self,object ):
        reviews= object.review_product.all().count()
        return reviews
    
    def get_avg_rate(self ,object):
        reviews = object.review_product.all()
        temp =0 
        if len(reviews)>0:
            for obj in reviews:
                temp +=obj.rate
            avg_rate = temp /len(reviews)
        else :
            avg_rate =0 
        return avg_rate