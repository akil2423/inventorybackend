from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Location
from .models import ProductMovement

admin.site.register(Product)
admin.site.register(Location)
admin.site.register(ProductMovement)