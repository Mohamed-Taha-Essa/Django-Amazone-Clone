from django.shortcuts import render ,redirect

import settings
from .models import Product ,Brand , Review,ProductImages
from django.views.generic import ListView ,DetailView
from django.db.models import Q,F,Value,Max
from django.db.models.aggregates import Count ,Sum,Min,Avg
from django.views.decorators.cache import cache_page


from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.

@cache_page(60 * 1)
def mydebug(request):
    # data = Product.objects.all()

    """## Column number
    # data = Product.objects.filter(price =25)
    # data = Product.objects.filter(price__gt =95)
    # data = Product.objects.filter(price__gte =95)
    # data = Product.objects.filter(price__lt =95)
    # data = Product.objects.filter(price__lte =95)
    # data = Product.objects.filter(price__range =(80 ,88))
    # data = Product.objects.filter(price__range =(80 ,88))
"""

    '''## Relations -----------------------------------------------------------------
    # brand = Brand.objects.filter(id =5 )
    # data = Product.objects.filter(brand =brand'must take object from brand')
    # data = Product.objects.filter(brand__id =5)
    # data = Product.objects.filter(brand__slug ='dljflskjfd')
    # data = Product.objects.filter(brand__id__gt =58)
    # data = Product.objects.filter(brand__slug='gillespie-inc')
'''
    '''## Text -----------------------------------------------------------------
    # data = Product.objects.filter(name ='exact name')
    # data = Product.objects.filter(name__contains ='hell')
    # data = Product.objects.filter(name__startswith ='Burns')
    # data = Product.objects.filter(name__endswith ='Burns')
    # data = Product.objects.filter(brand__isnull =True)
    # data = Product.objects.filter(brand__isnull =False)
    '''

    '''## Date time  ---------------------------------------------------------------------------
    data = Product.objects.filter(date_columns__year =2023)
    data = Product.objects.filter(date_columns__month =2)
    data = Product.objects.filter(date_columns__day =20)

    '''

    '''## Complex queries ------------------------------------------------------------------
    # data = Product.objects.filter(price__gt =90 ,flag='New')#using and
    # data = Product.objects.filter(price__gt =90).filter(flag='New')#using and
    # data = Product.objects.filter(
    #     Q(price__gt =90) & Q(flag='New')
    #     )#using and
    # data = Product.objects.filter( Q(price__gt =90) | Q(flag='New'))#using or
    # data = Product.objects.filter(Q(price__gt =90) & ~Q(flag='New'))#using not
 '''

    '''## Field Reference ---------------------------------------------------------------
    # data = Product.objects.filter(price = F('id'))#equality of value of cloumn to another col
    data = Product.objects.filter(name= F('brand__name'))#equality of value of cloumn to another col
    '''
    '''## Order ------------------------------------------------------------------------------
    # data = Product.objects.all().order_by('name')#ASC
    # data = Product.objects.all().order_by('-name')#DSC
    # data = Product.objects.filter(name__contains ='hel').order_by('name')
    # data = Product.objects.all().order_by('name')[:10]
    # data = Product.objects.earliest('name')
    # data = Product.objects.latest('name')
'''

    '''## Limit Fields ---------------------------------------------------------------
    #---u can't show on template cloumn don't return from values or values_list
    # data = Product.objects.select_related('brand').all()
    #better than all in time
    data = Product.objects.values('name' ,'slug','flag')
    # data = Product.objects.values_list('name' ,'slug','flag')

    #---u can show any columns if u use only but it will take more time
    # data = Product.objects.only('flag')
    #------ don't show name ,subtitle 
    # data = Product.objects.defer('name' ,'subtitle')
    '''

    '''## Select Related -------------convert query to join multible table in one--------
    # data = Product.objects.select_related('brand').all() #foreign key ,on to one
    # data = Product.objects.select_related('brand').values('name' ,'slug','brand')
    # data = Product.objects.prefetch_related('brand').all()#using in many to many

    # data = Product.objects.all()
'''

## Aggregation  Count Sum Min Max Avg---------------------------------------------------------------

    # data = Product.objects.aggregate(Max('id') ,Avg('price'))
    # max_price = Product.objects.aggregate(max_price=Max('price'))['max_price']


## Annotate -----add virtual new column in data that they back from db to frontend    
    # data = Product.objects.annotate(new_col=Value(20))
    # data = Product.objects.annotate(max_col= Value(max_price))
    # data = Product.objects.annotate(price_wit_tax=F('price')*1.25) 
   
#    don't work
    # data = Product.objects.annotate(max_price=Max('price')) 

    data = Product.objects.all()

    return render(request ,'products/debug.html' ,{'data':data})



# class ProductList(ListView):
#     model = Product
#     paginate_by =50

#     #if you only want to show the product that have quantity > 0
#     ''' 
#         def get_queryset(self):
#         queryset= super().get_queryset()
#         queryset =queryset.filter(quantity__gt=0)
#         return queryset
#     '''
#     def get_queryset(self):
#             # Retrieve and return products sorted by quantity (biggest quantity first)
#             return Product.objects.order_by('-quantity')

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
    

# class BrandList(ListView):
#     model =Brand
#     paginate_by =50
class BrandList(ListView):
    model = Brand
    paginate_by =50
    queryset = Brand.objects.annotate(num_products=Count('product_brand'))

   
    
    
class BrandDetail(ListView):
    model =Product
    template_name ='products/brand_detail.html'
    paginate_by =50
    def get_queryset(self):
        brand = Brand.objects.get(slug = self.kwargs['slug'])#can do in one line
        queryset = super().get_queryset().filter(brand =brand)
        # queryset = super().get_queryset().filter(brand__slug =self.kwargs['slug'])
        return  queryset
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        # error annotate don't come with get it comw with kteer
        # context["brand"] =  Brand.objects.get(slug = self.kwargs['slug']).annotate(num_products=Count('product_brand'))
        #but filter return list so i will return first item
        context["brand"] =  Brand.objects.filter(slug = self.kwargs['slug']).annotate(num_products=Count('product_brand'))[0]
        return context
    

def add_review(request,slug):
    product =Product.objects.get(slug =slug)

    rate = request.POST['rating']
    review =request.POST.get('review')

    Review.objects.create(
        user =request.user,
        product =product ,
        rate =rate ,
        content =review
    )
    reviews= Review.objects.filter(product = product)
    page = render_to_string('includes/reviews.html',{'reviews':reviews})
    return JsonResponse({'result':page})

class ProductList(ListView):
    model = Product
    paginate_by = 50
    template_name = 'product_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        queryset = queryset.order_by('-quantity')     
        return queryset



    def render_to_response(self, context, **response_kwargs):
        is_ajax = self.request.headers.get('x-requested-with') == 'XMLHttpRequest'
        context['is_ajax'] = is_ajax
        if is_ajax:
            products = list(context['object_list'])
            products_with_image_url = []
            for product in products:
                product_with_image_url = {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image_url': product.image.url if product.image else '',  # Ensure image URL is included
                    'description': product.description,
                    'flag': product.flag,
                    'brand': product.brand
                    # Add other fields as needed
                }
                products_with_image_url.append(product_with_image_url)
            page = render_to_string('includes/products_price.html', {'object_list': products_with_image_url})
            return JsonResponse({'result': page})
            
        else:
            return super().render_to_response(context, **response_kwargs)