#coding: utf-8

'''
EXERCICIO 10 - Capitulo 03.
João Papo-de-Pescador, homem de bem, comprou um computador
para controlar o rendimento diário de seu trabalho. Toda vez que ele traz
um peso de peixes maior que o estabelecido pelo regulamento de pesca
do estado de São Paulo (50 quilos) deve pagar um multa de
R$ 4,00 por quilo excedente João precisa que você faça um
programa que leia a variável P (peso de peixes) e verifique se há
excesso. Se houver, gravar na variável E (Excesso) e na variável
M o valor da multa que João deverá pagar. Caso contrário mostrar
tais variáveis com o conteúdo ZERO.
'''

'''
Neste bloco João digita o Peso de peixes
'''

p = float(input("Digite o peso dos peixes: "))

'''
Neste bloco vamos verificar se o peso foi excedente
e realizar as operações necessárias
'''
if (p > 50):
    e = p - 50
    m = e * 4
else:
    e = 0
    m = 0

'''
Neste bloco mostramos a resposta para o usuário
'''
print("O valor do excesso é: " +str(e)+ " KG e o valor da multa é R$: " + str(m))



