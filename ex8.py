#coding: utf-8

'''
EXERCICIO 4 - Capitulo 03.
Escreva um programa que leia um ano e mostre se ele é ou não
um ano bissexto. Um ano é bissexto se for divisível por 4,
mas não por 100. Um ano também é bissexto se for divisível
por 400.
'''

'''
Neste bloco o usuário digita o ano
'''

ano = int(input("Digite a idade: "))

'''
Neste bloco vamos verificar se o ano é bissexto utilizando o operador
módulo
'''

if (ano % 4 == 0 and ano % 100 != 0):
    print("O ano digitado é bissexto")
elif(ano % 400 == 0):
    print("O ano digitado é bissexto")
else:
    print("O ano digitado NÃO é bissexto")