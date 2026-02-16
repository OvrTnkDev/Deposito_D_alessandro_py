'''Scrivete un programma che chiede all'utente una
serie di parole e restituisce solo le vocali e l’indice della vocale all’interno delle parole.'''

def voc_index(p):
    v = "aeiou"
    print(f"Le vocali presenti nella parola '{p}' sono:")
    for i in range(len(p)):
        if p[i] in v:
            print(f"{p[i]}: {i}")


while True:
    # chiedo all'utente di inserire una parola
    parola = input("inserisci una parola o 'x' per uscire: ").lower()
    if parola == 'x':
        print("Uscita dal programma.")
        break
    # chiamo la funzione voc_index per restituire le vocali e i loro indici, pulendo eventuali spazi bianchi
    voc_index(parola.strip())