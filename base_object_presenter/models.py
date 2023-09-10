from django.db import models


class BaseModelPresenter(models.Model):
    @staticmethod
    def get_many_service():
        return {
            "prefetch_related": [""],
            "related_name": [""],
            "annotate": {""},
            "only": [""],
        }

    @staticmethod
    def get_service():
        return {
            "prefetch_related": [""],
            "related_name": [""],
            "annotate": {""},
            "only": [""],
        }

    @staticmethod
    def get_object_serializer_fields():
        return "__all__"

    @staticmethod
    def get_object_serializer_extra_fields():
        return {}

    @staticmethod
    def object_form_serializer_update(instance, validated_data):
        BaseModelPresenter.objects.filter(id=instance.id).update(**validated_data)

    @staticmethod
    def object_form_serializer_create(validated_data):
        BaseModelPresenter.objects.create(**validated_data)

    @staticmethod
    def get_object_form_serializer_fields():
        return "__all__"

    @staticmethod
    def get_object_form_serializer_extra_fields():
        return {}

    @staticmethod
    def get_objects_serializer_extra_fields():
        return {}

    @staticmethod
    def get_objects_serializer_fields():
        return "__all__"
