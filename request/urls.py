from base_object_presenter.urls import BaseURLsPresenter
from .views import RequestViewsPresenter


class RequestURLsPresenter(BaseURLsPresenter):
    views = RequestViewsPresenter()
    urls = ["get_many", "add", "update_fields"]


urlpatterns = RequestURLsPresenter().get_urlpatterns()
