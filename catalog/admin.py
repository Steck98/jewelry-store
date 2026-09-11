"""Admin registrations for the catalog app will go here."""

from django.contrib import admin

from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
