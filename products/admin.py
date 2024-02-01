from django.contrib import admin
from products.models import CoffeeProducts,CoffeeCategory,ProductPrice

# Register your models here.
admin.site.register(CoffeeProducts)
admin.site.register(CoffeeCategory)
admin.site.register(ProductPrice)