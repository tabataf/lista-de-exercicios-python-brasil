"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
Mostrar os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_15_clt_onerosa
    >>> numeros =['80', '55.62']
    >>> ex_15_clt_onerosa.input = lambda k: numeros.pop()
    >>> ex_15_clt_onerosa.calcular_assalto_no_salario()
    + Salário Bruto : 4449.60
    - IR (11%) : R$ 489.46
    - INSS (8%) : R$ 355.97
    - Sindicato ( 5%) : R$ 222.48
    = Salário Liquido : R$ 3381.70

"""


def calcular_assalto_no_salario():
    """Escreva aqui em baixo a sua solução"""
    salario_hora = float(input ('Digite o valor do salário por hora ')) 
    horas_trabalhadas = float(input ('Digite a quantidade de horas trabalhadas por mes '))
    salario_mes= (salario_hora*horas_trabalhadas) 
    desconto_ir= (salario_mes * 0.11)
    desconto_inss= (salario_mes * 0.08)
    desconto_sindicato= (salario_mes * 0.05)
    salario_liquido= (salario_mes - desconto_ir - desconto_inss - desconto_sindicato)

    print('+ Salário Bruto :','%.2f' %salario_mes)
    print('- IR (11%) : R$','%.2f' %desconto_ir)
    print('- INSS (8%) : R$','%.2f' %desconto_inss)
    print('- Sindicato ( 5%) : R$','%.2f' %desconto_sindicato)
    print('= Salário Liquido : R$','%.2f' %salario_liquido)