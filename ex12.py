#coding: utf-8

'''
EXERCICIO 8 - Capitulo 03.
Construa um programa para ler uma variável numérica N.
Mostre a variável somente se ela for maior que 100, caso contrário
mostre o valor zero.
'''

'''
Neste bloco o usuário digita um numero
'''

numero = int(input("Digite um valor: "))


'''
Neste bloco verificamos se o numero é maior que 100
'''

if(numero >= 100):
    print(numero)
else:
    print(0)