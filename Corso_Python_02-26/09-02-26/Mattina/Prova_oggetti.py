# Creazione di una classe Automobile con attributi e metodi
class Automobile():
    numero_ruote = 4
    # Il metodo __init__ è il costruttore della classe, che viene chiamato quando si crea un nuovo oggetto della classe.
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    # Il metodo __str__ è un metodo speciale che viene chiamato quando si stampa un oggetto della classe. Restituisce una stringa che rappresenta l'oggetto.
    def __str__(self):
        return f"Automobile: {self.marca} {self.modello} ({self.anno})"
    
    # Il metodo stampa_info è un metodo della classe che stampa le informazioni dell'automobile.
    def stampa_info(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
# Creazione di una classe Calcolatrice con un metodo statico
class Calcolatrice():
    @staticmethod
    def somma(a, b):
        return a + b
#Creazione di una classe Contatore con un attributo di classe e un metodo di classe
class Contatore():
    n_istanze = 0
    def __init__(self):
        Contatore.n_istanze += 1
# Il metodo numero_istanze è un metodo di classe che stampa il numero di istanze create della classe Contatore.
    @classmethod
    def numero_istanze(cls):
        print(cls.n_istanze)
        
# Creazione di un oggetto della classe Automobile e chiamata del metodo stampa_info
auotFabio_OBJ = Automobile("Alfa Romeo", "Stelvio", 2025)
auotFabio_OBJ.stampa_info()
# La funzione type() restituisce il tipo dell'oggetto passato come argomento. In questo caso, restituirà "Automobile" perché auotFabio_OBJ è un'istanza della classe Automobile.
print(f"[INFO]: {type(auotFabio_OBJ).__name__}")
# Quando si stampa un oggetto, viene chiamato il metodo __str__ per ottenere una rappresentazione stringa dell'oggetto.
print(auotFabio_OBJ)
# uso del metodo statico somma della classe Calcolatrice
result = Calcolatrice.somma(5, 10)
print(f"Il risultato della somma è: {result}\n")
# Creazione di istanze della classe Contatore e chiamata del metodo numero_istanze
contatore_OBJ1 = Contatore()
contatore_OBJ2 = Contatore()
Contatore.numero_istanze()