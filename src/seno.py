import math

def calcola_seno(gradi):
    # Converte i gradi in radianti
    radianti = math.radians(gradi)
    # Calcola il seno
    risultato = math.sin(radianti)
    return risultato
