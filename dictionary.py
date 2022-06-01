#ordina modificabili NOduplicati
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}
print(persona)
print(len(persona))
print(type(persona))

#ACCEDERE AD ELEMENTI
print(persona["nome"])
print(persona.get("nome"))
x = persona.keys() #stampa chiave
x = persona.values() #stampa valore
x = persona.items() #stampa chiave-valore
print("nome" in persona) #true

#MODIFICARE 
persona["nome"] = "marco"
persona.update({"nome": "Anna"})
persona["colore"] = "blu"
persona.pop("nome")
persona.popitem #toglie ultima chiave
persona.clear #vuoto
#del persona["nome"]
#del persona

#CICLI
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}
for x in persona:
    print(x) #stampa chiave
    print(persona[x]) #stampa valore
for x in persona.values():
    print(x) #stampa valore
for x in persona.keys():
    print(x) #stampa chiave
for x, y in persona.items():
    print(x, y) #stampa chiave e valore

#COPIARE
x = persona.copy()
print(x)
y = dict(persona)

#ANNIDATI
persona = {
    "nome": "Luca",
    "indirizzo": {
        "citta": "Milano"
    }
}
print(persona["indirizzo"]["citta"])