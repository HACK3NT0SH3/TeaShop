from django.contrib import admin
from testapp.models import Item, Review, Cart, Order, Catalog

# Register your models here.
admin.site.register(Item)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Catalog)
