from django.contrib import admin
from webapp.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'description', 'status', 'created_at']
    list_filter = ['name']
    fields = ['name', 'email', 'description', 'status']


admin.site.register(Book, BookAdmin)
# Register your models here.

# Register your models here.
