from django.contrib import admin
from .models import Product, Review,Brand,ProductImages
# Register your models here.

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Brand)
admin.site.register(ProductImages)
