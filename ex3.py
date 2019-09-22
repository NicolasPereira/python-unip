#coding: utf-8
'''
EXERCICIO 3 - Capitulo 02.
Crie um programa que receba quatro valores quaisquer e mostre a média entre
eles, o somatório entre eles e o resto da divisão do somatório por cada um
dos valores.
'''

'''
Neste bloco recebemos os 4 valroes e definimos eles como inteiros através
da função int()
'''
valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))
valor3 = int(input("Digite o valor 3: "))
valor4 = int(input("Digite o valor 4: "))

'''
Neste bloco realizamos o calculo do somatorio total e da media dos valores
'''
somaTotal = valor1 + valor2 + valor3 + valor4
media = somaTotal / 4

'''
Neste bloco realizamos os calculos para mostrar o resto da divisão.
Vamos utilizar o operador de módulo (%) para realizar esta tarefa
'''
resto1 = somaTotal % valor1
resto2 = somaTotal % valor2
resto3 = somaTotal % valor3
resto4 = somaTotal % valor4


'''
No bloco abaixo vamos apenas imprimir na tela os resultados necessários
transformando todos os valores em string utilizando a função str()
'''
print("O valor do somatório dos numeros é: " + str(somaTotal))
print("O valor da media dos numeros é: " +str(media))
print("O valor do resto da divisão do somatório pelo primeiro numero é:" +str(resto1))
print("O valor do resto da divisão do somatório pelo segundo numero é:" +str(resto2))
print("O valor do resto da divisão do somatório pelo terceiro numero é:" +str(resto3))
print("O valor do resto da divisão do somatório pelo quarto numero é:" +str(resto4))
