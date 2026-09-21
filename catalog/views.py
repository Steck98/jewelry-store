from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Product


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category = request.GET.get("category")
    if category:
        products = Product.objects.filter(category__name=category)
    else:
        products = Product.objects.all()
    return render(
        request,
        "catalog/catalog.html",
        {
            "products": products,
            "categories": categories,
        },
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        "catalog/product_detail.html",
        {"product": product},
    )
