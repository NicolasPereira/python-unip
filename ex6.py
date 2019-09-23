#coding: utf-8

'''
EXERCICIO 2 - Capitulo 03.
Faça um programa que diga se um usuário é maior ou menor
de idade.
Se for maior que 18, imprima "maior de idade".
Se for menor que 18, imprima "menor de idade".
Verifique se a idade é um numero inteiro positivo.
'''

'''
Neste bloco o usuário digita a idade
'''

idade = int(input("Digite a idade: "))

'''
Neste bloco vamos verificar se a idade é um numero positivo
e logo depois verificar se é maior ou menor que 18 anos
'''

if (idade > 0):
    if(idade >= 18):
        print("Maior de idade")
    else:
        print("Menor de idade")
else:
    print("Idade invalida, digite um numero maior que 0")