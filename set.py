#NOordine NOmodiciabile NOduplicati
x = {"milano", "roma", "napoli"}
print(type(x))
print(len(x))
y = set(("mialno", "roma", "napoli"))

#ACCEDERE SOLO CON LOOP
for citta in x:
    print(citta)
print("milano" in x) #true

#NO MODIFICARE, POSSO AGGIUNGERE ED ELIMINARE
x.add("venezia")
x = {"milano", "roma", "napoli"}
y = {"venezia", "genova", "bat"}
x.update(y)
x.remove("milano") #se non esiste da errore
x.discard("roma") #se non esiste non da errore
x.pop() #toglie ultimo elemento (casuale)
#x.clear()
#del x

#UNIRE
x = {"milano", "roma", "napoli"}
y = {"venezia", "genova", "bat"}
z = x.union(y) #crea un nuovo set
x.update(y)
#con elementi duplicati
x.intersection_update(y) #restituisce solo elementi in comune
z = x.intersection(y) #stesso risultato di sopra ma abbiamo un nuovo set
x.symmetric_difference_update(y) #restituisce tutto tranne elementi in comune
z = x.symmetric_difference(y) #stesso risultato di sopra ma abbiamo un nuovo set


