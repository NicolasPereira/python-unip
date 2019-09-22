#coding: utf-8
'''
EXERCICIO 4 - Capitulo 02.
Uma determinada pessoa que trabalha com a construção de piscina precisa de
um programa que calcule o valor das construções solicitadas pelos clientes,
sabendo-se que os clientes sempre fornecem o comprimento, a largura e a
profundidade da piscina a ser construída. Leve em consideração que o valor
da construção é cobrado por metro cúbico de água que a piscina conterá e o
preço é R$45.000 por metro cúbico.
'''

'''
Neste bloco vamos receber os valores de comprimento, largura e profundidade.
Os valores podem ser numeros com virgula por isso vamos utilizar a função float()
'''

comprimento = float(input("Digite o valor do comprimento da piscina: "))
largura = float(input("Digite o valor da largura da piscina: "))
profundidade = float(input("Digitie o valor de profundidade da piscina: "))


'''
Aqui vamos realizar o calculo de quantos metros cubicos a piscina possui
e o valor total do Orçamento.
'''

metroCubicos = comprimento * largura * profundidade
orcamento = metroCubicos * 45000

'''
No bloco abaixo vamos mostrar ao usuário as informações
da piscina e quantos metrosCubicos a piscina possui, logo
depois o valor do orçamento
'''

print("A piscina possui: " + str(comprimento) + " metros de comprimentos e tem " + str(largura)+" metros de largura e "+str(profundidade)+ " metros de profundidade")
print("A piscina tem " +str(metroCubicos) + " metros cubicos")
print("O valor total da piscina é de R$" +str(orcamento))