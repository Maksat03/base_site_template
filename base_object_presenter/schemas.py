from rest_framework import serializers


class BaseGetManyRequestSchema(serializers.Serizalizer):
    order_by = serializers.CharField(max_length=50, default="-id", required=False)
    filtration = serializers.JSONField(required=False)
    # TODO: implement getting by 50 and 50 each time, also related with order by and filtration (last_obj_id for ex.)


class BaseGetRequestSchema(serializers.Serizalizer):
    id = serializers.IntegerField()
