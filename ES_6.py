"""
Autore: Lorenzo Spina
Data: 29/03/2025
Titolo: Su una linea ferroviaria, rispetto alla tariffa piena, gli utenti pensionati usufruiscono di uno
sconto del 10%, gli studenti del 15% e i disoccupati del 25%. Codificando i pensionati con
un 1, gli studenti con un 2 e i disoccupati con un 3, scrivere un programma che, richiesto il
costo di un biglietto e l'eventuale condizione particolare dell'utente, visualizzi l'importo da
pagare.

"""


# Funzione per calcolare il prezzo del biglietto
def calcola_prezzo(big, categoria):
    if categoria == 1:  # Pensionati
        sconto = 0.10
    elif categoria == 2:  # Studenti
        sconto = 0.15
    elif categoria == 3:  # Disoccupati
        sconto = 0.25
    else:
        sconto = 0  # Nessuno sconto

    prezzo_finale = big * (1 - sconto)
    return prezzo_finale

# Input dell'utente
costo_biglietto = float(input("Inserisci il costo del biglietto: "))
categoria_utente = int(input("Inserisci la categoria (1: Pensionato, 2: Studente, 3: Disoccupato): "))

# Calcolo e visualizzazione del prezzo finale
prezzo_da_pagare = calcola_prezzo(costo_biglietto, categoria_utente)
print(f"L'importo da pagare è: {prezzo_da_pagare:.2f} euro")