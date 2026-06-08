from typing import Protocol, Text

class ILogger(Protocol):
    def info(self, mensaje: Text) -> None:
        ...
    def error(self, mensaje: Text) -> None:
        ...
