x = 5
y = 10
z = 7
# Operatore AND
print((x < y) and (y > z))  # True perché entrambe le condizioni sono vere
print((x > y) and (y > z))  # False perché una condizione è falsa
# Operatore OR
print((x < y) or (y < z))   # True perché una condizione è vera
print((x > y) or (y < z))   # False perché entrambe le condizioni sono false
# Operatore NOT
print(not(x < y))           # False perché la condizione è vera, quindi NOT la rende falsa
print(not(x > y))           # True perché la condizione è falsa, quindi NOT la rende vera