while True:
    scelta = input("Vuoi inserire 2 numeri per trovare i loro fattori comuni o comparare stringhe?(n/s): ").lower()
    match scelta:
        # fattori comuni tra due numeri
        case 'n':
            num = input("Inserisci 2 numeri separati da uno spazio (es. 6 12): ")
            num_list = list(map(int, num.split()))
            
            if len(num_list) != 2:
                print("Per favore, inserisci esattamente 2 numeri.\n")
                continue

            x, y = num_list
            
            # 1. Controllo validità input PRIMA di fare calcoli
            if x <= 0 or y <= 0:
                print("Per favore, inserisci numeri positivi.\n")
                continue
                
            # 2. Logica di calcolo
            fattori_comuni = []
            for j in range(1, min(x, y) + 1):
                if x % j == 0 and y % j == 0:
                    fattori_comuni.append(j)
            
            # 3. Output dei risultati
            # Se l'unico fattore comune è 1 (la lista ha lunghezza 1), sono coprimi
            if len(fattori_comuni) == 1:
                print(f"Fattori comuni di {x} e {y}: {fattori_comuni}. (Sono coprimi)")
            else:
                print(f"Fattori comuni di {x} e {y}: {fattori_comuni}")

        # comparazione stringhe
        case 's':
            s = input("Inserisci 2 stringhe separate da uno spazio (es. ubi abi): ")
            s_list = list(map(str, s.split()))
            if len(s_list) != 2:
                print("Per favore, inserisci esattamente 2 stringhe.\n")
                continue
            str1, str2 = s_list
            if len(str1) != len(str2):
                print(f"Le stringhe '{str1}' e '{str2}' hanno lunghezze diverse ({len(str1)} e {len(str2)} caratteri).")
            else:
                # Confronto carattere per carattere e vedere se sono polinomi con sorted() che ordina i caratteri in ordine alfabetico
                if sorted(str1) == sorted(str2):
                    print(f"Le stringhe '{str1}' e '{str2}' sono polinomi (hanno gli stessi caratteri).")
                else:
                    print(f"Le stringhe '{str1}' e '{str2}' hanno la stessa lunghezza ma non sono polinomi.")
                
            """if str1 == str2:
                print(f"Le stringhe '{str1}' e '{str2}' sono uguali.")
            else:
                print(f"Le stringhe '{str1}' e '{str2}' sono diverse.")"""
        case _:
            print("Opzione non valida. Per favore, scegli 'n' per numeri o 's' per stringhe.\n\n")

    continua = input("Vuoi continuare? (s/n): ").lower()
    if continua != 's':
        print("Uscita dal programma.")
        break