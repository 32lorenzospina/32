"""
Autore: Lorenzo Spina
Data: 29/03/2025
Titolo: Scrivere un programma che legga il raggio r di una circonferenza e ne calcoli l'area e la
lunghezza.
"""

import math  # Importiamo il modulo math per usare pi

# Funzione principale
def calcola_circonferenza():
    raggio = float(input("Inserisci il raggio della circonferenza: "))  # Leggi il raggio dall'utente
    area = math.pi * raggio ** 2  # Calcola l'area
    lunghezza = 2 * math.pi * raggio  # Calcola la lunghezza

    # Stampa i risultati
    print(f"L'area della circonferenza è: {area:.2f}")
    print(f"La lunghezza della circonferenza è: {lunghezza:.2f}")

# Chiamata alla funzione
calcola_circonferenza()