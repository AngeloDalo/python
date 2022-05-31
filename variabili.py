#non è possibile creare varibaili vuote
x = 5
#è case sensitive
# x != x
#no variabili che iniziano con numero
y, z = 10, 20
print(x) 
print(y)
print(z)

x=y=z = 30
print(x) 
print(y)
print(z)

citta = ["roma", "milano", "napoli"]
x, y, z = citta
print(x) 
print(y)
print(z)

x=32
y=40
z = x + y
print(z)
