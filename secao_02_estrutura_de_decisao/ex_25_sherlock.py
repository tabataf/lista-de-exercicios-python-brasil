"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""


<<<<<<< HEAD
from telnetlib import NAOCRD
import oauthlib


def investivar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):
=======
def investigar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):
>>>>>>> main
    """Escreva aqui em baixo a sua solução"""

    if telefonou == 'Sim':
        if estava_no_local == 'Sim':
            if mora_perto == 'Sim':
                if devia == 'Sim':
                    if trabalhou == 'Sim':
                        print("'Assassino'")
    if telefonou == 'Sim':
        if estava_no_local == 'Sim':
            if mora_perto == 'Sim':
                if devia == 'Sim' or 'Não':
                    if trabalhou == 'Não':
                        print("'Cúmplice'")

    if telefonou == 'Sim':
        if estava_no_local == 'Sim':
            if mora_perto == 'Não':
                        print("'Suspeito'")
    if telefonou == 'Sim' and estava_no_local !='Sim':
        print("'Inocente'")
    if telefonou =='Não':
        print("'Inocente'")