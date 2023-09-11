from base_object_presenter.services import BaseServicesPresenter
from .models import CaseModelPresenter


class CaseServicesPresenter(BaseServicesPresenter):
    def __init__(self):
        self.model_presenter = CaseModelPresenter()
        super().__init__()
