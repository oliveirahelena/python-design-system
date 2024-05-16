class HttpResponse:
    def __init__(self, status_code: int, body: dict = None) -> None:
        self._status_code = status_code
        self._body = body
