#coding: utf-8

'''
EXERCICIO 1 - Capitulo 02.
Faça um programa em Python que receba a quantidade e o valor de um
produto, vendido, ao final o programa deverá exibir o total recebido pela
venda do produto.
'''
'''
Definimos a variavel quantidade como um valor inteiro utilizando a função int()
'''
quantidade = int(input("Digite a quantidade de produto:"))

'''
Definimos a variavel valor como um valor float utilizando a função float()
'''
valor = float(input("Digite o valor do produto: "))

'''
Realizamos o valor do Total
'''
total = valor * quantidade

'''
Imprimimos um texto para o usuario e transformamaos a variavel total em uma 
string utilizando a função str()
'''
print("O valor total da venda é: " + str(total))