from django.contrib import admin
from .models import Product, Review,Brand,ProductImages
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model=ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand')
    inlines=[ProductImageInline]
    search_fields = ('name',) 


admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Brand)
