larg = float(input("Digite a altura da parede "))
alt = float (input("Digite a  largura da parede "))
área = larg * alt
print ("Sua parede tem a dimensão de {}mx{}m e sua área é de {}m².".format(larg, alt, área))
tinta = área / 2 
print ("Para pinta essa parede, voce precisara  de {:.0f}litros de tinta.".format(tinta))
