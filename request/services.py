from base_object_presenter.services import BaseServicesPresenter
from .models import RequestModelPresenter


class RequestServicesPresenter(BaseServicesPresenter):
    model_presenter = RequestModelPresenter()
