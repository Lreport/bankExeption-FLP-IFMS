from datetime import datetime
from models import Conta

class Transacao:
    def __init__(self, tipo:str, valor:float, conta: 'Conta'):
        self._tipo = tipo
        self._valor = valor
        self._conta = conta
        self._data = datetime.now()

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, valor):
        self._conta = valor

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, valor):
        self._data = valor


    def obterComprovante(self):
        print(f'Data: {self._data}')
        print(f'Tpo: {self._tipo}')
        print(f'Valor: R${self._valor:.2f}')
