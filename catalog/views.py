from django.views.generic import ListView

from django.shortcuts import render
from catalog.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


def index_1(request):
    context = {
        'title': "Контакты"
    }
    return render(request, 'catalog/index_1.html', context)

