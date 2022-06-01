#ordinate NOmodiciabili duplicati
x = ("milano", "roma", "napoli")
print(type(x)) #se c'è solo un valore è string altrimenti tupla, ("milano",) tupla con un valore
print(len(x))
z = tuple(("milano", "roma", "napoli"))

#ACCEDERE A TUPLA
print(x[0])
print(x[1:]) #vedere string
if "milano" in x:
    print("ok")

#NON POSSO MODIFICARE O INSERIRE ELEMENTI
#ESCAMOTAGE
y = list(x)
y[0] = "venezia"
y.remove("napoli")
x = tuple(y)
print(x)

#SPACCHETTARE
citta = ("milano", "roma", "napoli", "verona")
(x, y, *z) = citta
print(x)
print(y)
print(z) #è una lista

#CICLI
citta = ("milano", "roma", "napoli", "verona")
for i in citta:
    print(i)

for i in range(len(citta)):
        print(citta[i])

i=0
while i<len(i):
    print(citta[i])
    i+=1

#UNIONE 
x = ("milano", "roma", "napoli", "verona")
y = ("milano", "roma", "napoli", "verona")
z = x + y

#QUANTE VOLTE VALORE NELLA TUPLA
x = ("milano", "roma", "napoli", "verona", "milano")
y = x.count("milano")
y = x.index("milano") #primo indice di milano


