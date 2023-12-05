from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),    
    ('Feature','Feature')
]

class Product(models.Model):
    brand = models.ForeignKey('Brand',related_name='product_brand' ,on_delete=models.SET_NULL ,null=True)
    name =models.CharField(max_length=120)
    flag = models.CharField(max_length=10 ,choices=FLAG_TYPE)
    image =models.ImageField( upload_to='product')
    price =models.models.FloatField()
    sku =models.IntegerField()
    subtitle =models.TextField(max_length=500)
    description =models.TextField(max_length=50000)

    tags = TaggableManager()
    slug =models.SlugField(blank=True,null=True)

    def save(self ,*args, **kwargs):
        self.slug =slugify(self.name)
        super(Product ,self).save(*args, **kwargs) 

    def __str__(self):
        return self.name
    

class ProductImages(models.Model):
    product =models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    iamge =models.ImageField(upload_to='productimage')


class Brand(models.Model):
    name =models.CharField(max_length=100)
    iamge = models.ImageField(upload_to='brand')

    slug =models.SlugField(blank=True ,null=True)
    
    def save(self ,*args, **kwargs):
        self.slug =slugify(self.name)
        super(Brand ,self).save(*args, **kwargs) 

    def __str__(self):
        return self.name


class Review(models.Model):
    user =models.ForeignKey(User ,related_name='reviw_user' ,on_delete=models.SET_NULL ,null=True)
    product =models.ForeignKey(Product ,related_name='review_product' ,on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    rate = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    created_at =models.DateTimeField(default=timezone.now)

