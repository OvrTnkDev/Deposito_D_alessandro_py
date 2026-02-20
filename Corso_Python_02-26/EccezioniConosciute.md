# Tipi di errori in Python

- IndexError: list index out of range -> Errore index non trovato.
- TypeError: 'tuple' object does not support item assignment -> Errore di insert su una tupla, non si puo aggiungere poichè sono immutabili
- KeyError: 'key' -> Errore chiave non trovata, ad esempio in un dizionario.
- ValueError: invalid literal for int() with base 10: 'abc' -> Errore di conversione, non si può convertire una stringa in un numero intero.
- ZeroDivisionError: division by zero -> Errore di divisione per zero, non si può dividere un numero per zero.
- FileNotFoundError: [Errno 2] No such file or directory: 'file.txt' -> Errore di file non trovato, il file specificato non esiste.
- AttributeError: 'str' object has no attribute 'append' -> Errore di attributo, la stringa non ha il metodo append, che è invece presente nelle liste.
- ImportError: No module named 'module' -> Errore di importazione, il modulo specificato non esiste o non è installato.
- SyntaxError: invalid syntax -> Errore di sintassi, il codice non è scritto correttamente secondo le regole del linguaggio Python.
- IndentationError: unexpected indent -> Errore di indentazione, il codice non è indentato correttamente, ad esempio con spazi o tabulazioni non coerenti.
- NameError: name 'variable' is not defined -> Errore di nome, la variabile o funzione specificata non è definita nel contesto in cui viene utilizzata.
- RuntimeError: unhandled exception -> Errore di runtime, si verifica durante l'esecuzione del programma, ad esempio quando si verifica un'eccezione non gestita.
- MemoryError: out of memory -> Errore di memoria, il programma ha esaurito la memoria disponibile.
- OverflowError: int too large to convert -> Errore di overflow, un numero intero è troppo grande per essere convertito in un tipo di dato supportato.
- RecursionError: maximum recursion depth exceeded -> Errore di ricorsione, la profondità massima di ricorsione è stata superata, ad esempio quando una funzione chiama se stessa in modo ricorsivo senza una condizione di terminazione adeguata.
