from django.db import models
from base_object_presenter.models import BaseModelPresenter


class Case(models.Model):
    name = models.CharField(max_length=255)


class CaseModelPresenter(BaseModelPresenter):
    model = Case
