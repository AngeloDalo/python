class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print("ciao sono " + self.nome + " e sono una persona")

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia
    def saluta(self):
        print("ciao sono " + self.nome + " e sono una insegnante")
    def voto(self):
        print("hai preso 8")
    

persona1 = Persona("Luca", "Rossi")
insegnante1 = Insegnante("Anna", "Neri", "Matematica")

persona1.saluta()
insegnante1.saluta()
insegnante1.voto()
print(insegnante1.materia)