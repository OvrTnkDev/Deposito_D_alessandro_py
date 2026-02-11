import mod_squadra as ms
import random as rnd
import time
from termcolor import colored as cl

# Generatorei per descrivere le squadre e farle giocare contro
def descrivi_squadra(nome_squadra, allenatore, assistente, squadra):
    print(f"Descrizione della squadra {nome_squadra}:")
    print(f"Allenatore: {allenatore}")
    print(f"Assistente: {assistente}")
    for i in squadra:
        yield i.__str__()



# creo una lista di nomi
nomi = ["Goku", "Vegeta", "Piccolo", "Gohan", "Trunks", "Krillin",
        "Yamcha", "Tien", "Chiaotzu", "Bulma", "Chi-Chi", "Master Roshi",
        "Frieza", "Cell", "Majin Buu", "Beerus", "Whis"]
# creo una lista di eta
eta =[rnd.randint(20, 200) for _ in range(17)]
# creo una lista di ruoli
ruoli = ["attaccante", "difensore", "centrocampista"]
# creo una lista di numeri di maglia
numeri_maglia = [rnd.randint(1, 99) for _ in range(17)]
# creo una lista di anni di esperienza per gli allenatori
anni_esperienza = [rnd.randint(1, 30) for _ in range(17)]
# creo una lista di specializzazioni strane per gli assistenti
specializzazioni_strane = ["musicista", "imbianchino", "muratore", "ballerino", "mago", "sessuologo"]

# creo due squadre
# ciclo for per creare 5 giocatori per ogni squadra, assegnando loro un nome, un'età, un ruolo e un numero di maglia casuali
squadra_black_OBJ = [ms.Giocatore(nomi[i], eta[i], ruoli[rnd.randint(0, 2)], numeri_maglia[i]) for i in range(5)]
# creo la seconda squadra, range da 5 a 10 per evitare di sovrapporre i nomi con la prima squadra
squadra_red_OBJ = [ms.Giocatore(nomi[i], eta[i], ruoli[rnd.randint(0, 2)], numeri_maglia[i]) for i in range(5, 10)]
# creo un allenatore per ogni squadra
allenatore_black_OBJ = [ms.Allenatore(nomi[i], eta[i], anni_esperienza[i]) for i in range(0,16, 2)]
allenatore_red_OBJ = [ms.Allenatore(nomi[i], eta[i], anni_esperienza[i]) for i in range(0, 16, 1)]
# creo un assistente per ogni squadra
assistente_black_OBJ = [ms.Assistente(nomi[i], eta[i], specializzazioni_strane[rnd.randint(0, 5)]) for i in range(8, 16)]
assistente_red_OBJ = [ms.Assistente(nomi[i], eta[i], specializzazioni_strane[rnd.randint(0, 5)]) for i in range(0, 8)]

# faccio giocare le due squadre contro
print("Partita tra la squadra Black e la squadra Red!")

# descrivo le squadre
print(cl(list(descrivi_squadra("Black", allenatore_black_OBJ[0], assistente_black_OBJ[0], squadra_black_OBJ)), "blue"))
print(assistente_black_OBJ[0].supporta_team())
print("\n")
time.sleep(3)

print(cl(list(descrivi_squadra("Red", allenatore_red_OBJ[0], assistente_red_OBJ[0], squadra_red_OBJ)), "red"))
print(assistente_red_OBJ[0].supporta_team())
print("\n")
time.sleep(3)

# annido 2 cicli per far giocare le due squadre contro ma cosi non va bene perche per ogni azione black se ne fanno n red
# quindi annido i cicli in modo che prima giocano tutti i black e poi tutti i red

for i in range(0, 91, 5):
        print(cl("Azioni della squadra Black:", "blue", attrs=["bold"]))
        for giocatore in squadra_black_OBJ:
                print(cl(f"Score: {float(i)*1,0}", "white", attrs=["bold"]))
                print(cl(giocatore.gioca_partita(), "blue"))
                print("\n")
                time.sleep(1)

        print(cl("Azioni della squadra Red:", "red", attrs=["bold"]))
        for giocatore in squadra_red_OBJ:
                print(cl(f"Score: {float(i)*1,0}", "white", attrs=["bold"]))
                print(cl(giocatore.gioca_partita(), "red"))
                print("\n")
                time.sleep(1)