from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print(f"{''.ljust(50, '=')}\n"
          f"{' Bem-vindo(a) '.center(50, '=')}\n"
          f"{' Guaxa Shop '.center(50, '=')}\n"
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

    opcao: int = int(input('Opção: '))

    if opcao == 1:
        cadastrar_produto()
    if opcao == 2:
        listar_produtos()
    if opcao == 3:
        comprar_produto()
    if opcao == 4:
        visualizar_carrinho()
    if opcao == 5:
        fechar_pedido()
    if opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print(' Cadastro de produto '.center(50, '-'))
    print(''.ljust(50, '-'))

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto_listado = list(filter(lambda produto: produto.nome == nome, produtos))
    
    if produto_listado:
        print('Produto já está cadastrado com os seguintes dados: ')
        print(str(produto_listado[0]))
        _altera_preco_produto_listado(produto_listado[0], preco)
    else:
        produto_novo: Produto = Produto(nome=nome, preco=preco)
        produtos.append(produto_novo)
        print(f'O produto {produto_novo.nome} foi cadastrado com sucesso!')
    _volta_menu()


def listar_produtos() -> None:
    if produtos:
        print(' Listagem de produtos '.center(50, '-'))
        print(''.ljust(50, '-'))

        for produto in produtos:
            print(str(produto))
            print(''.ljust(30, '-'))
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    _volta_menu()


def comprar_produto() -> None:
    if produtos:
        print('Informe o código do produto deseja adicionar ao carrinho: ')
        print('----------------------------------------------------------')
        print(' Produtos Disponíveis '.center(58, '='))
        for produto in produtos:
            print(str(produto))
            print(''.ljust(58, '-'))
            sleep(1)
        codigo: int = int(input('Código: '))
        quantidade_produto: int = int(input('Quantidade: '))

        produto: Produto = _pega_produto_codigo(codigo)

        if produto:
            if carrinho:
                produto_contido_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)
                    if quantidade:
                        item[produto] += quantidade_produto
                        produto_contido_carrinho = True
                        print(f'O produto {produto.nome} agora possui {item[produto]} unidades no carrinho.')
                if not produto_contido_carrinho:
                    _adiciona_produto_carrinho(produto, quantidade_produto)
            else:
                _adiciona_produto_carrinho(produto, quantidade_produto)
        else:
            print(f'O produto com código {codigo} não foi encontrado')
    else:
        print('Ainda não existente produtos para vender.')
    _volta_menu()


def visualizar_carrinho() -> None:
    if carrinho:
        print(' Produtos no carrinho '.center(50, '-'))
        print(''.ljust(50, '-'))
        for item in carrinho:
            for produto, quantidade in item.items():
                print(str(produto))
                print(f'Quantidade: {quantidade}')
                print(''.ljust(30, '-'))
                sleep(1)
    else:
        print('Ainda não existente produtos no carrinho.')
    _volta_menu()


def fechar_pedido() -> None:
    if carrinho:
        print(' Fechamento do pedido '.center(50, '-'))
        print(''.ljust(50, '-'))

        valor_total: float = _calcular_valor_total()

        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    _volta_menu()


def _altera_preco_produto_listado(produto_listado: Produto, preco: float) -> None:
    alterar_preco: int = int(input('Deseja alterar o preço do produto? [1 - SIM, 2 - NÃO'))
    if alterar_preco == 1:
        produto_listado.preco = preco
        print(f'Preço do produto {produto_listado.nome} alterado para {produto_listado.preco}!')
    elif alterar_preco != 2:
        print('Opção inválida! Informe novamente!')
        _altera_preco_produto_listado(produto_listado, preco)


def _calcular_valor_total() -> float:
    print(' Produtos do carrinho '.center(50, '-'))
    print(''.ljust(50, '-'))

    valor_total: float = 0
    for item in carrinho:
        for produto, quantidade in item.items():
            valor_total += produto.preco * quantidade
            print(str(produto))
            print(f'Quantidade: {quantidade}')
            print(''.ljust(30, '-'))
            sleep(1)
    return valor_total


def _pega_produto_codigo(codigo: int) -> Produto:
    produto_codigo: Produto = list(filter(lambda produto: produto.codigo == codigo, produtos))[0]
    if produto_codigo:
        return produto_codigo


def _adiciona_produto_carrinho(produto: Produto, quantidade: int) -> None:
    item: dict = {produto: quantidade}
    carrinho.append(item)
    print(f'{quantidade} produto(s) {produto.nome} foi/foram adicionado(s) ao carrinho.')


def _volta_menu() -> None:
    sleep(2)
    menu()


if __name__ == '__main__':
    main()
