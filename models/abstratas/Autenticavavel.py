from abc import ABC, abstractmethod


class Autenticavel(ABC):
    @abstractmethod
    def autenticar(self, senha:str) -> bool:
        pass