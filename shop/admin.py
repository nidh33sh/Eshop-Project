from django.contrib import admin
from .models import *


# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']


admin.site.register(category, catadmin)


class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'img', 'stock', 'price']
    list_editable = ['price', 'stock']


admin.site.register(product, prodadmin)


# admin.site.register(products_extra)
