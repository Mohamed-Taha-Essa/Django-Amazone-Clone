from django.contrib import admin
from . models import Order,OrderDetail,Cart,CartDetail,Coupon
# Register your models here.


class OrderTDetail(admin.TabularInline):
    model=OrderDetail

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderTDetail]


admin.site.register(Order,OrderAdmin)

admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Coupon)