from re import A


a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Esta em maiusculas? ', a.isupper())
print('Esta em minusculas? ', a.islower())
print('Esta captalizada? ', a.istitle())