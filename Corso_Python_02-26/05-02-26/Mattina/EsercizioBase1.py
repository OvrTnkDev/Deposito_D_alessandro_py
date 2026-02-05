while True:
    o = input("Vuoi inserire un numero o una stringa? (n/s): ").lower()
    
    match o:
        case 'n':
            num = float(input("Inserisci un numero: "))
            if num % 2 == 0:
                print(f"Il numero {num} è pari.")
            else:
                print(f"Il numero {num} è dispari.")
        case 's':
            stringa = input("Inserisci una stringa: ")
            lunghezza = len(stringa)
            if lunghezza % 2 == 0:
                print(f"La stringa '{stringa}' ha una lunghezza pari di {lunghezza} caratteri ed è pari.")
            else:
                print(f"La stringa '{stringa}' ha una lunghezza dispari di {lunghezza} caratteri ed è dispari.")
        case _:
            print("Opzione non valida. Per favore, scegli 'n' per numero o 's' per stringa.\n\n")
            
    continua = input("Vuoi continuare? (s/n): ").lower()
    if continua != 's':
        print("Uscita dal programma.")
        break