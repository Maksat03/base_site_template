from django.urls import path
from .views import *


urlpatterns = [
    path("", main_page_view, name="main_page"),
    path("portfolio/", portfolio_page_view, name="portfolio_page")
]
