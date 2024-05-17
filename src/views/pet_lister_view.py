from src.controllers.pet_lister_controller import PetListerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self._controller.list()
        return HttpResponse(status_code=200, body=body_response)
