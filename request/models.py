from django.db import models
from project.utils import datetime_now


class RequestCategory(models.Model):
    name = models.CharField(max_length=100)


class Request(models.Model):
    category = models.ForeignKey(RequestCategory, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=datetime_now, editable=False)
    answered_at = models.DateTimeField(null=True)
    is_accepted = models.BooleanField(default=False)
    comment = models.TextField()
    data = models.JSONField(null=True, blank=True)
