from typing import MutableMapping
from .models import BaseModelPresenter
from .serializers import BaseSerializerPresenter


class BaseServicesPresenter:
    model_presenter: BaseModelPresenter

    def __init__(self):
        self.serializers = {
            "objects": BaseSerializerPresenter(self.model_presenter, "objects"),
            "object_form": BaseSerializerPresenter(self.model_presenter, "object_form"),
            "object": BaseSerializerPresenter(self.model_presenter, "object"),
        }

    def get_many(self, get_many_request_schema: MutableMapping):
        get_many_query = self.model_presenter.get_many_service()

        objects = (self.model_presenter.model.objects
                   .prefetch_related(*get_many_query["prefetch_related"])
                   .select_related(*get_many_query["select_related"])
                   .filter(**get_many_request_schema.get("filtration", {}))
                   .annotate(**get_many_query["annotate"])
                   .order_by(get_many_request_schema.get("order_by", "-id"))
                   .only(*get_many_query["only"])
                   .distinct())

        return self.serializers["objects"](objects, many=True)

    def get(self, obj_id: int):
        get_query = self.model_presenter.get_service()

        obj = (self.model_presenter.model.objects
               .prefetch_related(*get_query["prefetch_related"])
               .select_related(*get_query["select_related"])
               .filter(id=obj_id)
               .annotate(**get_query["annotate"])
               .only(*get_query["only"])
               .first())

        return self.serializers["object"](obj)

    def delete(self, obj_id: int) -> None:
        self.model_presenter.model.objects.filter(id=obj_id).delete()

    def add(self, add_request_schema: MutableMapping) -> int:
        serializer = self.serializers["object_form"](data=add_request_schema)
        serializer.is_valid(raise_exception=True)
        return serializer.save().id

    def edit(self, obj_id: int, edit_request_schema: MutableMapping) -> None:
        obj = self.model_presenter.model.objects.filter(id=obj_id).first()
        serializer = self.serializers["object_form"](obj, data=edit_request_schema)
        serializer.is_valid(raise_exception=True)
        serializer.save()
