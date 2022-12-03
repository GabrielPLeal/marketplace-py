class Product:

    counter: int = 1

    def __init__(self, name: str, price: float) -> None:
        self.__code: int = Product.counter
        self.__name: str = name
        self.__price: float = price
        Product.counter += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"Código: {self.code} \nNome: {self.name} \nPreço: {self.price}"

    @name.setter
    def name(self, value):
        self.__name = value

    @price.setter
    def price(self, value):
        self.__price = value
