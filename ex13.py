#coding: utf-8

'''
EXERCICIO 9 - Capitulo 03.
Escreva um programa que leia três valores inteiros diferentes e
mostre-os em ordem crescente.
'''

'''
Neste bloco o usuário digita os 3 numeros
'''

numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite um valor: "))
numero3= int(input("Digite um valor: "))

'''
Neste bloco verificamos quais são os numeros e colocamos na ordem crescente
'''

if(numero1 < numero2 and numero1 < numero3):
    if(numero2 < numero3):
        print(str(numero1) + " " + str(numero2) + " " + str(numero3))
    else:
        print(str(numero1) + " " + str(numero3) + " " + str(numero2))
elif(numero2 < numero3):
    if(numero1 < numero3):
        print(str(numero2) + " " + str(numero1) + " " + str(numero3))
    else:
        print(str(numero2) + " " + str(numero3) + " " + str(numero1))
else:
    if(numero1 < numero2):
        print(str(numero3) + " " + str(numero1) + " " + str(numero2))
    else:
        print(str(numero3) + " " + str(numero2) + " " + str(numero1))


