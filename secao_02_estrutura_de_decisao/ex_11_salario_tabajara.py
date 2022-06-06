"""
Exercício 11 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.

Mostrar valores monetários com duas casas decimais.

    >>> calcular_aumento(100)
    Salário atual: R$ 100.00
    Aumento porcentual: 20%
    Valor do aumento: R$ 20.00
    Novo salário: R$ 120.00
    >>> calcular_aumento(300)
    Salário atual: R$ 300.00
    Aumento porcentual: 15%
    Valor do aumento: R$ 45.00
    Novo salário: R$ 345.00
    >>> calcular_aumento(800)
    Salário atual: R$ 800.00
    Aumento porcentual: 10%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 880.00
    >>> calcular_aumento(1600)
    Salário atual: R$ 1600.00
    Aumento porcentual: 5%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 1680.00

"""


def calcular_aumento(salario: float):
  """Escreva aqui em baixo a sua solução"""
  
  """#salario atual
  if salario <=280:
    print
  elif salario >280 and salario <=700:
    print
  elif salario >700 and salario <=1500:
    print
  elif salario >1500:
  
   print(f'Salário atual: {salario:.2f}')

   #salario com aumento
  salario_baixo= salario * 0.2
  salario_medio= salario * 0.15
  salario_alto= salario * 0.1
  salario_muito_alto= salario * 0.05


  #apenas aumento
  if salario_baixo :
    print(f'Aumento porcentual: 20%')
    print(f'Valor do aumento: {salario_baixo}')

  elif salario_medio:
    print(f'Aumento porcentual: 15%')
    print(f'Valor do aumento: {salario_medio}')

  elif salario_medio:
    print(f'Aumento porcentual: 10%')
    print(f'Valor do aumento: {salario_alto}')

  else:
    print(f'Aumento porcentual: 5%')
    print(f'Valor do aumento: {salario_muito_alto}')"""



  if salario <=280:
    aumento_percentual= 20
  elif 280 < salario <=700: 
    aumento_percentual= 15
  elif 700 < salario <=1500:
    aumento_percentual= 10
  else:
    aumento_percentual= 5

  valor_aumento= salario * (aumento_percentual/100)
  novo_salario= salario + valor_aumento

  print(f'Salário atual: R$ {salario:.2f}')
  print(f'Aumento porcentual: {aumento_percentual}%')
  print(f'Valor do aumento: R$ {valor_aumento:.2f}')
  print(f'Novo salário: R$ {novo_salario:.2f}')
