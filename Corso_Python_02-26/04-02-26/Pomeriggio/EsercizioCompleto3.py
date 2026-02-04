on = True
while on:
    n = input("Inserisci una serie di numeri separati da spazi: ")
    n_list = n.split()
    for i in n_list:
        num = int(i)
        print(f"Quadrato di {num} è {num**2}")
    stop = input("Vuoi continuare? (s/n): ")
    if stop.lower() == 'n':
        on = False