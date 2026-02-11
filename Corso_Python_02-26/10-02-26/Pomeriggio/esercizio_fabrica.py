"""Classe Prodotto: (ok)
Attributi:
nome (stringa che descrive il nome del prodotto)(ok)
costo_produzione (costo per produrre il prodotto)(ok)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)(ok)
Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.(ok)
Classi parallele:
Creare almeno due classi parallele a Prodotto, per esempio auto e moto.(ok)
Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
Classe Fabbrica:
Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario."""

class Automobile():
    def __init__(self, ruote, porte:bool, cilindrata):
        self.ruote = ruote
        self.porte = porte
        self.cilindrata = cilindrata
        
    def __str__(self):
        return f"Automobile: {self.ruote} ruote, {' ha' if self.porte else self.porte} porte, {self.cilindrata} cc"

class Moto():
    def __init__(self, ruote, porte:bool, cilindrata):
        self.ruote = ruote
        self.porte = porte
        self.cilindrata = cilindrata

    def __str__(self):
        return f"Moto: {self.ruote} ruote, {'non ha' if not self.porte else self.porte} porte, {self.cilindrata} cc"


class Prodotto(Automobile, Moto):
    def __init__(self, nome, costo_produzione:float, prezzo_vendita:float):
        Automobile.__init__(self, ruote=0, porte=False, cilindrata=0)
        Moto.__init__(self, ruote=0, porte=False, cilindrata=0)
        
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
class Fabrica():
    open = False
    inventario = {}
    
    def aggiungi_prodotto(self, prodotto, quantità):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantità
        else:
            self.inventario[prodotto.nome] = quantità
        print(f"Aggiunti {quantità} {prodotto.nome} all'inventario.")
        
    def vendi_prodotto(self, prodotto, quantità):
        if prodotto.nome in self.inventario and self.inventario[prodotto.nome] >= quantità:
            self.inventario[prodotto.nome] -= quantità
            profitto = prodotto.calcola_profitto() * quantità
            print(f"Venduti {quantità} {prodotto.nome}. Profitto realizzato: {profitto}€")
        else:
            print(f"Non abbastanza {prodotto.nome} in inventario per vendere.")
            
    def resi_prodotto(self, prodotto, quantità):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantità
            print(f"Resi {quantità} {prodotto.nome} all'inventario.")
        else:
            print(f"{prodotto.nome} non esiste nell'inventario.")

def main():
    fabrica_OBJ = Fabrica()
    print("Benvenuto nella fabbrica!")
    
    if not Fabrica.open:
        print("La fabbrica è chiusa. Aprendo la fabbrica...")
        Fabrica.open = True

    while True:
        print("\nScegli un opzione:\n1. Aggiungi prodotto\n2. Vendi prodotto\n3. Resi prodotto\n4. Esci")
        s = input("scegli l'opzione: ")
        match s:
            case "1":
                i = input("Cosa vui aggiungere? (1.Auto - 2.Moto): ")
                if i == "1":
                    n = input("Inserisci il nome dell'auto: ")
                    cp = float(input("Inserisci il costo di produzione: "))
                    pv = float(input("Inserisci il prezzo di vendita: "))
                    q = int(input("Inserisci la quantità da aggiungere: "))
                    
                    auto_OBJ = Prodotto(n, cp, pv)
                    fabrica_OBJ.aggiungi_prodotto(auto_OBJ, q)
                elif i == "2":
                    n = input("Inserisci il nome della moto: ")
                    cp = float(input("Inserisci il costo di produzione: "))
                    pv = float(input("Inserisci il prezzo di vendita: "))
                    q = int(input("Inserisci la quantità da aggiungere: "))
                    
                    moto_OBJ = Prodotto(n, cp, pv)
                    fabrica_OBJ.aggiungi_prodotto(moto_OBJ, q)
                else:
                    print("Opzione non valida, riprova.")
                    continue
            case "2":
                n = input("Inserisci il nome del prodotto da vendere: ")
                q = int(input("Inserisci la quantità da vendere: "))
                cp = float(input("Inserisci il costo di produzione: "))
                pv = float(input("Inserisci il prezzo di vendita: "))
                if n in fabrica_OBJ.inventario:
                    prodotto_OBJ = Prodotto(n, cp, pv)
                    fabrica_OBJ.vendi_prodotto(prodotto_OBJ, q)
                else:
                    print(f"{n} non esiste nell'inventario.")
                    
            case "3":
                n = input("Inserisci il nome del prodotto da restituire: ")
                q = int(input("Inserisci la quantità da restituire: "))
                cp = float(input("Inserisci il costo di produzione: "))
                pv = float(input("Inserisci il prezzo di vendita: "))
                
                if n in fabrica_OBJ.inventario:
                    prodotto_OBJ = Prodotto(n, cp, pv)
                    fabrica_OBJ.resi_prodotto(prodotto_OBJ, q)
                else:
                    print(f"{n} non esiste nell'inventario.")
            case "4":
                    print("Arrivederci!")
                    break
            case _ :
                print("Opzione non valida, riprova.")
                continue

    
if __name__ == "__main__":
    main()