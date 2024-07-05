from django.contrib import admin
from .models import Product, Variation

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}



class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',) # set to editable
    list_filter = ('product', 'variation_category', 'variation_value') #set filter

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)