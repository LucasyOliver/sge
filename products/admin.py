from django.contrib import admin
from .models import Brand, Category, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category')
    search_fields = ('title',)

    # NEW: Adds filters to the right sidebar of the admin panel
    list_filter = ('brand', 'category')

    # NEW: Optimizes database queries to prevent the N+1 problem
    list_select_related = ('brand', 'category')
