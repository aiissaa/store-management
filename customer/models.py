from django.db import models


class CustomerCredit(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<CreditedCredit: {self.id}>'
    
    class Meta:
        verbose_name = 'Crédit client'
        verbose_name_plural = 'Crédits clients'


class Customer(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    credited_products = models.ManyToManyField('product.Product', through=CustomerCredit, related_name='credited_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Payment(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='payments')
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Payment: {self.id}>'
    
    class Meta:
        verbose_name = 'Paiement'
        verbose_name_plural = 'Paiements'
