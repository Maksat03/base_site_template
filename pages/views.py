from django.http import HttpRequest
from django.shortcuts import render


def main_page_view(request: HttpRequest):
    return render(request, "main_page.html")


def portfolio_page_view(request: HttpRequest):
    return render(request, "portfolio_page.html")
