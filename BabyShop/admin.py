from django.contrib import admin
from .models import Product, Author

class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'page', 'wtitten')
    list_display_links = ('title', 'author')

admin.site.register(Product, BdAdmin)
admin.site.register(Author)

