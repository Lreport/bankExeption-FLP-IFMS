from abc import ABC, abstractmethod

class Rentavel(ABC):
    @abstractmethod
    def obterRendimento(self) -> float:
        pass