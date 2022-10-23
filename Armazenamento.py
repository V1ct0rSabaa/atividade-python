from Consulta import Pessoa

def gerar_arquivo(lista_objetos: list[Pessoa]) -> str:
    texto: str = ""
    nome_arquivo: str = "dados_usuario.txt"
    if len(lista_objetos) == 0:
            texto = "Nenhuma pessoa foi cadastrada ainda"
    else:
        with open(nome_arquivo, "w+") as arquivo:
            arquivo.writelines("".join(map(str, lista_objetos)))
            texto = f"O arquivo {nome_arquivo} foi criado"
    return texto