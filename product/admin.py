from django.contrib import admin
from product.models import Product
from product.forms import ProductAdminForm
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    list_filter = ('name',)
    search_fields = ('name',)
    form = ProductAdminForm
    def get_queryset(self, request):
        return super().get_queryset(request).filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

admin.site.register(Product, ProductAdmin)
