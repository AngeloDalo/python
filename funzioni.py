def fai_azione(tipo_azione, bool):
    print("prima azione")
    print("seconda azione")
    print(tipo_azione)
    if bool:
        print("true")

fai_azione("azione1", True)
fai_azione("azione2", False)
fai_azione("azione3", False)
fai_azione(tipo_azione="azione4", bool=True)

#USO UN SOLO PARAMETRO
def fai_qualcosa(*opzione):
    print("qualcosa")
    print(opzione[0])
    if opzione[1]:
        print("qualcosa")

fai_qualcosa("ciao", False)

#VALORE DEFAULT
def fai_azioni(tipo = "azione"):
    print(tipo)

fai_azioni() #se non metto niente di default il valore è azione

#RETURN
def calcolatrice(x, y):
    somma = x + y
    return somma

x = calcolatrice(5,2)
print(x)