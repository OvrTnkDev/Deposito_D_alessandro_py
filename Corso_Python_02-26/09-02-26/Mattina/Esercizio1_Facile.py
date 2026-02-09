"""Esercizio 1 (Facile):
Crea una classe chiamata Punto. Questa classe dovrebbe avere:
Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano."""
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distanza_da_origine(self):
        return (self.x**2 + self.y**2)**0.5
    
# Creazione di un oggetto della classe Punto e chiamata dei metodi
def m1():
    # Il ciclo while True permette di continuare a chiedere all'utente di inserire le coordinate del punto e i valori di dx e dy finché non decide di interrompere il programma.
    while True:
        # Il blocco try-except viene utilizzato per gestire eventuali errori di input da parte dell'utente. Se l'utente inserisce un valore non valido (ad esempio, una stringa invece di un numero), il programma stamperà un messaggio di errore e chiederà nuovamente l'input.
        while True:
            try:
                x = float(input("Inserisci la coordinata x del punto: "))
                y = float(input("Inserisci la coordinata y del punto: "))
                break
            except ValueError:
                print("Per favore, inserisci un numero valido.")
                # Il comando continue fa sì che il programma torni all'inizio del ciclo while True, permettendo all'utente di inserire nuovamente le coordinate del punto.
                continue
        punto1_OBJ = Punto(x,y)
        print(f"Il punto è stato creato con le coordinate: ({punto1_OBJ.x}, {punto1_OBJ.y})")

        while True:
            try:
                dx = float(input("Inserisci il valore di dx per muovere il punto: "))
                dy = float(input("Inserisci il valore di dy per muovere il punto: "))
                break
            except ValueError:
                print("Per favore, inserisci un numero valido.")
        punto1_OBJ.muovi(dx, dy)
        print(f"Il punto è stato mosso alle nuove coordinate: ({punto1_OBJ.x}, {punto1_OBJ.y})")
        print(f"La distanza del punto dall'origine è: {punto1_OBJ.distanza_da_origine()}")
        # Chiediamo all'utente se vuole continuare a inserire nuovi punti o se vuole interrompere il programma.
        continua = input("Vuoi inserire un nuovo punto? (s/n): ")
        if continua.lower() != 's':
            print("Programma terminato.")
            exit()
        else:
            continue

def main():
    # Il ciclo while True permette di continuare a chiedere all'utente di inserire le coordinate del punto e i valori di dx e dy finché non decide di interrompere il programma.
    while True:
        # creazione di una lista vuota per memorizzare gli oggetti della classe Punto creati dall'utente.
        list_obj = []
        # iniziamo il loop
        while True:
            """Try -Except è una struttura di controllo del flusso che permette di gestire le eccezioni (errori)
            che possono verificarsi durante l'esecuzione del codice."""
            try:
                obj = int(input("Quanti punti vuoi creare? "))
                break
            except ValueError:
                print("Per favore, inserisci un numero valido.")
                continue
        """Il ciclo for viene utilizzato per iterare un numero specifico di volte,
        in questo caso, il numero di punti che l'utente vuole creare."""
        for i in range(obj):
            """Il blocco try-except viene utilizzato per gestire eventuali errori di input da parte dell'utente."""
            while True:
                try:
                    x = float(input("Inserisci la coordinata x del punto: "))
                    y = float(input("Inserisci la coordinata y del punto: "))
                    break
                except ValueError:
                    print("Per favore, inserisci un numero valido.")
                    continue
                
            list_obj.append(Punto(x,y))
            print(f"Il punto è stato creato con le coordinate: ({list_obj[i].x}, {list_obj[i].y})")
        for i in range(obj):
            while True:
                try:
                    dx = float(input(f"Inserisci il valore di dx per muovere il punto {i+1}: "))
                    dy = float(input(f"Inserisci il valore di dy per muovere il punto {i+1}: "))
                    break
                except ValueError:
                    print("Per favore inserisci un numero valido.")
                    continue
            list_obj[i].muovi(dx, dy)
            print(f"Il punto {i+1} è stato mosso alle nuove coordinate: ({list_obj[i].x}, {list_obj[i].y})")
            print(f"La distanza del punto {i+1} dall'origine è: {list_obj[i].distanza_da_origine()}")


        # Chiediamo all'utente se vuole continuare a inserire nuovi punti o se vuole interrompere il programma.
        continua = input("Vuoi inserire un nuovo punto? (s/n): ")
        if continua.lower() != 's':
            print("Programma terminato.")
            exit()
        else:
            continue

"""# Il blocco if __name__ == "__main__":
è una convenzione in Python che permette di eseguire il codice all'interno di questo blocco solo se il file viene
eseguito direttamente (ad esempio, python Esercizio1_Facile.py) e non quando viene importato come modulo in un altro file."""
if __name__ == "__main__":
    main()