
"""
Autore: Lorenzo Spina
Data: 29/03/2025
Titolo: Un negoziante per ogni spesa di importo superiore a 100 € effettua uno sconto del 5%, se
l’importo risulta superiore a 300€ lo sconto è del 10%. Scrivere un programma che richieda
all'utente l'ammontare della spesa e visualizzi quindi l'importo effettivo da pagare.

"""

# Richiesta dell'importo della spesa all'utente
spesa = float(input("Inserisci l'importo della spesa: "))

# Inizializzazione dell'importo da pagare
importo_da_pagare = spesa

# Applico gli sconti
if spesa > 300:
    importo_da_pagare = spesa * 0.90  # Sconto del 10%
elif spesa > 100:
    importo_da_pagare = spesa * 0.95  # Sconto del 5%

# Visualizzo l'importo effettivo da pagare
print("L'importo effettivo da pagare è: €", importo_da_pagare)