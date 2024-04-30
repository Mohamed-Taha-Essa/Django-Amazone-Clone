from django.shortcuts import render
from django.db.models import Count
from products.models import Product ,Review,Brand

# Create your views here.
def home(request):
    new_product = Product.objects.filter(flag ='New')[:10]
    # sale_product = Product.objects.filter(flag ='Sale').annotate(review_count = Count('review_product'))[:10]
    sale_product = Product.objects.filter(flag ='Sale')[:10]
   
    feature_product = Product.objects.filter(flag ='Feature')[:6]
    # i want to know the number of product in every brand
    brands = Brand.objects.all().annotate(product_count =Count('product_brand'))[:10]
    reviews = Review.objects.all()[:10]

   
    return render(request ,'settings/home.html',{
        'new_product':new_product,
        'sale_product':sale_product,
        'feature_product':feature_product,
        'brands':brands,
        'reviews':reviews,
        
    })