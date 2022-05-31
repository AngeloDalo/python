x = "ciao"
y = 'ciao'
print("hello")
print(x)
z = """ciao
posso 
andare a capo
"""
print(z)

x = "prova"
print(x[0]) #stampa p, parte da 0
print(len(x)) #stampa lunghezz di x, parte da 1

#stampare singoli caratteri con ciclo
for carattere in "computer":
    print(carattere)

x = "ciao sono io"
print(x[:3]) #cia, stampa fino al carattere in posizione 3, parte da 1, incluso
print(x[2:7]) #ao so,dal 3 al 7, ecluso incluso
print(x[-1])  #o, parte dal fondo, incluso
print(x[-2:]) #io, dal carattere -2 in poi, incluso
print(x[:-2]) #ciao sono, dall'inizio fino al carattere -2 escluso

x = "ciao sono io"
print(x.upper()) #maiuscolo
print(x.lower()) #minuscolo
print(x.strip()) #toglie spazio dietro e davanti
print(x.replace("o", "w")) #sostituisce o con w
y = " ho 20 anni"
print(x + y)
prova = "ciao io {} peso {}" #nelle parentesi posso mettere numeri che riprende le ()
print(prova.format(y, 90)) #come il . o + in php o js

prova = "ciao sono io e sono \"alto\"" #escape ""
prova = 'ciao io sono \'io' #escape ''
