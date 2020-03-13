from django.conf.urls import url, include
from .views import request_page

urlpatterns = [
    url(r'^$', request_page, name='request_page'),
]