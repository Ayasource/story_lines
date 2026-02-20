from django import views
from django.urls import path
from .views import home_page_view
from . import views


urlpatterns = [
    ## path("", home_page_view),
    path('', views.HomePage.as_view(), name='home'),
]
