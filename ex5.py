#coding: utf-8

'''
EXERCICIO 1 - Capitulo 03.
Faça um aplicativo que receba três números inteiros na linha
de comando e mostre o maior dentre eles.
'''

'''
Neste bloco o usuário digita 3 numeros inteiros, utilizamos
a função int() para definir os numeros entrantes como inteiros
'''

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

'''
No bloco abaixo vamos definir a ordem dos numeros
'''

'''
Este primero bloco verifica se o num1 é maior que num2 e num3
caso seja, a variavel maior recebe o valor do num1


Caso a primeira condição não seja verdadeira este bloco sera executado
Este segundo bloco verifica se o num2 é maior que o num3 caso seja,
a variavel maior recebe o valor do num2

Caso a segunda condição não seja verdadeira este bloco sera executado
Este terceiro bloco define que o num3 é maior que os outros numeros
e a variavel maior recebe o valor de num3
'''
if(num1 > num2 and num1 > num3):
    maior = num1
elif(num2>num3):
    maior = num2
else:
    maior = num3

'''
Agora vamos apresentar o maior numero, vamos transforma-lo em uma
string utilizando a função str()
'''

print("O maior numero é:" + str(maior))