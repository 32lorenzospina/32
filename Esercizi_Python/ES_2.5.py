
"""
Autore: Lorenzo Spina
Data: 29/03/2025
Titolo: Scrivere un programma che chiede quanti alunni ci sono in una classe poi per ogni alunno
fa inserire M voti, M dato in input, e ne scrive la media.

"""

# Chiedo all'utente il numero di alunni
num_alunni = int(input("Quanti alunni ci sono nella classe? "))

# Cicliamo per ogni alunno
for i in range(num_alunni):
    print(f"\nAlunno {i + 1}:")
    
    # Chiediamo quanti voti inserire
    M = int(input("Quanti voti vuoi inserire? "))
    
    somma_voti = 0  # Inizializziamo la somma dei voti
    
    # Cicliamo per ogni voto
    for j in range(M):
        voto = float(input(f"Inserisci il voto {j + 1}: "))
        somma_voti += voto  # Aggiungiamo il voto alla somma
    
    # Calcoliamo la media
    media = somma_voti / M
    print(f"La media dei voti per l'alunno {i + 1} è: {media:.2f}")