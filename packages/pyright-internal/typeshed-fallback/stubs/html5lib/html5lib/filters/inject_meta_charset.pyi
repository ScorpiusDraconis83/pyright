from . import base

class Filter(base.Filter):
    encoding: str | None
    def __init__(self, source, encoding: str | None) -> None: ...
    def __iter__(self): ...
