x = 10
y = 5

# Condizione semplice
if (x > y):
    print("x è maggiore di y")


if (x < y):
    print("x è minore di y")
# Condizione con else
else:
    print("x non è minore di y")

# Condizione con elif
if (x == y):
    print("x è uguale a y")
elif (x > y):
    print("x è maggiore di y")
else:
    print("x è minore di y")
    
    
# Condizione match-case (Python 3.10+)
cmd = input("Inserisci un comando (start/stop/exit): ")
# Uso di match-case per gestire i comandi
match cmd.lower():
    case "start":
        print("Comando avviato")
    case "stop":
        print("Comando fermato")
    case "exit":
        print("Uscita dal programma")
    case _:
        print("Comando non riconosciuto")