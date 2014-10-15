from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from core import models as core_models
import models


class ProductAttributeInline(admin.TabularInline):
    model = models.ProductAttribute
    suit_classes = 'suit-tab suit-tab-attributes'
    extra = 10


class ProductImageInlineForm(forms.ModelForm):
    info = forms.CharField(widget=forms.Textarea(), required=False)

    class Meta:
        model = models.ProductImage


class ProductImageInline(admin.StackedInline):
    model = models.ProductImage
    suit_classes = 'suit-tab suit-tab-images'
    form = ProductImageInlineForm
    extra = 6


class ProductAdminForm(forms.ModelForm):
    info = forms.CharField(widget=CKEditorWidget())
    video_code = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = models.Product


class ProductAdmin(core_models.ModelAdmin):
    list_display = ['category', 'manufacturer', 'model', ]
    list_filter = ['category', 'manufacturer', ]
    inlines = [ProductAttributeInline, ProductImageInline, ]
    form = ProductAdminForm
    fieldsets = [
        ('Relations', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'Product relations',
            'fields': ['category', 'manufacturer', ]
        }),
        ('General', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'Product general information',
            'fields': ['model', 'size', 'weight', 'info', ]
        }),
        ('Media', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'Related media sources',
            'fields': ['image', 'video_code', ]
        }),
    ]
    suit_form_tabs = (
        ('general', 'General'),
        ('attributes', 'Attributes'),
        ('images', 'Images'),
    )


class ShopProductInlineForm(forms.ModelForm):
    info = forms.CharField(widget=forms.Textarea(), required=False)

    class Meta:
        model = models.ShopProduct


class ShopProductInline(admin.StackedInline):
    model = models.ShopProduct
    form = ShopProductInlineForm
    suit_classes = 'suit-tab suit-tab-products'
    exclude = ['url', ]
    extra = 20


class ShopAdminForm(forms.ModelForm):
    info = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Shop


class ShopAdmin(core_models.ModelAdmin):
    list_display = ['title', 'is_active', ]
    inlines = [ShopProductInline, ]
    fieldsets = [
        ('General', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'Shop general information',
            'fields': ['title', 'slug', 'info']
        }),
        ('Media', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'Shop media files',
            'fields': ['image', ]
        }),
    ]
    suit_form_tabs = (
        ('general', 'General'),
        ('products', 'Products'),
    )
    form = ShopAdminForm


class ShopProductAdmin(core_models.ModelAdmin):
    list_display = ['shop', 'product', 'currency', 'price', 'quantity', ]
    list_filter = ['shop', 'product', ]


# Reviews

class ProductReviewAdmin(core_models.ModelAdmin):
    list_display = ['is_approved', 'product', 'status', 'comment', 'is_approved', ]
    list_filter = ['is_approved', 'status', ]


class ShopReviewAdminForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = models.ShopReview


class ShopReviewAdmin(core_models.ModelAdmin):
    form = ShopReviewAdminForm
    list_display = ['shop', 'rating', 'comment', 'is_approved', ]
    list_filter = ['shop', 'rating', 'is_approved', ]


admin.site.register(models.Currency)
admin.site.register(models.Manufacturer)
admin.site.register(models.Category)
admin.site.register(models.AttributeGroup)
admin.site.register(models.Attribute)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Shop, ShopAdmin)
admin.site.register(models.ShopProduct, ShopProductAdmin)

admin.site.register(models.ProductReview, ProductReviewAdmin)
admin.site.register(models.ShopReview, ShopReviewAdmin)

