from typing import List, TYPE_CHECKING
from excecoes import ErroSaldoInsuficiente, ErroValorInvalido
from models.Conta import Conta
from models.Transacao import Transacao
from models.abstratas.Tributavel import Tributavel

if TYPE_CHECKING:
    from models.Cliente import Cliente
    from models.Transacao import Transacao

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

    def depositar(self, valor: float):
        self._validar_valor(valor)
        self._saldo += valor
        self._transacoes.append(Transacao("Depósito", valor, self))

    def sacar(self, valor: float):
        self._validar_valor(valor)
        valor_total = valor + self._taxaSaque
        disponivel = self._saldo + self._limite

        if valor_total > disponivel:
            raise ErroSaldoInsuficiente(self._saldo, self._limite, valor_total)

        self._saldo -= valor_total
        if self._saldo < 0:
            deficit = abs(self._saldo)
            self._saldo = 0.0
            self._limite = max(0.0, self._limite - deficit)

        self._transacoes.append(Transacao("Saque", valor, self))

    def obterValorImposto(self):
        """Retorna 1% do saldo disponível como valor de imposto."""
        return max(self._saldo * 0.01, 0.0)

    