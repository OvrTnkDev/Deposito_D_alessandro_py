# Conto alla rovescia con iput utente solo while
on = True
while on:
    n = int(input("Inserisci un numero intero positivo per il conto alla rovescia: "))
    while n >= 0:
        print(n)
        n-=1
risposta = input("Vuoi inserire un altro numero? (s/n): ")
if risposta.lower() != 's':
    on = False

# Conto alla rovescia con iput utente while e for
continuare = True
while continuare:
    x = int(input("Inserisci un numero intero positivo per il conto alla rovescia: "))
    for i in range(x, -1, -1):
        print(i)
    risposta2 = input("Vuoi inserire un altro numero? (s/n): ")
    if risposta2.lower() != 's':
        continuare = False