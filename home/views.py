from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    featured_products = Product.objects.filter(featured=True)[:4]
    categories = Category.objects.all()
    return render(
        request,
        "home/home.html",
        {"featured_products": featured_products, "categories": categories},
    )
