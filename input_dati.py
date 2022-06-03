# x = input("cosa vuoi fare ")
# print(x)
def aggiungi(param):
    print(param)
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore

persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

# operazioni = {"aggiungere", "modificare", "eliminare"}

# def start():
# operazione = input("Cosa vuoi fare? ")
# if operazione == operazioni[0]:
x = input("aggiungi chiave valore separati da virgola ")
aggiungi(x.split(","))
    # elif operazione == operazioni[1]:
    #     pass
    # elif operazione == operazioni[2]:
    #     pass

# while True:
#     start()