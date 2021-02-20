from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('created_by',)
    list_display = ('name', 'slug', 'category', 'price', 'discount_price',
                    'description', 'is_available', 'is_on_stock',
                    'created_by', 'created_at', 'updated', 'label')
    list_filter = ('created_at', 'updated', 'is_available', 'is_on_stock')
    list_editable = ('price', 'discount_price', 'is_available', 'is_on_stock')
    prepopulated_fields = {'slug': ('name',)}
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)