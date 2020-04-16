from django.conf.urls import url, include
from .views import request_page, request_sent

urlpatterns = [
    url(r'^$', request_page, name='request_page'),
    # <!-- Michal homework -->
    url(r'^request_sent/$', request_sent, name='request_sent'),
    # <!-- Michal homework -->
]