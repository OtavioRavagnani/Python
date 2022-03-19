import random
a1 = input('Qual o primeiro aluno ? ')
a2 = input('Qual o segundo aluno ? ')
a3 = input('Qual o terceiro aluno ? ')
a4 = input('Qual o qurto aluno ? ')
lista = [a1, a2, a3 , a4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))