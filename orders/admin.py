from django.contrib import admin
from .models import Payment, Order, OrderProduct, Address
# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'district', 'order_total', 'discount', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','country', 'province', 'district', 'sector', 'cell', 'village', 'nearest_market', 'nearest_Agakiriro', 'save_info', 'default', 'use_default']

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
admin.site.register(Address, AddressAdmin)
