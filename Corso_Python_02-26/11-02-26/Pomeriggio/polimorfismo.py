class Animale():
    def verso(self):
        print("L'animale emette un verso generico.")
        
class Cane(Animale):
    def verso(self):
        print("Il cane abbaia: Bau Bau!")

class Gatto(Animale):
    def verso(self):
        print("Il gatto miagola: Miao Miao!")
        
#overloading simulato(in python non esiste): stesso nome, parametri diversi
class Stampa():
    def mostra(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Stampa di due valori: {a} e {b}")
        elif a is not None:
            print(f"Stampa di un valore: {a}")
        else:
            print("Nessun valore da stampare.")

animale_OBJ = (Animale(), Cane(), Gatto())

for a in animale_OBJ:
    a.verso()

#overloading simulato
stampa_OBJ = Stampa()
stampa_OBJ.mostra()
stampa_OBJ.mostra(42)
stampa_OBJ.mostra("Ciao", "Mondo")