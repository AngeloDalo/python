class Persona:
    nome = "Luca"
    cognome = "Rossi"

persona1 = Persona()
persona2 = Persona()
print(persona1.nome)
print(persona1.cognome)

#COSTRUTTORI
class Persona2:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

persona1 = Persona2("Luca", "Rossi")
persona2 = Persona2("Marco", "Verdi")
print(persona2.nome)

#METODI
class Persona3:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self, nome):
        print("ciao sono " + self.nome + " tu sei " + nome)

persona1 = Persona3("Luca", "Rossi")
persona1.saluta("Ciro")

#MODIFICARE ED ELIMINARE
persona1.nome = "Maria"
persona1.saluta("Ciro")
#del persona1.nome
#del persona1