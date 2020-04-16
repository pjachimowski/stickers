from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse

# Create your views here.
def request_page(request):
    """A view that opens the request page"""
    return render(request, "request_page.html")
    # if function(response)


def request_sent(request):
    """A view that displays message after sending a request"""
    messages.success(request, 'Your request was sent. We will get back to you within 5 working days.')
    return redirect(reverse('request_page.html'))
