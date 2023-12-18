from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, index_1

app_name = CatalogConfig.name
urlpatterns = [
    path('', index, name='index'),
    path('contacts/', index_1, name='index_1'),
]
