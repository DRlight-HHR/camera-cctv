from django.contrib import admin
from .models import book


class edit(admin.ModelAdmin):
    search_fields = ['name', 'author', 'Publisher']
    list_display = ['name', 'author', 'Publisher']


admin.site.register(book, edit)
