from django.contrib import admin

from categories.models import Category

# Register your models here.


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
