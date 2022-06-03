#r = read, a = append, w = write, x = create
#R
f = open("testo.txt", "r")
print(f.read(4)) #numero caratteri se voglio
print(f.readline())
for riga in f:
    print(riga)
f.close()

#A
f = open("testo.txt", "a")
f.write("scrivo cosa voglio")
f.close()
f = open("testo.txt", "r")
print(f.read())

#W
f = open("testo.txt", "w")
f.write("scrivo cosa voglio")
f.close()
f = open("testo.txt", "r")
print(f.read())

#X
f = open("prova.txt", "r") #posso crearlo anche con w e a

#ELIMINAZIONE
import os
os.remove("prova.txt")
if os.path.exists():
    os.remove("prova.txt")
else:
    print("non esiste file con questo nome")