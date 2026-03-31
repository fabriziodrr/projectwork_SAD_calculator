import builtins
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
    print("Suggerimento: digita 'ans' per usare il risultato precedente.")

def operazione_divisione():
    """Funzione wrapper per la divisione che gestisce l'input dell'utente."""
    risultato = calcola_divisione_utente()
    if risultato is not None:
        print(f"\nRisultato della divisione: {risultato}")
    return risultato

def main():
    """Funzione principale che gestisce il ciclo della calcolatrice."""
    cronologia = []
    ultimo_risultato = 0
    
    # Override di input() per iniettare il valore "ans" in tutti i sottomoduli
    input_originale = builtins.input
    def input_con_ans(prompt=""):
        valore = input_originale(prompt).strip()
        if valore.lower() == "ans":
            print(f" [Recuperato ans: {ultimo_risultato}]")
            return str(ultimo_risultato)
        return valore
    
    # Applica l'override globalmente
    builtins.input = input_con_ans

    while True:
        # Uso input_originale per il menu, così non viene interpretato "ans" accidentalmente
        menu_principale()
        scelta = input_originale("\nScegli un'operazione (1-6): ").strip()
        risultato_corrente = None
        
        if scelta == "1":
            print("\n--- ADDIZIONE ---")
            risultato_corrente = calcola_somma_utente()
            if risultato_corrente is not None:
                print(f"\nLa somma totale è: {risultato_corrente}")
                cronologia.append(f"Addizione -> Risultato: {risultato_corrente}")
            
        elif scelta == "2":
            print("\n--- SOTTRAZIONE ---")
            risultato_corrente = sottrazione_vettore()
            valore_salvato = risultato_corrente if risultato_corrente is not None else "Eseguita"
            cronologia.append(f"Sottrazione -> Risultato: {valore_salvato}")
            
        elif scelta == "3":
            print("\n--- MOLTIPLICAZIONE ---")
            risultato_corrente = moltiplicazione()
            print(f"\nRisultato della moltiplicazione: {risultato_corrente}")
            cronologia.append(f"Moltiplicazione -> Risultato: {risultato_corrente}")
            
        elif scelta == "4":
            print("\n--- DIVISIONE ---")
            risultato_corrente = operazione_divisione()
            if risultato_corrente is not None:
                cronologia.append(f"Divisione -> Risultato: {risultato_corrente}")
        
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

        # Salva l'ultimo risultato valido nella variabile 'ans'
        if isinstance(risultato_corrente, (int, float)):
            ultimo_risultato = risultato_corrente

if __name__ == "__main__":
    main()