"""create un programma che richiede all’utente tre numeri e verifica la presenza di almeno due numeri uguali,
se non ci sono ci restituisce il numero più grande dei tre"""

def verifica_numeri(a, b, c):
    # verifico se ci sono numeri uguali tra i tre inseriti
    if a == b: return "Il primo e il secondo numero sono uguali."
    elif a == c: return "Il primo e il terzo numero sono uguali."
    elif b == c: return "Il secondo e il terzo numero sono uguali."
    else: return f"Non ci sono numeri uguali."
    
def numero_max(a, b, c):
    # uso un operatore ternario per restituire il numero più grande tra i tre
    return f"Il numero più grande è: {a if a > b and a > c else b if b > a and b > c else c}."



# chiedo all'utente di inserire tre numeri e li converto in interi
num1 = int(input("inserisci il primo numero: "))
num2 = int(input("inserisci il secondo numero: "))
num3 = int(input("inserisci il terzo numero: "))

print(verifica_numeri(num1, num2, num3))
print(numero_max(num1, num2, num3))