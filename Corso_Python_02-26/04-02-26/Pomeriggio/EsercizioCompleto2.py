on = True
while on:
    n = int(input("Inserisci un numero: "))
    if n > 0:
        for i in range(n, -1, -1):
            print(f"Numero: {i}")
    else:
        print("Inserisci un numero positivo.")
    stop = input("Vuoi continuare? (s/n): ")
    if stop.lower() == 'n':
        on = False