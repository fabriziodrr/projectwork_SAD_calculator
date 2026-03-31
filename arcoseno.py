import math

def calcola_arcoseno(valore):
    if valore < -1 or valore > 1:
        return "Errore: l'input deve essere compreso tra -1 e 1"
    
    radianti = math.asin(valore)
    
    gradi = math.degrees(radianti)
    
    return round(gradi, 10)