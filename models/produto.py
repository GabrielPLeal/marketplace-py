class Produto:

    contador: int = 1

    def __init__(self, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco

    def __str__(self) -> str:
        return f"Código: {self.codigo} \nNome: {self.nome} \nPreço: {self.preco}"

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @preco.setter
    def preco(self, value):
        self.__preco = value
