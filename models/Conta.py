from abc import ABC
from typing import List, TYPE_CHECKING
from excecoes import ErroValorInvalido
from models.abstratas import Autenticavavel

if TYPE_CHECKING:
    from models.Cliente import Cliente
    from models.Transacao import Transacao


class Conta(Autenticavavel, ABC):
    def __init__(self,id:int, cliente: 'Cliente', saldo:float, senha:str) -> None:
        self._id = id
        self._cliente = cliente
        self._saldo = saldo
        self._senha = senha
        self._transacoes: List['Transacao'] = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        self._cliente = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        self._senha = valor

    @property
    def transacoes(self):
        return self._transacoes

    def autenticar(self, senha: str) -> bool:
        """Valida a senha informada pelo cliente."""
        return self._senha == senha

    @staticmethod
    def _validar_valor(valor: float) -> None:
        """Garante que o valor utilizado em operações seja positivo."""
        if valor <= 0:
            raise ErroValorInvalido(valor)
