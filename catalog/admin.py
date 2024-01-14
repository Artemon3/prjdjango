from django.contrib import admin

from catalog.models import Product, Category, Version


#
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_one', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'desc')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'desc')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version_number',)
