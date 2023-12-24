from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_1, ProductListView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', index_1, name='index_1'),
]
