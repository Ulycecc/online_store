from django.contrib import admin
from .models import Category, Product


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date', 'price']
    search_fields = ['description']
    actions = [reset_quantity]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
