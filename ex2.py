#coding: utf-8
'''
EXERCICIO 2 - Capitulo 02.
Crie um programa que receba a largura e o comprimento de um lote de terra e
mostre a área total existente.
'''

'''
Neste primeiro bloco definimos a entrada de dados, nas variaveis
largura e comprimento, utilizamos a função float() para dizer ao 
computador que nossos dados serão do tipo float(numeros com numeros após a virgula)
'''
largura = float(input("Digite a largura do lote: "))
comprimento = float(input("Digite o comprimento do lote: "))

'''
Aqui realizamos o calculo da area, por isto declaramos a variavel area
'''
area = largura * comprimento

'''
Imprimimos um texto para o usuario e transformamaos a variavel area em uma 
string utilizando a função str()
'''
print("A area total é: " + str(area) )