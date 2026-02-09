"""Esercizio 2 (Facile):
Crea una classe chiamata Libro. 
Questa classe dovrebbe avere:
Tre attributi: titolo, autore e pagine.
Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine."""
class Libro():
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def __str__(self):
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha '{self.pagine}' pagine."
    
    
def main():
    list_libri = []
    while True:
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        while True:
            try:
                pagine = int(input("Inserisci il numero di pagine del libro: "))
                break
            except ValueError:
                print("Per favore, inserisci un numero valido.")
                continue
        # Creazione di un oggetto della classe Libro e stampa della sua descrizione
        libro1_OBJ = Libro(titolo, autore, pagine)
        list_libri.append(libro1_OBJ)
        # Quando si stampa un oggetto, viene chiamato il metodo __str__ per ottenere una rappresentazione stringa dell'oggetto.
        print(libro1_OBJ)
        
        continua = input("Vuoi inserire un nuovo libro? (s/n): ")
        if continua.lower() != 's':
            print("Programma terminato.")
            exit()
        else:
            continue
            
if __name__ == "__main__":
    main()