# Dicionário que mapeia formas de pagamento para percentuais de desconto
lista_descontos_via_pagamento = {'A vista': 20, 'Parcelado 2x': 15, 'Parcelado 3x': 12, 'Parcelado 4x': 10, 'Parcelado de 5x a 12x': 0}

# Função que calcula e imprime o preço com desconto para diferentes formas de pagamento
def desconto_avista(preco):
    # Converte o preço para um número de ponto flutuante
    preco = float(preco.replace('.', ''))
    
    # Itera sobre as formas de pagamento e seus respectivos descontos
    for forma_pagamento, desconto in lista_descontos_via_pagamento.items():
        # Calcula o valor do desconto em reais
        desconto_percentual = (desconto / 100) * preco
        # Calcula o preço com desconto
        preco_com_desconto = preco - desconto_percentual

        # Imprime a informação formatada com o preço com desconto
        print(f'Pagamento: {forma_pagamento}. Produto fica R${preco_com_desconto:.2f} com {desconto}% de desconto')

# Solicita ao usuário inserir o preço do produto
preco_produto = input('Insira o preço do produto [INSIRA NUMEROS INTEIROS EX: 12,15,100]: ').replace(',', '.')
# Chama a função para calcular e imprimir os descontos
print('ok')
desconto_avista(preco_produto)
