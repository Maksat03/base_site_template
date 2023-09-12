from django.db import models

from base_object_presenter.models import BaseModelPresenter
from project.utils import datetime_now


class Request(models.Model):
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=datetime_now, editable=False)
    answered_at = models.DateTimeField(null=True)
    is_accepted = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)
    data = models.JSONField(null=True, blank=True)


class RequestModelPresenter(BaseModelPresenter):
    model = Request()

    @staticmethod
    def get_object_form_serializer_fields():
        return ["fullname", "phone_number"]

    @staticmethod
    def get_updatable_fields():
        return ["is_accepted", "comment"]
