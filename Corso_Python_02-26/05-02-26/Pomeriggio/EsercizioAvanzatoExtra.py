"""EXTRA: creare una funzione che converte da input a lista e una
    per convertire da lista a tupla e viceversa"""
    
#Funzione che converte da input a lista
def input_to_list(v,i:list):
    i.append(v)
    return i

def conversion(i:list):
    if type(i) == list:
        return tuple(i)
    elif type(i) == tuple:
        return list(i)
    else:
        return None

lst = []
while True:
    print("Giochiamo con le conversioni tra liste e tuple!\n")
    n = input("Inserisci qualcosa da inserire in una lista: ")
    #Richiamo la funzione per convertire da input a lista
    input_to_list(n,lst)
    r = input("Vuoi inserire un altro elemento? (s/n): ")
    if r.lower() != 's':
        break
    
print(f"Hai creato la lista: {lst}\n")
    
cnv = conversion(lst)
print(f"Vediamo ora la conversione, era una *{type(lst).__name__}* ed è diventata una *{type(cnv).__name__}*:\n{cnv}\n")