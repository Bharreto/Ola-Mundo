# Vamos pedir o valor original do produto
valor_original = float( input("Preço do prodtuo: R$ ") )

# Desconto ganho de 20%
valor_descontado = valor_original * 0.05

# Valor com desconto incluso
novo_valor = valor_original * 0.95

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Desconto ganho:     R$', valor_descontado)
print('Valor com desconto: R$', novo_valor)