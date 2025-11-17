#talvez criar um class localizacao


from typing import List
from models.classes import Agencia


class Banco:
    def __init__(self, nome:str, cnpj:str, localizacao: str, fone:str) -> None:
        self._nome = nome
        self._cnpj = cnpj
        self._localizacao = localizacao
        self._fone = fone
        self._agencias: List['Agencia'] = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, valor):
        self._cnpj = valor

    @property
    def localizacao(self):
        return self._localizacao

    @localizacao.setter
    def localizacao(self, valor):
        self._localizacao = valor

    @property
    def fone(self):
        return self._fone

    @fone.setter
    def fone(self, valor):
        self._fone = valor

    @property
    def agencias(self):
        return self._agencias

    def addAgencia(self, agencia: 'Agencia'):
        if isinstance(agencia, Agencia):
            self._agencias.append(agencia)
            print('Agencia adcionada com sucesso.')
        if agencia nao e agencia:
            print('Objeto fornecido nao é agencia')

    def mostrarAgencia(self, agencia: 'Agencia'):
        print(f'Agencia do {self._nome}')
        for agencia in self._agencias:
            print(f'Agência: {agencia.nome} ({agencia.localizacao})')