'''Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}'''

def char_count(s):
    # creo un dizionario usando una comprensione del dizionario che conta la frequenza di ogni carattere nella stringa
    return {char: s.count(char) for char in set(s)}

while True:
    # chiedo all'utente di inserire una parola
    s = input("inserisci una parola o 'x' per uscire: ").lower().strip()
    if s == 'x':
        print("Uscita dal programma.")
        break
    # stampo il dizionario restituito dalla funzione char_count
    print(char_count(s))