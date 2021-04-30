from django.contrib import admin

# Register your models here.

from .models import  Brands,Mobile,Order,Cart
admin.site.register(Brands)
admin.site.register(Mobile)
admin.site.register(Order)
admin.site.register(Cart)



