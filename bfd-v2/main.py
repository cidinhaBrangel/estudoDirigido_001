# maun.py
from funcoes import exibir_menu, cadastrar, listar


def main():
    itens = []
    print("===App de itens (BFD 2.0)===")
    while True:
        exibir_menu()
        opcao = input("Escolha:").strip()
        if opcao == "1":
            cadastrar(itens)

        elif opcao == "2":
            listar(itens)
        elif opcao == "0":
            print("Ate´mais!")
            break
        else:
            print("opcao invalida.")

            if __name__ == "__main__":
                main()
