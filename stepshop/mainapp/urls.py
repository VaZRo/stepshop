from django.urls import path
from mainapp.views import index, about, contacts, products

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contacts/', contacts),
    path('products/', products),

]
