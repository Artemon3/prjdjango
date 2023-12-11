from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def index_1(request):
    return render(request, 'catalog/index_1.html')
