from base_object_presenter.urls import BaseURLsPresenter
from .views import CaseViewsPresenter


class CaseURLsPresenter(BaseURLsPresenter):
    views = CaseViewsPresenter()


urlpatterns = CaseURLsPresenter().get_urlpatterns()
