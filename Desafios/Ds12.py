preço = float(input('Qual o valor do produto RS'))
novo = preço - (preço* 5 /100)
print('O produto que custava R${} estara custando R${} na promoção !'.format(preço, novo))
