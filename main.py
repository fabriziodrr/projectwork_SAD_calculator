import builtins
from src.addizione import calcola_somma_utente
from src.sottrazione import sottrazione_vettore
from src.moltiplicazione import moltiplicazione
from src.divisione import calcola_divisione_utente
from src.seno import calcola_seno
from src.coseno import calcola_coseno_utente
from src.tangente import calcola_tangente_utente
from src.cotangente import calcola_cotangente_utente
from src.arcoseno import calcola_arcoseno
from src.arcocoseno import calcola_arcocoseno_utente


def menu_principale():
    """Presenta il menu principale della calcolatrice."""
    print("\n" + "=" * 50)
    print("CALCOLATRICE MODULARE - SAD Calculator")
    print("=" * 50)
    print("1. Addizione (somma di più numeri)")
    print("2. Sottrazione (sottrazione progressiva)")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Seno")
    print("6. Coseno")
    print("7. Tangente")
    print("8. Arcoseno")
    print("9. Arcocoseno")
    print("10. Cotangente")
    print("11. Cronologia")
    print("12. Esci")
    print("=" * 50)
    print("Suggerimento: digita 'ans' per usare l'ultimo valore numerico calcolato.")


def operazione_divisione():
    """Funzione wrapper per la divisione che gestisce l'input dell'utente."""
    risultato = calcola_divisione_utente()
    if risultato is not None:
        print(f"\nRisultato della divisione: {risultato}")
    return risultato


def operazione_seno():
    """Esegue il calcolo del seno per una serie di valori in gradi."""
    try:
        quantita = int(input("Di quanti valori vuoi calcolare il seno? "))
        if quantita <= 0:
            print("Inserisci un numero di elementi valido.")
            return None

        risultati = []
        for i in range(quantita):
            gradi = float(input(f"Inserisci il valore {i + 1} in gradi: "))
            risultati.append(round(calcola_seno(gradi), 10))

        print(f"\nRisultati del seno: {risultati}")
        return risultati

    except ValueError:
        print("Errore: Inserisci solo numeri validi!")
        return None


def operazione_arcoseno():
    """Esegue il calcolo dell'arcoseno per un singolo valore."""
    try:
        valore = float(input("Inserisci il valore per l'arcoseno (tra -1 e 1): "))
        risultato = calcola_arcoseno(valore)

        if isinstance(risultato, str):
            print(risultato)
            return None

        print(f"\nArcoseno in gradi: {risultato}")
        return risultato

    except ValueError:
        print("Errore: Inserisci solo numeri validi!")
        return None


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
        scelta = input_originale("\nScegli un'operazione (1-12): ").strip()
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
            if risultato_corrente is not None:
                cronologia.append(f"Sottrazione -> Risultato: {risultato_corrente}")

        elif scelta == "3":
            print("\n--- MOLTIPLICAZIONE ---")
            risultato_corrente = moltiplicazione()
            if risultato_corrente is not None:
                print(f"\nRisultato della moltiplicazione: {risultato_corrente}")
                cronologia.append(f"Moltiplicazione -> Risultato: {risultato_corrente}")

        elif scelta == "4":
            print("\n--- DIVISIONE ---")
            risultato_corrente = operazione_divisione()
            if risultato_corrente is not None:
                cronologia.append(f"Divisione -> Risultato: {risultato_corrente}")

        elif scelta == "5":
            print("\n--- SENO ---")
            risultato_corrente = operazione_seno()
            if risultato_corrente is not None:
                cronologia.append(f"Seno -> Risultati: {risultato_corrente}")

        elif scelta == "6":
            print("\n--- COSENO ---")
            risultato_corrente = calcola_coseno_utente()
            if risultato_corrente is not None:
                print(f"\nRisultati del coseno: {risultato_corrente}")
                cronologia.append(f"Coseno -> Risultati: {risultato_corrente}")

        elif scelta == "7":
            print("\n--- TANGENTE ---")
            risultato_corrente = calcola_tangente_utente()
            if risultato_corrente is not None:
                print(f"\nRisultati della tangente: {risultato_corrente}")
                cronologia.append(f"Tangente -> Risultati: {risultato_corrente}")

        elif scelta == "8":
            print("\n--- ARCOSENO ---")
            risultato_corrente = operazione_arcoseno()
            if risultato_corrente is not None:
                cronologia.append(f"Arcoseno -> Risultato: {risultato_corrente}")

        elif scelta == "9":
            print("\n--- ARCOCOSENO ---")
            risultato_corrente = calcola_arcocoseno_utente()
            if risultato_corrente is not None:
                print(f"\nRisultati dell'arcocoseno: {risultato_corrente}")
                cronologia.append(f"Arcocoseno -> Risultati: {risultato_corrente}")

        elif scelta == "10":
            print("\n--- COTANGENTE ---")
            risultato_corrente = calcola_cotangente_utente()
            if risultato_corrente is not None:
                print(f"\nRisultati della cotangente: {risultato_corrente}")
                cronologia.append(f"Cotangente -> Risultati: {risultato_corrente}")

        elif scelta == "11":
            print("\n--- CRONOLOGIA ---")
            if not cronologia:
                print("Nessuna operazione in cronologia.")
            else:
                for i, op in enumerate(cronologia, 1):
                    print(f"{i}. {op}")

        elif scelta == "12":
            print("\nGrazie per aver usato la Calcolatrice SAD!")
            print("Arrivederci!")
            break

        else:
            print("Scelta non valida. Per favore, inserisci un numero tra 1 e 11.")

        # Salva l'ultimo risultato valido nella variabile 'ans'
        if isinstance(risultato_corrente, (int, float)):
            ultimo_risultato = risultato_corrente


if __name__ == "__main__":
    main()