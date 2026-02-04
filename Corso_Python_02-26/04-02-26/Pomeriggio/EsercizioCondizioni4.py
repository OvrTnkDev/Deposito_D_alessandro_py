# Controllo dell'età per l'accesso a un film per maggiorenni con condizione match-case
eta = int(input("Inserisci la tua età: "))
match eta:
    # case _: Accetta qualsiasi valore (wildcard)
    # if eta >= 18: Questa è la "Guard". Il case viene eseguito SOLO se 
    #              la condizione è True.
    case _ if eta >= 18:
        print("Accesso consentito.")
    
    # case _: Se la condizione sopra è False, questo cattura tutto il resto
    #         (ovvero chiunque abbia meno di 18 anni).
    case _:
        print("Accesso negato.")
