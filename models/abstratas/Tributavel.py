from abc import ABC, abstractmethod

class Tributavel(ABC):
    @abstractmethod
    def obterValorImposto(self) -> float:
        pass

    