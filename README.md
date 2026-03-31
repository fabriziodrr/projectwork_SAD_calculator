# SAD Calculator - Calcolatrice Modulare

Una calcolatrice interattiva modulare sviluppata in Python con operazioni matematiche di base organizzate in moduli separati.

## 📋 Descrizione Progetto

SAD Calculator è un progetto didattico che dimostra i principi della programmazione modulare in Python. Il progetto è organizzato in moduli indipendenti per ogni operazione matematica, con un'interfaccia principale che integra tutte le funzionalità.

## ✨ Funzionalità

- **Addizione**: Somma di più numeri inseriti dall'utente
- **Sottrazione**: Sottrazione progressiva di più numeri
- **Moltiplicazione**: Moltiplicazione di più numeri
- **Divisione**: Divisione progressiva di più numeri con gestione degli errori
- **Menu Interattivo**: Interfaccia user-friendly con ciclo continuo

## 📁 Struttura del Progetto

```
projectwork_SAD_calculator/
├── main.py                    # File principale con menu interattivo
├── addizione.py               # Modulo per le operazioni di addizione
├── sottrazione.py             # Modulo per le operazioni di sottrazione
├── moltiplicazione.py         # Modulo per le operazioni di moltiplicazione
├── divisione.py               # Modulo per le operazioni di divisione
├── testSomma.py               # Test unitari per addizione
├── testSottrazione.py         # Test unitari per sottrazione
├── testMoltiplicazione.py     # Test unitari per moltiplicazione
├── testDivisione.py           # Test unitari per divisione
└── README.md                  # Questo file
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
5. Esci
==================================================
```

Scegli un numero (1-5) e segui le istruzioni per eseguire l'operazione desiderata.

## 🧪 Test Unitari

Per eseguire i test di ogni modulo:

```bash
# Test addizione
python testSomma.py

# Test sottrazione
python testSottrazione.py

# Test moltiplicazione
python testMoltiplicazione.py

# Test divisione
python testDivisione.py
```

## 📚 Dettagli Moduli

### addizione.py
Gestisce operazioni di addizione permettendo all'utente di inserire più numeri e calcolarne la somma totale.

### sottrazione.py
Implementa la sottrazione progressiva: il primo numero inserito è il minuendo, i successivi sono sottratti in sequenza.

### moltiplicazione.py
Calcola il prodotto di più numeri inseriti dall'utente.

### divisione.py
Esegue divisioni progressive con gestione degli errori (divisione per zero). Il primo numero è il dividendo, i successivi sono divisori applicati in sequenza.

## 🔧 Requisiti

- Python 3.6+
- Nessuna libreria esterna richiesta

## 📝 Note di Sviluppo

Il progetto segue i principi di:
- **Modularità**: Ogni operazione è in un modulo separato
- **Separazione dei Compiti**: Logica di input/output separata dalla logica di calcolo
- **Test Driven Development**: Ogni modulo è accompagnato da test unitari
- **Codice Leggibile**: Funzioni ben documentate con docstring

## 👨‍💻 Autore

Progetto sviluppato come esercitazione su programmazione modulare in Python.

## 📄 Licenza

Questo progetto è open source e disponibile per scopi didattici.

---

**Versione**: 1.0  
**Ultimo aggiornamento**: Marzo 2026
