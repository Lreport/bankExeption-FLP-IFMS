import datetime
from models.Conta import Cliente, Conta
from models.abstratas import Rentavel


class ContaPoupanca(Conta, Rentavel):
    def __init__(self, id: int, titular: 'Cliente', saldo: float, senha: str, rendimentoAnual: float) -> None:
        super().__init__(id, titular, saldo, senha)
        self._rendimentoAnual = rendimentoAnual
        self._dataAniversario = datetime.now().day

    def obterRendimento(self):
        pass

    def sacar(self):
        pass

    def depositar(self):
        pass