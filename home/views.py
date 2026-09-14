from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(
        request, "home/home.html", {"products": products, "categories": categories}
    )
