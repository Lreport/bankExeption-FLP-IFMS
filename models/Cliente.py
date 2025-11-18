from typing import List
from models import Conta


class Cliente:
    def __init__(self, nome:str, idade:int) -> None:
        self._nome = nome
        self._idade = idade
        self._contas: List['Conta'] = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @property
    def contas(self):
        return self._contas
