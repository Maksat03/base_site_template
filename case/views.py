from base_object_presenter.views import BaseViewsPresenter
from .services import CaseServicesPresenter


class CaseViewsPresenter(BaseViewsPresenter):
    services = CaseServicesPresenter()
