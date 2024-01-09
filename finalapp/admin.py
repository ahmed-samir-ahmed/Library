from django.contrib import admin

from .models import Category
from .models import Book


admin.site.register(Category)
admin.site.register(Book)
