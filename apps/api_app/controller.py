from apps.api_app.views import index
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.renderers import JSONRenderer


class Controller:
    @extend_schema(
        description="This is the description of the endpoint",
        responses={
            200: "OK",
            400: "Bad Request",
            404: "Not Found",
        },
    )
    @api_view(["GET"])
    @renderer_classes([JSONRenderer])  # Use JSONRenderer for this view

    def get(request: Request) -> Response:
        """
        A simple view function that returns a Hello, World! response.
        """
        return index(request)