import math

def calcola_cotangente_utente():
    """
    Chiede all'utente quanti valori processare e restituisce i loro valori di cotangente.
    L'input è in gradi. La funzione non è definita per multipli di 180°.
    """
    try:
        quantita_input = input("Di quanti valori vuoi calcolare la cotangente? ")
        quantita = int(quantita_input)
        
        if quantita <= 0:
            print("Inserisci un numero di elementi valido.")
            return []
        
        risultati = []
        
        for i in range(quantita):
            gradi = float(input(f"Inserisci il valore {i + 1} in gradi: "))
            
            # La cotangente non è definita dove il seno è 0 (0°, 180°, 360°...)
            if (gradi % 180) == 0:
                print(f"Errore: La cotangente non è definita per {gradi} gradi.")
                return None
            
            radianti = math.radians(gradi)
            # calcolo: 1 / tan(x)
            valore_cot = 1 / math.tan(radianti)
            risultati.append(round(valore_cot, 10))
            
        return risultati

    except ValueError:
        print("Errore: Inserisci solo numeri validi!")
        return None

if __name__ == "__main__":
    res = calcola_cotangente_utente()
    if res is not None:
        print(f"I valori della cotangente sono: {res}")