from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class CarAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Car
        fields = '__all__'


class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = CarAdminForm
    save_as = True
    list_display = ("id", "title", "slug", "category", "created_at", "get_photo")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("category", "tags")
    readonly_fields = ("views", "created_at", "get_photo")
    fields = ("title", "slug", "author", "category", "tags", "content", "photo", "price", "get_photo", "views", "created_at")

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")
        return "-"
    get_photo.short_description = "Image"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Car, CarAdmin)
