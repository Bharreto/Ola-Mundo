km = float(input("Quanto km rodados? "))
dia = int (input("Quantos dias alugados? "))

dia_alugados = dia * 60

km_rodado = km * 0.15

valor_final = km_rodado + dia_alugados

print ("O total a pagar é R${:.0f}".format(valor_final))