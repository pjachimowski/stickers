from django.conf.urls import url, include
from .views import shop
from .views import all_products

urlpatterns = [
    url(r'^$', shop, name='shop'),
    url(r'^$', all_products, name='products'),
]