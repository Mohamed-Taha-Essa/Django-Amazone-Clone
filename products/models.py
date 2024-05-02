from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.
FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),    
    ('Feature','Feature')
]

class Product(models.Model):
    brand = models.ForeignKey('Brand',verbose_name=_('brand') ,related_name='product_brand' ,on_delete=models.SET_NULL ,null=True)
    name =models.CharField(_('name'),max_length=120)
    flag = models.CharField(_('flag'),max_length=10 ,choices=FLAG_TYPE)
    image =models.ImageField(_('image'), upload_to='product')
    price =models.FloatField(_('price'),)
    sku =models.IntegerField(_('sku'), unique=True)
    subtitle =models.TextField(_('subtitle'),max_length=500)
    description =models.TextField(_('description'),max_length=50000)
    quantity = models.IntegerField(_('quantity'))

    tags = TaggableManager()
    slug =models.SlugField(blank=True,null=True ,unique=True)

    def save(self ,*args, **kwargs):
        self.slug =slugify(self.name)
        super(Product ,self).save(*args, **kwargs) 

    def __str__(self):
        return self.name
    
    @property
    def review_count(self ):
        reviews= self.review_product.all().count()
        return reviews
    
    @property
    def avg_rate(self ):
        reviews = self.review_product.all()
        temp =0 
        if len(reviews)>0:
            for obj in reviews:
                temp +=obj.rate
            avg_rate = temp /len(reviews)
        else :
            avg_rate =0 
        return avg_rate
    


class ProductImages(models.Model):
    product =models.ForeignKey(Product,verbose_name=_('product'),related_name='product_image',on_delete=models.CASCADE)
    image =models.ImageField(_('image'),upload_to='productimage')


class Brand(models.Model):
    name =models.CharField(_('name'),max_length=100)
    image = models.ImageField(_('image'),upload_to='brand')

    slug =models.SlugField(blank=True ,null=True)

    def save(self ,*args, **kwargs):
        self.slug =slugify(self.name)
        super(Brand ,self).save(*args, **kwargs) 

    def __str__(self):
        return self.name


class Review(models.Model):
    user =models.ForeignKey(User,verbose_name=_('user') ,related_name='reviw_user' ,on_delete=models.SET_NULL ,null=True)
    product =models.ForeignKey(Product ,verbose_name=_('product') ,related_name='review_product' ,on_delete=models.CASCADE)
    content = models.TextField(_('content'),max_length=500)
    rate = models.IntegerField(_('rate '),choices=[(i,i) for i in range(1,6)])
    created_at =models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user