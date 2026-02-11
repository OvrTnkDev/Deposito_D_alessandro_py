import conto_bancario as cb

if __name__ == "__main__":
    while True:
        u = input("Benvenuto nella banca del plebeo!\n" + 
              "Sei un utente, un admin o vuoi uscire? (u/a/e): ").lower()
        
        match u:
            case "u":
                n = input("Inserisci il tuo nome: ")
                user_OBJ = cb.Utente(n)
                while True:
                    a = input("Cosa vuoi fare?\n1. Deposita\n2. Preleva\n3. Visualizza saldo\n4. Esci dal conto\nScelta: ")
                    match a:
                        case "1":
                            importo = float(input("Inserisci l'importo da depositare: "))
                            user_OBJ.deposita(importo)
                        case "2":
                            importo = float(input("Inserisci l'importo da prelevare: "))
                            user_OBJ.preleva(importo)
                        case "3":
                            user_OBJ.visualizza_saldo()
                        case "4":
                            print("Grazie per aver utilizzato la banca del plebeo. Arrivederci!")
                            break
                        case _:
                            print("Scelta non valida. Riprova.")

            case "a":
                n = input("Inserisci il tuo nome: ")
                admin_OBJ = cb.Admin(n, user_OBJ.get_importo())
                while True:
                    a = input("Cosa vuoi fare?\n1. Deposita\n2. Preleva\n3. Visualizza saldo\n4. Esci dal conto\nScelta: ")
                    match a:
                        case "1":
                            importo = float(input("Inserisci l'importo da depositare: "))
                            admin_OBJ.deposita(importo)
                            
                        case "2":
                            importo = float(input("Inserisci l'importo da prelevare: "))
                            admin_OBJ.preleva(importo)
                        case "3":
                            admin_OBJ.visualizza_saldo()
                        case "4":
                            print("Grazie per aver utilizzato la banca del plebeo. Arrivederci!")
                            break
                        case _:
                            print("Scelta non valida. Riprova.")

            case "e":
                print("Grazie per aver utilizzato la banca del plebeo. Arrivederci!")
                break

            case _:
                print("Scelta non valida. Riprova.")
                continue








