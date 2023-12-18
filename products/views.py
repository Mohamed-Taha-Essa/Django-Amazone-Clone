from django.shortcuts import render
from .models import Product ,Brand , Review,ProductImages
from django.views.generic import ListView ,DetailView
from django.db import models

# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by =50


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # dictionary of object from product
        context["reviews"] = Review.objects.filter(product =self.get_object()) #any single cbv (detail ,delete,update) have self.get_object()
        context['images'] = ProductImages.objects.filter(product = self.get_object())
        context['related'] =Product.objects.filter(brand =self.get_object().brand)

        #activate next and prev product 
        # Get the current product
        current_product = self.get_object()
        # Get the queryset of all products
        all_products = Product.objects.all()
        # Find the index of the current product in the queryset
        current_index = list(all_products).index(current_product)
        # Get the next product (if exists)
        next_product = None
        if current_index < len(all_products) - 1:
            next_product = all_products[current_index + 1]
        # Get the previous product (if exists)
        prev_product = None
        if current_index > 0:
            prev_product = all_products[current_index - 1]
        context['next_product'] = next_product
        context['prev_product'] = prev_product
    
        return context
    

class BrandList(ListView):
    model =Brand
    paginate_by =50

   
    
    
class BrandDetail(ListView):
    model =Product
    template_name ='products/brand_detail.html'
    paginate_by =50
    def get_queryset(self):
        brand = Brand.objects.get(slug = self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand =brand)
        return  queryset
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brand"] =  Brand.objects.get(slug = self.kwargs['slug'])
        return context
    