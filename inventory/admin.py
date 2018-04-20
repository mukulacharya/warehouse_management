from django.contrib import admin

from .models import Inventory, InventoryReservation


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['sku', 'entity', 'quantity', 'status', 'stock_type']
    list_filter = ['status', 'stock_type', 'entity']
    search_fields = ['sku', 'entity', 'status', 'stock_type']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class InventoryReservationAdmin(admin.ModelAdmin):
    list_display = ['reference', 'sku', 'entity', 'quantity', 'status']
    list_filter = ['status', 'entity']
    search_fields = ['sku', 'entity', 'status', 'reference']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryReservation, InventoryReservationAdmin)
