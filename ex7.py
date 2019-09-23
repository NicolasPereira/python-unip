#coding: utf-8

'''
EXERCICIO 3 - Capitulo 03.
Escreva um programa que receba dois números e um sinal, e
faça a operação matemática definida pelo sinal.
'''

'''
Neste bloco vamos receber os 2 valores e o sinal
'''

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print("Os sinais de operações são:")
print("adição: +")
print("subtração: -")
print("multiplicação: *")
print("divisão: /")
sinal = input("Digite o sinal da operação")

'''
Vamos verificar qual o sinal que o usuário digitou
e realizar a operação
'''

if(sinal == "+"):
    resultado = num1 + num2
    print("O resultado da soma é: " + str(resultado))
elif(sinal == "-"):
    resultado = num1 - num2
    print("O resultado da substração é: " +str(resultado))
elif(sinal == "*"):
    resultado = num1 * num2
    print("O resultado da multiplicação é: "+str(resultado))
elif(sinal == "/"):
    resultado = num1 / num2
    print("O resultado da divisão é: " + str(resultado))
else:
    print("ERRO: Digite uma operação valida")