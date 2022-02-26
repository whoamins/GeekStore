from django.shortcuts import render
from django.views import View
from products.models import Category, Product


class IndexView(View):
    def get(self, request):
        context = {
            'title': 'GeekStore'
        }

        return render(request, "products/index.html", context=context)


class ProductView(View):
    def get(self, request):
        context = {
            'title': 'GeekStore | Catalog',
            'categories': Category.objects.all(),
            'products': Product.objects.all()
        }

        return render(request, "products/products.html", context=context)
