def calcola_somma_utente():
    """
    Chiede all'utente quanti numeri sommare e ne restituisce il totale.
    """
    try:
        # Chiediamo il numero di elementi da processare
        quantita_input = input("Quanti valori vuoi sommare? ")
        quantita = int(quantita_input)
        
        if quantita <= 0:
            print("Per favore, inserisci un numero maggiore di zero.")
            return 0
        
        totale = 0
        
        # Iteriamo per il numero di volte richiesto
        for i in range(quantita):
            valore = float(input(f"Inserisci il valore {i + 1}: "))
            totale += valore
            
        return totale

    except ValueError:
        print("Errore: devi inserire un numero valido!")
        return None

# --- IMPORTANTE: Proteggi l'esecuzione automatica ---
if __name__ == "__main__":
    # Questo blocco viene eseguito SOLO se lanci direttamente questo file.
    # Se il file viene IMPORTATO dai test, questa parte viene ignorata.
    risultato = calcola_somma_utente()
    if risultato is not None:
        print(f"\nLa somma totale è: {risultato}")