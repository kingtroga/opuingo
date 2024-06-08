from django.shortcuts import render, get_object_or_404
from product.models import ProductItem

def index(request):
    products  = ProductItem.objects.all()
    return render(request, 'core/index.html',{
        'products': products 
    })

def product_item(request, pk):
    product = get_object_or_404(ProductItem, pk=pk)
    return render(request, 'core/product_item.html', {
        'product': product,
    })
