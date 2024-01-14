from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_1, ProductListView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', index_1, name='index_1'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]