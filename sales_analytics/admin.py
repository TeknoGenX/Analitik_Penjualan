from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'amount', 'quantity', 'transaction_date', 'total_price')
    list_filter = ('transaction_date',)
