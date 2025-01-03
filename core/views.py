from django.shortcuts import render, get_object_or_404
from product.models import ProductItem, Category

def index(request):
    categories = Category.objects.all()
    products  = ProductItem.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'core/index.html', context)

def product_item(request, pk):
    categories = Category.objects.all()
    product = get_object_or_404(ProductItem, pk=pk)

    context = {
        'product':product,
        'categories': categories
    }
    return render(request, 'core/product_item.html', context)

# I've never seen a view sponsor `base.html`` 😂
# but there's a first time for everything
# so there's no need for this let's just index
