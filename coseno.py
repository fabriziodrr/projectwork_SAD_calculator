import math

def calcola_coseno_utente():
    """
    Chiede all'utente quanti valori processare e restituisce una lista dei loro coseni.
    L'input è atteso in gradi e convertito in radianti.
    """
    try:
        quantita_input = input("Di quanti valori vuoi calcolare il coseno? ")
        quantita = int(quantita_input)
        
        if quantita <= 0:
            print("Inserisci un numero di elementi valido.")
            return []
        
        risultati = []
        
        for i in range(quantita):
            gradi = float(input(f"Inserisci il valore {i + 1} in gradi: "))
            # Convertiamo in radianti perché math.cos usa i radianti
            radianti = math.radians(gradi)
            risultati.append(round(math.cos(radianti), 10))
            
        return risultati

    except ValueError:
        print("Errore: Inserisci solo numeri validi!")
        return None

if __name__ == "__main__":
    res = calcola_coseno_utente()
    if res is not None:
        print(f"I coseni calcolati sono: {res}")