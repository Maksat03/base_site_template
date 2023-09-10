from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response

from project.utils import request_schema_validation
from .services import BaseServicesPresenter
from .schemas import BaseGetManyRequestSchema, BaseGetRequestSchema


class BaseViewsPresenter:
    schemas = {
        "get_many": BaseGetManyRequestSchema,
        "get": BaseGetRequestSchema,
    }
    services: BaseServicesPresenter

    @api_view(["GET"])
    @request_schema_validation("GET", schemas["get_many"])
    def get_many_view(self, request: Request) -> Response:
        objs = self.services.get_many(request.query_params)
        return Response(objs.data)

    @api_view(["GET"])
    @request_schema_validation("GET", schemas["get"])
    def get_view(self, request: Request) -> Response:
        obj = self.services.get(request.query_params)
        return Response(obj.data)

    @api_view(["POST"])
    @permission_classes([IsAdminUser])
    def delete_view(self, request: Request) -> Response:
        self.services.delete(request.data.get("id"))
        return Response({"success": True})

    @api_view(["POST"])
    @permission_classes([IsAdminUser])
    @parser_classes([MultiPartParser, FormParser])
    def add_view(self, request: Request) -> Response:
        obj_id = self.services.add(request.data, request.FILES)
        return Response({"obj_id": obj_id})

    @api_view(["POST"])
    @permission_classes([IsAdminUser])
    @parser_classes([MultiPartParser, FormParser])
    def edit_view(self, request: Request) -> Response:
        self.services.edit(request.data.pop("id"), request.data, request.FILES)
        return Response({"success": True})
