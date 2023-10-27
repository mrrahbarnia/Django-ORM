from django.contrib import admin
from .models import (
    Category,
    Product,
    Product_Category
)

admin.site.register(Product_Category)

class CategoryInline(admin.TabularInline):
    model = Product.categories.through

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    inlines = [CategoryInline]