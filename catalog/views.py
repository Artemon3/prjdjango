from django.shortcuts import render
from catalog.models import Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': "Главная"
    }
    return render(request, 'catalog/index.html', context)


def index_1(request):
    context = {
        'title': "Контакты"
    }
    return render(request, 'catalog/index_1.html', context)
