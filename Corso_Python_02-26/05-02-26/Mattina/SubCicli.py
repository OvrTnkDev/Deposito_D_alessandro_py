fruits = ("apple", "banana", "cherry", "date", "elderberry")

for fruit in fruits:
    if fruit.lower() == "date":
        # interrompe il ciclo quando si incontra "date"
        break
    print(fruit)

print("\n---\n")

iot = ("Raspberry Pi", "Arduino", "ESP32", "BeagleBone", "Particle")

for d in iot:
    if d.lower() == "beaglebone":
        # salta "BeagleBone" e continua con l'iterazione successiva
        continue
    print(d)
    
print("\n---\n")

for i in range(15):
    if i % 2 ==0:
        # pass serve come segnaposto, non fa nulla
        pass
    print(i)

print("\n---\n")

# Operatore di SPLAT -> * -> scompattare liste o tuple
n = [*range(0, 11, 2)]  # crea una lista di numeri dispari da 1 a 10
print(n)

