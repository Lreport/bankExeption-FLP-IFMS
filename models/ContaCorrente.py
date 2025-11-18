from typing import List
from models import Cliente, Conta, Transacao
from abstratas import Tributavel

class ContaCorrente(Conta, Tributavel):
    def __init__(self, id:int, cliente:'Cliente', saldo:float, senha:str, limite:float):
        super().__init__(id, cliente, saldo, senha)
        self._limite = limite
        self._taxaSaque = 5.0
        self._transacoes: List['Transacao'] = []

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    @property
    def taxaSaque(self):
        return self._taxaSaque

    @taxaSaque.setter
    def taxaSaque(self, valor):
        self._taxaSaque = valor

    @property
    def transacoes(self):
        return self._transacoes

    def depositar(self, valor:float):
        pass

    def obterValorEmposto(self):
        pass

    