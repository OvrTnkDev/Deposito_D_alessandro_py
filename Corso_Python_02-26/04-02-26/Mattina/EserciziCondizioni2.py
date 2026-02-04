# Esercizio 2: Gestione di una lista di nomi con Crud
x = ["Andrea", "Giovanni", "Francesco", "Luca", "Matteo"]
print("Questa è una lista di nomi -> ",x, "\n0 -Elimina\n1 -Aggiungi\n2 -Sostituisci\n3 -Esci")
scelta = int(input("Cosa vuoi fare? "))
if (scelta == 0):
    nome = input("Quale nome vorresti eliminare?")
    if (nome in x):
        x.remove(nome)
        print("Il nome è stato eliminato\n", x)
        
elif (scelta == 1):
    nome = input("Quale nome vorresti aggiungere?")
    x.append(nome)
    print("Il nome è stato aggiunto\n", x)
elif (scelta == 2):
    nome = input("Quale nome vorresti sostituire?")
    if (nome in x):
        nuovo_nome = input("Con quale nome vorresti sostituirlo?")
        indice = x.index(nome)
        x[indice] = nuovo_nome
        print("Il nome è stato sostituito\n", x)
elif (scelta == 3):
    print("Uscita dal programma")
else:
    print("Scelta non valida, riprova")
x.clear()