def calcola_divisione_utente():
    """
    Chiede all'utente quanti valori dividere e restituisce il quoziente.
    """
    try:
        quantita_input = input("Quanti valori vuoi inserire per la divisione? ")
        quantita = int(quantita_input)
        
        if quantita <= 0:
            print("Inserisci un numero di elementi valido.")
            return None
        
        # Prendiamo il primo numero come base
        risultato = float(input("Inserisci il primo valore (dividendo): "))
        
        # Iteriamo per i restanti valori
        for i in range(1, quantita):
            divisore = float(input(f"Inserisci il divisore {i}: "))
            
            if divisore == 0:
                print("Errore: Il divisore non può essere zero.")
                return None # Restituisce None per indicare un errore matematico
            
            risultato /= divisore
            
        return risultato

    except ValueError:
        print("Errore: Inserisci solo numeri validi!")
        return None

if __name__ == "__main__":
    res = calcola_divisione_utente()
    if res is not None:
        print(f"Risultato: {res}")