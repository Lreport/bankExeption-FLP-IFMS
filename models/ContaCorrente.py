from models import Cliente, Conta
from abstratas import Tributavel

class ContaCorrent(Conta, Tributavel):
    def __init__(self, id:int, cliente:'Cliente', saldo:float, senha:str, limite:float) -> None:
        super().__init__(id, cliente, saldo, senha)


    def depositar(self, valor:float):
        pass

    def obterValorEmposto(self):
        pass

    