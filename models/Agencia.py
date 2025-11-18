class Agencia:
    def __init__(self, id:int, nome:str, localizacao:str, fone: str):
        self._id = id
        self._nome = nome
        self._localizacao = localizacao
        self._fone =  fone

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

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
