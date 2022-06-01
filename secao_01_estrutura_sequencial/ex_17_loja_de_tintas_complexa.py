"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
 quadrados da área a ser pintada. --
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
 que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 
situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere 
latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""



import math


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""

    area_pintura = int(input('Digite o valor da área em metros quadrados a ser pintada: '))
    cobertura_tinta= 6
    qtd_litros= math.ceil((area_pintura*1.1)/cobertura_tinta)

    #latas
    lata_litro= 18
    lata_valor= 80
    compra_lata= math.ceil(qtd_litros/ lata_litro)
    valor_total_lata= (compra_lata*lata_valor)
    sobra_lata= (compra_lata *lata_litro)-qtd_litros

    #galoes
    galao_litro= 3.6
    galao_valor= 25
    compra_galao=math.ceil(qtd_litros/galao_litro)
    valor_total_galao=(compra_galao*galao_valor)
    sobra_galao= (compra_galao*galao_litro)-qtd_litros

    #menor custo tinta lata
    compra_lata_otimizada= math.floor(qtd_litros/lata_litro)
    valor_lata_otimizado= compra_lata_otimizada*lata_valor
    sobra_tinta_lata= qtd_litros/(valor_lata_otimizado*lata_litro)

    #menor custo tinta galao
    compra_galao_otimizada= math.ceil(sobra_tinta_lata/galao_litro)
    valor_galao_otimizado= compra_galao_otimizada*galao_valor
    sobra_tinta_galao=(valor_galao_otimizado*galao_litro) - sobra_tinta_lata

    #valor geral
    valor_total_geral= valor_galao_otimizado + valor_lata_otimizado

    teste= (qtd_litros-(compra_lata_otimizada*lata_litro)-(compra_galao_otimizada*galao_litro))
    teste2= teste * (-1)
    
    print(f'Você deve comprar {qtd_litros:.0f} litros de tinta.')
    print(f'Você pode comprar {compra_lata} lata(s) de 18 litros a um custo de R$ {valor_total_lata}. Vão sobrar {sobra_lata:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {compra_galao} lata(s) de 3.6 litros a um custo de R$ {valor_total_galao}. Vão sobrar {sobra_galao:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {compra_lata_otimizada} lata(s) de 18 litros e {compra_galao_otimizada} galão(ões) de 3.6 litros a um custo de R$ {valor_total_geral}. Vão sobrar {teste2} litro(s) de tinta.')

    

