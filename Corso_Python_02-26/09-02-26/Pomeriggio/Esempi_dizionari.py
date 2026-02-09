"""I dizionari in Python sono strutture dati che memorizzano coppie chiave-valore.
Sono simili alle liste, ma invece di utilizzare indici numerici per accedere agli elementi"""
studente = {"nome": "Fabio",
            "cognome": "D'alessandro",
            "età": 27,
            "corso": "Python"}

print(studente["nome"])  # Output: Fabio
print(studente["cognome"])  # Output: D'alessandro
print(studente["età"])  # Output: 27
print(studente["corso"])  # Output: Python

studente["età"]=28
print(studente["età"])  # Output: 28

print(studente.keys())  # Output: dict_keys(['nome', 'cognome', 'età', 'corso'])
print(studente.values())  # Output: dict_values(['Fabio', "D'alessandro", 28, 'Python'])
print(studente.items())  # Output: dict_items([('nome', 'Fabio'), ('cognome', "D'alessandro"), ('età', 28), ('corso', 'Python')])

studente["università"] = "Università Telematica Pegaso"
print(studente)

studente["Città"] = "Napoli"
print(studente.items()) # serve per stampare tutte le coppie chiave-valore del dizionario