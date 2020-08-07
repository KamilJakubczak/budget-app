from django.contrib import admin
from .models import Category, Tag, Payment, Transaction, TransactionType
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Payment)
admin.site.register(TransactionType)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'transaction_date',
        'category',
        'description',
        'payment_target',
        'payment_source',
        'transaction_type')
