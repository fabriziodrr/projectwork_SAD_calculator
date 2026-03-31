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
    print("5. Esci")
    print("="*50)


def operazione_divisione():
    """Funzione wrapper per la divisione che gestisce l'input dell'utente."""
    risultato = calcola_divisione_utente()
    if risultato is not None:
        print(f"\nRisultato della divisione: {risultato}")


def main():
    """Funzione principale che gestisce il ciclo della calcolatrice."""
    while True:
        menu_principale()
        scelta = input("\nScegli un'operazione (1-5): ").strip()
        
        if scelta == "1":
            print("\n--- ADDIZIONE ---")
            risultato = calcola_somma_utente()
            if risultato is not None:
                print(f"\nLa somma totale è: {risultato}")
            
        elif scelta == "2":
            print("\n--- SOTTRAZIONE ---")
            sottrazione_vettore()
            
        elif scelta == "3":
            print("\n--- MOLTIPLICAZIONE ---")
            risultato = moltiplicazione()
            print(f"\nRisultato della moltiplicazione: {risultato}")
            
        elif scelta == "4":
            print("\n--- DIVISIONE ---")
            operazione_divisione()
            
        elif scelta == "5":
            print("\nGrazie per aver usato la Calcolatrice SAD!")
            print("Arrivederci!")
            break
            
        else:
            print("Scelta non valida. Per favore, inserisci un numero tra 1 e 5.")


if __name__ == "__main__":
    main()
