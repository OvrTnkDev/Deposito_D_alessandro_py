# classe base
class Animale():
    def __init__(self, nome):
        self.nome = nome
        
    def parla(self):
        print(f"{self.nome} fa un suono generico.")
        
# classe derivata da Animale
class Cane(Animale):
    def parla(self):
        print(f"{self.nome} dice: Bau!")
        
# esempi ereditarietà multipla
# classe veicolo
class Veicolo():
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def descrizione(self):
        print(f"Veicolo: {self.marca} {self.modello}")

# classe dotazioni speciali
class DotazioniSpeciali():
    def __init__(self, dotazione):
        self.dotazione = dotazione
        
    def mostra_dotazione(self):
        print(f"Dotazione speciale: {', '.join(self.dotazione)}")

# classe che eredita da Veicolo e DotazioniSpeciali
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__ (self, marca, modello, dotazione, cavalli):
        Veicolo.__init__(self, marca, modello)
        DotazioniSpeciali.__init__(self, dotazione)
        self.cavalli = cavalli
        
    def mostra_informazioni(self):
        # prendo il metodo descrizione dalla classe Veicolo usando super() per mostrare la marca e il modello dell'automobile sportiva
        super().descrizione()
        print(f"Cavalli: {self.cavalli} HP")
        # prendo il metodo mostra_dotazione dalla classe DotazioniSpeciali usando super() per mostrare la dotazione speciale dell'automobile sportiva
        self.mostra_dotazione()
        
animale_padre_OBJ = Animale("Generico")
animale_figlio_OBJ = Cane("Max")

animale_padre_OBJ.parla()  # Output: Generico fa un suono generico.
animale_figlio_OBJ.parla()  # Output: Max dice: Bau!

print("\n")

auto_sportiva_OBJ = AutomobileSportiva("Ferrari", "488 GTB", ["Freni in ceramica", "Sospensioni attive"], 670)
auto_sportiva1_OBJ = AutomobileSportiva("Lamborghini", "Huracán EVO", ["Freni in ceramica", "Sospensioni attive"], 640)

auto_sportiva_OBJ.mostra_informazioni()
auto_sportiva1_OBJ.mostra_informazioni()