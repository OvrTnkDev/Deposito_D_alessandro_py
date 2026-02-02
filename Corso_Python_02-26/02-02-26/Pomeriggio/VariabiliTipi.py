name = "Fabio"
surname = "D'alessandro"
age = 27

# Interpolazione di stringhe
print(f"Ciao,sono {name} {surname} e ho {age} anni!")
# concatenazione di stringhe
print("Mirko "+"ha detto: \"Python è fantastico!\"")

#------Input utente-----------------------

n = input("Inserisci il tuo nome: ")
a = int(input("inserisci la tua età: "))

print(f"Ciao, sono {n} e ho {a} anni. Benvenuto in Python!")

#------Calcoli matematici con print-------
# Addizione
print(3 + 5)
# Sottrazione
print(10 - 2)
# Moltiplicazione
print(4 * 2)
# Divisione dove il type del risultato sarà float
print(16 / 2)
# Elevamento a potenza
print(5 ** 2)
# Resto della divisione
print(15 % 4)

# tipi di variabili
x = 10          # int
y = 3.14        # float
z = "Ciao"      # str

# verifica lettera in una stringa
testo = "Python è divertente"
lettera = input(f"Inserisci una lettera da cercare nella frase '{testo}': ")
print(lettera.lower() in testo.lower())

# concatenazione di variabili
saluto = "Ciao"
nome = "Luca"
# concatenone con +
frase = saluto + ", " + nome + "!"
print(frase)

# metodi di sistema
s = "Ciao, Mondo"
print(len(s)) #lunghezza stringa
print(s.upper()) #tutto maiuscolo
print(s.lower()) #tutto minuscolo
print(s.replace("Mondo", "Universo")) #sostituzione testo
print(s.split(',')) #divisione in lista

#char
carattere = 'A'

#boolean
boolT = True
boolF = False
print(boolT, boolF)

#conversione tipi
boolT_int = int(boolT)
boolF_int = int(boolF)
print(boolT_int, boolF_int)

# operatori di confronto
print(5 > 3)   # Maggiore
print(2 < 4)   # Minore
print(7 >= 7)  # Maggiore o uguale
print(6 <= 8)  # Minore o uguale
print(3 == 3)  # Uguale
print(5 != 2)  # Diverso