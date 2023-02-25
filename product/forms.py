from django import forms

from product.models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_by',)