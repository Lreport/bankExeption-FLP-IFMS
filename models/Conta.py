from abc import ABC
from models.Cliente import Cliente
from models.abstratas import Autenticavavel


class Conta(Autenticavavel, ABC):
    def __init__(self,id:int, cliente: 'Cliente', saldo:float, senha:str) -> None:
        pass