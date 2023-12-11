from django.urls import path
from catalog.views import index, index_1

urlpatterns = [
    path('', index),
    path('contacts/', index_1),
]
