#indici modificabile e duplicati
x = ["milano", "roma", "napoli"]
y = ["verona", "parma", "bat"]
z = list(("milano", "roma", "napoli"))

#STAMPARE LISTE
print(type(x)) #list
print(len(x)) #3
print(x[0]) #milano
print(x[1:]) #roma napoli
print(x[1:3]) #roma napoli

#MODIFICARE LISTE
x[0] = "brescia"
x[1:3] = ["novara", "udine"] #se metto solo novara lista avrà due elementi brescia e novara
x.append("taranto") #aggiunge alla fine
x.insert(1, "torino") #dopo 1 mette torino
x.extend(y) #aggiunge alla fine la lista y
x.remove("brescia") #rimuove in maniera specifica
x.pop() #toglie elemento in fondo
x.pop(1) #toglie elemento in posizione 1
del x[0] #toglie elemento in posizione 0
#del x #eleimina tutta la lista
x.clear() #pulisce la lista senza eliminarla
print(x)

#CICLI CON LISTE
x = ["milano", "roma", "napoli"]
for citta in x:
    print (citta)

for i in range(len(x)):
    print(x[i])

[print(citta) for citta in x]

i=0
while i < len(x):
    print(x[i])
    i += 1
#RIEMPIRE CON CICLO FOR SHORTCUT
lista = ["milano" for citta in x]
print(lista)

#MOFICARE ORDINE DELLA LISTA
x.sort() #in questo caso ordina in ordine alfabetico
x.sort(reverse=True) #ordina al contrario
print(x)

#COPIARE LISTA
y = x #creo riferimento e quando cambio y cambio anche x
y[0] = "NY" #anche x[0] = NY
#devo creare una copia e non un riferimento
y = x.copy()
y = list(x)

#UNIRE PIU' LISTE
x = ["milano", "roma", "napoli"]
y = ["verona", "parma", "bat"]
print(x + y)
z = x + y
for citta in y:
    x.append(citta)
x.extend(y)

