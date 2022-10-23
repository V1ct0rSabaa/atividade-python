
class Pessoa:
    def __init__(self, nome: str, cpf: str, endereco: str) -> None:
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @cpf.setter
    def cpf(self, novo_cpf: str) -> None:
        self._cpf = novo_cpf
    
    @property
    def endereco(self) -> str:
        return self._endereco
    
    @endereco.setter
    def endereco(self, novo_endereco: str) -> None:
        self._endereco = novo_endereco
    
    def __str__(self) -> str:
        texto: str = f"Nome: {self._nome}\nCPF: {self._cpf}\nEndereço: {self._endereco}\n"
        return texto