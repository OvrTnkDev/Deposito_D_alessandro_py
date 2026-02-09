"""Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
Definizione della Classe:
Creare una classe chiamata Ristorante. (fatto)
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).(fatto)
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).(fatto)
Un Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante(fatto)
Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.(fatto)
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.(fatto)
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.(fatto)
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.(fatto)
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu(fatto)
togli_dal_menu(): Un metodo per togliere piatti al menu(fatto)
stampa_menu(): Un metodo per stampare il menu(fatto)
Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto."""

# sleep mette in pausa l'esecuzione del programma per un tot numero di secondi
from asyncio import sleep

# creo il dizionario del menu
class Menu():
    menu = {"Cucina italiana": {"Pasta": 10, "Pizza": 8, "Lasagna": 14},
            "Cucina giapponese": {"Sushi": 12, "Ramen": 9, "Tempura": 11},
            "Cucina messicana": {"Tacos": 7, "Burrito": 9, "Quesadilla": 8},
            "Cucina indiana": {"Curry": 10, "Naan": 3, "Biryani": 12}}


# creo la classe Ristorante
class Ristorante():
    # Definisco attributo open
    opn = False
    
    # definisco il costruttore
    def __init__(self, nome, t_cucina, menu):
        self.nome = nome
        self.t_cucina = t_cucina
        self.menu = menu

    # descrivi ristorante
    def __str__(self):
        return f"Benvenuti nel ristorante '{self.nome}', il nostro tipo di cucina è '{self.t_cucina}'!"
    
    # stato apertura
    def stato_apertura(self):
        if self.opn:
            print(f"Il ristorante '{self.nome}' è aperto.")
        else:
            print(f"Il ristorante '{self.nome}' è chiuso.")
    
    # apri ristorante
    def apri_ristorante(self):
        if not self.opn:
            self.opn = True
            print(f"Il ristorante '{self.nome}' è ora aperto.")
        else:
            print(f"Il ristorante '{self.nome}' è già aperto.")
            
    # chiudi ristorante
    def chiudi_ristorante(self):
        if self.opn:
            self.opn = False
            print(f"Il ristorante '{self.nome}' è ora chiuso.")
        else:
            print(f"Il ristorante '{self.nome}' è già chiuso.")
            
    # aggiungi al menu
    def aggiungi_al_menu(self, t_cucina, piatto, prezzo):
        # se il tipo esiste già nel menu, aggiungo il piatto al dizionario nel tipo di cucina
        if t_cucina in self.menu:
            self.menu[t_cucina][piatto]=prezzo
        # se il tipo di cucina non esiste, lo creo e aggiungo il piatto al dizionario del nuovo tipo di cucina
        else:
            self.menu[t_cucina] = {piatto: prezzo}

    
    # togli dal menu
    def togli_dal_menu(self, t_cucina, piatto):
        # se il tipo di cucina esiste nel menu, controllo se il piatto esiste e lo rimuovo
        if t_cucina in self.menu:
            if piatto in self.menu[t_cucina]:
                del self.menu[t_cucina][piatto]
                print(f"Il piatto '{piatto}' è stato rimosso dal menu del ristorante '{self.nome}'.")
            else:
                print(f"Il piatto '{piatto}' non esiste nel menu del ristorante '{self.nome}'.")
        else:
            print(f"Il tipo di cucina '{t_cucina}' non esiste nel menu del ristorante '{self.nome}'.")
    
    # stampa menu
    def stampa_menu(self):
        print(f"Menu del ristorante '{self.nome}':")
        # iterazione attraverso il dizionario del menu per stampare i tipi di cucina e i piatti con i prezzi
        # items() restituisce una vista degli elementi del dizionario, che è una sequenza di coppie chiave-valore.
        for t_cucina, piatti in self.menu.items():
            print(f"{t_cucina}:")
            # iterazione attraverso il dizionario dei piatti per stampare i piatti e i prezzi
            for piatto, prezzo in piatti.items():
                print(f"  - {piatto}: {prezzo}€")

# definisco il main per testare la classe Ristorante
def main():
    # creo l'oggetto menu e ristorante
    menu_OBJ = Menu()
    ristorante_OBJ = Ristorante("Il cardamone", "Cucina italiana", menu_OBJ.menu)
    
    # test dei metodi
    ristorante_OBJ.stato_apertura()
    # con sleep() metto in pausa per n secondi l'esecuzione del programma
    sleep(2)
    # apro il ristorante e stampo lo stato di apertura
    ristorante_OBJ.apri_ristorante()
    # do il benvenuto e descrivo il ristorante
    print(ristorante_OBJ)
    # stampo il menu
    ristorante_OBJ.stampa_menu()
    # aggiungo un nuovo piatto al menu e stampo il menu aggiornato
    ristorante_OBJ.aggiungi_al_menu("Cucina italiana", "Risotto", 11)
    ristorante_OBJ.stampa_menu()
    # rimuovo un piatto dal menu e stampo il menu aggiornato
    ristorante_OBJ.togli_dal_menu("Cucina italiana", "Pizza")
    ristorante_OBJ.stampa_menu()
    # chiudo il ristorante e stampo lo stato di apertura
    ristorante_OBJ.chiudi_ristorante()
    # stampo lo stato di apertura del ristorante
    ristorante_OBJ.stato_apertura()


if __name__ == "__main__":
    main()