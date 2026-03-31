def moltiplicazione() -> int:
    while True:
        try:
            n_operandi = int(input("Quanti numeri vuoi moltiplicare? "))
            if n_operandi > 0:
                break
            print("Inserisci un numero maggiore di zero.")
        except ValueError:
            print("Input non valido. Inserisci un numero intero.")

    risultato = 1
    for i in range(n_operandi):
        while True:
            try:
                numero = int(input(f"Inserisci il numero {i + 1}: "))
                risultato *= numero
                break
            except ValueError:
                print("Input non valido. Riprova.")

    return risultato

