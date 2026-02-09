"""Crea una class biblioteca che permette di creare un libro e stamparlo.
extra: permetti di creare quanti libri vuole l'utente"""

# Creazione di una classe Libro con attributi e metodi
class Libro():
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
# Stampo le informazioni con __str__ che sarebbe il toString() di C#
    def __str__(self):
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha '{self.pagine}' pagine."
# Creazione di una classe Biblioteca che contiene una lista di libri e metodi per aggiungere e stampare i libri
class Biblioteca():
    def __init__(self):
        """ Il costruttore della classe Biblioteca inizializza un attributo chiamato libri, che è una lista vuota.
        Questa lista sarà utilizzata per memorizzare gli oggetti della classe Libro che vengono creati e aggiunti alla biblioteca.
        Se lo avessi creato fuori dal costruttore, sarebbe un attributo di classe e condiviso da tutte le istanze della classe Biblioteca,
        il che non è desiderabile in questo caso, poiché ogni biblioteca dovrebbe avere la propria lista di libri."""
        self.libri = []
        
    def aggiungi_libro(self,libro):
        self.libri.append(libro)
        
    def stampa_libri(self):
        for l in self.libri:
            print(l)
            
def main():
    biblioteca_OBJ = Biblioteca()
    while True:
        t = input("Inserisci il titolo del libro: ")
        a = input("Inserisci l'autore del libro: ")
        while True:
            try:
                p = int(input("Inserisci il numero di pagine del libro: "))
                break
            except ValueError:
                print("Per favore, inserisci un numero valido.")
                continue
        # Creazione di un oggetto della classe Libro e aggiunta alla biblioteca
        libro1_OBJ = Libro(t, a, p)
        """Porto in biblioteca l'oggetto libro1_OBJ creato,
        perche la classe Biblioteca ha un metodo chiamato aggiungi_libro che prende un oggetto libro
        come argomento e lo aggiunge alla lista dei libri della biblioteca."""
        biblioteca_OBJ.aggiungi_libro(libro1_OBJ)
        
        continua = input("Vuoi inserire un nuovo libro? (s/n): ")
        if continua.lower() != 's':
            print("Ecco la lista dei libri nella biblioteca:")
            biblioteca_OBJ.stampa_libri()
            print("Programma terminato.")
            exit()
        else:
            continue
        

if __name__ == "__main__":
    main()