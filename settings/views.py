from django.shortcuts import render
from django.db.models import Count ,Sum
from products.models import Product ,Review,Brand ,OrderProduct
from orders.models import OrderDetail

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

# Create your views here.
def home(request):
    new_product = Product.objects.filter(flag ='New')[:10]
    # sale_product = Product.objects.filter(flag ='Sale').annotate(review_count = Count('review_product'))[:10]
    sale_product = Product.objects.filter(flag ='Sale')[:10]
   
    feature_product = Product.objects.filter(flag ='Feature')[:6]

     # i want to know the number of product in every brand
    brands = Brand.objects.all().annotate(product_count =Count('product_brand'))[:10]
    reviews = Review.objects.all()[:10]

   
    # order_details = OrderDetail.objects.all()
    top_order_products = (
        OrderDetail.objects
        .values('product__id', 'product__name','product__image','product__price' ,'product__slug','product__quantity')  # Group by Product ID and name
        .annotate(total_quantity=Sum('quantity'))  # Calculate total quantity per Product
        .order_by('-total_quantity')  # Order by total quantity in descending order
    )
    products_list =[]
    for item in top_order_products:
        product_data = {
            'id': item['product__id'],
            'name': item['product__name'],
            'image': item['product__image'],
            'quantity': item['product__quantity'],

            'price': item['product__price'],
            'slug': item['product__slug'],
            'review_count': Product.objects.get(id=item['product__id']).review_count,
            'avg_rate': Product.objects.get(id=item['product__id']).avg_rate,
        }
        products_list.append(product_data)
        
    avg_rate = sorted(products_list,key=lambda x: x['avg_rate'],reverse=True)
    top_disc = sorted(products_list,key=lambda x: x['avg_rate'])

    return render(request ,'settings/home.html',{
        'new_product':new_product,
        'sale_product':sale_product,
        'feature_product':feature_product,
        'brands':brands,
        'top_order_products':products_list,
        'top_rate':avg_rate,
        'top_disc':top_disc,
    })