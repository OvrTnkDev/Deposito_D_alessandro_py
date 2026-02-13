"""- ES COMPLESSIVO - Esercizio di TEST -Gestionale per L'Ingresso a Lavoro (OOP completo) In una cartella specifica della tua repositoryCad
  esempio:/progetti/0OP_GestionaleIngressoLavoro)
  - realizza un gestionale per L'ingresso a lavoro (accesso dipendenti, badge, turni, ecc.) utilizzando la programmazione ad oggetti.

  - Obiettivo generale:
    Progettare e implementareun piccolo sistema software che gestisca la logica di ingresso in azienda (ad esempio persone, ruoli, badge, turni. controlli di accesso, log di entrata/uscita, ecc.),usando in modo evidente tuttee quattro le regole principali dell'0OP:
    ·Astrazione
    ·Ereditarietà ·Incapsulamento
    ·Polimorfismo Il progetto dovrà:
    essere organizzato nella cartella indicata alu interno della vostra repository,
    ·contenere più file e/o moduli coerenti con l'idea di "gestionale per l'ingresso a lavoro",
    mostrare chiaramente, nel codice e nella struttura, dove e come vengono applicate le
    quattro regole OOP.
    Non ci sono altre specifiche obbligatorie: siete voi a dover definire quali oggetti esistono, come interagiscono, quali responsabilità hanno e come dimostrare in modo chiaro l'uso di astrazione, ereditarietà, incapsulamento e polimorfismo."""
    
    # Esempio di struttura del progetto:
    # - progetti/
    #   - 0OP_GestionaleIngressoLavoro/
    #     - main.py
    #     - dipendenti.py
    #     - turni.py
    #     - log.py
    #     - README.md
    
from dipendenti import Dipendente, Badge
from turni import Turno
from log import Accesso, Log

def main():
    print("Benvenuto al gestionale per l'ingresso a lavoro!")
    
    while True:
      r = input("\n0. Esci\n1. Crea dipendente(con badge)\n2. Crea turno\n3. Registra accesso\n4. Visualizza log\nScegli un'opzione: ")
      
      match r:
        
        case "0":
          print("Arrivederci!")
          break
        
        case "1":
          nome = input("Inserisci il nome del dipendente: ")
          ruolo = input("Inserisci il ruolo del dipendente: ")
          dip_OBJ = Badge(nome, ruolo)
          print(f"Dipendente creato: {dip_OBJ}")
          dip_OBJ.salva_dipendente()
        
        case "2":
          nome = input("Inserisci il nome del dipendente per il turno: ")
          ruolo = input("Inserisci il ruolo del dipendente per il turno: ")
          orario_inizio = input("Inserisci l'orario di inizio del turno (es. 09:00): ")
          orario_fine = input("Inserisci l'orario di fine del turno (es. 17:00): ")
          turno_OBJ = Turno(nome, ruolo, orario_inizio, orario_fine)
          print(f"Turno creato: {turno_OBJ}")
          turno_OBJ.salva_turno()
          
        case "3":
          nome = input("Inserisci il nome del dipendente per l'accesso: ")
          ruolo = input("Inserisci il ruolo del dipendente per l'accesso: ")
          orario = input("Inserisci l'orario dell'accesso (es. 09:00): ")
          tipo = input("Inserisci il tipo di accesso (entrata/uscita): ")
          accesso_OBJ = Accesso(nome, ruolo, orario, tipo)
          accesso_OBJ.controllo_accesso()
          log_OBJ = Log()
          if tipo == "entrata":
              log_OBJ.registra_entrata(accesso_OBJ)
          elif tipo == "uscita":
              log_OBJ.registra_uscita(accesso_OBJ)
          else:
              print("Tipo di accesso non valido. Deve essere 'entrata' o 'uscita'.")
        
        case "4":
          log_OBJ = Log()
          print("\nLog di entrata:")
          for nome, orario in log_OBJ.entrate.items():
              print(f"{nome} - {orario}")
          print("\nLog di uscita:")
          for nome, orario in log_OBJ.uscite.items():
              print(f"{nome} - {orario}")
        case _:
          print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()