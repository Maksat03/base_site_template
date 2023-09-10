from django.urls import path
from .views import *


urlpatterns = [
    path("get_feedbacks/", get_feedbacks_view),
    path("add_feedback/", add_feedback_view),
    path("get_feedback/", get_feedback_view),
    path("edit_feedback/", edit_feedback_view),
    path("delete_feedback/", delete_feedback_view),
]
