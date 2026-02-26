import random as rnd

def crea_gruppi(n_persone:list, n_gruppi:int):
    if n_gruppi > len(n_persone):
        print("Il numero di gruppi deve essere minore o uguale al numero di persone.")
        return
    else:
        rnd.shuffle(n_persone)
        gruppi = [[] for _ in range(n_gruppi)]
        for i, persona in enumerate(n_persone):
            gruppi[i % n_gruppi].append(persona)
        for idx, gruppo in enumerate(gruppi):
            print(f"Gruppo {idx + 1}: {', '.join(gruppo)}")


list_name =["Fabio D'alessandro", "Gabriele Carucci", "Elisabetta Carella", "Gabriele Giuliani",
             "Maria Visione", "Mariagrazia Nuzzolese", "Nico Davide Cognetta",
            "Valerio Carìa", "Marco A. De Felicis", "Giovanni Iadalise"]

print(crea_gruppi(list_name, 5))