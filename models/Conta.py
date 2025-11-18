from abc import ABC
from typing import List
from models import Transacao, Cliente
from models.abstratas import Autenticavavel


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
