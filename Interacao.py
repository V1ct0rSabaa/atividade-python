from Consulta import Pessoa
from copy import deepcopy
from Armazenamento import gerar_arquivo

def entrada_dados() -> Pessoa:
    nome: str = input("Digite o nome do usuario: ")
    cpf: str = input("Digite o CPF do usuario: ")
    endereco: str = input("Digite o endereço do usuario: ")
    objeto_pessoa = Pessoa(nome, cpf, endereco)
    return objeto_pessoa

def saida_dados(lista_objetos: list[Pessoa]) -> str:
    if len(lista_objetos) == 0:
        texto = "Nenhuma pessoa foi cadastrada ainda"
    else:
        texto = "\n".join(map(str, lista_objetos))
    return texto

    
def mostrar_menu() -> None:
    menu: str = "1- adicionar usuario\n2- mostrar dados do usuario"
    menu += "\n3- gerar arquivo com dados dos usuarios\n4- sair do programa: "
    escolha = 0
    lista_pessoas: list[Pessoa] = []
    print("Bem vindo ao menu de gerenciamento dos usuários")
    while escolha != 4:
        texto_erro: str = "ERRO, digite apenas números inteiros entre 1 e 3"
        escolha = input(menu)
        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > 4:
                print(texto_erro)
            else:
                if escolha == 1:
                    lista_pessoas.append(deepcopy(entrada_dados()))
                elif escolha == 2:
                    print(saida_dados(lista_pessoas))
                elif escolha == 3:
                    print(gerar_arquivo(lista_pessoas))
                elif escolha == 4:
                    print("Fim do programa")
        except ValueError or TypeError:
            print(texto_erro)

mostrar_menu()