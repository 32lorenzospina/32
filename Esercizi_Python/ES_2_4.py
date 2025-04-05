"""
Autore: Lorenzo Spina
Data: 29/03/2025
Titolo: Scrivere un programma che legge N numeri da tastiera, N dato in input, e ne restituisca il
minimo.
"""

# Chiedo all'utente quanti numeri vuole inserire
N = int(input("Quanti numeri vuoi inserire? "))

# Inizializziamo una lista per memorizzare i numeri
numeri = []

# Ciclo per leggere N numeri
for i in range(N):
    numero = float(input(f"Inserisci il numero {i + 1}: "))  # Leggiamo il numero
    numeri.append(numero)  # Aggiungiamo il numero alla lista

# Troviamo il numero minimo nella lista
minimo = min(numeri)

# Stampiamo il numero minimo
print(f"Il numero minimo è: {minimo}") 