import miomodulo as em
#ALIAS DEL MODULO PER ACCORCIARE NOME

#miomodulo.saluta("Luca")
em.saluta("Luca")

#x = miomodulo.persona1["nome"]
#miomodulo.saluta(x)
x = em.persona1["nome"]
em.saluta(x)

import math
#STAMPARE TUTTE FUNZIONI
print(dir(math))

#IMPORTARE SOLO UN MODULO
from miomodulo import persona1
print(persona1["nome"])