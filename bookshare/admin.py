from django.contrib import admin
from .models import Category,City,Book,Trade

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Book)
admin.site.register(Trade)