#coding: utf-8

'''
EXERCICIO 7 - Capitulo 03.
Escreva um programa que leia um número. Verifique se o
número é positivo ou negativo. No final mostrar o resultado.
'''

'''
Neste bloco o usuário digita um numero
'''

numero = int(input("Digite um valor: "))


'''
Neste bloco verificamos se o numero é positivo ou negativo
'''

if(numero > 0):
    print("O numero é positivo")
else:
    print("O numero é negativo")