"""
Autore: Lorenzo Spina
Data: 29/03/2025
Titolo: Scrivere un programma che legga il raggio r di una circonferenza e ne calcoli l'area e la
lunghezza.
"""

# Definizione del valore di pi greco
pi = 3.14

# Funzione per calcolare la lunghezza e l'area della circonferenza
def calcola_circonferenza(raggio):
    lunghezza = 2 * pi * raggio
    area = pi * (raggio ** 2)
    return lunghezza, area

# Input dell'utente
raggio = float(input("Inserisci il raggio della circonferenza: "))

# Calcolo della lunghezza e dell'area
lunghezza, area = calcola_circonferenza(raggio)

# Stampo i risultati
print(f"La lunghezza della circonferenza è: {lunghezza}")
print(f"L'area della circonferenza è: {area}")
