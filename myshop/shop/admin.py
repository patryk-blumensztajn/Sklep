from django.contrib import admin
from .models import Category, Product, SubCategory, SubSubCategory, Computer

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(SubCategory, CategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(SubSubCategory, CategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Computer, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','slug','price','stock', 'available', 'created', 'updated']
	list_filter = ['available','created','updated']
	list_editable = ['price','stock','available']
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Product, ProductAdmin)

# Register your models here.
