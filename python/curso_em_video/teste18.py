"""import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarta aluno: "))
lista =  [n1, n2, n3, n4]
escolhido = random.choice(lista)
print ("O Aluno escolhido foi {}".format(escolhido))//////
Forma que importa toda a biblioteca do random para ser usado
"""

#mssaneira que importa um função especifica do random,
# o choice que seleciona itens de uma lista

from random import choice
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarta aluno: "))
lista = [n1, n2, n3, n4]

escolhido = choice (lista)
print ("Aluno escolhido foi {}".format(escolhido))