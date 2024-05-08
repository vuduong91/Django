from django.contrib import admin
from .models import Product,Category,ProductDetail,Order,OrderDetail,Shipping,User

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductDetail)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Shipping)
admin.site.register(User)