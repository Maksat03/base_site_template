from base_object_presenter.views import BaseViewsPresenter
from .services import RequestServicesPresenter


class RequestViewsPresenter(BaseViewsPresenter):
    services = RequestServicesPresenter()
