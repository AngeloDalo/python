x = 300 #scope globale

def funzione():
    y = 400 #locale
    print(y)
    global x
    print(x)
    x = 100
    print(x)
    def sottofunzione():
        print(y)
    sottofunzione()
    return y #ora la posso usare fuori

y = funzione()
print(x) #diventa 100
print(y)
#NO print(y) senza return