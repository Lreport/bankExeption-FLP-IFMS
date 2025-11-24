# ===================================================================
# ARQUIVO: excecoes.py
# Define as exceções personalizadas da aplicação
# ===================================================================

class ErroValidacao(Exception):
    """Exceção base para erros de validação."""
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class ErroIdadeInvalida(ErroValidacao):
    """Lançada quando uma idade inválida (ex: negativa) é fornecida."""
    def __init__(self, idade, mensagem="Idade inválida fornecida."):
        self.idade = idade
        self.mensagem = f"{mensagem} (Idade fornecida: {self.idade})"
        super().__init__(self.mensagem)

class ErroSaldoInsuficiente(ErroValidacao):
    """Lançada ao tentar sacar um valor maior que o disponível."""
    def __init__(self, saldo, limite, valor_saque, mensagem="Saldo insuficiente para o saque."):
        self.saldo = saldo
        self.limite = limite
        self.valor_saque = valor_saque
        self.disponivel = saldo + limite
        self.mensagem = (f"{mensagem} | Saldo: R${saldo:.2f}, Limite: R${limite:.2f}, "
                        f"Disponível: R${self.disponivel:.2f}, Saque Desejado: R${valor_saque:.2f}")
        super().__init__(self.mensagem)

class ErroValorInvalido(ErroValidacao):
    """Lançada ao tentar depositar ou sacar um valor não positivo."""
    def __init__(self, valor, mensagem="O valor da operação deve ser positivo."):
        self.valor = valor
        self.mensagem = f"{mensagem} (Valor fornecido: {valor})"
        super().__init__(self.mensagem)