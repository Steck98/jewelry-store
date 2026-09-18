from django.shortcuts import get_object_or_404, render

from catalog.models import Product


def products(request):
    products = Product.objects.all()

    return render(request, "catalog/catalog.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        "catalog/product_detail.html",
        {"product": product},
    )
