on = True
while on:
    n = input("Inserisci una serie di numeri separati da spazi: ")
    n_list = n.split()
    one = 0
    for i in n_list:
        two = int(i)
        if two > one:
            one = two
    print(f"Il numero più grande è: {one}")
    
    count = 0
    if len(n_list) == 0:
        print("Non sono stati inseriti numeri.")
    else:
        while len(n_list) > 0:
            count += 1
            n_list.pop()
        print(f"Sono stati inseriti {count} numeri.")
        print(f"Quind il numero più grande è {one} e sono stati inseriti {count} numeri.")
        if input("Vuoi continuare? (s/n): ").lower() != 's':
            on = False