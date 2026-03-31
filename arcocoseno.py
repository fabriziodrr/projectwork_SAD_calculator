import math

def calcola_arcocoseno_utente():
    """
    Chiede all'utente quanti valori processare e restituisce i loro arcocoseni in gradi.
    L'input deve essere compreso tra -1 e 1.
    """
    try:
        quantita_input = input("Di quanti valori vuoi calcolare l'arcocoseno? ")
        quantita = int(quantita_input)
        
        if quantita <= 0:
            print("Inserisci un numero di elementi valido.")
            return []
        
        risultati = []
        
        for i in range(quantita):
            valore = float(input(f"Inserisci il valore {i + 1} (tra -1 e 1): "))
            
            # Controllo del dominio: l'arcocoseno esiste solo tra -1 e 1
            if valore < -1 or valore > 1:
                print(f"Errore: il valore {valore} è fuori dal dominio [-1, 1].")
                return None
            
            # Calcolo in radianti e conversione in gradi per leggibilità
            radianti = math.acos(valore)
            gradi = math.degrees(radianti)
            risultati.append(round(gradi, 2))
            
        return risultati

    except ValueError:
        print("Errore: Inserisci solo numeri validi!")
        return None

if __name__ == "__main__":
    res = calcola_arcocoseno_utente()
    if res is not None:
        print(f"Gli angoli calcolati (in gradi) sono: {res}")