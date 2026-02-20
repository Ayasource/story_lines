from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'


def home_page_view(request):  
    return HttpResponse("Welcome to Storylines!")