from addizione import calcola_somma_utente
from sottrazione import sottrazione_vettore
from moltiplicazione import moltiplicazione
from divisione import calcola_divisione_utente


def menu_principale():
    """Presenta il menu principale della calcolatrice."""
    print("\n" + "="*50)
    print("CALCOLATRICE MODULARE - SAD Calculator")
    print("="*50)
    print("1. Addizione (somma di più numeri)")
    print("2. Sottrazione (sottrazione progressiva)")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Cronologia")
    print("6. Esci")
    print("="*50)


def operazione_divisione():
    """Funzione wrapper per la divisione che gestisce l'input dell'utente."""
    risultato = calcola_divisione_utente()
    if risultato is not None:
        print(f"\nRisultato della divisione: {risultato}")
    return risultato


def main():
    """Funzione principale che gestisce il ciclo della calcolatrice."""
    cronologia = []

    while True:
        menu_principale()
        scelta = input("\nScegli un'operazione (1-6): ").strip()
        
        if scelta == "1":
            print("\n--- ADDIZIONE ---")
            risultato = calcola_somma_utente()
            if risultato is not None:
                print(f"\nLa somma totale è: {risultato}")
                cronologia.append(f"Addizione -> Risultato: {risultato}")
            
        elif scelta == "2":
            print("\n--- SOTTRAZIONE ---")
            risultato = sottrazione_vettore()
            # Se la funzione non restituisce nulla, salva solo l'avvenuta esecuzione
            valore_salvato = risultato if risultato is not None else "Eseguita"
            cronologia.append(f"Sottrazione -> Risultato: {valore_salvato}")
            
        elif scelta == "3":
            print("\n--- MOLTIPLICAZIONE ---")
            risultato = moltiplicazione()
            print(f"\nRisultato della moltiplicazione: {risultato}")
            cronologia.append(f"Moltiplicazione -> Risultato: {risultato}")
            
        elif scelta == "4":
            print("\n--- DIVISIONE ---")
            risultato = operazione_divisione()
            if risultato is not None:
                cronologia.append(f"Divisione -> Risultato: {risultato}")
        
        elif scelta == "5":
            print("\n--- CRONOLOGIA ---")
            if not cronologia:
                print("Nessuna operazione in cronologia.")
            else:
                for i, op in enumerate(cronologia, 1):
                    print(f"{i}. {op}")
                    
        elif scelta == "6":
            print("\nGrazie per aver usato la Calcolatrice SAD!")
            print("Arrivederci!")
            break
            
        else:
            print("Scelta non valida. Per favore, inserisci un numero tra 1 e 6.")


if __name__ == "__main__":
    main()