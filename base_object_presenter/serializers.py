from rest_framework import serializers
from base_object_presenter.models import BaseModelPresenter


class ObjectsSerializer(serializers.Serializer):
    class Meta:
        def __init__(self):
            self.model = BaseModelPresenter
            self.fields = self.model.get_objects_serializer_fields()

            for field_name, field in self.model.get_objects_serializer_extra_fields().items():
                setattr(self, field_name, field)


class ObjectFormSerializer(serializers.Serializer):
    class Meta:
        def __init__(self):
            self.model = BaseModelPresenter
            self.fields = self.model.get_object_form_serializer_fields()

            for field_name, field in self.model.get_object_form_serializer_extra_fields().items():
                setattr(self, field_name, field)

    def create(self, validated_data):
        return self.Meta().model.object_form_serializer_create(validated_data)

    def update(self, instance, validated_data):
        return self.Meta().model.object_form_serializer_update(instance, validated_data)


class ObjectSerializer(serializers.Serializer):
    class Meta:
        def __init__(self):
            self.model = BaseModelPresenter
            self.fields = self.model.get_object_serializer_fields()

            for field_name, field in self.model.get_object_serializer_extra_fields().items():
                setattr(self, field_name, field)
