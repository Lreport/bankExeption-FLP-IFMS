from typing import Dict, Tuple

from excecoes import ErroIdadeInvalida, ErroSaldoInsuficiente, ErroValorInvalido
from models.Cliente import Cliente
from models.ContaCorrente import ContaCorrente
from models.ContaPoupanca import ContaPoupanca


def configurar_sistema() -> Tuple[Cliente, Dict[str, ContaCorrente]]:
    """Cria um cenário básico com cliente e duas contas para testes."""
    cliente = Cliente("Fernanda", 32)
    conta_corrente = ContaCorrente(id=1, cliente=cliente, saldo=1500.0, senha="1234", limite=600.0)
    conta_poupanca = ContaPoupanca(id=2, titular=cliente, saldo=2500.0, senha="1234", rendimentoAnual=0.06)

    cliente.contas.append(conta_corrente)
    cliente.contas.append(conta_poupanca)

    return cliente, {"corrente": conta_corrente, "poupanca": conta_poupanca}


def solicitar_valor(operacao: str) -> float:
    """Lê um valor numérico do teclado, tratando erros de conversão."""
    while True:
        try:
            valor = float(input(f"Informe o valor para {operacao}: ").replace(",", "."))
            return valor
        except ValueError:
            print("Entrada inválida. Utilize apenas números (ex: 150.75).")


def autenticar_conta(conta) -> bool:
    """Solicita a senha da conta com até três tentativas."""
    tentativas = 3
    while tentativas > 0:
        senha = input("Digite sua senha: ")
        if conta.autenticar(senha):
            return True
        tentativas -= 1
        print(f"Senha incorreta. Tentativas restantes: {tentativas}")
    print("Número de tentativas excedido.")
    return False


def escolher_conta(contas: Dict[str, ContaCorrente]):
    """Permite alternar entre conta corrente e poupança."""
    while True:
        print("\nSelecione a conta:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        escolha = input("Opção: ")
        if escolha == "1":
            return contas["corrente"]
        if escolha == "2":
            return contas["poupanca"]
        print("Opção inválida.")


def exibir_transacoes(conta) -> None:
    """Mostra o histórico básico de transações."""
    if not conta.transacoes:
        print("Nenhuma transação registrada.")
        return
    for transacao in conta.transacoes:
        print(f"- {transacao.data.strftime('%d/%m %H:%M')} | {transacao.tipo} | R${transacao.valor:.2f}")


def exibir_menu(conta) -> None:
    """Mostra o menu principal."""
    print("\n==============================")
    print(f"Operando com a conta #{conta.id} ({conta.__class__.__name__})")
    print(f"Saldo: R${conta.saldo:.2f}")
    if hasattr(conta, "limite"):
        print(f"Limite: R${conta.limite:.2f}")
    print("==============================")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver transações")
    print("4 - Trocar de conta")
    print("5 - Sair")


def loop_principal():
    try:
        cliente, contas = configurar_sistema()
    except ErroIdadeInvalida as erro:
        print(f"Falha ao criar cliente: {erro}")
        return

    conta_atual = contas["corrente"]
    print(f"Bem-vindo(a), {cliente.nome}! Sistema inicializado com sucesso.")

    while True:
        exibir_menu(conta_atual)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = solicitar_valor("depositar")
            try:
                conta_atual.depositar(valor)
                print("Depósito realizado com sucesso.")
            except ErroValorInvalido as erro:
                print(f"Operação cancelada: {erro}")

        elif opcao == "2":
            if not autenticar_conta(conta_atual):
                continue
            valor = solicitar_valor("sacar")
            try:
                conta_atual.sacar(valor)
                print("Saque realizado com sucesso.")
            except (ErroValorInvalido, ErroSaldoInsuficiente) as erro:
                print(f"Operação cancelada: {erro}")

        elif opcao == "3":
            exibir_transacoes(conta_atual)

        elif opcao == "4":
            conta_atual = escolher_conta(contas)
            print(f"Você agora está utilizando a conta #{conta_atual.id}.")

        elif opcao == "5":
            print("Obrigado por utilizar o sistema bancário. Até logo!")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    loop_principal()

