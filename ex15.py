#coding: utf-8

'''
EXERCICIO 11 - Capitulo 03.
Elabore um programa que leia as variáveis C e N,
respectivamente código e número de horas trabalhadas de um
operário. E calcule o salário sabendo-se que ele ganha R$ 10,00
por hora. Quando o número de horas exceder a 50 calcule o
excesso de pagamento armazenando-o na variável E, caso
contrário zerar tal variável. A hora excedente de trabalho vale R$
20,00. No final do processamento imprimir o salário total e o
salário excedente.
'''

'''
Neste bloco vamos ler as variaveis C (código) e numero de horas trabalhadas (N)
'''

c = int(input("Digite seu codigo: "))
n = float(input("Digite suas horas trabalhadas: "))

'''
Neste bloco vamos verificar se houve hora excedente e realiza
os calculos dos salários conforme regra do enunciado
'''

if (n > 50):
    e = n - 50
    salario_excedente = e * 20
    salario_normal = (n-e) * 10
    salario_total = salario_excedente + salario_normal
    print("Ola " + str(c) + " seu salario total é: R$: " +str(salario_total)+ " sendo o salario normal R$: " +str(salario_normal) + " e R$: " +str(salario_excedente)+" de hora extra")
else:
    salario_normal = n * 10
    print("Ola " + str(c) + " seu salario total é: R$: " +str(salario_normal))