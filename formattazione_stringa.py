peso = 65
altezza = 184
frase = "ciao sono alto " + str(altezza) + " e peso " + str(peso)
print(frase)

#STRING FORMATTING
frase2 = "ciao sono alto {:.2f}"
print(frase2.format(altezza))

frase3 = "ciao sono alto {} e peso {} e ho {eta}" #posso mettere numero nelle parentesi
print(frase3.format(altezza, peso, eta="23"))
