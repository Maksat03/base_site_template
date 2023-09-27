from base_object_presenter.permission_classes import NoPermission, IsAdmin
from base_object_presenter.views import BaseViewsPresenter
from .services import RequestServicesPresenter


class RequestViewsPresenter(BaseViewsPresenter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.services = RequestServicesPresenter()
        self.permissions = {
            "get_many": [IsAdmin],
            "add": [NoPermission],
            "update_fields": [IsAdmin]
        }
