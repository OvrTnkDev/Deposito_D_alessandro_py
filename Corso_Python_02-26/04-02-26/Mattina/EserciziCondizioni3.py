# Esercizio 3: Creazione di un account con if else semplice
x = input("Hai già un account? (s/n): ")
id = 0
if (x.lower() == "n"):
    y=[]
    print("Benvenuto!\nCreiamo il tuo account")
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password: ")
    id += 1
    # Aggiungo il nuovo account alla lista degli account
    y.append((nome, password, id))
    print("Il tuo account è stato creato con successo!\nEcco i tuoi dati di accesso:\nNome: ", nome, "\nPassword: ", password, "\nID: ", id)
    
else:
    print("Vabene sei a bordo!")