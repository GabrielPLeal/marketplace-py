from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import (
   format_money_float_str,
   change_listed_product_price,
   calc_total_value,
   take_product_code,
   take_product_index_in_cart,
   adding_product_in_cart,
   back_home
)

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    home()

def home() -> None:
    print(
        f"{''.ljust(50, '=')}\n"
        f"{' Bem-vindo(a) '.center(50, '=')}\n"
        f"{' Leal Shop '.center(50, '=')}\n"
        f"{''.ljust(50, '=')}\n"
        f"\n"
        f"Selecione uma opção abaixo: \n"
        f"1 - Cadastrar produto \n"
        f"2 - Listar produto \n"
        f"3 - Comprar produto \n"
        f"4 - Visualizar carrinho \n"
        f"5 - Fechar pedido \n"
        f"6 - Sair do sistema \n"
    )

    option: int = int(input('Opção: '))

    if option == 1:
        register_product()
    if option == 2:
        list_products()
    if option == 3:
        buy_product()
    if option == 4:
        view_cart()
    if option == 5:
        close_request()
    if option == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        home()

def register_product() -> None:
    print(' Cadastro de produto '.center(50, '-'))
    print(''.ljust(50, '-'))

    name: str = input('Informe o nome do produto: ')
    price: float = float(input('Informe o preço do produto: '))

    listed_product = list(filter(lambda product: product.name == name, products))
    
    if listed_product:
        print('Produto já está cadastrado com os seguintes dados: ')
        print(str(listed_product[0]))
        change_listed_product_price(listed_product[0], price)
    else:
        new_product: Product = Product(name=name, price=price)
        products.append(new_product)
        print(f'O produto {new_product.name} foi cadastrado com sucesso!')
    back_home(home)

def list_products() -> None:
    if products:
        print(' Listagem de produtos '.center(50, '-'))
        print(''.ljust(50, '-'))

        for product in products:
            print(str(product))
            print(''.ljust(30, '-'))
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    back_home(home)

def buy_product() -> None:
    if products:
        print('Informe o código do produto deseja adicionar ao carrinho: ')
        print('----------------------------------------------------------')
        print(' Produtos Disponíveis '.center(58, '='))

        for product in products:
            print(str(product))
            print(''.ljust(58, '-'))
            sleep(1)

        code: int = int(input('Código: '))
        quantity: int = int(input('Quantidade: '))

        product: Product = take_product_code(code, products)

        if product:
            index: int = take_product_index_in_cart(product, cart)
            if index:
                cart[index][product] += quantity
                print(f'O produto {product.name} agora possui {cart[index][product]} unidades no carrinho.')
            else:
                adding_product_in_cart(product, quantity, cart)
        else:
            print(f'O produto com código {code} não foi encontrado')
    else:
        print('Não há produtos disponíveis para compra.')
    back_home(home)

def view_cart() -> None:
    if cart:
        print(' Products no carrinho '.center(50, '-'))
        print(''.ljust(50, '-'))
        for item in cart:
            for produto, quantidade in item.items():
                print(str(produto))
                print(f'Quantidade: {quantidade}')
                print(''.ljust(30, '-'))
                sleep(1)
    else:
        print('Nenhum produto no carrinho.')
    back_home(home)

def close_request() -> None:
    if cart:
        print(' Fechamento do pedido '.center(50, '-'))
        print(''.ljust(50, '-'))

        total_value: float = calc_total_value(cart)

        print(f'Sua fatura é {format_money_float_str(total_value)}')
        print('Volte sempre!')
        cart.clear()
        sleep(5)
    else:
        print('Nenhum produto no carrinho.')
    back_home(home)

if __name__ == '__main__':
    main()
