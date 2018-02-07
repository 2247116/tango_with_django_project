from django.contrib import admin
from rango.models import Category
from rango.models import page
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
	prepoulared_fields ={'slug':('name',)}

admin.site.register(Category, CategoryAdmin )

admin.site.register(page)

# Register your models here.
