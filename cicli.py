#WHILE
i = 0
while(i < 6):
    print(i)
    if i == 3:
        break #esci dal ciclo while
    i+=1
    print(i)

i = 0
while(i < 6):
    print(i)
    i+=1
    if i == 3:
        continue #non fa print(i) ma va avanti al i=4
    print(i)

i=0
while(i < 6):
    print(i)
    if i == 3:
        break
    i+=1
    print(i)
else: 
    print("ho finito")

#FOR
x = ["milano", "roma"]
for citta in x:
    print(citta)

string = "ciao"
for lettera in string:
    if lettera=="a":
        break
    if lettera=="i":
        continue
    print(lettera)
else:
    print("ho finito")

for x in range(6):
    print(x)





