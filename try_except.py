try:
    print(x)
except NameError:
    #pass se non voglio fare niente
    print("x non definita")
except:
    print("non è name error")
else:
    print("nessun problema")
finally:
    print("con o senza errore esco")


#CREARE ERRORE
x = -1
if x < 0:
    raise Exception("Numero minore di 0")
