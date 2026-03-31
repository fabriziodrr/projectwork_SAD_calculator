def sottrazione_vettore():
    n = int(input("Quanti numeri vuoi inserire? "))
    
    if n < 1:
        print("Devi inserire almeno un numero.")
        return None 

    vettore = []
    for i in range(n):
        numero = float(input(f"Inserisci il numero {i+1}: "))
        vettore.append(numero)

    risultato = vettore[0]
    for i in range(1, len(vettore)):
        risultato -= vettore[i]

    print(f"Il risultato è: {risultato}")
    
    
    return risultato 