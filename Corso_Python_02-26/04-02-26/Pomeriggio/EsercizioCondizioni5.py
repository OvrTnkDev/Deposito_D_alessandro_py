# Calcolatrice con match-case
num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
operazione = input("Inserisci l'operazione (+, -, *, /): ")
# Uso di match-case per eseguire l'operazione richiesta
match operazione:
    #Operazioni aritmetiche di base
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        # Controllo per evitare la divisione per zero
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Errore: Divisione per zero non consentita.")
    case _:
        print("Operazione non valida.")