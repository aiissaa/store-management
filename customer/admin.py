from django.contrib import admin
from django.contrib.auth.models import Group, User
from customer.models import Customer, CustomerCredit, Payment
from customer.forms import CustomerAdminForm

admin.site.unregister(User)
admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    def get_queryset(self, request):
        return super().get_queryset(request).filter(id=request.user.id)

admin.site.register(User, UserAdmin)


class CustomerCreditInline(admin.TabularInline):
    model = CustomerCredit
    extra = 1
    fields = ('product', 'quantity', 'price')
    readonly_fields = ('price',)
    autocomplete_fields = ('product',)

    def price(self, obj):
        return obj.product.price * obj.quantity

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1
    fields = ('amount', 'created_at')
    readonly_fields = ('created_at',)


class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerCreditInline, PaymentInline]
    list_display = ('name', 'phone', 'email', 'address', 'total_payment_amount' , 'total_credit_amount', 'total_due_amount')
    readonly_fields = ('total_credit_amount', 'total_payment_amount', 'total_due_amount')

    form = CustomerAdminForm

    def get_queryset(self, request):
        return super().get_queryset(request).filter(created_by=request.user)

    def total_credit_amount(self, obj):
        return sum([credit.product.price * credit.quantity for credit in obj.customercredit_set.all()])
    
    def total_payment_amount(self, obj):
        return sum([payment.amount for payment in obj.payments.all()])
    
    def total_due_amount(self, obj):
        return self.total_credit_amount(obj) - self.total_payment_amount(obj)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


class CustomerCreditAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity')
    list_filter = ('customer', 'product')
    search_fields = ('customer', 'product')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'amount')
    list_filter = ('customer',)
    search_fields = ('customer',)
    readonly_fields = ('created_at',)

# admin.site.register(Payment, PaymentAdmin)
# admin.site.register(CustomerCredit, CustomerCreditAdmin)
admin.site.register(Customer, CustomerAdmin)
