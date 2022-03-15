salario = float(input('Qual o salario do Funcionario ? R$'))
novo = salario + (salario * 15 / 100)
print('o funcionario que ganha {}R$ irá ganhar {} com um aumento de 15%'.format(salario, novo))