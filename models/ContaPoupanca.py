from datetime import datetime
from typing import TYPE_CHECKING
from excecoes import ErroSaldoInsuficiente, ErroValorInvalido
from models.Conta import Conta
from models.Transacao import Transacao
from models.abstratas.Rentavel import Rentavel

if TYPE_CHECKING:
    from models.Cliente import Cliente


class ContaPoupanca(Conta, Rentavel):
    def __init__(self, id: int, titular: 'Cliente', saldo: float, senha: str, rendimentoAnual: float) -> None:
        super().__init__(id, titular, saldo, senha)
        self._rendimentoAnual = rendimentoAnual
        self._dataAniversario = datetime.now().day

    @property
    def rendimentoAnual(self):
        return self._rendimentoAnual

    @rendimentoAnual.setter
    def rendimentoAnual(self, valor):
        self._rendimentoAnual = valor

    @property
    def dataAniversario(self):
        return self._dataAniversario

    @dataAniversario.setter
    def dataAniversario(self, valor):
        self._dataAniversario = valor

    def obterRendimento(self) -> float:
        """Retorna o rendimento mensal baseado no percentual anual informado."""
        rendimento_mensal = self._rendimentoAnual / 12
        return self._saldo * rendimento_mensal

    def sacar(self, valor: float):
        self._validar_valor(valor)
        if valor > self._saldo:
            raise ErroSaldoInsuficiente(self._saldo, 0.0, valor)
        self._saldo -= valor
        self._transacoes.append(Transacao("Saque", valor, self))

    def depositar(self, valor: float):
        self._validar_valor(valor)
        self._saldo += valor
        self._transacoes.append(Transacao("Depósito", valor, self))