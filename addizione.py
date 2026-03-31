def calcola_somma_utente():
    
    #Chiede all'utente quanti numeri sommare e ne restituisce il totale.
    try:
        # Chiediamo il numero di elementi da processare
        quantita = int(input("Quanti valori vuoi sommare? "))
        
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

# Chiamata della funzione e stampa del risultato
risultato = calcola_somma_utente()

if risultato is not None:
    print(f"\nLa somma totale è: {risultato}")