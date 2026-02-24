import numpy as np
from tqdm import tqdm
import time
from termcolor import colored as c

def loading():
    for i in tqdm(range(100), desc=c("Loading", "yellow")):
        time.sleep(0.03)

while True:
    
    arr = np.linspace(0, 10, 50)
    arr = arr.round(2) #arrotondamento a 2 decimali
    print("Array creato con linspace:", arr)


    #generare un array di 50 numeri compresi tra 0 e 1
    random_arr = np.random.rand(50) #creazione di un array con 50 numeri casuali tra 0 e 1
    random_arr = random_arr.round(2) #arrotondamento a 2 decimali
    print("Array creato con random:", random_arr)

    #soomo i due array elemento per elemento per ottenere un nuovo arrasy
    sum_arr = arr + random_arr.round(2) #somma elemento per elemento
    print("Somma dei due array elemento per elemento:", sum_arr.round(2))

    #calcolo la somma degli elementi maggiori di 5
    sum_elements = np.sum(sum_arr[sum_arr > 5]).round(2)
    print("Somma degli elementi maggiori di 5:", sum_elements)
    
    i = input("Vuoi aggiungere, sovrascrivere o uscire? (a/s/e): ")
    
    match i:
        case "a":
            #salviamo su un file txt con append
            loading()
            with open(r"Corso_Python_02-26/24-02-26/Mattina/output.txt", "a") as f:
                f.write(f"Array creato con linspace: {arr}")
                f.write(f"\nArray creato con random: {random_arr}")
                f.write(f"\nSomma dei due array elemento per elemento: {sum_arr}")
                f.write(f"\nSomma degli elementi maggiori di 5: {sum_elements}\n")
        case "s":
            #salviamo su un file txt sovrascrivendo
            loading()
            with open(r"Corso_Python_02-26/24-02-26/Mattina/output.txt", "w") as f:
                f.write(f"Array creato con linspace: {arr}")
                f.write(f"\nArray creato con random: {random_arr}")
                f.write(f"\nSomma dei due array elemento per elemento: {sum_arr}")
                f.write(f"\nSomma degli elementi maggiori di 5: {sum_elements}\n")
        case "e":
            print("Uscita dal programma.")
            break
        case _:
            print("Input non valido. Riprova.")