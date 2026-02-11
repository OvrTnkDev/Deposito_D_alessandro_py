class MiaClasse():
    def __init__(self):
        self.__variabile_privata = "Sono una variabile privata"
        
    def __metodo_privato(self):
        print("Sono un metodo privato")
        
    def metodo_pubblico(self, a):
        print("sono un metodo pubblico")
        if a > 12:
            print(self.__metodo_privato())
        else:
            print("Il numero è troppo piccolo per chiamare il metodo privato")
        
obj = MiaClasse()

print(obj._MiaClasse__variabile_privata)  # Accesso alla variabile privata tramite name mangling
obj._MiaClasse__metodo_privato()  # Accesso al metodo privato tramite name mangling

obj.metodo_pubblico(15)  # Chiamata al metodo pubblico che a sua volta chiama il metodo privato
obj.metodo_pubblico(10)  # Chiamata al metodo pubblico con un numero troppo piccolo per chiamare il metodo privato