# SAD Calculator - Calcolatrice Modulare

Una calcolatrice interattiva modulare sviluppata in Python con operazioni matematiche di base organizzate in moduli separati.

## 📋 Descrizione Progetto

SAD Calculator è un progetto didattico che dimostra i principi della programmazione modulare in Python. Il progetto è organizzato in moduli indipendenti per ogni operazione matematica, con un'interfaccia principale che integra tutte le funzionalità.

## ✨ Funzionalità

- **Addizione**: Somma di più numeri inseriti dall'utente
- **Sottrazione**: Sottrazione progressiva di più numeri
- **Moltiplicazione**: Moltiplicazione di più numeri
- **Divisione**: Divisione progressiva di più numeri con gestione degli errori
- **Seno/Coseno/Tangente/Arcoseno/Arcocoseno**: Funzioni trigonometriche sugli angoli in gradi
- **Menu Interattivo**: Interfaccia user-friendly con ciclo continuo
- **Cronologia**: Log delle operazioni eseguite in sessione

## 📁 Struttura del Progetto

```
projectwork_SAD_calculator/
├── main.py                    # File principale con menu interattivo
├── README.md                  # Documentazione del progetto
├── src/                       # Moduli operativi
│   ├── addizione.py
│   ├── sottrazione.py
│   ├── moltiplicazione.py
│   ├── divisione.py
│   ├── seno.py
│   ├── coseno.py
│   ├── tangente.py
│   ├── arcoseno.py
│   └── arcocoseno.py
└── tests/                     # Test unitari di tutti i moduli
    ├── testSomma.py
    ├── testSottrazione.py
    ├── testMoltiplicazione.py
    ├── testDivisione.py
    ├── testSeno.py
    ├── testCoseno.py
    ├── testTangente.py
    ├── testArcoseno.py
    ├── testArcocoseno.py
    └── testCotangente.py
```

## 🚀 Come Utilizzare

### Avvio del Programma

```bash
python main.py
```

### Navigazione nel Menu

Il programma presenta un menu principale con le seguenti opzioni:

```
==================================================
CALCOLATRICE MODULARE - SAD Calculator
==================================================
1. Addizione (somma di più numeri)
2. Sottrazione (sottrazione progressiva)
3. Moltiplicazione
4. Divisione
5. Seno
6. Coseno
7. Tangente
8. Arcoseno
9. Arcocoseno
10. Cotangente
11. Cronologia
12. Esci
==================================================
```

## 🧪 Test Unitari

`main.py` supporta il comando speciale `ans` in tutti i prompt numerici, che sostituisce l'ultimo valore calcolato valido.

Esegui i test con:

```bash
cd tests
python -m unittest
```

## 📚 Dettagli Moduli

- `src/addizione.py`: operazioni di addizione
- `src/sottrazione.py`: operazioni di sottrazione
- `src/moltiplicazione.py`: operazioni di moltiplicazione
- `src/divisione.py`: operazioni di divisione
- `src/seno.py`: funzione seno in gradi
- `src/coseno.py`: funzione coseno in gradi
- `src/tangente.py`: funzione tangente in gradi
- `src/arcoseno.py`: arcoseno in gradi
- `src/arcocoseno.py`: arcocoseno in gradi

## 🔧 Requisiti

- Python 3.6+
- Nessuna libreria esterna richiesta

## 👨‍💻 Autore

Progetto sviluppato come esercitazione su programmazione modulare in Python.

## 📄 Licenza

Questo progetto è open source e disponibile per scopi didattici.

---

**Versione**: 1.0  
**Ultimo aggiornamento**: Marzo 2026
