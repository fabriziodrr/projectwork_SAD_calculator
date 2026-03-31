import math

def calcola_tangente_utente():
    """
    Chiede all'utente quanti valori processare e restituisce i loro valori di tangente.
    L'input è atteso in gradi e convertito in radianti.
    """
    try:
        quantita_input = input("Di quanti valori vuoi calcolare la tangente? ")
        quantita = int(quantita_input)
        
        if quantita <= 0:
            print("Inserisci un numero di elementi valido.")
            return []
        
        risultati = []
        
        for i in range(quantita):
            gradi = float(input(f"Inserisci il valore {i + 1} in gradi: "))
            
            # Controllo per angoli dove la tangente non è definita (90, 270, -90, ecc.)
            if (gradi % 180) == 90:
                print(f"Errore: La tangente non è definita per {gradi} gradi.")
                return None
            
            radianti = math.radians(gradi)
            # Arrotondiamo a 10 decimali per gestire la precisione floating point
            risultati.append(round(math.tan(radianti), 10))
            
        return risultati

    except ValueError:
        print("Errore: Inserisci solo numeri validi!")
        return None

if __name__ == "__main__":
    res = calcola_tangente_utente()
    if res is not None:
        print(f"I valori della tangente sono: {res}")