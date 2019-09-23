#coding: utf-8

'''
EXERCICIO 6 - Capitulo 03.
Escreva um programa que leia a velocidade de um veículo, se
ele ultrapassar 80km/h, envie uma mensagem informando que ele
foi multado e o valor da multa que corresponde a R$ 15,00 por km
ultrapassado.
'''

'''
Neste bloco o usuário digita a velocidade
'''

velocidade = int(input("Digite a velocidade: "))

'''
Neste bloco vamos verificar se a velcoidade é maior que 80km e calcular o valor da 
multa
'''

if (velocidade > 80):
    totalUltrapasssado = velocidade - 80
    valorMulta = totalUltrapasssado * 15

    print("Você foi multado no valor de: R$" +str(valorMulta))
else:
    print("Você não foi multado.")