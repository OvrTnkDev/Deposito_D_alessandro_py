#Esercizio Extra: match annidato
sesso = input("Inserisci il tuo sesso (M/F): ")

match sesso.lower():
    case "m":
        eta = int(input("Inserisci la tua età: "))
        match eta:
            case _ if eta < 18:
                print("Sei un ragazzo minorenne.")
            case _ if eta >= 18:
                print("Sei un uomo adulto.")
    case "f":
        eta = int(input("Inserisci la tua età: "))
        match eta:
            case _ if eta < 18:
                print("Sei una ragazza minorenne.")
            case _ if eta >= 18:
                print("Sei una donna adulta.")
    case _:
        print("Sesso non riconosciuto.")