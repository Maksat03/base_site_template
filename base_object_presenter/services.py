from typing import MutableMapping
from .models import BaseModelPresenter
from .serializers import ObjectSerializer, ObjectsSerializer, ObjectFormSerializer


class BaseServicesPresenter:
    model = BaseModelPresenter
    serializers = {
        "objects": ObjectsSerializer,
        "object_form": ObjectFormSerializer,
        "object": ObjectSerializer,
    }

    def get_many(self, get_many_request_schema: MutableMapping):
        get_many_query = self.model.get_many_service()

        objects = (self.model.objects
                   .prefetch_related(*get_many_query["prefetch_related"])
                   .related_name(*get_many_query["related_name"])
                   .filter(**get_many_request_schema["filtration"])
                   .annotate(**get_many_query["annotate"])
                   .order_by(get_many_request_schema["order_by"], "-id")
                   .only(*get_many_query["only"])
                   .distinct())

        return self.serializers["objects"](objects, many=True)

    def get(self, get_request_schema: MutableMapping):
        get_query = self.model.get_service()

        obj = (self.model.objects
               .prefetch_related(*get_query["prefetch_related"])
               .related_name(*get_query["related_name"])
               .filter(**get_request_schema["filtration"])
               .annotate(**get_query["annotate"])
               .order_by(get_request_schema["order_by"], "-id")
               .only(*get_query["only"])
               .first())

        return self.serializers["object"](obj)

    def delete(self, obj_id: int) -> None:
        self.model.objects.filter(id=obj_id).delete()

    def add(self, add_request_schema: MutableMapping, files: MutableMapping) -> int:
        serializer = self.serializers["object_form"](data=add_request_schema)
        serializer.is_valid(raise_exception=True)
        return serializer.save(files=files).id

    def edit(self, obj_id: int, edit_request_schema: MutableMapping, files: MutableMapping) -> None:
        obj = self.model.objects.filter(id=obj_id).first()
        serializer = self.serializers["object_form"](obj, data=edit_request_schema)
        serializer.is_valid(raise_exception=True)
        serializer.save(files=files)
