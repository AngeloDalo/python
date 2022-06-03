import json

#LEGGERE JSON
x = '{ "nome": "Luca, "cognome: "Rossi", "eta": 25 }'
y = json.loads(x)
print(y)
print(y["nome"])

#CREARE JSON
x = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25,
    "is_online": False,
    "interessi": ["calcio", "basket"],
    "soldi": 4.34
}
y = json.dumps(x)
z = json.dumps(["roma", "napoli"])
print(type(y))

#FORMATTARE JSON
y = json.dumps(x, indent=4, separators=(". ", "= "), sort_keys=True) #posso mettere separatori che voglio
