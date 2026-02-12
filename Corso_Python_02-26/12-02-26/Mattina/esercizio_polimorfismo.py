"""creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento.
Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.

Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento."""

import random as rnd

# classi per il polimorfismo
class MetodoPagamento():
    # attributo di classe per simulare il saldo disponibile
    __saldo = rnd.randint(100, 1000)
    
    # metodo per ottenere l'importo disponibile
    def get_importo(self):
        return self.__saldo
    
    # metodo per verificare se l'importo è valido (simulazione)
    def ceck_importo(self, importo):
        if importo.isdigit():
            importo = float(importo)
            return importo
        else:
            print("L'importo deve essere un numero decimale.")
            return False
        
    # metodo astratto da implementare nelle sottoclassi
    def effettua_pagamento(self, importo):
        pass

# classi derivate che implementano il metodo effettua_pagamento
class CartaDiCredito(MetodoPagamento):

    # implementazione del metodo effettua_pagamento specifica per CartaDiCredito
    def effettua_pagamento(self, importo):
        importo = self.ceck_importo(importo)
        if not importo:
            return
        if importo > self.get_importo():
            print(f"Saldo insufficiente per il pagamento con carta di credito, attualmente hai {self.get_importo()}.")
        else:
            print(f"Pagamento di {importo} effettuato con carta di credito.")

# implementazione del metodo effettua_pagamento specifica per PayPal
class PayPal(MetodoPagamento):

    # implementazione del metodo effettua_pagamento specifica per PayPal
    def effettua_pagamento(self, importo):
        importo = self.ceck_importo(importo)
        if not importo:
            return
        if importo > self.get_importo():
            print(f"Saldo insufficiente per il pagamento con PayPal, attualmente hai {self.get_importo()}.")
        else:
            print(f"Pagamento di {importo} effettuato con PayPal.")

# implementazione del metodo effettua_pagamento specifica per BonificoBancario
class BonificoBancario(MetodoPagamento):

    # implementazione del metodo effettua_pagamento specifica per BonificoBancario
    def effettua_pagamento(self, importo):
        importo = self.ceck_importo(importo)
        if not importo:
            return
        if importo > self.get_importo():
            print(f"Saldo insufficiente per il pagamento con bonifico bancario, attualmente hai {self.get_importo()}.")
        else:
            print(f"Pagamento di {importo} effettuato con bonifico bancario.")

class GestorePagamenti():
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.metodo_pagamento = metodo_pagamento

    def effettua_pagamento(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)


# menu
def menu():
    # ciclo infinito per mostrare il menu finché l'utente non decide di uscire
    while True:
        # input dell'utente per scegliere il metodo di pagamento
        r = input("\n0. Esci\n1. Carta di credito\n2. PayPal\n3. Bonifico bancario\nScegli un metodo di pagamento:")
        
        # match-case per gestire la scelta dell'utente
        match r:
            # caso per uscire dal programma
            case "0":
                print("Arrivederci!")
                exit()
            
            # caso per scegliere il metodo di pagamento con carta di credito
            case "1":
                gestore_OBJ = GestorePagamenti(CartaDiCredito())
                importo = input("Inserisci l'importo da pagare:")
                gestore_OBJ.effettua_pagamento(importo)
            
            # caso per scegliere il metodo di pagamento con PayPal
            case "2":
                gestore_OBJ = GestorePagamenti(PayPal())
                importo = input("Inserisci l'importo da pagare:")
                gestore_OBJ.effettua_pagamento(importo)
            
            # caso per scegliere il metodo di pagamento con bonifico bancario
            case "3":
                gestore_OBJ = GestorePagamenti(BonificoBancario())
                importo = input("Inserisci l'importo da pagare:")
                gestore_OBJ.effettua_pagamento(importo)
            
            case _:
                print("Scelta non valida. Riprova.")
                continue


# avvio del menu
menu()