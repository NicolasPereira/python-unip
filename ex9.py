#coding: utf-8

'''
EXERCICIO 5 - Capitulo 03.
Escreva um programa que leia um número e informe se ele é par ou ímpar.
'''

'''
Neste bloco o usuário digita o numero
'''

numero = int(input("Digite um numero: "))

'''
Neste bloco vamos verificar se o numero é impar ou par utilizando o operador
módulo
'''

if (numero % 2 == 0):
    print("O numero é par")
else:
    print("o numero é impar")