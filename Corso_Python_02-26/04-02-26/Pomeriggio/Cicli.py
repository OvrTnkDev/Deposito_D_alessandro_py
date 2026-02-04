# Ciclo while
count = 0

# ciclo while che conta fino a 5
while count <= 5:
    print(f"Count è: {count}")
    count += 1
    
# Ciclo while con booleano
running = True
while running:
    print("Il ciclo è in esecuzione.")
    stop = input("Vuoi fermare il ciclo? (s/n): ")
    if stop.lower() == 's':
        running = False
        
# Ciclo for su una lista
language = ["Python", "Java", "C++", "JavaScript"]
for l in language:
    print(f"Linguaggio di programmazione: {l}")
    
# Ciclo for con range
for i in range(5):
    print(f"Numero: {i}") #--> 0, 1, 2, 3, 4 (5 non incluso)
    
# Ciclo for con range e step numeri dispari
for i in range(1, 10, 2):
    print(f"Numero dispari: {i}") #--> 1, 3, 5, 7, 9 (10 non incluso)