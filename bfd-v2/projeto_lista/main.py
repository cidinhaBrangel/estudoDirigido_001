
from funcoes import cadastrar, listar
itens = []
while True:
    print("\n[1] cadastrar [2] listar [0] sair")
    op = input("escolha: ").strip()
    if op == "1":
        nome = input("item:").strip()
        cadastrar(itens, nome)
    elif op == "2":
        listar(itens)
    elif op == "0":
        break
    else:
        print("opçao invalida.")
