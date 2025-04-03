"""
Autore: Lorenzo Spina
Data: 29/03/2025
Titolo: Si hanno in input due numeri reali A e B e una successione di numeri reali positivi che
termina con il valore 0. Si vuole in output la media dei soli numeri compresi tra A e B.
"""

# Funzione per calcolare la media dei numeri tra A e B
def calcola_media(A, B):
    somma = 0
    conteggio = 0
    
    while True:
        numero = float(input("Inserisci un numero (0 per terminare): "))
        if numero == 0:
            break
        if A < numero < B:  # Controlla se il numero è tra A e B
            somma += numero
            conteggio += 1

    if conteggio == 0:  # Evita la divisione per zero
        return "Nessun numero valido inserito."
    
    media = somma / conteggio
    return f"La media dei numeri tra {A} e {B} è: {media}"

# Esempio di utilizzo
A = float(input("Inserisci il valore di A: "))
B = float(input("Inserisci il valore di B: "))
print(calcola_media(A, B))