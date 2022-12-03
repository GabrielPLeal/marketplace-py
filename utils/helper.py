from typing import List, Dict, Callable
from time import sleep

from models.product import Product


def format_money_float_str(valor: float) -> str:
    return f"R$ {valor:,.2f}"

def change_listed_product_price(listed_product: Product, price: float) -> None:
    alter_price: int = int(input('Deseja alterar o preço do produto? [1 - SIM, 2 - NÃO'))
    if alter_price == 1:
        listed_product.price = price
        print(f'Preço do produto {listed_product.name} alterado para {listed_product.price}!')
    elif alter_price != 2:
        print('Opção inválida! Informe novamente!')
        change_listed_product_price(listed_product, price)

def calc_total_value(cart: List[Dict[Product, int]]) -> float:
    print(' Products do carrinho '.center(50, '-'))
    print(''.ljust(50, '-'))

    total_value: float = 0
    for item in cart:
        for product, quantity in item.items():
            total_value += product.price * quantity
            print(str(product))
            print(f'Quantidade: {quantity}')
            print(''.ljust(30, '-'))
            sleep(1)
    return total_value

def take_product_code(code: int, products: List[Product]) -> Product:
    product: List = list(filter(lambda product: product.code == code, products))
    if product:
        return product[0]

def take_product_index_in_cart(product: Product, cart: List[Dict[Product, int]]) -> int:
    for index, item in enumerate(cart):
        if item.get(product):
            return index

def adding_product_in_cart(product: Product, quantity: int, cart: List[Dict[Product, int]]) -> None:
    item: dict = {product: quantity}
    cart.append(item)
    print(f'{quantity} produto(s) {product.name} foi/foram adicionado(s) ao carrinho.')

def back_home(home: Callable) -> None:
    sleep(2)
    home()
