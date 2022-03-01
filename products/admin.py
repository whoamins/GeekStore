from django.contrib import admin
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'short_description', 'price', 'quantity')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
