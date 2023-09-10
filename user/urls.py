from django.urls import path
from .views import *


urlpatterns = [
    path("change_password/", change_password_view),
]
