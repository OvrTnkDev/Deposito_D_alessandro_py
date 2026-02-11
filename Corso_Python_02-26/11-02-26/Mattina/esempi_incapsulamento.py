class Computer():
    def __init__(self):
        self.__processore = "Intel i7" # attributo privato

    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore = processore
    
    
pc_OBJ = Computer()
print(pc_OBJ.get_processore())
# modifico il processore del computer usando il metodo setter
pc_OBJ.set_processore("AMD Ryzen 7")
# verifico che il processore sia stato modificato correttamente usando il metodo getter
print(pc_OBJ.get_processore())

# variabile globale
numero = 10

def funzione_esterna():
    # variabile locale
    numero = 5
    print(f"Numero dentro la funzione(locale): {numero}")
    
    def funzione_interna():
        nonlocal numero
        numero += 1
        print(f"Numero dentro la funzione interna(nonlocal): {numero}")
    
    funzione_interna()

print(f"Numero nel main(globale): {numero}")
funzione_esterna()
print(f"Numero nel main dopo la funzione esterna(globale): {numero}")