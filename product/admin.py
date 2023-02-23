from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
